class Solution():
    
    def BubbleSort(self, nums):
        n = len(nums)
        Flag = True

        while Flag:
            Flag = False
            for i in range(0,n - 1):
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                    Flag = True
            
        return nums

    def SelectionSort(self, nums):
        n = len(nums)
        
        for i in range(0, n - 1):
            label = i
            for j in range(i+1, n):
                if nums[j] < nums[label]:
                    label = j
            nums[i], nums[label] = nums[label], nums[i]

        return nums

    def InsertionSort(self, nums):
        n = len(nums)

        for i in range(1, n):
            num = nums.pop(i)
            label = i
            for j in range(0,i):
                if num < nums[j]:
                    label = j
                    break
            nums.insert(label, num)
        
        return nums

    def ShellSort(self, arr):
        n = len(arr)
        gap = n//2
        while gap > 0:
            
            # 下面其实就是一个插入排序
            for j in range(gap, n):
                i = j
                while i >= gap and arr[i] < arr[i - gap]:
                    arr[i], arr[i - gap] = arr[i - gap], arr[i]
                    i -= gap
                    print(arr)
            gap //= 2
        return arr

    def MergeSort(self, nums):
        n = len(nums)
        if n == 0 or n == 1:
            return nums
        
        left = self.MergeSort(nums[:n//2])
        right = self.MergeSort(nums[n//2:])

        for i in range(len(right)):
            label = len(left)
            for j in range(len(left)):
                if right[i] < left[j]:
                    label = j
                    break

            left.insert(label, right[i])
        return left
    
    def QuickSort(self, nums):
        n = len(nums)
        if not nums:
            return []

        base = nums[0]
        left = []
        right = []
        for i in range(1, n):
            if nums[i] < base:
                left.append(nums[i])
            else:
                right.append(nums[i])
        
        return self.QuickSort(left) + [base] + self.QuickSort(right)

    # 堆排序
    def heapify(self, nums, n, i): # 对nums[i]进行堆排序，排序的最大index是n
        largest = i  
        l = 2 * i + 1     # left = 2*i + 1 
        r = 2 * i + 2     # right = 2*i + 2 

        # 小顶堆
        # if l < n and nums[i] < nums[l]: 
        #     largest = l 
    
        # if r < n and nums[largest] < nums[r]: 
        #     largest = r 

        # 大顶堆
        if l < n and nums[i] > nums[l]: 
            largest = l 
    
        if r < n and nums[largest] > nums[r]: 
            largest = r 
    
        if largest != i: 
            nums[i],nums[largest] = nums[largest],nums[i]  # 交换
            self.heapify(nums, n, largest) 
  
    def heapSort(self, nums):
        n = len(nums)

        for i in range(n-1, -1, -1):
            self.heapify(nums, n, i)

        for i in range(n-1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            self.heapify(nums, i, 0)
        
        
        return nums

a = Solution()

nums_1 = [2,4,3214,5,14,31,5431,653,7, 4321,45,543,541,43,44]
nums_2 = []
b = a.QuickSort(nums_1)
c = a.QuickSort(nums_2)
print(b)
print(c)
