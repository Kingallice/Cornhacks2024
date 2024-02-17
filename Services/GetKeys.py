
def KeyError(ex: Exception):
    print("Key Error: ", ex)

def GetAzureKey() -> str:
    try:
        return open("./Keys/AzureKey").read()
    except Exception as ex:
        KeyError(ex)
        return "ERROR"