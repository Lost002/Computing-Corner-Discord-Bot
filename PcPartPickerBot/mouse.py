from pcpartpicker import API
import json

api = API()

print(f"_DEBUG: SUPPORTED PARTS: {api.supported_parts}\n")


mouse_data = str(api.retrieve("mouse"))


mouse_data = mouse_data.split("Mouse")


mouse_dict = {}
mouse_list = []
for mouse in mouse_data:
  if mouse == mouse_data[0]:
    pass

  else:
    mouse_to_add = mouse[1:-3].replace("<", "'").replace(">", "'")

    mouse_dict[mouse_data.index(mouse)-1] = mouse_to_add


with open("jsons/mouse_list.json", "w") as mouse_json_file:
  mouse_json_file.write('')
  json.dump(mouse_dict, mouse_json_file)

