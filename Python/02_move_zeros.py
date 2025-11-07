🧩 Problem: Move Zeroes

Question:
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input:  nums = [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]

-----------------------------------------------------------------------

✅ Approach 1

Code:
________

def moveZeros(nums):
    pos=0
    for i in range(len(nums)):
        if nums[i]!=0:
            nums[pos], nums[i]= nums[i], nums[pos]
            pos+=1
    return nums
    
print(moveZeros([0, 1, 0, 3, 12]))
________

-----------------------------------------------------------------------

✅ Approach 2 — In-Place Compact + Fill Zeros

Idea:
Instead of swapping every time, first move all non-zeroes forward, then fill rest with 0.

Code:

________

def moveZeroes(nums):
    insert_pos = 0
    for num in nums:
        if num != 0:
            nums[insert_pos] = num
            insert_pos += 1
    while insert_pos < len(nums):
        nums[insert_pos] = 0
        insert_pos += 1
    return nums
________

⏱️ Time Complexity: O(n)
📦 Space Complexity: O(1)

🧠 Key Concept Learned:

👉 Two-pointer pattern — one pointer for reading, one for writing.
This is one of the most common interview patterns in array problems.
