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

=======================================================================
=======================================================================

A little Advance:----------

✅ Option 1 — Return all index pairs
________

def allTwoSums(nums, target):
    seen = {}
    pairs = []
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            pairs.append([seen[diff], i])
        seen[num] = i
    return pairs

print(allTwoSums([1, 3, 5, 7, 9, 11, 14], 14))

________ 🔹 Output: [[1, 5], [2, 4]]

✅ Option 2 — Return all number pairs
________

def allTwoSums(nums, target):
    seen = set()
    pairs = []
    for num in nums:
        diff = target - num
        if diff in seen:
            pairs.append((diff, num))
        seen.add(num)
    return pairs

print(allTwoSums([1, 3, 5, 7, 9, 11, 14], 14))

________ 🔹 Output: [(3, 11), (5, 9)]

💎 Final Clean Version — Unique Pairs (Numbers Only)
________

def allTwoSums(nums, target):
    seen = set()
    pairs = set()
    for num in nums:
        diff = target - num
        if diff in seen:
            # add pair in sorted order so (3,11) and (11,3) are treated same
            pairs.add(tuple(sorted((diff, num))))
        seen.add(num)
    return list(pairs)


print(allTwoSums([1, 3, 5, 7, 9, 11, 14, 3, 11, 5, 9], 14))

________ 🔹 Output: [(3, 11), (5, 9)]

⚙️ Two Pointer Method 
________

def twoPointerPairs(nums, target):
    nums.sort()  # sort list first (important!)
    left, right = 0, len(nums) - 1
    pairs = []

    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            pairs.append((nums[left], nums[right]))
            # Move both pointers to avoid duplicates
            left += 1
            right -= 1
            # skip duplicate values
            while left < right and nums[left] == nums[left - 1]:
                left += 1
            while left < right and nums[right] == nums[right + 1]:
                right -= 1
        elif total < target:
            left += 1
        else:
            right -= 1

    return pairs


print(twoPointerPairs([1, 3, 5, 7, 9, 11, 14, 3, 11, 5, 9], 14))

________ 🔹 Output: [(3, 11), (5, 9)]

