from Services.GetKeys import GetAzureKey
from Services.GetConfiguration import GetConfig
from GUI.MainMenu import MainMenu

def main() -> int:
    main_menu = MainMenu()

    main_menu.start()

    return 0

if __name__ == '__main__':
    main()