# ham doc mot so
def ham_doc_so(x):
    if x == 0:
        return "KHONG"
    elif x == 1:
        return "MOT"
    elif x == 2:
        return "HAI"
    elif x == 3:
        return "BA"
    elif x == 4:
        return "BON"
    elif x == 5:
        return "NAM"
    elif x == 6:
        return "SAU"
    elif x == 7:
        return "BAY"
    elif x == 8:
        return "TAM"
    elif x == 9:
        return "CHIN"

# xu ly doc so cho n co ba chu so
def doc_so_3_chu_so(n):

    print("n = ", n)
    print("-----------------")

    # luu ket qua cach doc
    cach_doc = ""

    # n = abc
    # buoc 1: tinh chu so hang tram (a)
    a = n // 100
    print("a = ", a)
    print("cach doc: ", a, "TRAM")

    # goi ham doc so va luu vao ket qua
    cach_doc_a = ham_doc_so(a)
    cach_doc += cach_doc_a + " TRAM "
    print("-----------------")

    # buoc 2: lay ra bc
    bc = n % 100
    print("bc = ", bc)

    # buoc 3: lay ra b
    b = bc // 10
    print("b = ", b)
    print("cach doc: ", b, "CHUC")

    # goi ham doc so va luu vao ket qua
    if b > 0:
        cach_doc_b = ham_doc_so(b)
        cach_doc += cach_doc_b + " MUOI "
    print("-----------------")

    # buoc 4: lay ra c
    c = bc % 10
    print("c = ", c)
    print("cach doc: ", c, "DON VI")

    # goi ham doc so va luu vao ket qua
    if c > 0:
        cach_doc_c = ham_doc_so(c)

        # neu b = 0: vi du 102, them chu "LINH"
        if b == 0:
            cach_doc += "LINH "

        cach_doc += cach_doc_c

    # buoc 5: in ra cach doc
    print(n, " CACH DOC: ", cach_doc)

if __name__ == '__main__':

    # 123
    n = 123
    doc_so_3_chu_so(n)
    print("===============================")

    # 100
    n = 100
    doc_so_3_chu_so(n)
    print("===============================")

    # 102
    n = 102
    doc_so_3_chu_so(n)

    """
    # ------------- OUTPUT -------------
    n =  123
    -----------------
    a =  1
    cach doc:  1 TRAM
    -----------------
    bc =  23
    b =  2
    cach doc:  2 CHUC
    -----------------
    c =  3
    cach doc:  3 DON VI
    123  CACH DOC:  MOT TRAM HAI MUOI BA
    ===============================
    n =  100
    -----------------
    a =  1
    cach doc:  1 TRAM
    -----------------
    bc =  0
    b =  0
    cach doc:  0 CHUC
    -----------------
    c =  0
    cach doc:  0 DON VI
    100  CACH DOC:  MOT TRAM 
    ===============================
    n =  102
    -----------------
    a =  1
    cach doc:  1 TRAM
    -----------------
    bc =  2
    b =  0
    cach doc:  0 CHUC
    -----------------
    c =  2
    cach doc:  2 DON VI
    102  CACH DOC:  MOT TRAM LINH HAI
    # ------------- OUTPUT -------------
    """
