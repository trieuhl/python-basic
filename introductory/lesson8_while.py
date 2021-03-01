# tong day so
def day_so_le():
    a = 1
    print(a)

    while a < 21:
        a += 2
        print(a)


# nhap ten
def nhap_ten():
    ten = input("Hay nhap vao ten cua ban: ")
    print()

    # vong lap
    while ten != "Nam":
        print("Ban vua nhap: ", ten)
        print("Ten khong dung.")
        print()
        ten = input("Hay nhap lai ten cua ban: ")

    print("Chao mung: ", ten)

    return

# nhap ten gioi han so lan
def nhap_ten_gioi_han():
    ten = input("Hay nhap vao ten cua ban: ")
    print()

    so_lan = 1

    # vong lap
    while (ten != "Nam") and (so_lan < 3):
        print("Ban vua nhap: ", ten)
        print("Ten khong dung.")
        print()

        # nhap lai ten
        ten = input("Hay nhap lai ten cua ban: ")

        # cap nhat so lan
        so_lan += 1

    if so_lan < 3:
        print("Chao mung: ", ten)
    else:
        print("Ba da nhap qua so lan. Dang nhap khong thanh cong.")

    return

# so sanh for va while
def for_and_while():
    print("1. Vong lap for")
    for i in range(5):
        print(i)

    print("2. Vong lap while")
    j = 0
    while j < 5:
        print(j)
        j = j + 1

# cau lenh break
def lenh_break():

    # while
    print("while: tinh tong")
    sum = 0
    i = 0
    while sum < 20 and i < 100:
        sum += i
        print(i, sum)
        i += 1

    print(sum)

    # for
    print("for: tinh tong")
    sum = 0
    for i in range(100):
        sum += i
        print(i, sum)
        if sum >= 20:
            break
    print(sum)

if __name__ == '__main__':
    # day so le
    print("In ra day so le")
    day_so_le()

    # nhap ten
    print()
    print("Bai toan nhap ten")
    nhap_ten()

    # nhap ten gioi han so lan
    print()
    print("Bai toan nhap ten co gioi han so lan")
    nhap_ten_gioi_han()

    # so sanh for va while
    print()
    print("So sanh for va while")
    for_and_while()

    # cau lenh break
    print()
    print("Cau lenh break")
    lenh_break()


    """
    # ------------- OUTPUT -------------
    In ra day so le
    1
    3
    5
    7
    9
    11
    13
    15
    17
    19
    21
    
    Bai toan nhap ten
    Hay nhap vao ten cua ban: Nam
    
    Chao mung:  Nam
    
    Bai toan nhap ten co gioi han so lan
    Hay nhap vao ten cua ban: Viet
    
    Ban vua nhap:  Viet
    Ten khong dung.
    
    Hay nhap lai ten cua ban: Ha
    Ban vua nhap:  Ha
    Ten khong dung.
    
    Hay nhap lai ten cua ban: Noi
    Ba da nhap qua so lan. Dang nhap khong thanh cong.
    
    So sanh for va while
    1. Vong lap for
    0
    1
    2
    3
    4
    2. Vong lap while
    0
    1
    2
    3
    4
    
    Cau lenh break
    while: tinh tong
    0 0
    1 1
    2 3
    3 6
    4 10
    5 15
    6 21
    21
    for: tinh tong
    0 0
    1 1
    2 3
    3 6
    4 10
    5 15
    6 21
    21
    # ------------- OUTPUT -------------
    """
