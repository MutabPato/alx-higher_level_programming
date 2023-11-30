#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 1
    len = len(sys.argv)
    print("{} {}".format(
        len - 1,
        "arguments." if len == 1 else "argument:" if len == 2 else "arguments:"
        ))
    for argument in sys.argv[1:]:
        print("{}: {}".format(i, argument))
        i += 1
