with open('str.txt', 'r') as file:
        data = file.read()

data = data.split()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
len_data = len(data)
count_literal = [0]*26

def count_sort(A, k, d):
        C = [0] * 26
        B = [0] * len_data
        for i in range(len(A)):
                C[alphabet.find(A[i][d])] = C[alphabet.find(A[i][d])] + 1
        for i in range(len(C)):
                count_literal[i] = count_literal[i] + C[i]
        for j in range(1, 26):
                C[j] = C[j] + C[j - 1]
        for i in range(len_data - 1, -1, -1):
                B[C[alphabet.find(A[i][d])] - 1] = A[i]
                C[alphabet.find(A[i][d])] = C[alphabet.find(A[i][d])] - 1
        return B

def radix_sort(n):
        l = count_sort(data, len_data, n)
        print l
        v = count_sort(l, len_data, n - 1)
        print v
        b = count_sort(v, len_data, n - 2)
        return b
        
                
print radix_sort(2)


