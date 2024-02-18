class Config:
    def __init__(self) -> None:
        if not hasattr(Config, "_config"):
            self._config = self.LoadConfig()

    def LoadConfig(self):
        config_lines = open("./configuration.yml").readlines()

        config = {}

        for line in config_lines:
            parts = line.strip().split(":", 1)
            config[parts[0].strip()] = parts[1].strip()[1:-1]

        return config

    def GetConfig(self, key: str) -> str:
        if(key in self._config.keys()):
            return self._config[key]
        else:
            return None