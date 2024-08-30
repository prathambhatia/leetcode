### Intuition

If an array is sorted and rotated, there is only one breakpoint where `nums[x] > nums[x+1]`. If the array is only sorted (without rotation), there are zero breakpoints.

### Complexity

- **Time Complexity**: O(n)
- **Space Complexity**: O(1)

### Code

```python
class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        n = len(nums)
        for i in range(n):
            # Check if there is a breakpoint
            if nums[i] > nums[(i + 1) % n]:
                count += 1
        # Return true if there is at most one breakpoint
        return count <= 1

### Explanation
"""
The `% n` is used to handle the case where the comparison wraps around from the end of the array to the beginning. Consider the case `nums = [2, 1, 3, 4]`.

Without `% n`, the function would incorrectly return `true` for this case, as it would only compare adjacent elements within the bounds of the array. By using `% n`, the function correctly checks the transition from the last element to the first, ensuring accurate detection of whether the array is sorted and rotated.
"""

O(n^2) Solution:-
    def check(self, nums: List[int]) -> bool:     ## O(n^2)
        n= len(nums)
        sorted_nums=sorted(nums)
        for i in range(n):
            if nums[i:]+nums[:i]==sorted_nums:
                return True
        return False
