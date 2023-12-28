from gtts import gTTS
from playsound import playsound

def convert_text_to_speech(text, output_file="speech.mp3"):
    # Convert text to speech
    tts = gTTS(text=text, lang='en')
    tts.save(output_file)
    
    # Play the audio file
    playsound(output_file)

if __name__ == "__main__":
    # Example usage
    text = "Hello, how are you today?"
    output_file = "speech.mp3"
    convert_text_to_speech(text, output_file)

