# In ra cac so tu 0 den 9
def bai7_1():
    print()
    print("-----------------------")
    print("Bai 7.1. In ra cac so tu 0 den 9")
    for i in range(10):
        print(i)


# In ra cac so tu 123 den 134
def bai7_2(a, b):
    print()
    print("-----------------------")
    print("Bai 7.2. In ra cac so tu 123 den 134")
    for i in range(a, b + 1):
        print(i)


# In ra dong chu "Viet Nam" 10 lan
def bai7_3():
    print()
    print("-----------------------")
    print("Bai 7.3. In dong chu Viet Nam 10 lan")
    for i in range(10):
        print(i + 1, " Viet Nam")


# Tinh tong cac so tu 0 den 9, 100 den 1000
def bai7_4_sum(a, b):
    print()
    print("-----------------------")
    print("Bai 7.4. Tinh tong cac so tu a den b")
    sum = 0
    for i in range(a, b + 1):
        sum += i
    print("Tong tu ", a, " den ", b, " la: ", sum)


# Tinh tich cac so tu 4 den 6, 5 den 10
def bai7_5_tich(a, b):
    print()
    print("-----------------------")
    print("Bai 7.5. Tinh tich cac so tu a den b")
    tich = 1
    for i in range(a, b + 1):
        tich *= i
    print("Tich tu ", a, " den ", b, " la: ", tich)


# Cac so chia het cho 5 va <= 100
def bai7_6_chiahet():
    print()
    print("-----------------------")
    print("Bai 7.6. Cac so chia het cho 5 va <= 100")
    so_luong = 0
    for i in range(101):
        if i % 5 == 0:
            print(i)
            so_luong += 1
    print("So luong: ", so_luong)


if __name__ == '__main__':
    # bai 7.1
    bai7_1()

    # bai 7.2
    bai7_2(123, 134)

    # bai 7.3
    bai7_3()

    # bai 7.4
    bai7_4_sum(0, 9)
    bai7_4_sum(100, 1000)

    # bai 7.5
    bai7_5_tich(4, 6)
    bai7_5_tich(5, 10)

    # bai 7.6
    bai7_6_chiahet()
