def tong_tich_cach1(n):
    print()
    print("Cach 1:")
    tong = 0
    tich = 1

    for i in range(1, n + 1):
        tich *= i
        tong += tich

        print(i, tong)

    return tong


def tong_tich_cach2(n):
    print()
    print("Cach 2:")

    s = 0

    for i in range(1, n + 1):

        a = 1
        for j in range(1, i + 1):
            a = a * j
        s = s + a

        print(i, s)

    return s


if __name__ == '__main__':
    n = input("Nhap vao n: ")
    n = int(n)

    print("S(n) = 1 + 1*2 + 1*2*3 + ... + 1*2*...*N")

    s1 = tong_tich_cach1(n)
    s2 = tong_tich_cach2(n)
    print("Ket qua: ", s1, s2)

    """
    # ------------- OUTPUT -------------
    Nhap vao n: 5
    S(n) = 1 + 1*2 + 1*2*3 + ... + 1*2*...*N
    
    Cach 1:
    1 1
    2 3
    3 9
    4 33
    5 153
    
    Cach 2:
    1 1
    2 3
    3 9
    4 33
    5 153
    Ket qua:  153 153
    # ------------- OUTPUT -------------
    """
