import random
A = 25
B = [random.randint(0, 100) for i in range(A)]
print(B)
C = 5
while C < A - 1:
    for i in range(A - C):
        if B[i] > B[i + 1]:
            B[i], B[i + 1] = B[i + 1], B[i]
    C += 1
print(B)