import json
from os import system

MONITOR_DICT_PARSED = {}

with open("jsons/monitor_list.json", "r") as monitor_list_unparsed:
  monitor_list = json.load(monitor_list_unparsed)

needed = ["brand", "model", "size", "resolution", "refresh_rate", "response_time", "panel_type", "aspect_ratio", "price"]
for monitor_num in monitor_list:
  data = monitor_list[monitor_num]


  has_needed = []
  for need in needed:
    if need in data:
      has_needed.append(need)

  if has_needed == needed:

    def Resolution(width, height):
      return (width, height)

    exec(f"""
  
def parse({data}):
  MONITOR_DICT_PARSED[{monitor_num}] = [brand, model, size, resolution, refresh_rate, response_time, panel_type, aspect_ratio, price]
    """)
  
    parse()



with open("jsons/MONITOR_JSON_PARSED.json", "w") as MONITOR_JSON_PARSED:
  MONITOR_JSON_PARSED.write("")
  json.dump(MONITOR_DICT_PARSED, MONITOR_JSON_PARSED)

with open("MONITORS.json", "w") as format:
  format.write("")



system("cat jsons/MONITOR_JSON_PARSED.json | jq > MONITORS.json")