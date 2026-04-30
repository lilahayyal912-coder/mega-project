import speech_recognition as sr
import pyttsx3
import webbrowser
print(" hi")

# 1. Initialize the engine

recognizer = sr.Recognizer()

engine = pyttsx3.init()



def speak(text):

    """This function makes the AI talk"""

    print(f"Assistant: {text}") # Good for debugging

    engine.say(text)

    engine.runAndWait()



if __name__ == "__main__":

    # Now this will work!

    speak("INITIALIZING JARVIS......")

    # obtain audio from the microphone

    while True:

        r = sr.Recognizer()

        print("recognize.....")

        # recognize speech using Sphinx  

        try:

            with sr.Microphone() as source:

                print("Listening.....")

                audio = r.listen(source, timeout=2, phrase_time_limit=1)

            command = r.recognize_google(audio)

            print(command)

        except sr.RequestError as e:

            print("error; {0}".format(e))
