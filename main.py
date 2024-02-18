from Services.KeyService import *
from Services.ConfigurationService import *
from Services.SettingsService import *
from Services.TranslationService import *
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

translation = Translation()

result = translation.TranslateText("Las flores son una maravillosa manifestación de la naturaleza que nos regala su belleza y fragancia. Con una amplia variedad de colores, formas y aromas, las flores alegran nuestros jardines, hogares y corazones. Desde las delicadas rosas hasta las exóticas orquídeas, cada flor tiene su propio encanto y significado especial. Son símbolos de amor, alegría, esperanza y renovación. Contemplar un campo lleno de flores es como sumergirse en un mundo de paz y armonía, donde la belleza florece en cada pétalo. Las flores nos recuerdan la importancia de cuidar y apreciar la naturaleza, así como de cultivar la belleza en nuestras vidas.")

for i in range(5):
    print(translation.RandomTranslate(result), "\n\n")

def main() -> int:
    
    main_menu.start()

    return 0

if __name__ == '__main__':
    main()