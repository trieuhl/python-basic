"""
https://pythoncoban.wordpress.com/bai-2-mot-so-phep-toan/
Code lại theo code mẫu trên, thay các biến a, b, c, d, e, f, g, h bằng các biến m, n, p, q, z, y, z, t trong đó m = 2, n = 4, p = 6, q = 8, x = 1, y = 3, z = 5, t = 7
"""

if __name__ == '__main__':
    m = 2
    n = 4
    p = 6
    q = 8
    x = 1
    y = 3
    z = 5
    t = 7

    # phep cong
    t1 = m + n
    print("phep cong hai so")
    print(m)
    print(n)
    print(t1)
    print("ket qua = ", t1)

    # phep tru
    print()
    print("phep tru hai so")
    t2 = p - q
    print(p, "-", q, "=", t2)

    # phep nhan
    print()
    print("phep nhan")
    print(x, y, x * y)

    # phep chia
    print()
    print("phep chia")
    t3 = q / p
    print(q, "/", p, " = ", t3)

    # phep gan
    print()
    print("phep gan")
    z = 5
    print("z = ", z)
    z = z + 1
    print("z = ", z)

    print()
    z = 5
    print("z = ", z)
    z += 1
    print("z = ", z)

    print()
    t = 7
    print("t = ", t)
    t *= 2
    print("h = ", t)

    """
    # ------------- OUTPUT -------------
    phep cong hai so
    2
    4
    6
    ket qua =  6
    
    phep tru hai so
    6 - 8 = -2
    
    phep nhan
    1 3 3
    
    phep chia
    8 / 6  =  1.3333333333333333
    
    phep gan
    z =  5
    z =  6
    
    z =  5
    z =  6
    
    t =  7
    h =  14
    # ------------- OUTPUT -------------
    """

