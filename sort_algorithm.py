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
    
    def HeapSOrt(self, nums):
        return nums

a = Solution()

nums_1 = [2,4,3214,5,14,31,5431,653,7, 4321,45,543,541,43,44]
nums_2 = []
b = a.QuickSort(nums_1)
c = a.QuickSort(nums_2)
print(b)
print(c)