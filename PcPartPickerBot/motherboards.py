from pcpartpicker import API
import json

api = API()

print(f"_DEBUG: SUPPORTED PARTS: {api.supported_parts}\n")


motherboard_data = str(api.retrieve("motherboard"))


## Parse motherboard data
motherboard_data = motherboard_data.split("Motherboard")


motherboard_dict = {}
motherboard_list = []
for motherboard in motherboard_data:
  if motherboard == motherboard_data[0]:
    pass

  else:
    motherboard_to_add = motherboard[1:-3].replace("<", "'").replace(">", "'")

    motherboard_dict[motherboard_data.index(motherboard)-1] = motherboard_to_add


with open("jsons/motherboard_list.json", "w") as motherboard_json_file:
  motherboard_json_file.write('')
  json.dump(motherboard_dict, motherboard_json_file)

