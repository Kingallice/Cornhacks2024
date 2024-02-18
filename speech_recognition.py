import azure.cognitiveservices.speech as speechsdk
from recordaudio import record_audio


import Services.GetKeys as key
import Services.GetConfiguration as config
from JakeTestDirectory import jakeTkinter as window



def recognize_from_microphone():
    running = True
    # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
    speech_config = speechsdk.SpeechConfig(subscription=key.GetAzureKey(), region=config.GetConfig("region"))
    speech_config.speech_recognition_language = "en-US"
    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    while running:
        result = speech_recognizer.recognize_once_async().get()

        if result.reason == speechsdk.ResultReason.RecognizedSpeech:
            return "speech could be recognized: {}".format(result.text)

        elif result.reason == speechsdk.ResultReason.NoMatch:
            return "No speech could be recognized: {}".format(result.no_match_details)


# Everything just returns right now.
def recognize_from_computer():
    running = True
    speech_config = speechsdk.SpeechConfig(subscription=key.GetAzureKey(), region=config.GetConfig("region"))
    speech_config.speech_recognition_language = "en-US"

    record_audio()
    audio_config = speechsdk.audio.AudioConfig(filename="output.wav")
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    while running:
        result = speech_recognizer.recognize_once_async().get()

        if result.reason == speechsdk.ResultReason.RecognizedSpeech:
            return "speech could be recognized: {}".format(result.text)

        elif result.reason == speechsdk.ResultReason.NoMatch:
            return "No speech could be recognized: {}".format(result.no_match_details)



print(recognize_from_computer())
