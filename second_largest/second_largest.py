def second_largest(A):
    largest = float('-inf')
    second_largest = float('-inf')

    for i in range(len(A)):
        if A[i] > largest:
            second_largest = largest
            largest = A[i]
        elif A[i] > second_largest and A[i] != largest:
            second_largest = A[i]

    if second_largest != float('-inf'):
        return second_largest
    else:
        return -1

A = list(map(int, input("Enter the Array Elements: ").split()))
print(second_largest(A))
