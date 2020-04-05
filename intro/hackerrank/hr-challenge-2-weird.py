# HackerRank challenge 2, to determing weird / not weird numbers

num = int(input())

if num < 1 or num > 100:
    print('Not Weird')
else:
    if (num % 2) > 0:
        # print('odd number')
        print('Weird')
    else:
        # print('even number')
        if (num >= 2 and num <=5) or (num > 20):
            print('Not Weird')
        else:
            print('Weird')
