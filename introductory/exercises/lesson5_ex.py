if __name__ == '__main__':
    # and
    print("phep AND")
    a = 5
    b = 1
    s1 = a > 0
    s2 = b > 5
    t3 = s1 and s2
    print(s1, " and ", s2, " = ", t3)

    # or
    print()
    print("phep OR")
    c = -1
    d = 0
    t4 = (a > 0) or (c < 1)
    print((a > 0), " or ", (c < 1), " = ", t4)

    # not
    print()
    print("phep NOT")
    e = -2
    s6 = e > 0
    print(s6)
    s7 = not s6
    print(s7)

    """
    # ------------- OUTPUT -------------
    phep AND
    True  and  True  =  True
    
    phep OR
    True  or  True  =  True
    
    phep NOT
    False
    True
    # ------------- OUTPUT -------------
    """
