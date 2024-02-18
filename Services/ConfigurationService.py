class Config:
    def __init__(self) -> None:
        if not hasattr(Config, "_config"):
            Config._config = Config.LoadConfig()

    def LoadConfig():
        config_lines = open("./configuration.yml").readlines()

        config = {}

        for line in config_lines:
            parts = line.strip().split(":", 1)
            config[parts[0].strip()] = parts[1].strip()[1:-1]

        return config

def GetConfig(key: str) -> str:
    if(key in Config._config.keys()):
        return Config._config[key]
    else: 
        return None