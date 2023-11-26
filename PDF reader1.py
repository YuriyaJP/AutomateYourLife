import pyttsx3
import PyPDF2

pdf_file_path = 'C:/Users/Yuliia/Downloads/pytorch_image_class/PDF_reader.pdf'

# Initialize the text-to-speech engine with the desired English voice
speaker = pyttsx3.init()
speaker.setProperty('voice', 'TTS_MS_EN-GB_HAZEL_11.0')

# Open the PDF file
with open(pdf_file_path, 'rb') as file:
    # Create a PdfReader object
    pdfreader = PyPDF2.PdfReader(file)

    # Iterate through each page and extract text
    for page_num in range(len(pdfreader.pages)):
        text = pdfreader.pages[page_num].extract_text()
        clean_text = text.strip().replace('\n', ' ')
        print(clean_text)

        # Speak the extracted text
        speaker.say(clean_text)

    # Save the spoken text to an audio file (e.g., audio.mp3)
    speaker.save_to_file(clean_text, 'audio.mp3')

# Wait for the speech to finish
speaker.runAndWait()

# Stop the text-to-speech engine
speaker.stop()
