#!/usr/bin/python3
for i in range(0, 8):
    for j in range(0, 10):
        if i == j:
            continue
        if i >= j:
            continue
        print("{:d}".format(i), end="")
        print("{:d}".format(j), end=", ")
print("89")
