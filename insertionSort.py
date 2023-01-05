def insertionSort(list):
    n = len(list)
    for j in range(1, n):
        key = list[j]
        i = j - 1
        while i >= 0 and list[i] > key:
            list[i+1] = list[i]
            i = i - 1
        list[i+1] = key
    print(list)


a = [24, 5, 77, 8, 19, 2, 6, 1]
insertionSort(a)


def inserstionSortZJ(A):
    n = len(A)
    for j in range(1, n):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i -= 1
        A[i+1] = key
    print(A)


b = [76, 5, 4, 3, 2, 1, 77]
inserstionSortZJ(b)


def insertionSortIncrease(A):
    n = len(A)
    for j in range(1, n):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] < key:
            A[i+1] = A[i]
            i -= 1
        A[i+1] = key
    print(A)


c = [4, 5, 6, 1, 2, 9, 90, 102, 77]
insertionSortIncrease(c)


def linearSearch(A, j):
    for i in A:
        if i == j:
            print(f"we found it {i} == {j}")
            return i
    print(f"sorry we couldn't find {j} in {A}")
    return 0


'''
loop invarient -- to prove that your algorithm is correct, ensure it meets three (3) necessary properties
1. Initialization
    a. The subarray A[0..i] consists of just a single element A[0], which will be the first element
    to be checked in our search
2. Maintenance
    a. for each itteration the subarray A[0..i] are the elements that have been search for in the array
    and consists of the elements orginally in A[0..i]
3. Termination
    a. the condition which causes for termination is when the the last element in A has been utilized
    in our for loop; i == A[n]
    b. subarray A[0..n] consists of the elements originally in A[0..n] but they have now been checked
    for equality.

'''

d = [1, 2, 3, 4, 5, 6]
e = 7
f = 2
linearSearch(d, e)
linearSearch(d, f)

# consider adding two (2) n-bit binary integers, stored in two (2) n-element arrays A & B
# the sume of the two integers should be stored in binary form in an (n + 1)-element array C
# state the problem formally and write pseudocode for adding the two integers

100101 + 1011111


def addBinary(A, B):
    n = len(A)
    C = [0] * (n+1)
    for i in range(n-1, -1, -1):
        C[i+1] += A[i] + B[i]
        if C[i+1] > 1:
            C[i+1] -= 2
            C[i] += 1
    print(C)


w = [1, 1, 1, 1, 0]
x = [1, 1, 1, 1, 1]
addBinary(w, x)
