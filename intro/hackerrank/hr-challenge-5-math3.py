# HackerRank challenge 3, Math: Power test

n = int(input())

if n >= 1 and n <= 20:
    for idx in range(0, n):
        print(idx**2)
