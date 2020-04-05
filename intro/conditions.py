# price = 125
# tax = 0
# if price > 100:
#     tax = 0.7
# else:
#     tax = 0
# print(tax)
#
# country = "CANADA"
# if country.lower() == "canada":
#     print("Hello Canadian !!!")
# else:
#     print("Non Canadian !")

# price = input("How much did you pay?")
#
# price = float(price)
# if price > 1:
#     tax = 0.7
# else:
#     tax = 0
# print("Tax rate is " + str(tax))


# country = input("What country you live in?")
#
# if country.lower() == "canada":
#     province = input("enter province:")
#     if province in ("Alberta", "Nunawat"):
#         tax = 0.07
#     elif province == "Ontario":
#         tax = 0.13
#     else:
#         tax = 0.15
# else:
#     tax = 0
# print(tax)

gpa = float(input("what is your GPA score?"))
low_grade = float (input("what is your lowest grade?"))

if gpa >= 0.85 and low_grade <=70:
    honour_roll = True
else:
    honour_roll = False

if honour_roll:
    print("well done")
else:
    print("Needs more work!!")
