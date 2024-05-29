from pcpartpicker import API
import json

api = API()

print(f"_DEBUG: SUPPORTED PARTS: {api.supported_parts}\n")


video_card_data = str(api.retrieve("video-card"))


video_card_data = video_card_data.split("GPU")


video_card_dict = {}
video_card_list = []
for video_card in video_card_data:
  if video_card == video_card_data[0]:
    pass

  else:
    video_card_to_add = video_card[1:-3].replace("<", "'").replace(">", "'")

    video_card_dict[video_card_data.index(video_card)-1] = video_card_to_add


with open("jsons/video_card_list.json", "w") as video_card_json_file:
  video_card_json_file.write('')
  json.dump(video_card_dict, video_card_json_file)

