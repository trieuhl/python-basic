if __name__ == '__main__':
    # so sanh lon hon, nho hon
    print("So sanh lon hon, nho hon")
    a = -2
    s1 = a > 0
    print(s1)

    b = -3
    s2 = b < 0
    print(s2)

    print("3 < 4 ", 3 < 4)
    print("5 > 6 ", 5 > 6)

    # so sanh bang
    print()
    print("So sanh bang")
    c = 6
    print(c == 7)

    d = 0.25
    e = 1.5
    print(d, "=", e, d == e)

    quoc_gia = "Nhat Ban"
    dat_nuoc = "Nhat Ban"
    chau_luc = "Chau Au"
    world_cup = "France 2022"
    print(quoc_gia, "=", dat_nuoc, quoc_gia == dat_nuoc)
    print(dat_nuoc, "=", chau_luc, dat_nuoc == chau_luc)
    print(chau_luc, "=", world_cup, chau_luc == world_cup)

    # so sanh lon hon bang, nho hon bang
    print()
    print("So sanh lon hon bang, nho hon bang")
    print("3 >= 5", 3 >= 5)
    print("4 <= 6", 4 <= 6)

    """
    # ------------- OUTPUT -------------
    So sanh lon hon, nho hon
    False
    True
    3 < 4  True
    5 > 6  False
    
    So sanh bang
    False
    0.25 = 1.5 False
    Nhat Ban = Nhat Ban True
    Nhat Ban = Chau Au False
    Chau Au = France 2022 False
    
    So sanh lon hon bang, nho hon bang
    3 >= 5 False
    4 <= 6 True
    # ------------- OUTPUT -------------
    """
