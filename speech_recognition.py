import azure.cognitiveservices.speech as speechsdk
import Services.KeyService as key
from Services.ConfigurationService import Config
from translator import Diplomat

configure = Config()

def recognize_from_microphone(lang: str, target:str):
    dip = Diplomat(target, "en")
    speech_config = speechsdk.SpeechConfig(subscription=key.GetAzureKey(), region=configure.GetConfig("region"))
    speech_config.speech_recognition_language = lang
    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    result = speech_recognizer.recognize_once_async().get()

    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        text = dip.getTranslation(result.text)
        return " {}".format(text)
    elif result.reason == speechsdk.ResultReason.NoMatch:
        return "No speech could be recognized: {}".format(result.no_match_details)
# Everything just returns right now.

def recognize_from_computer():
    speech_config = speechsdk.SpeechConfig(subscription=key.GetAzureKey(), region=configure.GetConfig("region"))
    speech_config.speech_recognition_language = "en-US"
    audio_config = speechsdk.audio.AudioConfig(filename='output.wav')
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    result = speech_recognizer.recognize_once_async().get()

    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        return " {}".format(result.text)
    elif result.reason == speechsdk.ResultReason.NoMatch:
        return "No speech could be recognized"

taking_info = True
while taking_info:
    print(recognize_from_microphone("en-US","es"))
