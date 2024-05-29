import json
from os import system

POWER_SUPPLY_DICT_PARSED = {}

with open("jsons/power_supply_list.json", "r") as power_supply_list_unparsed:
  power_supply_list = json.load(power_supply_list_unparsed)

needed = ["brand", 'model', "form_factor", "efficiency_rating", "wattage", "modular", "color", "price"]
for power_supply_num in power_supply_list:
  data = power_supply_list[power_supply_num]


  has_needed = []
  for need in needed:
    if need in data:
      has_needed.append(need)

  if has_needed == needed:

    exec(f"""
  
def parse({data}):
  POWER_SUPPLY_DICT_PARSED[{power_supply_num}] = [brand, model, form_factor, efficiency_rating, wattage, modular, color, price]
    """)
  
    parse()



with open("jsons/POWER_SUPPLY_JSON_PARSED.json", "w") as POWER_SUPPLY_JSON_PARSED:
  POWER_SUPPLY_JSON_PARSED.write("")
  json.dump(POWER_SUPPLY_DICT_PARSED, POWER_SUPPLY_JSON_PARSED)

with open("POWER_SUPPLYS.json", "w") as format:
  format.write("")



system("cat jsons/POWER_SUPPLY_JSON_PARSED.json | jq > POWER_SUPPLYS.json")