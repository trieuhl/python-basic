if __name__ == '__main__':

    n = input("Nhap vao n: ")
    n = int(n)

    print("Cac uoc nguyen duong cua {} la: ".format(n))
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)

    """
    # ------------- OUTPUT -------------
    Nhap vao n: 12
    Cac uoc nguyen duong cua 12 la: 
    1
    2
    3
    4
    6
    12
    # ------------- OUTPUT -------------
    """
