from pcpartpicker import API
import json

api = API()

print(f"_DEBUG: SUPPORTED PARTS: {api.supported_parts}\n")


power_supply_data = str(api.retrieve("power-supply"))


power_supply_data = power_supply_data.split("PSU")


power_supply_dict = {}
power_supply_list = []
for power_supply in power_supply_data:
  if power_supply == power_supply_data[0]:
    pass

  else:
    power_supply_to_add = power_supply[1:-3].replace("<", "'").replace(">", "'")

    power_supply_dict[power_supply_data.index(power_supply)-1] = power_supply_to_add


with open("jsons/power_supply_list.json", "w") as power_supply_json_file:
  power_supply_json_file.write('')
  json.dump(power_supply_dict, power_supply_json_file)

