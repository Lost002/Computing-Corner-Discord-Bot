import json
from os import system

FAN_CONTROLLER_DICT_PARSED = {}

with open("jsons/fan_controller_list.json", "r") as fan_controller_list_unparsed:
  fan_controller_list = json.load(fan_controller_list_unparsed)

needed = ["brand", "model", "channels", "channel_wattage", "pwm", "form_factor", "color", "price"]
for fan_controller_num in fan_controller_list:
  data = fan_controller_list[fan_controller_num]


  has_needed = []
  for need in needed:
    if need in data:
      has_needed.append(need)

  if has_needed == needed:

    exec(f"""
  
def parse({data}):
  FAN_CONTROLLER_DICT_PARSED[{fan_controller_num}] = [brand, model, channels, channel_wattage, pwm, form_factor, color, price]
    """)
  
    parse()



with open("jsons/FAN_CONTROLLER_JSON_PARSED.json", "w") as FAN_CONTROLLER_JSON_PARSED:
  FAN_CONTROLLER_JSON_PARSED.write("")
  json.dump(FAN_CONTROLLER_DICT_PARSED, FAN_CONTROLLER_JSON_PARSED)

with open("FAN_CONTROLLERS.json", "w") as format:
  format.write("")



system("cat jsons/FAN_CONTROLLER_JSON_PARSED.json | jq > FAN_CONTROLLERS.json")