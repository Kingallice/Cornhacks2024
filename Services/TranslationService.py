import json
from Services.ConfigurationService import *
import requests
import random

class Translation:
    def __init__(self) -> None:
        if not hasattr(Translation, "_url"):
            Translation._config = Config()
            Translation._url = Translation._config.GetConfig("translate_url")
            Translation._port = Translation._config.GetConfig("translate_port")

    def GetLanguages(self, lang="en") -> list:
        req = requests.get(Translation._url+":"+Translation._port+"/languages")

        result = req.json()
        for x in result:
            if x['code'] == lang:
                return x['targets']
        return result[0]['targets']
    
    def TranslateText(self, text, source="auto", target="en") -> str:
        req = requests.post(Translation._url+":"+Translation._port+"/translate", data={
            "q": text, "source":source, "target":target, "format":"text"
        })

        return req.json()['translatedText']

    def RandomTranslate(self, text, total=5, target="en") -> str:
        languages = self.GetLanguages()

        latest = text
        for i in range(total):
            latest = self.TranslateText(latest, target=languages[random.randint(0, len(languages)-1)])

        return self.TranslateText(latest)
