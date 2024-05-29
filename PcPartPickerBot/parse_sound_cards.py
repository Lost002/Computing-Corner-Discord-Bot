import json
from os import system

SOUND_CARD_DICT_PARSED = {}

with open("jsons/sound_cards_list.json", "r") as sound_card_list_unparsed:
  sound_card_list = json.load(sound_card_list_unparsed)

needed = ["brand", "model", "channels", "bitrate", "snr", "sample_rate", "chipset", "interface", "price"]
for sound_card_num in sound_card_list:
  data = sound_card_list[sound_card_num]


  has_needed = []
  for need in needed:
    if need in data:
      has_needed.append(need)

  if has_needed == needed:

    exec(f"""
  
def parse({data}):
  SOUND_CARD_DICT_PARSED[{sound_card_num}] = [brand, model, channels, bitrate, snr, sample_rate, chipset, interface, price]
    """)
  
    parse()



with open("jsons/SOUND_CARD_JSON_PARSED.json", "w") as SOUND_CARD_JSON_PARSED:
  SOUND_CARD_JSON_PARSED.write("")
  json.dump(SOUND_CARD_DICT_PARSED, SOUND_CARD_JSON_PARSED)

with open("SOUND_CARDS.json", "w") as format:
  format.write("")



system("cat jsons/SOUND_CARD_JSON_PARSED.json | jq > SOUND_CARDS.json")