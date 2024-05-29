import json
from os import path

def PCPP(args):
    parts = json.load(open("PCPP.json"))
    spec_names = json.load(open("pretty_print_specs.json"))

    args = args.split()


    if len(args) == 1 or len(args) == 2:
        return ["Specify More", "?pcpp [part] [manufacturer] [model/filter=[filter]]", 0xFF0000]

    elif len(args) > 3:
        model = ""
        for arg in args:
            if args.index(arg) <= 1:
                pass
            else:
                model += arg
    
    elif len(args) == 3:
        model = args[2].upper()
    


    model = model.upper()
    part = args[0].upper()
    manu = args[1].upper()

    print(part, manu, model)

    if part in parts:
        file = parts[part]
        
        all_parts_selected = json.load(open("PcPartPickerBot/" + file))
            
        print(f"{part}, is a valid selection")
    else:
        return [f"No Valid Selections Found for, {part}", "?pcpp [part] [manufacturer] [model]", 0xFF0000]

    manu_found = False
    for part_number in all_parts_selected:
        if manu == all_parts_selected[part_number][0].upper():
            manu_found = True
            break
 
    if not manu_found:   
        return [f"No Valid Selections Found for, {manu}", "?pcpp [part] [manufacturer] [model]", 0xFF0000]
    
    print(f"{manu}, found")

    parts_found = []
    for part_number in all_parts_selected:
        if model in all_parts_selected[part_number][1].upper().replace(" ", ""):
            parts_found.append(all_parts_selected[part_number])
    
    if len(parts_found) == 0:
        return [f"No Valid Selections Found for, {model}", "?pcpp [part] [manufacturer] [model]", 0xFF0000]

    else:
        found_parts = ""
        part_grouping = file.replace(".json", "")
        for part_found in parts_found:
            found_parts += f"__**{part_found[0]} {part_found[1]}**__\n"
            kind_of_part = file.replace(".json", "")
            labels = spec_names[kind_of_part]
            #
            #max = 0
            #for label in labels:
            #    if len(label) > max:
            #        max = len(label)

            for spec in part_found:

                found_parts += f"- **{labels[part_found.index(spec)]}:  {spec}**\n"

                #found_parts += labels[part_found.index(spec)]
                #
                #for separate in range(max):
                #    found_parts += " "
                #
                #found_parts += f": {spec}\n"

            found_parts += "\n\n"


        return [f"Search for {model}",found_parts.replace("Money: ", "Cost: $"), 0x00000FF]


    #if path.isfile("PcPartPickerBot/" + part + ".json") or path.isfile("PcPartPickerBot/" + part + "S.json"):
    #    print("valid")
    #    return f"{part}, is a valid selection"