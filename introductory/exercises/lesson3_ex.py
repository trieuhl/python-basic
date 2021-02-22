"""
    - Viết hàm tính tổng ba số, gọi hàm để tính phép cộng 2 + 3 + 4
    - Viết hàm tính tích hai số, gọi hàm để tính phép nhân 5 * 6
    - Viết hàm tính hiệu hai số, gọi hàm để tính phép trừ 7 – 8
    - Viết hàm tính phép chia hai số, gọi hàm để tính phép chia 9 / 10
    - Viết hàm không có đối số gọi cả 4 hàm trên, in kết quả ra màn hình (tham khảo code mẫu)
    https://pythoncoban.wordpress.com/bai-3-ham/
"""


# ham tinh tong ba so
def tong_ba_so(a, b, c):
    sum = a + b + c
    return sum


# ham tinh tich hai so
def tich_hai_so(x, y):
    return x * y


# ham tinh hieu hai so
def hieu_hai_so(e, f):
    return e - f


# ham tinh thuong hai so
def thuong_hai_so(u, v):
    thuong = u / v
    return thuong


# ham khong doi so
def tinh_toan():
    # cong
    t1 = tong_ba_so(2, 3, 4)
    print("tong ba so: ", 2, " + ", 3, " + ", 4, " = ", t1)

    # nhan
    a1 = 5
    a2 = 6
    print("tich hai so: ", a1, " * ", a2, " = ", tich_hai_so(a1, a2))

    # tru
    a = 7
    b = 8
    t3 = hieu_hai_so(a, b)
    print("hieu hai so: ", a, " - ", b, " = ", t3)

    # chia
    so_bi_chia = 9
    so_chia = 10
    thuong = thuong_hai_so(so_bi_chia, so_chia)
    print("phep chia hai so: ", so_bi_chia, " / ", so_chia, " = ", thuong)


if __name__ == '__main__':
    tinh_toan()
