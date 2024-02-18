import json

class Settings:

    def __init__(self) -> None:
        if not hasattr(Settings, "_settings"):
            Settings._settings = Settings.LoadSettings()

    def LoadSettings() -> json:
        settings = json.loads("{}")
        try:
            file = open("settings.json", "r")
            settings = json.loads(file.read()) 
            file.close()

        except FileNotFoundError:
            settings["height"] = 300
            settings["width"] = 400
            settings["language"] = "en_us"

            file = open("settings.json", "w")
            file.write(json.dumps(settings))
            file.close()

        return settings

    def GetSettings(self) -> json:
        return Settings._settings
    
    def GetSetting(self, key: str) -> str:
        if key in Settings._settings:
            return Settings._settings[key]
        
    def UpdateSetting(self, key: str, value) -> str:
        Settings._settings[key] = value
        Settings.SaveSettings()

    def SaveSettings():
        try:
            file = open("settings.json", "w")
            file.write(json.dumps(Settings._settings))
            file.close()
        except Exception as ex:
            print(ex)
