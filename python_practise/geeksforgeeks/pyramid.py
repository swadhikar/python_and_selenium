def pyramidize(rows=1):
    """
    *
    * *
    * * *
    * * * *
    * * * * *
    """
    for _ in range(1, rows + 1):
        print(' * ' * _)


def de_pyramidize(rows):
    """
                  *
                **
              ***
            ****
          *****
        ******
      *******
    """
    maximum = rows
    for i in range(1, rows + 1):
        stars = '*' * i
        spaces = '  ' * (maximum - len(stars))
        print(spaces + stars)


if __name__ == '__main__':
    # pyramidize(10)
    de_pyramidize(10)
