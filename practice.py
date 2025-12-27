# input is a list of integers
# loop through the list and print if each number is evern or odd
# 1: Odd
# 2: Even
# ...
nums = [4, 4, 6, 2, 5, 7, 1, 0, -2, -5]
print(nums)
# for i in nums:
#     print(i)
# for i in range(len(nums)):
#     print(nums[i])

for i in nums:
    if i % 2 != 0:
        print(i, ": Odd")
    else:
        print(i, ": Even")