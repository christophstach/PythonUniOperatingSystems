from random import randint

loopsDice = 1200
min = 0
max = 5
numbers = [0, 0, 0, 0, 0, 0]


for i in range(loopsDice):
    rnd = randint(min, max)
    numbers[rnd] += 1


print(numbers)

loopSqrt = int(loopsDice / (max - min + 1))


for o in range(loopSqrt):
    if (o * o) == loopSqrt:
        print(o)
