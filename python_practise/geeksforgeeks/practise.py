def remove_duplicates(string):
    return_str = ''
    for char in string:
        if char not in return_str:
            return_str += char
    print(return_str)
    return return_str


def robots(instructions):
    """
    Input : move = "UDDLRL"
    Output : (-1, -1)
    Move U : (0, 0)--(0, 1)
    Move D : (0, 1)--(0, 0)
    Move D : (0, 0)--(0, -1)
    Move L : (0, -1)--(-1, -1)
    Move R : (-1, -1)--(0, -1)
    Move L : (0, -1)--(-1, -1)

    Therefore final position after the complete
    movement is: (-1, -1)

    Input : move = "UDDLLRUUUDUURUDDUULLDRRRR"
    Output : (2, 3)

    """

    class Robot:
        def __init__(self):
            """ Initial co-ordinates are (0, 0) """
            self.x = 0
            self.y = 0

        def move_up(self, step=1):
            """
                Moving one step upward increases 1 unit in the Y co-ordinates.

                      ↑ y
                      \
                -x    \     x
                <----------->
                      \
                      \
                      ↓ -y
            """
            print('MOVE U: {}'.format(self), end=' -- ')
            self.y += step
            print(self)

        def move_down(self, step=1):
            """
                Moving one step downward decreases 1 unit in the Y co-ordinates.

                      ↑ y
                      \
                -x    \     x
                <----------->
                      \
                      \
                      ↓ -y
            """
            print('MOVE D: {}'.format(self), end=' -- ')
            self.y -= step
            print(self)

        def move_left(self, step=1):
            """
                Moving one step leftward decreases 1 unit in the X co-ordinates.

                      ↑ y
                      \
                -x    \     x
                <----------->
                      \
                      \
                      ↓ -y
            """
            print('MOVE L: {}'.format(self), end=' -- ')
            self.x -= step
            print(self)

        def move_right(self, step=1):
            """
                Moving one step leftward increases 1 unit in the X co-ordinates.

                      ↑ y
                      \
                -x    \     x
                <----------->
                      \
                      \
                      ↓ -y
            """
            print('MOVE R: {}'.format(self), end=' -- ')
            self.x += step
            print(self)

        def __str__(self):
            """ Represents robot's current position in format (x, y) """
            return '({}, {})'.format(self.x, self.y)

    def operate_robot(instructions):
        """ Decompile the instructions and operate the robot """
        robot = Robot()

        # Let's create a map of instruction to the corresponding robot operation
        operation_map = {
            'u': robot.move_up,
            'd': robot.move_down,
            'l': robot.move_left,
            'r': robot.move_right
        }

        for instruction in instructions.lower():
            operation = operation_map[instruction]  # operation_map['u'] -> robot.move_up, etc.
            operation()  # Technically, operation() is equal to robot.move_up()

    operate_robot(instructions)


def second_largest_value(dictionary):
    # l = list(dictionary.values())
    # l.sort()
    # return l[1]
    return sorted(dictionary.values())[1]


def remove_spaces(dictionary):
    return {k.translate({ord(' '): None}): v for (k, v) in dictionary.items()}


# remove_duplicates('geeksforgeeks')
# robots("UDDLRL")
# robots("UDDLLRUUUDUURUDDUULLDRRRR")

d = {'a 1': 100, 'b 2': 101, 'c 3': 100.5}
# slv = second_largest_value(d)
# print(slv)

r = remove_spaces(d)
print(d)
print(r)

# print('a 3'.translate({ord('a'): 'apples'}))
