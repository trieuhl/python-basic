"""
1. Lặp lại code mẫu, kiểm tra số dương, thay a = -4, b = 0, c = 5
2. Lặp lại code mẫu, kiểm tra tính chia hết của 9 chia 4; 8 chia 2
3. Viết code: cho một số a, kiểm tra và in ra màn hình a là số chẵn hay số lẻ
4. Viết code: nhập vào một số x bất kỳ, kiểm tra x có vừa chia hết cho 5 vừa lớn hơn 10 hay không? ví dụ x = 20 là vừa chia hết cho 5, vừa lớn hơn 10
5. Viết code: nhập vào một số y bất kỳ, kiểm tra y có vừa chia hết cho 2 vừa nhỏ hơn 10 hay không? ví dụ y = 4 là vừa chia hết cho 2, vừa nhỏ hơn 10
6. Viết code: nhập vào ba số a, b, c bất kỳ và in ra màn hình số lớn nhất
"""


# kiem tra so duong, so am
def kiem_tra_so_duong(x):
    if x > 0:
        print(x, " la so duong")
    elif x < 0:
        print(x, " la so am")
    else:
        print("day la so 0")


# kiem tra tinh chia het
def chia_het(a, b):
    c = a % b
    if c == 0:
        print(a, " chia het cho ", b)
    else:
        print(a, " khong chia het cho ", b)

    print("so du = ", c)


# kiem tra tinh chan, le
def chan_le(a):
    if a % 2 == 0:
        print(a, " la so chan")
    else:
        print(a, " la so le")


# kiem tra chia het cho 5, > 10
def mod3_smaller10(a):
    if (a % 3 == 0) and (a < 10):
        print(a, " vua chia het cho 3, vua nho hon 10")
    else:
        print(a, " khong thoa man")


# tim so lon nhat
def so_lon_nhat(a, b, c):
    max = a
    if b > max:
        max = b
    if c > max:
        max = c
    return max


if __name__ == '__main__':
    print("Bai 1. Kiem tra so duong, so am")
    a = -4
    kiem_tra_so_duong(a)

    b = 0
    kiem_tra_so_duong(b)

    c = 5
    kiem_tra_so_duong(c)

    print()
    print("--------------------")
    print("Bai 2. Kiem tra tinh chia het")
    d = 9
    e = 4
    chia_het(d, e)

    print()
    g = 8
    f = 2
    chia_het(g, f)

    print()
    print("--------------------")
    print("Bai 3. Kiem tra tinh chan le")
    a = 13
    chan_le(a)

    print("--------------------")
    print("Bai 3. Kiem tra tinh chan le")
    a = 13
    chan_le(a)

    print("--------------------")
    print("Bai 4. Kiem tra chia het cho 3, < 10")
    x = 6
    mod3_smaller10(x)
    x = 12
    mod3_smaller10(x)
    x = 7
    mod3_smaller10(x)

    print("--------------------")
    print("Bai 5. Tim so lon nhat")
    a = 2
    b = 5
    c = 3
    max = so_lon_nhat(a, b, c)
    print(a, b, c, "so lon nhat la ", max)

    """
    # ------------- OUTPUT -------------
    Bai 1. Kiem tra so duong, so am
    -4  la so am
    day la so 0
    5  la so duong
    
    --------------------
    Bai 2. Kiem tra tinh chia het
    9  khong chia het cho  4
    so du =  1
    
    8  chia het cho  2
    so du =  0
    
    --------------------
    Bai 3. Kiem tra tinh chan le
    13  la so le
    --------------------
    Bai 3. Kiem tra tinh chan le
    13  la so le
    --------------------
    Bai 4. Kiem tra chia het cho 3, < 10
    6  vua chia het cho 3, vua nho hon 10
    12  khong thoa man
    7  khong thoa man
    --------------------
    Bai 5. Tim so lon nhat
    2 5 3 so lon nhat la  5
    # ------------- OUTPUT -------------
    """
