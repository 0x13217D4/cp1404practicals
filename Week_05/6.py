import json
# name_and_age = {"Cliff":56,"Lea":34}
# json_name_and_age = json.dumps(name_and_age)
json_name_and_age = '{"Cliff":56,"Lea":34}'
name_and_age = json.loads(json_name_and_age)