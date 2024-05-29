from pcpartpicker import API
import json

api = API()

print(f"_DEBUG: SUPPORTED PARTS: {api.supported_parts}\n")


fan_controller_data = str(api.retrieve("fan-controller"))

fan_controller_data = fan_controller_data.split("FanController")


fan_controller_dict = {}
fan_controller_list = []
for fan_controller in fan_controller_data:
  if fan_controller == fan_controller_data[0]:
    pass

  else:
    fan_controller_to_add = fan_controller[1:-3].replace("<", "'").replace(">", "'")

    fan_controller_dict[fan_controller_data.index(fan_controller)-1] = fan_controller_to_add


with open("jsons/fan_controller_list.json", "w") as fan_controller_json_file:
  fan_controller_json_file.write('')
  json.dump(fan_controller_dict, fan_controller_json_file)

