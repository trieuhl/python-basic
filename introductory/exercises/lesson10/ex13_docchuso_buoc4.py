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

if __name__ == '__main__':

    n = 100
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
    cach_doc +=  cach_doc_a + " TRAM "
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
        cach_doc += cach_doc_c

    # buoc 5: in ra cach doc
    print(n, " CACH DOC: ", cach_doc)

    """
    # ------------- OUTPUT -------------
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
    # ------------- OUTPUT -------------
    """
