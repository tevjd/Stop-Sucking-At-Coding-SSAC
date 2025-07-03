#!/usr/bin/env python3
"""A python file to learn how to use for loop"""

a_string = "123"
a_list = [1, 2, 3]
a_tuple = (1, 2, 3)
a_range = range(1, 4)
a_2D_list = ["toto", range(3), ["t", "o", "t", "o"]]
a_2D_tuple = ([1, 2, 3], [4, 5, 6])
a_3D_list = [[[1, 2], [3, 4]], [[5, 6]]]

def go_through(data_structure):
    """Function to go through a data structure with for loop"""

    print(f"Here is all the elements of the data structure: {data_structure}")

    stack = [data_structure]

    while stack : 
        current = stack.pop()

        if isinstance(current, str):
            for elem in current:
                print(elem)

        elif isinstance(current, range):
            for elem in current:
                print(elem)

        elif isinstance(current, (list, tuple)):
            for elem in reversed(current):
                stack.append(elem)

        else:
            print(current)

go_through(a_string)
go_through(a_list)
go_through(a_tuple)
go_through(a_range)
go_through(a_2D_tuple)
go_through(a_2D_list)
go_through(a_3D_list)
