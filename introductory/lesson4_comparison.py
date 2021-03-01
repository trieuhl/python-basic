if __name__ == '__main__':
    # so sanh lon hon, nho hon
    print("So sanh lon hon, nho hon")
    a = 1
    s1 = a > 0
    print(s1)

    b = 2
    s2 = b < 0
    print(s2)

    print("3 < 4 ", 3 < 4)
    print("5 > 6 ", 5 > 6)

    # so sanh bang
    print()
    print("So sanh bang")
    c = 7
    print(c == 7)

    d = 0.125
    e = 1.3
    print(d, "=", e, d == e)

    quoc_gia = "Viet Nam"
    dat_nuoc = "Viet Nam"
    chau_luc = "Chau A"
    world_cup = "Quatar 2022"
    print(quoc_gia, "=", dat_nuoc, quoc_gia == dat_nuoc)
    print(dat_nuoc, "=", chau_luc, dat_nuoc == chau_luc)
    print(chau_luc, "=", world_cup, chau_luc == world_cup)

    # so sanh khac
    print()
    print("So sanh khac")
    a = 1
    b = 2
    c = 1
    print(a, " khac ", b, a != b)
    print(a, " khac ", c, a != c)
    print(dat_nuoc, " khac ", chau_luc, dat_nuoc != chau_luc)

    # so sanh lon hon bang, nho hon bang
    print()
    print("So sanh lon hon bang, nho hon bang")
    print("2 >= 0", 2 >= 0)
    print("3 <= 1", 3 <= 1)

    """
    # ------------- OUTPUT -------------
    So sanh lon hon, nho hon
    True
    False
    3 < 4  True
    5 > 6  False
    
    So sanh bang
    True
    0.125 = 1.3 False
    Viet Nam = Viet Nam True
    Viet Nam = Chau A False
    Chau A = Quatar 2022 False
    
    So sanh khac
    1  khac  2 True
    1  khac  1 False
    Viet Nam  khac  Chau A True
    
    So sanh lon hon bang, nho hon bang
    2 >= 0 True
    3 <= 1 False
    # ------------- OUTPUT -------------
    """
