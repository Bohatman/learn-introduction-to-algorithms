
# 1. Illustrate the operation of insertion sort A = [31,41,59,26,41,58]
[31,41,59,26,41,58]
[31,41,59,26,41,58]
[26,31,41,59,41,58]
[26,31,41,41,59,58]
[26,31,41,41,58,59]

# 2. Nonincresing

def nonincressing(input: list):
    if input is None: return None
    for j in range(1,len(input)):
        key = input[j]
        i = j - 1
        while(i > -1 and key > input[i]):
            input[i+1] = input[i]
            i = i -1
        input[i + 1 ] = key
    return input
print(nonincressing([1,2,3,4,5,6,7,8]))

# 3. Search v in list
def search(v, input: list):
    if input is None: return None
    for i in range(len(input)):
        item = input[i]
        if item == v:
            return i
    return None
print(search(1,[9,8,7,6,5,4,3,2,1]))

# 4. merge 2 bit array of integer to once
# A and B is same size
def add_binary(A:list,B:list):
    C = [0] * (len(A) + 1)
    carry = 0
    for i in range(len(A)-1,-1,-1):
        C[i] = (A[i] + B[i] + carry) % 2
        carry = int((A[i] + B[i] + carry) / 2)
    C[0] = carry
    return C
A = [1,1,1,1]
B = [0,0,0,1]
print(add_binary(A,B))


