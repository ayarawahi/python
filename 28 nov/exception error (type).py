try:
    N=input ("ETER THE VALUE")
    v = input ("ETER THE VALUE")

    print(int(N)+int(v))
except Exception as exc:
    print("error:",type(exc))