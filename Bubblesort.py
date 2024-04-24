def bubble_sort(n):
    print("Enter elements : ")
    arr = []
    for i in range(n):
        x = int(input())
        arr.append(x)

    print("Your Array : ", arr)

    for i in range(n):
        for j in range(n-i-1):
            if arr[j+1] <= arr[j]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

    print("Sorted Array : ", arr)

size = int(input("enter the size of the array : "))
bubble_sort(size)