# ham tinh tong hai so
def tong_hai_so(a, b):
    sum = a + b

    return sum


# ham tinh tich ba so
def tich_ba_so(x, y, z):
    return x * y * z


# goi ham tong va tich
def tinh_toan():
    # tong hai so
    print("tong hai so")
    a = 1
    b = 2
    c = tong_hai_so(a, b)
    print(c)

    d = tong_hai_so(3, 4)
    print(d)

    # tich ba so
    print()
    print("tich ba so")
    e = tich_ba_so(2, 3, 4)
    print(e)


if __name__ == '__main__':
    tinh_toan()

    """
    # ------------- OUTPUT -------------
    tong hai so
    3
    7
    
    tich ba so
    24
    # ------------- OUTPUT -------------
    """
