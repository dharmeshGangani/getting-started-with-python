# y = int(input())
#
# leap = False
#
# #     if (y % 100) == 0 and (y % 400) == 0:
# #         leap = True
# #     else:
# #         if (y % 4) == 0:
# #             leap = True
# # print(leap)
#
# if y >= 1900 and y <= 100000:
#     if y % 400 == 0:
#         leap = True
#     elif y % 100 == 0:
#         leap = False
#     elif y % 4 == 0:
#         leap = True
# print(leap)
###################################

def is_leap(year):
    leap = False

    if year >= 1900 and year <= 100000:
        if year % 400 == 0:
            leap = True
        elif year % 100 == 0:
            leap = False
        elif year % 4 == 0:
            leap = True

    return leap

year = int(input())
print(is_leap(year))
