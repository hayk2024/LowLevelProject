import json

with open('data.json', 'r') as f:
    data = json.load(f)

new_list = []

for i in data:
    if i % 3 == 0:
        new_list.append(i)

print(sum(new_list)//len(new_list))



