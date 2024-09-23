
# voice assistant
import pyttsx3 #import  
import webbrowser
import speech_recognition as sr 



# Initialize the text-to-speech engine and recognizer
engine = pyttsx3.init()
recognizer = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def process_command(command):
    # Perform actions based on the command
    if 'open google' in command.lower():
        speak("Opening google.")
        webbrowser.open('https://www.google.com')
    elif 'open youtube' in command.lower():
        speak("opeing youtube,")
        webbrowser.open('https://www.youtube.com')  
     
    elif 'open facebook' in command.lower():
        speak("open facebook.")
        webbrowser.open('https://www.facebook.com')     
    elif 'hello' in command.lower():
        speak("Hello! How can I assist you?")
    # Add more commands here

def main():
    speak("give the command")

    while True:
        print("Listening...")
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

        try:
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            process_command(command)

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
