#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number < 0:
    print("{} is {}".format(number, "negative"))
elif number == 0:
    print("{} is {}".format(number, "zero"))
else:
    print("{} is {}".format(number, "positive"))
