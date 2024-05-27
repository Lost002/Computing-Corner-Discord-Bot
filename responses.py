from QOTD import QOTD
import json

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
        
        else:
            return "Sorry! I don't know that command yet!"