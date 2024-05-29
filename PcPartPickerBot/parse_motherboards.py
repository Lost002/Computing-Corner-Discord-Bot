import json
from os import system

MOTHERBOARD_DICT_PARSED = {}

with open("jsons/motherboard_list.json", "r") as motherboard_list_unparsed:
  motherboard_list = json.load(motherboard_list_unparsed)

needed =  ["brand", "model", "socket", "form_factor", "ram_slots", "max_ram", "color", "price"]
for motherboard_num in motherboard_list:
  
  data = motherboard_list[motherboard_num]

  has_needed = []
  for need in needed:
    if need in data:
      has_needed.append(need)

  if has_needed == needed:

    def Bytes(total):
      return total
    
    exec(f"""
  
def parse({data}):
  MOTHERBOARD_DICT_PARSED[{motherboard_num}] = [brand, model, socket, form_factor, ram_slots, max_ram, color, price]
    """)
    
    parse()


  
with open("jsons/MOTHERBOARD_JSON_PARSED.json", "w") as MOTHERBOARD_JSON_PARSED:
  MOTHERBOARD_JSON_PARSED.write("")
  json.dump(MOTHERBOARD_DICT_PARSED, MOTHERBOARD_JSON_PARSED)

with open("MOTHERBOARDS.json", "w") as format:
  format.write("")

system("cat jsons/MOTHERBOARD_JSON_PARSED.json | jq > MOTHERBOARDS.json")