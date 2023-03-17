class Heap:
    def __init__(self) :
        self.array = ['null']

# It is used to Insert the Value

    def insert(self,data):
        self.array.append(data) 
        n = len(self.array)-1
        while n > 1:
            if self.array[n //2] > data:
                self.array[n //2],self.array[n] = self.array[n],self.array[n //2]
            n = n //2

# It display the value level by level

    def display(self):
      i = 1
      while i < len(self.array):
        for j in range(i,2*i):
            if j < len(self.array):
                print(self.array[j],end=' ')                   
        print()
        i = 2*i

# It deletes the fist value from the list 
    def delete(self):
        self.array[1],self.array[len(self.array)-1] = self.array[len(self.array)-1],self.array[1]
        self.array.pop()
        self.heapify(1)

# This function only help to rearrange the 
# Values after deletion of one entry        
    def heapify(self,i):
        if  len(self.array) == 3 and  self.array[2*i] < self.array[i]:
            self.array[i], self.array[2*i] = self.array[2*i],self.array[i]
        if 2*i+1 > len(self.array)-1 or 2*i > len(self.array)-1:
            return
        if self.array[2*i] <= self.array[2*i+1] and self.array[2*i] < self.array[i]:
            self.array[i], self.array[2*i] = self.array[2*i],self.array[i]
            self.heapify(2*i)
        if self.array[2*i] > self.array[2*i+1] and self.array[2*i+1] < self.array[i]:
            self.array[i], self.array[2*i+1] = self.array[2*i+1],self.array[i]    
            self.heapify(2*i+1)
# It check that the array is a heap or not
    def Is_Heap(self, array):
        for i in range (1,len(array)):
            if 2*i+1 > len(array)-1 or 2*i > len(array)-1:
                return True
            if array[i] > array[2*i] or array[i] > array[2*i+1]:
                return False


# This Function gives the sorted value of heap and
# After that  delete all the value in the list
    def printsort(self,n):
        if n == 1:
            return
        print(self.array[1],end=' ')
        self.delete()
        self.printsort(len(self.array))

    def Functionalty(self):
        print('\n<------------------------------------------------------------------------------------->')
        print('|a : Add Value|, |b : delete value|, |c : Check Is-Heap |, | d : Display|, | e : Exist|')
        print('<------------------------------------------------------------------------------------->')
        var = input('Enter :: ')
        if var == 'a':
            self.insert(int(input('Enter Value to add ::')))
            print('Value Added')
            self.Functionalty()
        elif var == 'b':
            self.delete()
            print('Value Deleted')
            self.Functionalty()
        elif var == 'c':
            print(self.Is_Heap(self.array))
            self.Functionalty()
        elif var == 'd':
            self.display()
            self.Functionalty()
        elif var == 'e':
            print('Programme Existed')
        else:
            print('InValid ! ')
            self.Functionalty()  
      
h = Heap()
h.Functionalty()

            

      
