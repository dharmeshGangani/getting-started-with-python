x = 24
# y = 206
# if x == y:
#     print("successful")
# else
#     print("not successful")

z = 0
print()
try:
    print (x/z)
except ZeroDivisionError as zde:
    print("Not allowed to divide by Zero: " + str(zde))
else:
    print("something else went wrong!!")
finally:
    print("clean-up code")
