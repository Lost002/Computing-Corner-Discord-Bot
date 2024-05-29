from pcpartpicker import API
import json

api = API()

print(f"_DEBUG: SUPPORTED PARTS: {api.supported_parts}\n")


monitor_data = str(api.retrieve("monitor"))


monitor_data = monitor_data.split("Monitor")


monitor_dict = {}
monitor_list = []
for monitor in monitor_data:
  if monitor == monitor_data[0]:
    pass

  else:
    monitor_to_add = monitor[1:-3].replace("<", "'").replace(">", "'")

    monitor_dict[monitor_data.index(monitor)-1] = monitor_to_add


with open("jsons/monitor_list.json", "w") as monitor_json_file:
  monitor_json_file.write('')
  json.dump(monitor_dict, monitor_json_file)

