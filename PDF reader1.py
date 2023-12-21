import pyttsx3
import PyPDF2
from gtts import gTTS
import os

pdf_file_path = r'C:\Users\julia\coding projects\speech production\PDF_reader.pdf'

# Initialize the text-to-speech engine
speaker = pyttsx3.init()
speaker.setProperty('voice', 'TTS_MS_EN-GB_HAZEL_11.0')

# Open the PDF file
with open(pdf_file_path, 'rb') as file:
    # Create a PdfReader object
    pdfreader = PyPDF2.PdfReader(file)

    # Iterate through each page and extract text
    full_text = ''
    for page_num in range(len(pdfreader.pages)):
        text = pdfreader.pages[page_num].extract_text()
        clean_text = text.strip().replace('\n', ' ')
        print(clean_text)
        full_text += clean_text + '\n'

        # Speak the extracted text
        speaker.say(clean_text)

    # Save the spoken text to an audio file gTTS
    tts = gTTS(text=full_text, lang='en')
    tts.save('audio.mp3')

# Wait for the speech to finish
speaker.runAndWait()

# Stop the text-to-speech engine
speaker.stop()
