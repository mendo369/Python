import speech_recognition as sr
import pyttsx3

# Inicializar el reconocimiento de voz
r = sr.Recognizer()

# Inicializar el sintetizador de voz
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    with sr.Microphone() as source:
        speak("Dime algo")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio, language="es-ES")
            return text.lower()
        except sr.UnknownValueError:
            return "No te he entendido."
        except sr.RequestError:
            return "No puedo acceder al servicio de reconocimiento de voz."


def process_command(command):
    if "hola" in command:
        speak("¡Hola! ¿En qué puedo ayudarte?")
    elif "adiós" in command:
        speak("¡Hasta luego! Que tengas un buen día.")
    else:
        speak("Lo siento, no puedo entender tu comando.")


# Programa principal
while True:
    command = listen()
    process_command(command)
