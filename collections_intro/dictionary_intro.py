#key-value pairs

dataeng37 = {
    "course_name": "Data engineering 37",
    "client": "Home office",
    "trainer": "David"
}

print(dataeng37, type(dataeng37))

print(dataeng37["client"])

dataeng37["trainer"] = "David Harvey"
dataeng37["trainees"] = ["munir", "darnell", "dan"]

print(dataeng37["trainer"])
#can nest disctionaries

print(dataeng37.get("course_name"))

#get() returns none if key doesnt exist but using square brackets would return an error

print(bool(dataeng37.get("missing key")))

dataeng37.update({"course_length": "8 weeks"})
#we can add to it



game = {"name":"grand theft auto V",
       "release date":"17/09/2013",
       "budget":"265 million"}

print(game)

game["budget"] = 265000000
game["copies sold"] = 165000000
game["hours to complete"] = 31.5

print(game)

del game["budget"]

print(game)

game["characters"] = {"michael": 37, "franklin": 28, "trevor": 50}

print(game["characters"]["michael"])

print(game.values())
print(game.keys())

game.get("rating")


print(game.items())

print(f"\n\n\nGame title is {game['name']}. It takes {game['hours to complete']} hours to complete, it has a rating of {game.get('Rating')}")