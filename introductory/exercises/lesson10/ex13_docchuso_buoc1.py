if __name__ == '__main__':

    n = 123
    print("n = ", n)
    print("-----------------")

    # n = abc
    # buoc 1: tinh chu so hang tram (a)
    a = n // 100
    print("a = ", a)
    print("cach doc: ", a, "TRAM")
    print("-----------------")

    # buoc 2: lay ra bc
    bc = n % 100
    print("bc = ", bc)

    # buoc 3: lay ra b
    b = bc // 10
    print("b = ", b)
    print("cach doc: ", b, "CHUC")
    print("-----------------")

    # buoc 4: lay ra c
    c = bc % 10
    print("c = ", c)
    print("cach doc: ", c, "DON VI")

    """
    # ------------- OUTPUT -------------
    n =  123
    -----------------
    a =  1
    cach doc:  1 TRAM
    -----------------
    bc =  23
    b =  2
    cach doc:  2 CHUC
    -----------------
    c =  3
    cach doc:  3 DON VI
    # ------------- OUTPUT -------------
    """
