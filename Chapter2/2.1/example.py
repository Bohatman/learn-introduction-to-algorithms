



A = [5,2,4,6,1,3]




def insertion_sort(input: list):
    for j in range(1,len(input)):
        key = input[j]
        i = j - 1
        while(i > -1 and input[i] > key):
            input[i + 1] = input[i]
            i = i - 1
        input[i + 1] = key
    return input

def insertion_sort_inverted(input: list):
    for j in range(1,len(input)):
        key = input[j]
        i = j - 1
        while(i>-1 and input[i] < key):
            input[i + 1] = input[i]
            i = i -1
        input[i + 1] = key
    return input
        
print(insertion_sort_inverted(A))
            