shopping_list = ["bread", "bananas", "milk", "crisps", "fish"]
print(shopping_list, type(shopping_list))

#indexing and slicing work the same as with list

print(shopping_list[0])
print(shopping_list[-1])
print(shopping_list[::-1])

#Lists are mutable

shopping_list[0] = "sugar"
print(shopping_list)

del shopping_list[0]
print(shopping_list)

shopping_list.append("cereal")
print(shopping_list)

print(len(shopping_list))

shopping_list.remove("cereal") #note removes only the first instance
print(shopping_list)


print(shopping_list.pop())#return last item but also remove it from the list
print(shopping_list)

print(shopping_list.pop((1)))#same with 2nd item (index)







mixed_list = [True, "sugar", 18, "chocolate", 4.123, ["this", "is", "a nested list"]]
print(mixed_list)
print(mixed_list[5][1])



print(shopping_list.count("fish"))#how many times something appears - 0, not in list
print(shopping_list.index("fish"))#returns the index of the item
