from pcpartpicker import API
import json

api = API()

print(f"_DEBUG: SUPPORTED PARTS: {api.supported_parts}\n")


sound_cards_data = str(api.retrieve("sound-card"))


sound_cards_data = sound_cards_data.split("SoundCard")


sound_cards_dict = {}
sound_cards_list = []
for sound_cards in sound_cards_data:
  if sound_cards == sound_cards_data[0]:
    pass

  else:
    sound_cards_to_add = sound_cards[1:-3].replace("<", "'").replace(">", "'")

    sound_cards_dict[sound_cards_data.index(sound_cards)-1] = sound_cards_to_add


with open("jsons/sound_cards_list.json", "w") as sound_cards_json_file:
  sound_cards_json_file.write('')
  json.dump(sound_cards_dict, sound_cards_json_file)

