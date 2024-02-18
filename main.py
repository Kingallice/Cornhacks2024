from Services.KeyService import *
from Services.ConfigurationService import *
from Services.SettingsService import *
from Services.TranslationService import *
from GUI.MainMenu import MainMenu
from GUI.SettingsMenu import SettingsMenu
from GUI.CaptionOverlay import CaptionOverlay

main_menu = MainMenu()
settings_menu = SettingsMenu()
settings_menu.hide()
caption_overlay = CaptionOverlay()
caption_overlay.hide()

def show_main_menu():
    settings_menu.hide()
    caption_overlay.hide()
    main_menu.enable()
    main_menu.focus()

def show_settings():
    main_menu.disable()
    settings_menu.show()

def show_overlay():
    main_menu.hide()
    caption_overlay.show()

main_menu.set_start_command(show_overlay)
main_menu.set_settings_command(show_settings)
settings_menu.set_back_command(show_main_menu)
caption_overlay.set_stop_command(show_main_menu)

def main() -> int:
    
    main_menu.start()

    return 0

if __name__ == '__main__':
    main()