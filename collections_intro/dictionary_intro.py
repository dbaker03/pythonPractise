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