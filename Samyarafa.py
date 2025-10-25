def selection_sort(arr): 
  S = len(arr) 
Thelist=int input('enter the list')
    for i in range(S): 
        small = i 
        for j in range(i + 1, n):
            if arr[j] < arr[small]: 
                small = j 
        arr[i], arr[smallest] = arr[small], arr[i] 

    return arr
 
sorted = SelectionSort(Thelist) 
print(my_list)
