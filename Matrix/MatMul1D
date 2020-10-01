def matMul(A, B):
    # assert: A and B are two matrices represented in linear form. (establised)
    # A = [a11,a21,a31....an1,an2...ann] and similarly for B

    n = int(math.sqrt(len(A)))

    C = [0 for i in range(len(A))]

    # INV: After i iterations of the first loop, i rows of C are filled
    # i.e. cx1, cx2...cxn for all x<=i
    for i in range(0, n):
        # INV: After j iteration of second loop, jth row of C is filled
        # i.e. ci1, ci2...cpj
        for j in range(0, n**2, n):
            # INV: For matrix Cij = summation{k from 1 to n}(aik * bkj) is obtained
            for k in range(0, n):
                C[i+j] += A[i+n*k] * B[j+k]

    # assert: C is the matrix multiplication of A and B also represented in linear form like A and B.
    # C = [c11,c21,c31....cn1,cn2...cnn]
    return C


# A = [1, 3, 2, 4]
# B = [2, 1, 3, 4]

# print(matMul(A, B))
