def insertion_sort(n):
    arr = []
    print("Enter elements : ")
    for i in range(n):
        x = int(input())
        arr.append(x)

    print("Your Array : ", arr)

    for i in range(n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] >= key:
                arr[j+1] = arr[j]
                j = j - 1
        arr[j+1] = key

    print("Sorted Array : ", arr)

size = int(input("enter the size of the array : "))
insertion_sort(size)