from time import perf_counter


def bubble_sort(students, key):
    start = perf_counter()
    for i in range(len(students)):
        for j in range(len(students) - i - 1):
            if students[j][key] > students[j + 1][key]:
                students[j], students[j + 1] = students[j + 1], students[j]
    end = perf_counter()
    elapsed = end - start
    return students, elapsed

def selection_sort(students, key):
    start = perf_counter()
    for i in range(len(students)):
        min_index = i
        for j in range(i + 1, len(students)):
            if students[j][key] < students[min_index][key]:
                min_index = j
        if min_index != i:
            students[i], students[min_index] = students[min_index], students[i]
    end = perf_counter()
    elapsed = end - start
    return students, elapsed

def insertion_sort(students, key):
    start = perf_counter()
    for i in range(len(students)):
        value = students[i]
        j = i
        while j > 0 and students[j - 1][key] > value[key]:
            students[j] = students[j - 1]
            j -= 1
        students[j] = value
    end = perf_counter()
    elapsed = end - start
    return students, elapsed



def quick_sort(students, key):
    start = perf_counter()
    if len(students) <= 1:
        return students
    pivot = students[len(students) // 2][key]
    less = [x for x in students if x[key] < pivot]
    equal = [x for x in students if x[key] == pivot]
    greater = [x for x in students if x[key] > pivot]
    end = perf_counter()
    elapsed = end - start
    merge_runtimer(elapsed)
    return quick_sort(less, key) + equal + quick_sort(greater, key)


def merge_sort(students, key):
    start = perf_counter()
    if len(students) <= 1:
        return students

    def merge(left, right, key):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i][key] < right[j][key]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    mid = len(students) // 2
    left = merge_sort(students[:mid], key)
    right = merge_sort(students[mid:], key)
    
    end = perf_counter()
    elapsed = end - start
    merge_runtimer(elapsed)
    return merge(left, right, key)


def heap_sort(students, key):
  start = perf_counter()  
  n = len(students)
  for i in range(n // 2 - 1, -1, -1):
    heapify(students, n, i, key)
    
  for i in range(n - 1, 0, -1):
    students[i], students[0] = students[0], students[i]
    heapify(students, i, 0, key)
    
    end = perf_counter()
    elapsed = end - start
    return students, elapsed

def heapify(students, n, i, key):
  largest = i
  l = 2 *i + 1
  r = 2 * i + 2
  
  if l< n and students[l][key] > students[largest][key]:
    largest = l
    
  if r< n and students[r][key] > students[largest][key]:
    largest = r
    
  if largest != i:
    students[i], students[largest] = students[largest], students[i]
    heapify(students, n, largest, key)
    

quick_runtime = 0
merge_runtime = 0
def quick_runtimer(runtime):
    global quick_runtime
    quick_runtime = runtime
    return quick_runtime

def merge_runtimer(runtime):
    global merge_runtime
    merge_runtime = runtime
    return merge_runtime


'''


**Bubble Sort:**
1. Iterate through each element in the list of students.
2. For each element, iterate through the remaining unsorted elements.
3. Compare each pair of adjacent elements based on the specified key attribute.
4. If the element on the left is greater than the element on the right, swap them.
5. Track the number of swaps and iterations.
6. Repeat steps 2-5 until the entire list is sorted.
7. Return the sorted list of students.

**Selection Sort:**
1. Iterate through each element in the list of students.
2. Set the current element as the minimum element.
3. Iterate through the remaining unsorted elements.
4. Find the minimum element among the unsorted elements based on the specified key attribute.
5. Swap the minimum element with the current element.
6. Track the number of swaps and iterations.
7. Repeat steps 2-6 until the entire list is sorted.
8. Return the sorted list of students.

**Insertion Sort:**
1. Iterate through each element in the list of students.
2. Set the current element as the value to be inserted.
3. Compare the current element with the sorted elements on its left.
4. Shift the sorted elements to the right until the correct position for the current element is found.
5. Insert the current element at the correct position.
6. Track the number of swaps and iterations.
7. Repeat steps 2-6 until the entire list is sorted.
8. Return the sorted list of students.

**Quick Sort:**
1. If the list of students has one element or is empty, return the list.
2. Choose a pivot element from the list (here, the middle element is chosen).
3. Divide the list into three sublists: elements less than the pivot, elements equal to the pivot, and elements greater than the pivot based on the specified key attribute.
4. Recursively apply quick sort to the sublists of elements less than and greater than the pivot.
5. Combine the sorted sublists and the pivot in the correct order.
6. Return the sorted list of students.

**Merge Sort:**
1. If the list of students has one element or is empty, return the list.
2. Divide the list into two equal-sized sublists.
3. Recursively apply merge sort to the sublists.
4. Merge the sorted sublists by comparing the elements based on the specified key attribute.
5. Return the merged and sorted list of students.

**Heap Sort:**
1. Build a max heap from the list of students based on the specified key attribute.
2. Starting from the last non-leaf node, heapify the heap to maintain the max heap property.
3. Repeat step 2 for each non-leaf node in reverse order.
4. Swap the root element (maximum element) with the last element and reduce the heap size.
5. Heapify the reduced heap to maintain the max heap property.
6. Repeat steps 4-5 until the entire list is sorted.
7. Return the sorted list of students.


'''