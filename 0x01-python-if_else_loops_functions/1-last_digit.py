#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = int(str(number)[-1])

if last_digit > 5:
    end_tag = "and is greater than 5"
elif last_digit == 0:
    end_tag = "and is 0"
else:
    end_tag = "and is less than 6 and not 0"

print("Last digit of {} is {} {}".format(number, last_digit, end_tag))
