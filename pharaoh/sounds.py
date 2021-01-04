import pygame


def load_sound(name, volume=0.25, extension="ogg"):
    name = pygame.mixer.Sound( f"Sounds/{name}.{extension}" )
    name.set_volume( volume )
    return name


sound_dict = {}


def load():
    sound_names = ["pop", "win", "tiles_drop"]
    for i in range( len( sound_names ) ):
        file_path = "Sounds/" + sound_names[i] + ".wav"
        sound_dict[sound_names[i]] = pygame.mixer.Sound( file_path )


# Plays named sound effects
def play_effect(name):
    effect = sound_dict[name]
    effect.play(0)

