marvel_characters = {"Iron Man", "Thor", "Captain America"}

print(marvel_characters, type(marvel_characters))
#there is no order - it will print out randomly

marvel_characters.add("Hawkeye")
print(marvel_characters.pop())
marvel_characters.discard("Iron Man")

marvel_characters.add("Thor")
#we can add multiple same values without error but it will remove duplicates


nums = [1,2,3,4,5,6,7,8,9]

#Frozen set
fs = frozenset(nums)
print(fs, type(fs))
#similar to set but immutable, cant pop or add


