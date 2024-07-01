# Bulk Transcribe script

i guess we need a readme doc to tell you what this is about. 

## why thisss?
I was working on a project and needed a way to get written notes from things i've said in my older voice memos and videos. I couldn't find any services that did this in a cheap way; and i didn't want to have to transcribe each file one by one. Better if I can do it all offline, no internet, just local on my computer, point to a folder full of audio files, and say hey computah transcribe all these mp3s and put them in this other folder as a text file.

with the help of gpt's and my old remaining brain cells, we now have this script to bulk transcribe.

## what do i need to run it?
it's free.

for now.

i'm running this in terminal CLI off a 2016 old macbook pro. using big sur... i did eventually update to whatever mountain thing came after that. in anycase... it should run off python 3, and hugging face whisper libraries.

## am i missing anything?
yes... you will need to download a few things first, like Python, and whisper, and a few other dependencies.

i will work on a docker thingy so it's all together. feel free to ping me if you know a better solution.


# semi-offich audio transcribe script guide

## Overview
This script transcribes audio files from a specified folder into text files using the Hugging Face Whisper model. The script processes audio files in chunks, handles padding requirements, and saves the transcriptions to a designated output folder. Additionally, it reports the time taken to transcribe each audio file.

## Prerequisites
Before running the script, ensure you have the following dependencies installed:

- Python 3.6+
- `transformers`
- `soundfile`
- `pydub`
- `numpy`
- `torch`
- `ffmpeg` (for handling `.mp3` files with PyDub)

You can install the Python dependencies using pip:

```bash
pip install transformers soundfile pydub numpy torch
```

To install `ffmpeg`, follow the installation instructions for your operating system from [ffmpeg.org](https://ffmpeg.org/download.html).

## Script Setup
1. **Clone or download the script** to your local machine.\
2. **Place your audio files** (in `.mp3` format) in a folder.\
3. **Run the script** from the command line or an IDE.\
\
## Usage\
1. **Running the Script**:\
   - Open a terminal or command prompt.\
   - Navigate to the directory containing the script.\
   - Execute the script with the following command:\
     ```bash\
     python transcribe_audio.py\
     ```\
\
2. **Input Prompts**:\
   - The script will prompt you to enter the path to the folder containing your audio files.\
   - It will also prompt you to enter the path to the folder where you want the transcribed text files to be saved.\
\
## Script Components\
### Imports\
The script imports necessary modules for audio processing, file handling, and the Hugging Face Whisper model.\
\
### `transcribe_audio_chunk` Function\
This function processes a chunk of audio:\
- Normalizes the audio data.\
- Converts the audio to input features using the Whisper processor.\
- Pads the input features to the required length.\
- Generates the transcription for the chunk.\
\
### `transcribe_audio` Function\
This function handles the complete transcription of an audio file:\
- Loads the audio file and splits it into manageable chunks.\
- Calls `transcribe_audio_chunk` for each chunk and concatenates the results.\
- Returns the full transcription of the audio file.\
\
### `main` Function\
This is the entry point of the script:\
- Prompts the user for input and output folder paths.\
- Ensures the output folder exists.\
- Loads the pre-trained Whisper model and processor.\
- Iterates over the audio files in the specified folder, transcribes each file, and saves the transcriptions.\
- Prints the time taken for each file's transcription.\
\
## Example Output\
After running the script, you should see output similar to the following:\
```plaintext\
Please enter the path to your audio files folder: /path/to/audio/files\
Please enter the path to your output folder: /path/to/output/files\
Output folder set to: /path/to/output/files\
Loading model and processor...\
Model and processor loaded successfully.\
Found 3 audio files in the folder: /path/to/audio/files\
Transcribing file: audio1.mp3\
Transcription saved to: /path/to/output/files/audio1.txt\
Time taken for audio1.mp3: 12.34 seconds\
Transcribing file: audio2.mp3\
Transcription saved to: /path/to/output/files/audio2.txt\
Time taken for audio2.mp3: 10.56 seconds\
Transcribing file: audio3.mp3\
Transcription saved to: /path/to/output/files/audio3.txt\
Time taken for audio3.mp3: 15.78 seconds\
Transcription process completed.\
```\
\
## Troubleshooting\
- **Dependencies**: Ensure all required Python packages and `ffmpeg` are installed correctly.\
- **File Formats**: Ensure your audio files are in `.mp3` format. If using another format, adjust the script accordingly.\
- **Errors**: If you encounter errors, check the traceback for specific issues, such as missing dependencies or incorrect file paths.\
\
## Customization\
- **Chunk Length**: Adjust the `chunk_length_ms` parameter in the `transcribe_audio` function to change the chunk size for processing longer or shorter audio segments.\
- **Model**: Change the model by modifying the `from_pretrained` method in the `main` function to use a different Whisper model variant.\
\
## Conclusion\
This guide provides a comprehensive overview of the audio transcription script, including setup, usage, and customization options. By following this guide, users can efficiently transcribe audio files using the Whisper model and tailor the script to their needs.\
\
---}
