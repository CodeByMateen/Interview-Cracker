🧩 Problem: Maximum Subarray

Question:
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum, and return that sum.

Example:

Input:  nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6

🧠 Intuition:

The array can have positive and negative numbers.
We need a continuous subarray with the highest possible total.

→ This is where Kadane’s Algorithm shines.
It’s elegant, powerful, and often reused in 10+ variations.

✅ Approach 1 — Brute Force (for understanding)

Idea:
Check sum of every possible subarray and keep track of the maximum.

Code:

def maxSubArray(nums):
    max_sum = float('-inf')
    for i in range(len(nums)):
        curr_sum = 0
        for j in range(i, len(nums)):
            curr_sum += nums[j]
            max_sum = max(max_sum, curr_sum)
    return max_sum


⏱️ Time: O(n²)
📦 Space: O(1)
(Too slow for large input, but good for understanding)

---------------------------------------------

 🧩 LEVEL 1: Basic Understanding — Sum of All Elements

Goal: Just learn how to loop and add numbers.

def sum_of_all(nums):
    total = 0
    for num in nums:
        total += num
    return total

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(sum_of_all(nums))


🧠 Concept learned:
→ Looping through list
→ Adding each element

✅ Output: 1

🧩 LEVEL 2: Subarray Basics — Print All Subarrays

Goal: Understand what subarrays even are.
(You’ll see every possible contiguous chunk of the array.)

def print_subarrays(nums):
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            print(nums[i:j+1])

nums = [1, 2, 3]
print_subarrays(nums)


🧠 Concept learned:
→ Nested loops = start and end points of subarray
✅ Output:

[1]
[1, 2]
[1, 2, 3]
[2]
[2, 3]
[3]

🧩 LEVEL 3: Subarray + Sum

Goal: Calculate each subarray’s sum.

def subarray_sums(nums):
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            sub = nums[i:j+1]
            print(sub, "=> Sum:", sum(sub))

nums = [-2, 1, -3, 4]
subarray_sums(nums)


🧠 Concept learned:
→ Every possible subarray
→ Its sum using sum(sub)

🧩 LEVEL 4: Track Maximum Sum Manually

Goal: Keep updating max as you find bigger sums.

def find_max_sum_brute(nums):
    max_sum = float('-inf')
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            sub = nums[i:j+1]
            s = sum(sub)
            print(f"{sub} => sum = {s}")
            if s > max_sum:
                max_sum = s
                print("🎯 New Max Found:", max_sum, "for subarray:", sub)
    return max_sum

nums = [-2,1,-3,4,-1,2,1,-5,4]
print("Max Subarray Sum:", find_max_sum_brute(nums))


🧠 Concept learned:
→ You now simulate what the main code does, but in readable form
→ You can see each step, not just compute fast

✅ Output shows exactly which subarray gives new max each time.

🧩 LEVEL 5: The Original Compact Version

Once you understand all the above, this version becomes easy:

def maxSubArray(nums):
    max_sum = float('-inf')
    for i in range(len(nums)):
        curr_sum = 0
        for j in range(i, len(nums)):
            curr_sum += nums[j]
            max_sum = max(max_sum, curr_sum)
    return max_sum


Now you’ll recognize:

curr_sum replaces sum(sub) for speed

We’re not printing anymore

The logic is same — just optimized

🧩 Bonus: return that list as well

def maxSum(nums):
    max_sum = float('-inf')
    best_subarray = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            sub = nums[i:j+1]
            summ = sum(sub)
            if summ > max_sum:
                max_sum = summ
                best_subarray = sub
    return best_subarray, max_sum

nums = [-2,1,-3,4,-1,2,1,-5,4]
print("Max Subarray and Sum:", maxSum(nums))

---------------------------------------------

