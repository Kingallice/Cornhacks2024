config_lines = open("./configuration.yml").readlines()

config = {}

for line in config_lines:
    parts = line.strip().split(":", 1)
    config[parts[0].strip()] = parts[1].strip()[1:-1]

def GetConfig(key: str) -> str:
    if(key in config.keys()):
        return config[key]
    else: 
        return None