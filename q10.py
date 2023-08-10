A = float(input("Digite o valor de A: "))
B = float(input("Digite o valor de B: "))
C = float(input("Digite o valor de C: "))

if A <= B and A <= C:
    print(A, end=" ")
    if B <= C:
        print(B, C)
    else:
        print(C, B)
elif B <= A and B <= C:
    print(B, end=" ")
    if A <= C:
        print(A, C)
    else:
        print(C, A)
else:
    print(C, end=" ")
    if A <= B:
        print(A, B)
    else:
        print(B, A)