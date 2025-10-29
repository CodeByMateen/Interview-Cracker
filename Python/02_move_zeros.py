🧩 Problem: Move Zeroes

Question:
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input:  nums = [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]

-----------------------------------------------------------------------

✅ Approach 1 — In-Place Using Two Pointers (Efficient)

Idea:
Use a pointer last_non_zero to track where the next non-zero element should go.

Steps:

Traverse array.

If current number ≠ 0 → swap it with nums[last_non_zero] and increment last_non_zero.

Code:
________

def moveZeroes(nums):
    result = [num for num in nums if num != 0]
    zero_count = nums.count(0)
    result.extend([0] * zero_count)
    return result
________

Example walkthrough:

________

nums = [0, 1, 0, 3, 12]

Step 1: i=1 → num=1 → swap with nums[0] → [1,0,0,3,12], last_non_zero=1  
Step 2: i=3 → num=3 → swap with nums[1] → [1,3,0,0,12], last_non_zero=2  
Step 3: i=4 → num=12 → swap with nums[2] → [1,3,12,0,0], last_non_zero=3 ✅
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
