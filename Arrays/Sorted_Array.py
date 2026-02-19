#Question: Check if Array is sorted or not
#Time Complexity: O(n)
#Space Complexity: O(1)
arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 3, 2, 4, 5]

def isSorted(arr, n):
    if n == 1:
        return True

    if arr[n - 1] >= arr[n - 2]:
        return isSorted(arr, n - 1)

    return False


def arraySortedOrNot(arr):
    n = len(arr)
    return isSorted(arr, n)


print("Array 1:", arr2)
print("Is sorted?", arraySortedOrNot(arr2))
