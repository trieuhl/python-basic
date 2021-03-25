if __name__ == '__main__':

    n = 123
    print("n = ", n)

    # n = abc
    # buoc 1: tinh chu so hang tram (a)
    a = n // 100
    print("a = ", a)
    print("cach doc: ", a, "TRAM")
    print()

    # buoc 2: lay ra bc
    bc = n % 100
    print("bc = ", bc)

    # buoc 3: lay ra b
    b = bc // 10
    print("b = ", b)
    print("cach doc: ", b, "CHUC")

    # buoc 4: lay ra c
    c = bc % 10
    print("c = ", c)
    print("cach doc: ", c)

    ketqua = a + "TRAM" + b + "CHUC" + c
    print("KET QUA: ", ketqua)