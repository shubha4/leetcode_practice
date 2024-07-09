#Two Sum Problem

def twoSum(nums, target):
    index = 0
    for i in range(len(nums)):
        val = nums[i]
        index += 1
        if index > len(nums):
            break
        else:
            new_list = nums[index:]
            second_pointer = i+1
            for j in new_list:
                if (val + j) == target:
                    list_of_vals = [i, second_pointer]
                    return list_of_vals
                else:
                    second_pointer += 1  
nums = [3,3]
target = 6
print(twoSum(nums, target))
