def heapify(arr, n, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] < arr[smallest]:
        smallest = left
    if right < n and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, n, smallest)

def build_heap(arr):
    n = len(arr)

    #start from the last non-leaf node
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

nums = [3, 2, 1, 5, 6, 4]
build_heap(nums)
print(nums)