#CEBASTIAN SANTIAGO   
#COMPUTING ALGROITHMS SEARCH,FACTORIAL,BINARY AND SORTING ALGORITHMS FROM ALGORITMS UNLOCKED BOOK 
#FROM CHAPTER 2 & 3             
#PSEUDOCODE TO PYTHON 3 CODE 
import array as arr
import math 

#QUICKSORT 
def Quick_Sort(A,p,r):
    if p >= r:
        return A 
    q = Partition(A,p,r)
    Quick_Sort(A,p,q-1)
    Quick_Sort(A,q+1,r)
    return A 

    

#PARTITION
def Partition(A,p,r):
    q = p
    for u in range(p,r):
        if A[u] <= A[r]:
            A[q],A[u] = A[u],A[q]
            q+=1
    A[q],A[r] = A[r],A[q]
  
    return q



#MERGE SORT
def Merge_Sort(A,p,r):
    #IF ONE ELEMENT OR LESS RETURN ARRAY
    if p >= r:                  
        return A
    #GRAB THE MIDPOINT OF THE SUB ARRAYS 
    q = (p+r)//2
    Merge_Sort(A,p,q)
    Merge_Sort(A,q+1,r)
    Merge(A,p,q,r)
   
    return A

#MERGE
def Merge(A,p,q,r):
    #GET THE LENGTH OF THE LEFT AND RIGHT SUB ARRAYS 
    left_array_length = q-p+1
    right_array_length = r-q
   
   #SET THE LENGTH OF THE ARRAYS TO BE SENTINELS IN THE FIRST ELEMENTS 
    left = [0]*(left_array_length)
    right = [0]*(right_array_length)
   #INSERT THE FIRST HALF OF THE ARRAY ARRAY TO THE LEFT 
    for i in range(0,left_array_length):
        left[i] = A[p+i]
   #INSERT ARRAY TO THE RIGHT HALF OF THE ARRAY
    for j in range(0,right_array_length):
        right[j] = A[q+1+j]
       
    
    #INDEXS FOR ARRAYS
    i = 0
    j = 0
    k = p
    #INSERT ELMENTS BACK INTO THE ARRAY 
    while i < left_array_length and j < right_array_length:
        if left[i] <= right[j]:
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j+=1
        k += 1
    while i < left_array_length:
        A[k] = left[i]
        i +=1
        k +=1

    while j < right_array_length:
        A[k] = right[j]
        j+=1
        k+=1








#INSERTION SORT ALGROITHM
#A IS THE ARRAY 
#N IS THE LENGTH OF THE ARRAY 
def insertion_sort(A,n):
    #Loop THROUGH THE ARRAY 
    for i in range(0,n):
        #SET FIRST ELEMENT TO KEY 
        key = A[i] 
        j = i-1
        #CONDITIONS OF J AND KEY MAKE SURE THE INDEX IS"NT OUT OF RANGE 
        while(j >= 0 and A[j] > key):
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
    return A





#SELECTION SORT ALGROITHMS 
#A IS THE ARRAY 
#N IS THE LENGTH OF THE ARRAY 
def selection_sort(A,n):
  #LOOP THROUGH THE ARRAY 
  for i in range(0,n):
  #SAY THE FIRST ELEMENT I IS THE SMALLEST 
      smallest = i 
  #ANOTHER LOOP TO GO THROUGH THE REST OF THE ARRAY
      for j in range(i+1,n):
          #IF J is less then smallest set smallest to j
          if A[j] < A[smallest]:
              smallest = j
  #SWAP ELEMENTS 
      A[i],A[smallest] = A[smallest] , A[i]
  #RETURN THE ARRAY SORTED IN ASCENDING ORDER 
  return A

      
#RECURSIVE BINARY SEARCH ALGROITHMS
#A is THE ARRAY PASSED 
#P IS THE LEFTMOST POSITION IN THE ARRAY 
#R IS THE LENGTH OF THE ARRAY 
#X IS THE NUMBER TO LOOK FOR IN THE ARRAY 
def recursive_binary_search(A,p,r,x):
    #BASE CASE ONCE THE LEFT INDEX MEETS THE RIGHT INDEX  
    if p > r:
        return print("NOT FOUND!")
    #AS LONG AS LEFT = 0 AND RIGHT IS GREATER OR EQUAL 
    elif(p <= r):
    #GET HALF POINT OF THE ARRAY 
        q = (p+r)/2
        q = math.floor(q)
    #IF NUMBER WERE LOOKING FOR FOUND EXIT 
        if A[q] == x:
            return print(F"Number {x} is at index {q}")
    #ELSE RECURSIVE CALL IF NUMBER NOT FOUND
        elif A[q] > x:
            return recursive_binary_search(A,p,q-1,x)
    #ELSE RECURSIVE CALL IF NUMBER NOT FOUND
        elif A[q] < x:
            return recursive_binary_search(A,q+1,r,x)
    #IF NUMBER NOT INDEX RETURN -1
    return print(f"Number {x} is not in the array")



