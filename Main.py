from typing import List

def selectionSort(array, size) -> List[int]:
  # Write your code here
  def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        if i == min_index:
            continue
        array[i], array[min_index] = array[min_index], array[i]
    return

array = list(sys.argv[1])
selection_sort(array)
print ''.join(array)
