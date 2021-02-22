if __name__ == '__main__':
    a = 1
    b = 2
    c = 3
    d = 4
    e = 5
    f = 6

    # phep cong
    t1 = a + b
    print("phep cong hai so")
    print(a)
    print(b)
    print(t1)
    print("ket qua = ", t1)

    # phep tru
    print()
    print("phep tru hai so")
    t2 = c - d
    print(c, "-", d, "=", t2)

    # phep nhan
    print()
    print("phep nhan")
    print(e, f, e * f)

    # phep chia
    print()
    print("phep chia")
    t3 = d / c
    print(d, "/", c, " = ", t3)

    # phep gan
    print()
    print("phep gan")
    g = 7
    print("g = ", g)
    g = g + 1
    print("g = ", g)

    print()
    g = 7
    print("g = ", g)
    g += 1
    print("g = ", g)

    print()
    h = 8
    print("h = ", h)
    h *= 2
    print("h = ", h)

    """
    # ------------- OUTPUT -------------
    phep cong hai so
    1
    2
    3
    ket qua =  3
    
    phep tru hai so
    3 - 4 = -1
    
    phep nhan
    5 6 30
    
    phep chia
    4 / 3  =  1.3333333333333333
    
    phep gan
    g =  7
    g =  8
    
    g =  7
    g =  8
    
    h =  8
    h =  16
    # ------------- OUTPUT -------------
    """
