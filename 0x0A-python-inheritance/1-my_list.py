#!/usr/bin/python3
"""

list: parent class

"""


class MyList(list):
    """

    MyList: inherits from list

    """

    def print_sorted(self):
        """

        print a sorted list

        """

        print(sorted(self))
