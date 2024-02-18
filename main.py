from Services.GetKeys import GetAzureKey
from Services.GetConfiguration import GetConfig
from GUI.MainMenu import MainMenu
from GUI.SettingsMenu import SettingsMenu

main_menu = MainMenu()
settings_menu = SettingsMenu()
settings_menu.hide()

def show_main_menu():
    settings_menu.hide()
    main_menu.enable()
    main_menu.focus()

def show_settings():
    main_menu.disable()
    settings_menu.show()

main_menu.set_settings_command(show_settings)
settings_menu.set_back_command(show_main_menu)

def main() -> int:
    main_menu.start()

    return 0

if __name__ == '__main__':
    main()