#BINARY SEARCH ALGROITHMS
#A is the array passed to the function 
#n is the length of the array  
#x is the number to look for in the array  
def binary_search(A,n,x):
    #SET P TO ZERO TO START AT THE LEFTEST INDEX 
    #SET R EQUAL TO THE LENGTH OF THE ARRAY
    p = 0
    r = n
    #LOOP WORKS SINCE  P = 0 AND R IS THE LENGTH OF THE ARRAY
    while(p <= r):
        #GET THE HALF POINT OF THE ARRAY 
        q = (p+r)/2
        # USE FLOOR THE FUNCTION TO DECREASE FLOAT TO INT  
        q = math.floor(q)
        #IF THE NUMBER WHERE LOOKING FOR IS FOUND WE EXIT THE FUNCTION 
        if A[q] == x:
            return print(f"The number {x} is at index {q}.")
        #IF ARRAY IS GREATER THEN THE NUMBER WHERE LOOKING FOR
        elif A[q] > x:
            r = q-1 
        elif A[q] < x:
        #IF ARRAY IS LESS THEN THE NUMBER WHERE LOOKING FOR 
            p = q+1
    #PRINT STATEMENT  IF THE NUMBER IS NOT IN THE ARRAY
    return print(f"The number {x} is not in the array.") 


#FINDS FACTROIAL AS LONG AS UM POSTIVE AND DOES NOT EXCEED INT MEMORY
def factorial(n):
    #BASE CASE 
    if n == 0:
        return 1
    else:
    #TO REACH BASE CASE OR SOME SORT OF INSTANCE THAT WOULD LEAD YOU TO THE BASE CASE 
        return n*factorial(n-1)


#LINEAR SEARCH ALGROITHMS 
#LIST IS THE ARRAY
#N IS THE LENGTH 
#X NUMBER TO LOOK FOR 
def linear_search(list,n,x):

    #LOOP IREATATION THROUGH THE LIST 
    for i in range(0,n):
    #STARTS LEFT TO RIGHT AND CHECKS EVERY IRATION IF THE GIVEN INDEX RETURNS MATCH IF FOUND 
        if list[i] == x:
            return print(f"Number {x} is in index {i}")
        
    #PRINTS IF THE NUMBER IS NOT IN THE INDEX 
    print(f"Number {x} is not in the given array")
        

#CREATE ARRAY 
list =arr.array('i',[1, 4, 5, 7, 9, 12])
array = arr.array('i',[10, 9 ,8, 7, 6, 5, 4, 3, 2, 1])
lists = [12,9,3,23,44,32,9,1,0]

#a = input("Enter a number to search the list: ")
#num = int(a)

#Length of arrays
#n = len(list)
nums = len(lists)
#length = len(lists)


#CALL FUNCTION Linear Search 
#linear_search(list,n,num)


#DRIVER CODE FOR FACTORIAL FUNCTION RECURIVELY 
#x=100
#print(factorial(x))

#DRIVER CODE FOR BINARY SEARCH ALGORITHMS RECURSIVE 
#print(binary_search(list,n,num))

#DRIVER CODE BINARY SEARCH ALGORITHMS RECURSIVE 
#recursive_binary_search(list,0,n,num)

#DRIVER CODE FOR SELECTION SORT 
#print(array)
#answer = selection_sort(array,nums)
#print(answer)
 
#DRIVER CODE FOR INSERTION SORT 
#lists = insertion_sort(array,nums)
#print(lists)
 
#answer = insertion_sort(lists,length)
#print(answer)


#DRIVER CODE MERGE SORT 
#Merge_Sort(lists,0,nums-1)
#print(lists)

#Driver code quicksort
lists = Quick_Sort(lists,0,nums-1)
print(lists)