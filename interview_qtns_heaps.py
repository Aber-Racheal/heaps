# MAX HEAP IMPLEMENTATION

class MaxHeap:
    def __init__(self):
        self.heap = [] 
    
    def insert(self, val):
        self.heap.append(val)
        self.heapify_up(len(self.heap) - 1)# Fix index to len(self.heap) - 1

    def heapify_up(self, i):
        # Perform heapify-up to maintain heap property
        while i > 0 and self.heap[i] > self.heap[(i - 1) // 2]:  # Use (i - 1) // 2 for parent index
            # Swap current element with its parent if it violates the max heap property
            self.heap[i], self.heap[(i - 1) // 2] = self.heap[(i - 1) // 2], self.heap[i]
            i = (i - 1) // 2  # Update index to parent

    def delete(self, val):
        # Find the index of the element to delete
        idx = self.heap.index(val)
        # Swap the element with the last element in the heap
        self.heap[idx], self.heap[-1] = self.heap[-1], self.heap[idx]
        deleted = self.heap.pop()
        # Perform heapify-down to maintain heap property
        self.heapify_down(idx)
        return deleted  # Return the deleted value

    def heapify_down(self, i):
        n = len(self.heap)
        while 2 * i + 1 < n:  # Ensure left child exists
            # Determine the larger child
            left = 2 * i + 1
            right = 2 * i + 2
            largest = left
            if right < n and self.heap[right] > self.heap[left]:
                largest = right
            # Swap with the larger child if necessary
            if self.heap[i] < self.heap[largest]:
                self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
                i = largest
            else:
                break

    def extract_max(self):
        if len(self.heap) == 0:
            return None  # Return None if heap is empty
        # Swap the root (max element) with the last element
        max_elem = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        # Perform heapify-down to maintain heap property
        self.heapify_down(0)
        return max_elem  # Return the maximum element

# Example usage:
heap = MaxHeap()
heap.insert(5)
heap.insert(3)
heap.insert(8)
heap.insert(1)
heap.insert(10)

print(heap.heap)  # Print current state of the heap
print(heap.extract_max())  # Output: 10
print(heap.heap)
print(heap.delete(5))  # Output: 5
print(heap.heap)








# CONVERTING ARRAY TO HEAPS

import heapq

def convert_to_min_heap(nums):
    heapq.heapify(nums)  # Convert array to min-heap

def convert_to_max_heap(nums):
    # Convert each element to its negative and heapify
    nums = [-num for num in nums]
    heapq.heapify(nums)
    # Convert back to positive numbers
    nums = [-num for num in nums]
    return nums  # Return the max-heap array

# Example usage:
nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print("Original array:", nums)

# Convert to min-heap
convert_to_min_heap(nums.copy())
print("Min-heap:", nums)  # Output: Min-heap: [1, 1, 2, 3, 3, 5, 4, 6, 5, 5, 9]

# Convert to max-heap
max_heap = convert_to_max_heap(nums.copy())
print("Max-heap:", max_heap)  # Output: Max-heap: [9, 5, 6, 5, 5, 5, 4, 1, 3, 3, 2]









# FINDING Kth LARGEST ELEMENT
def findKthLargest(nums, k):
    min_heap = []
    
    # Insert first k elements into the min-heap
    for num in nums[:k]:
        heapq.heappush(min_heap, num)
    
    # Process the remaining elements
    for num in nums[k:]:
        heapq.heappush(min_heap, num)
        # If heap size exceeds k, remove the smallest element
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    
    # The root of the heap is the Kth largest element
    return min_heap[0]  # Return the root of the heap

# Example usage:
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(findKthLargest(nums, k))  # Output: 5




# SORTING AN ALMOST SORTED ARRAY
def sort_almost_sorted(nums, k):
    n = len(nums)
    result = []
    min_heap = []
    
    # Insert first k+1 elements into the min-heap
    for i in range(min(k + 1, n)):
        heapq.heappush(min_heap, nums[i])
    
    # Process the remaining elements in the array
    for i in range(k + 1, n):
        # Extract the minimum element from the heap
        min_element = heapq.heappop(min_heap)
        result.append(min_element)
        # Insert the next element from the array into the heap
        heapq.heappush(min_heap, nums[i])
    
    # Extract remaining elements from the heap
    while min_heap:
        min_element = heapq.heappop(min_heap)
        result.append(min_element)
    
    return result  # Return the sorted array

# Example usage:
nums = [3, 2, 1, 5, 6, 4]
k = 2
sorted_nums = sort_almost_sorted(nums, k)
print(sorted_nums)  # Output: [1, 2, 3, 4, 5, 6]









# PRIORITY QUEUE IMPLEMENTATION
import heapq

class PriorityQueue:
    def __init__(self):
        self._pq = []  # Initialize an empty priority queue
        self._index = 0  # Used to maintain the insertion order when priorities are equal
    
    def insert(self, priority, item):
        # We use a tuple (priority, index, item) to maintain the heap invariant
        entry = (priority, self._index, item)
        heapq.heappush(self._pq, entry)
        self._index += 1  # Increment index to maintain order

    def delete(self):
        # Remove and return the highest priority element
        _, _, item = heapq.heappop(self._pq)
        return item
    
    def get_highest_priority_element(self):
        # Return the highest priority element without removing it
        if not self._pq:
            raise IndexError("Priority queue is empty")
        priority, _, item = self._pq[0]
        return item
    
    def is_empty(self):
        # Check if the priority queue is empty
        return len(self._pq) == 0
    
    def size(self):
        # Return the number of elements in the priority queue
        return len(self._pq)

# Example usage:
pq = PriorityQueue()

# Insert elements with priorities
pq.insert(3, 'Task 3')
pq.insert(1, 'Task 1')
pq.insert(2, 'Task 2')

# Get and remove the highest priority element
print("Highest priority element:", pq.delete())  # Output: Task 1

# Get the element with the current highest priority
print("Current highest priority element:", pq.get_highest_priority_element())  # Output: Task 2

# Insert another element
pq.insert(0, 'Task 0')

# Check if the priority queue is empty
print("Is priority queue empty?", pq.is_empty())  # Output: False

# Get the size of the priority queue
print("Size of priority queue:", pq.size())  # Output: 3


