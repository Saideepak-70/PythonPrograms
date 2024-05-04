def selection_sort(size):
    for i in range(size):
        x = int(input())
        arr.append(x)

    print("Your Array : ", arr)
    for i in range(0, size - 1):
        min = i
        for j in range(i + 1, size):
            if j >= 0 and arr[min] >= arr[j]:
                min = j

        temp = arr[i]
        arr[i] = arr[min]
        arr[min] = temp

    sorted_list = list(arr)
    print("Sorted Array : ", sorted_list)

n = int(input("Enter the size : "))
arr = []
print("Enter the values for the array : ")
selection_sort(n)


