import json
from os import system

VIDEO_CARD_DICT_PARSED = {}

with open("jsons/video_card_list.json", "r") as video_card_list_unparsed:
  video_card_list = json.load(video_card_list_unparsed)

needed = ["brand", "model", "chipset", "vram", "core_clock", "boost_clock", "length", "price"]
for video_card_num in video_card_list:
  data = video_card_list[video_card_num]


  has_needed = []
  for need in needed:
    if need in data:
      has_needed.append(need)

  if has_needed == needed:

    def Bytes(total):
      return total

    def ClockSpeed(cycles):
      return cycles

    exec(f"""
  
def parse({data}):
  VIDEO_CARD_DICT_PARSED[{video_card_num}] = [brand, model, chipset, vram, core_clock, boost_clock, length, price]
    """)
  
    parse()



with open("jsons/VIDEO_CARD_JSON_PARSED.json", "w") as VIDEO_CARD_JSON_PARSED:
  VIDEO_CARD_JSON_PARSED.write("")
  json.dump(VIDEO_CARD_DICT_PARSED, VIDEO_CARD_JSON_PARSED)

with open("VIDEO_CARDS.json", "w") as format:
  format.write("")



system("cat jsons/VIDEO_CARD_JSON_PARSED.json | jq > VIDEO_CARDS.json")