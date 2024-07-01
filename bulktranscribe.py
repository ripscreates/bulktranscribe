from transformers import WhisperProcessor, WhisperForConditionalGeneration
import soundfile as sf
from pydub import AudioSegment
import numpy as np
import torch
import os
import time

def transcribe_audio_chunk(processor, model, audio_chunk):
    audio_input = np.array(audio_chunk.get_array_of_samples(), dtype=np.float32) / 32768.0  # Normalize audio

    # Tokenize the input
    input_features = processor(audio_input, sampling_rate=16000, return_tensors="pt").input_features

    # Pad the input features to the required length
    required_length = 3000
    if input_features.shape[-1] < required_length:
        padding = required_length - input_features.shape[-1]
        input_features = torch.nn.functional.pad(input_features, (0, padding), 'constant', 0)

    # Generate transcription
    generated_ids = model.generate(input_features)
    transcription = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]

    return transcription

def transcribe_audio(processor, model, audio_file, chunk_length_ms=30000):
    print(f"Transcribing file: {audio_file}")

    # Load the audio file and convert to a format compatible with soundfile
    audio = AudioSegment.from_file(audio_file)
    audio = audio.set_frame_rate(16000).set_channels(1)

    transcriptions = []

    # Process audio in chunks
    for i in range(0, len(audio), chunk_length_ms):
        audio_chunk = audio[i:i + chunk_length_ms]
        text = transcribe_audio_chunk(processor, model, audio_chunk)
        transcriptions.append(text)

    # Join the transcriptions of each chunk
    full_transcription = ' '.join(transcriptions)
    
    return full_transcription

def main():
    # Prompt the user to input the path to the audio files folder
    audio_folder = input("Please enter the path to your audio files folder: ")

    # Prompt the user to input the path to the output folder
    output_folder = input("Please enter the path to your output folder: ")

    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)
    print(f"Output folder set to: {output_folder}")

    # Load the pre-trained Whisper model and processor
    print("Loading model and processor...")
    processor = WhisperProcessor.from_pretrained("openai/whisper-small")
    model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-small")
    print("Model and processor loaded successfully.")

    # Get all audio files in the folder
    audio_files = [f for f in os.listdir(audio_folder) if os.path.isfile(os.path.join(audio_folder, f))]
    print(f"Found {len(audio_files)} audio files in the folder: {audio_folder}")

    # Iterate over audio files
    for audio_file in audio_files:
        if audio_file.endswith(".mp3"):  # Assuming all files are in .mp3 format
            audio_path = os.path.join(audio_folder, audio_file)
            
            # Start timer
            start_time = time.time()
            
            text = transcribe_audio(processor, model, audio_path)

            # Stop timer
            end_time = time.time()
            elapsed_time = end_time - start_time

            # Write transcript to text file
            output_file = os.path.join(output_folder, os.path.splitext(audio_file)[0] + ".txt")
            with open(output_file, "w") as f:
                f.write(text)
            print(f"Transcription saved to: {output_file}")
            print(f"Time taken for {audio_file}: {elapsed_time:.2f} seconds")

    print("Transcription process completed.")

if __name__ == "__main__":
    main()
