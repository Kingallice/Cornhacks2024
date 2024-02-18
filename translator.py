from translate import Translator

class Diplomat:
    def __init__(self, target, source:str, provider:str= "MyMemory"):
        self._target = target
        self._source = source
        self._provider = provider
        self._translator = Translator(to_lang=self._target)

    def getTarget(self):
        return self._target

    def getSource(self):
        return self._source

    def getProvider(self):
        return self._provider

    def setTarget(self, target):
        self._target = target

    def setSource(self, source):
        self._source = source

    def setProvider(self, provider):
        self._provider = provider
        self._translator.provider = self._provider

    def getTranslation(self, phrase:str):
        return self._translator.translate(phrase)
