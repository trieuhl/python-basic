# Cau lenh lap
def cau_lenh_lap():
    a = 6
    print("Cac so tu 0 den ", a - 1)
    for i in range(a):
        print(i)

    print()
    b = 2
    c = 6
    print("Cac so tu ", b, " den ", c - 1)
    for j in range(b, c):
        print(j)

    so_lan = 3
    print()
    print("In dong chu ")
    for k in range(so_lan):
        print(k, "Toi yeu Viet Nam")


# Tinh tong
def sum_loop(a):
    sum = 0

    for i in range(a):
        sum = sum + i
        print("Vong lap hien tai: ", i)
        print("Tong hien tai = ", sum)
        print()

    return sum


# Tinh tich
def multi_loop(a, b):
    tich = 1

    for j in range(a, b):
        tich = tich * j
        print("Vong lap hien tai: ", j)
        print("Tich hien tai = ", tich)
        print()

    return tich


# chia het cho 5
def chia_het_cho_3(a):
    so_luong = 0

    for i in range(a):
        if i % 3 == 0:
            print(i)
            so_luong += 1

    print("So luong: ", so_luong)


if __name__ == '__main__':
    # Cau lenh lap
    print("Cau lenh lap")
    cau_lenh_lap()

    # Tinh tong
    print()
    print("-----------------")
    print("Tinh tong")
    a = 4
    tong = sum_loop(a)
    print("Tong la: ", tong)

    # Tinh tich
    print()
    print("-----------------")
    print("Tinh tich")
    b = 2
    c = 5
    tich = multi_loop(b, c)
    print("Tich la: ", tich)

    # Chia het
    print()
    print("-----------------")
    print("Chia het cho 3, < 10")
    chia_het_cho_3(10)

    """
    # ------------- OUTPUT -------------
    Cau lenh lap
    Cac so tu 0 den  5
    0
    1
    2
    3
    4
    5
    
    Cac so tu  2  den  5
    2
    3
    4
    5
    
    In dong chu 
    0 Toi yeu Viet Nam
    1 Toi yeu Viet Nam
    2 Toi yeu Viet Nam
    
    -----------------
    Tinh tong
    Vong lap hien tai:  0
    Tong hien tai =  0
    
    Vong lap hien tai:  1
    Tong hien tai =  1
    
    Vong lap hien tai:  2
    Tong hien tai =  3
    
    Vong lap hien tai:  3
    Tong hien tai =  6
    
    Tong la:  6
    
    -----------------
    Tinh tich
    Vong lap hien tai:  2
    Tich hien tai =  2
    
    Vong lap hien tai:  3
    Tich hien tai =  6
    
    Vong lap hien tai:  4
    Tich hien tai =  24
    
    Tich la:  24
    
    -----------------
    Chia het cho 3, < 10
    0
    3
    6
    9
    So luong:  4
    # ------------- OUTPUT -------------
    """