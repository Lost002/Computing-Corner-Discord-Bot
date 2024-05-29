import json
from os import system

MOUSE_DICT_PARSED = {}

with open("jsons/mouse_list.json", "r") as mouse_list_unparsed:
  mouse_list = json.load(mouse_list_unparsed)

needed = ["brand", 'model', "tracking", "connection", "max_dpi", "hand_orientation", "color", "price"]
for mouse_num in mouse_list:
  data = mouse_list[mouse_num]


  has_needed = []
  for need in needed:
    if need in data:
      has_needed.append(need)

  if has_needed == needed:

    exec(f"""
  
def parse({data}):
  MOUSE_DICT_PARSED[{mouse_num}] = [brand, model, tracking, connection, max_dpi, hand_orientation, color, price]
    """)
  
    parse()



with open("jsons/MOUSE_JSON_PARSED.json", "w") as MOUSE_JSON_PARSED:
  MOUSE_JSON_PARSED.write("")
  json.dump(MOUSE_DICT_PARSED, MOUSE_JSON_PARSED)

with open("MOUSES.json", "w") as format:
  format.write("")



system("cat jsons/MOUSE_JSON_PARSED.json | jq > MOUSES.json")