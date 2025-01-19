import json

# followers
f = open('./followers_1.json')
data = json.load(f)

follower = []

for i in data:
    for j in i["string_list_data"]:
        follower.append(j["value"])

# following
f = open('./following.json')
data = json.load(f)

following = []

for i in data["relationships_following"]:
    for j in i["string_list_data"]:
        following.append(j["value"])

# cek yang gak follow
unfollow = []

for i in following:
    if i in follower:
        unfollow.append(i)

print("\n List of users who aren't follback:")

for i in following:
    if i not in unfollow:
        print(f"{no}. {i}")
        
