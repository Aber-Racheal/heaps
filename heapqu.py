import heapq 

li= [5,7,9,1,1,3]
heapq.heapify(li)

# print("THe created heap is: ",li)
print ("The created heap is: ", end="")
print (list(li))
heapq.heappush(li, 10)
print (list(li))
print(heapq.heappop(li))
print(heapq.nlargest(4, li))
print(heapq.nsmallest(2,li))


heapq.heappushpop(li, 2)
print(li)


max_heap =[-5,-2,-7,-1]
heapq.heapify(max_heap)
print("Max_heap:", [-x for x in max_heap])