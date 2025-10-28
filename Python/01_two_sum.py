🧩 Problem: Two Sum

Question:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to the target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: Because nums[0] + nums[1] == 9

-----------------------------------------------------------------------

✅ Approach 1 — Brute Force (O(n²))

Idea:
Check every pair (i, j) and see if their sum equals target.

Code (Python):
________

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
              
________

⏱️ Time Complexity: O(n²)
📦 Space Complexity: O(1)

-----------------------------------------------------------------------

✅ Approach 2 — Hash Map (O(n))

Idea:
Store the seen numbers in a dictionary.
For each number, check if (target - current_number) is already in the dictionary.

Code (Python):
________

def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
      
________

Example walkthrough:
For nums = [2, 7, 11, 15], target = 9

i=0 → num=2 → diff=7 → not in seen → seen={2:0}

i=1 → num=7 → diff=2 → in seen → return [0,1] ✅

⏱️ Time Complexity: O(n)
📦 Space Complexity: O(n)

-----------------------------------------------------------------------

✅ Approach 3 — Two Pointer (if sorted)

Condition: Works only if array is sorted.

Idea:
Keep two pointers: left and right.
If sum < target → move left forward
If sum > target → move right backward

Code (Python):
________

def twoSumSorted(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            return [left, right]
        elif total < target:
            left += 1
        else:
            right -= 1
          
________

⏱️ Time Complexity: O(n)
📦 Space Complexity: O(1)
