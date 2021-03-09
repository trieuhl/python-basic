# In day so 0, 3, 6.. N, N <= 50
def bai8_1_in_day_so():
    print()
    print("-----------------------")
    print("Bai 8.1. In day so 0, 3, 6, ..., N (N khong vuot qua 50)")
    n = 0
    while n <= 50:
        print(n)
        n += 3


# Tinh tong day so 0 + 3 + 6 + ... N, (dung khi tong vuot qua 100)
def bai8_2_tong_day_so():
    print()
    print("-----------------------")
    print("Bai 8.2. Tong day so: S = 0 + 3 + 6 + ... + N (dung khi S vuot qua 100)")
    n = 0
    S = 0
    while S <= 100:
        n += 3
        S += n
        print(n, S)

    print("Tong la: ", S)


def bai8_3_nhap_ten_gioi_han():
    print()
    print("-----------------------")
    print("Bai 8.3. Nhap ten va mat khau, gioi han so lan nhap")
    ten = input("Hay nhap vao ten cua ban: ")
    mat_khau = input("Hay nhap vao mat khau cua ban: ")
    print()

    so_lan = 1

    # vong lap
    while (ten != "Nam" or mat_khau != "2020") and (so_lan < 3):

        # kiem tra ten, neu sai thi nhap lai ca ten va mat khau
        if ten != "Nam":
            print("Ten khong dung.")
            ten = input("Hay nhap lai ten cua ban: ")
            mat_khau = input("Hay nhap lai mat khau cua ban: ")
            print()

        # neu dung ten nhung sai mat khau, chi nhap lai mat khau
        elif mat_khau != "2020":
            print("Mat khau khong dung.")
            mat_khau = input("Hay nhap lai mat khau cua ban: ")
            print()

        # cap nhat so lan
        so_lan += 1

    # het vong lap: da nhap dung thong tin, hoac vuot qua so lan
    # kiem tra ket qua
    if ten == "Nam" and mat_khau == "2020":
        print("Chao mung: ", ten)
    else:
        print("Ba da nhap qua so lan. Dang nhap khong thanh cong.")

    return


# Tinh tong S = 1^2 + 2^2 + 3^2 + ... + N^2 (dung lai neu tong vuot qua 100)
def bai8_4_tong_day_so():
    print()
    print("-----------------------")
    print("Bai 8.4. Tong day so: S = 1^2 + 2^2 + 3^2 + ... + N^2 (dung khi S vuot qua 100)")
    print("Cach 1. Cau lenh while")
    n = 0
    S = 0
    while S <= 100:
        n += 1
        S += (n * n)
        print(n, S)

    print("Tong la: ", S)

    print("Cach 2. Cau lenh for")
    S = 0
    for n in range(1000):
        S += (n * n)
        print(n, S)
        if S >= 100:
            break

    print("Tong la: ", S)


if __name__ == '__main__':
    # bai 8.1
    bai8_1_in_day_so()

    # bai 8.2
    bai8_2_tong_day_so()

    # bai 8.3
    bai8_3_nhap_ten_gioi_han()

    # bai 8.4
    bai8_4_tong_day_so()
