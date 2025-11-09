class Student:
    def __init__(self, sid, name, marks, course):
        self.sid = sid
        self.name = name
        self.marks = marks
        self.course = course

# --- Hash Table Implementation ---
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return key % self.size

    def insertStudent(self, student):
        h = self._hash(student.sid)
        self.table[h].append(student)
        print(f"Student {student.name} (Roll {student.sid}) added.")

    def searchStudent(self, sid):
        h = self._hash(sid)
        for student in self.table[h]:
            if student.sid == sid:
                print(f"Found: {student.name}, Marks: {student.marks}, Course: {student.course}")
                return
        print("Student not found!")

# --- Searching Algorithms ---
def sequentialSearch(records, target):
    for student in records:
        if student.sid == target:
            return student
    return None

def binarySearch(records, target):
    records.sort(key=lambda x: x.sid)
    low, high = 0, len(records) - 1
    while low <= high:
        mid = (low + high) // 2
        if records[mid].sid == target:
            return records[mid]
        elif records[mid].sid < target:
            low = mid + 1
        else:
            high = mid - 1
    return None

# --- Sorting Algorithms ---
def heapSort(arr):
    def heapify(n, i):
        largest = i
        l, r = 2*i + 1, 2*i + 2
        if l < n and arr[l].marks > arr[largest].marks: largest = l
        if r < n and arr[r].marks > arr[largest].marks: largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(n, largest)
    n = len(arr)
    for i in range(n//2 - 1, -1, -1): heapify(n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(i, 0)

def quickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2].marks
    left = [x for x in arr if x.marks < pivot]
    middle = [x for x in arr if x.marks == pivot]
    right = [x for x in arr if x.marks > pivot]
    return quickSort(left) + middle + quickSort(right)

# --- Radix Sort for Roll Numbers ---
def countingSort(arr, exp):
    n = len(arr)
    output = [0]*n
    count = [0]*10
    for i in range(n):
        index = arr[i].sid // exp
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i-1]
    i = n - 1
    while i >= 0:
        index = arr[i].sid // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    for i in range(n):
        arr[i] = output[i]

def radixSort(arr):
    max1 = max(student.sid for student in arr)
    exp = 1
    while max1 // exp > 0:
        countingSort(arr, exp)
        exp *= 10

# --- Demonstration ---
records = [
    Student(102, "Alice", 85, "DSA"),
    Student(105, "Bob", 75, "DBMS"),
    Student(101, "Charlie", 90, "OOPS")
]

# Hash Table operations
hash_table = HashTable()
for s in records:
    hash_table.insertStudent(s)
hash_table.searchStudent(101)

# Search operations
print("\nSequential Search:")
result = sequentialSearch(records, 105)
print(f"Found: {result.name}" if result else "Not found")

print("\nBinary Search:")
result = binarySearch(records, 102)
print(f"Found: {result.name}" if result else "Not found")

# Sorting operations
print("\nQuick Sort by Marks:")
sorted_students = quickSort(records)
for s in sorted_students:
    print(s.name, s.marks)

print("\nRadix Sort by Roll Number:")
radixSort(records)
for s in records:
    print(s.sid, s.name)
