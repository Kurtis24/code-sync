class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #so we will be using DFS and so that
        n = len(nums)
        subset = []
        result = []
        
        def search(k):
            # Base Case: We have processed all elements (0 to n-1)
            if k == n:
                result.append(subset[:]) # Save a copy of the current subset
                return
            
            # Branch 1: Exclude the element at index k
            search(k + 1)
            
            # Branch 2: Include the element at index k
            subset.append(nums[k])
            search(k + 1)
            subset.pop() # Backtrack: Remove the element to restore state
            
        search(0)
        return result