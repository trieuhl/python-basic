def kiem_tra_so_duong(x):
    if x > 0:
        print(x, " la so duong")
    elif x < 0:
        print(x, " la so am")
    else:
        print("day la so 0")


def chia_het(a, b):
    c = a % b
    if c == 0:
        print(a, " chia het cho ", b)
    else:
        print(a, " khong chia het cho ", b)

    print("so du = ", c)


if __name__ == '__main__':
    print("kiem tra so duong, so am")
    a = 1
    kiem_tra_so_duong(a)

    b = -3
    kiem_tra_so_duong(b)

    c = 0
    kiem_tra_so_duong(c)

    print()
    print("kiem tra tinh chia het")
    d = 6
    e = 2
    chia_het(d, e)

    print()
    g = 7
    f = 3
    chia_het(g, f)

    """
    # ------------- OUTPUT -------------
    kiem tra so duong, so am
    1  la so duong
    -3  la so am
    day la so 0
    
    kiem tra tinh chia het
    6  chia het cho  2
    so du =  0
    
    7  khong chia het cho  3
    so du =  1
    # ------------- OUTPUT -------------
    """
