import json
from os import system

CPU_DICT_PARSED = {}

with open("jsons/cpu_list.json", "r") as cpu_list_unparsed:
  cpu_list = json.load(cpu_list_unparsed)

needed = ["brand", "model", "cores", "base_clock", "boost_clock", "tdp", "integrated_graphics", "multithreading", "price"]
for cpu_num in cpu_list:
  data = cpu_list[cpu_num]


  has_needed = []
  for need in needed:
    if need in data:
      has_needed.append(need)

  if has_needed == needed:

    def Bytes(total):
      return total
  
  def ClockSpeed(cycles):
    return cycles
  
  exec(f"""
  
def parse({data}):
  CPU_DICT_PARSED[{cpu_num}] = [brand, model, cores, base_clock, boost_clock, tdp, integrated_graphics, multithreading, price]
  """)
  
  parse()


  
with open("jsons/CPU_JSON_PARSED.json", "w") as CPU_JSON_PARSED:
  CPU_JSON_PARSED.write("")
  json.dump(CPU_DICT_PARSED, CPU_JSON_PARSED)

with open("CPUS.json", "w") as format:
  format.write("")

system("cat jsons/CPU_JSON_PARSED.json | jq > CPUS.json")