from pcpartpicker import API
import json

api = API()

print(f"_DEBUG: SUPPORTED PARTS: {api.supported_parts}\n")


cpu_data = str(api.retrieve("cpu"))


## Parse cpu data
cpu_data = cpu_data.split("CPU")


cpu_dict = {}
cpu_list = []
for cpu in cpu_data:
  if cpu == cpu_data[0]:
    pass

  else:
    cpu_to_add = cpu[1:-3].replace("<", "'").replace(">", "'")

    cpu_dict[cpu_data.index(cpu)-1] = cpu_to_add


with open("jsons/cpu_list.json", "w") as cpu_json_file:
  cpu_json_file.write('')
  json.dump(cpu_dict, cpu_json_file)

