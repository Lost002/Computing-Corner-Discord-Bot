from QOTD import QOTD
from games import games
import json
from pcpp import PCPP

def get_response(user_input) -> str:
    responses = json.load(open('responses.json'))

    command = user_input.lower()

    if command[:1] == "?":
        command = command[1:]

        if command == "qotd":
            return QOTD()
        
        elif command == "embed":
            return ["TEST EMBED", "A SIMPLE EMBED", 0x0000FF]

        elif command in str(responses["FCI"]):
            return [
                str(responses[command]["title"]),str(responses[command]["desc"]),int(responses[command]["color"],16)]
        
        elif command == "good bot":
            return "Yes!"
        
        elif command[:4] == "game":
            print("GAME TIME")
            games(command[4:])
        
        elif command[:4] == "pcpp":
            return PCPP(command[4:])
        
        elif command == "color_roles":
            return "<COLOR_ROLES>"
        
        else:
            return "Sorry! I don't know that command yet!"