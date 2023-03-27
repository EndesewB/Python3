class B(Exception):
    pass


class C(B):
    pass


class D(C):
    pass

for clss in [B, C, D, ]:

    try:
        raise clss ()
    except B:
        print("D")
    except D:
        print("C")
    except B:
        print("B")

