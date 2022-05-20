# age = int(input("Type age: "))
# has_ticket = True
#
# if age >= 15 and has_ticket:
#     print("You can watch this")
# elif age == 14 and has_ticket:
#     print("next year")
# else:
#     print("You can't watch")
#
# film_rating = "12A"
# #U PG 12 / 12A 15 18
#
# if film_rating == "U":
#     print("A U film should be suitable for audiences aged four years and over")
# elif film_rating == "12" or film_rating == "12A":
#     print("are suitable for children aged 12 and over")
# elif film_rating == "15":
#     print("Suitable for anyone aged 15 and over")
# elif film_rating == "18":
#     print("Suitable for anyone aged 18 and over")
# else:
#     print("Not a valid rating")

#we need a colon after each element of the if statement
#we dont have to include an else clause, so just if, if elif, if else, if elif else
#only 1 if (always) only 1 else (not mandatory) and as many elif as you want (not mandatory)

has_ticket = True
age = 25

if has_ticket:
    if age >= 15:
        print("Old enough")
    elif age == 14:
        print("nearly")
    else:
        print("Come back when older")
else:
    print("Buy a ticket")