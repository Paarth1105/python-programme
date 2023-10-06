def search(arr, N, x):
    for i in range(0, N):
        if (arr[i] == x):
            return i
        else:
            return -1
        result = search(arr, N, x)
        if(result == -1):
            print("element is not present in the array")
        else:
            print("element is present at the index", result)