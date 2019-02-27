class Bunk:
    """Petrol bunk object"""

    def __init__(self, p, d):
        self.petrol = p
        self.distance = d

    def __str__(self):
        return 'Bunk({}, {})'.format(self.petrol, self.distance)


class Vehicle:
    """Vehicle object that travels through petrol bunks """

    def __init__(self, l):
        self.bunks = l
        self.petrol = 0
        self.start = l[0]

    def ride(self):
        """
            Ride through all petrol bunks. If petrol is insufficient raise Exception
        """
        for bunk in self.bunks:
            self.petrol += bunk.petrol  # Load petrol from bunk
            if self.petrol < bunk.distance:
                raise Exception('Petrol tank empty!')

            # Ride to next distance
            self.petrol -= bunk.distance  # Subtract petrol after ride


def find_start(*args):
    for i in range(len(args)):
        v = Vehicle(rotate(args, i))
        try:
            v.ride()
            return v.start
        except Exception:
            pass
    else:
        return 'No solutions!'


def rotate(l, n):
    """
        rotate([1,2,3], 1) -> [2,3,1]
        rotate([1,2,3], 2) -> [3,1,2]
    """
    return l[n:] + l[:n]


if __name__ == '__main__':
    b1 = Bunk(1, 2)
    b2 = Bunk(2, 3)
    b3 = Bunk(4, 5)
    b4 = Bunk(10, 70)
    b5 = Bunk(500, 70)

    start = find_start(b1, b2, b3, b4, b5)
    print(start)

    """
    Result:
    /usr/bin/python3.5 /home/swadhi/PycharmProjects/pyselenium/python/geeksforgeeks/petrol.py
    Bunk(200000, 70)
    """
