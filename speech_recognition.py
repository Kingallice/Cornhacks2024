import azure.cognitiveservices.speech as speechsdk
import Services.GetKeys as key
import Services.GetConfiguration as config

def recognize_from_microphone():
    speech_config = speechsdk.SpeechConfig(subscription=key.GetAzureKey(), region=config.GetConfig("region"))
    speech_config.speech_recognition_language = "en-US"
    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    result = speech_recognizer.recognize_once_async().get()

    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        return " {}".format(result.text)
    elif result.reason == speechsdk.ResultReason.NoMatch:
        return "No speech could be recognized: {}".format(result.no_match_details)
# Everything just returns right now.

taking_info = True
while taking_info:
    print(recognize_from_microphone())
