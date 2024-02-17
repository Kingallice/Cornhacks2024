
import azure.cognitiveservices.speech as speechsdk
from azure.cognitiveservices.speech.audio import AudioInputStream, PushAudioInputStream, PullAudioInputStream

import Services.GetKeys as key
import Services.GetConfiguration as config
from JakeTestDirectory import jakeTkinter as window

def recognize_from_microphone():
    running = True
    # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
    speech_config = speechsdk.SpeechConfig(subscription=key.GetAzureKey(), region=config.GetConfig("region"))
    speech_config.speech_recognition_language="en-US"
    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    while running:
        result = speech_recognizer.recognize_once_async().get()

        if result.reason == speechsdk.ResultReason.RecognizedSpeech:
            return str(result.text)
        elif result.reason == speechsdk.ResultReason.NoMatch:
            return("No speech could be recognized: {}".format(result.no_match_details))

#Everything just returns right now.
def recognize_from_computer():
    speech_config = speechsdk.SpeechConfig(subscription=key.GetAzureKey(), region=config.GetConfig("region"))
    speech_config.speech_recognition_language = "en-US"






window.build_window(recognize_from_microphone())