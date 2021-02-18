nums = input("Введите числа: ").split(",")
new_nums = [nums[i] for i in range(0, len(nums)) if nums[i] != nums[i-1]]
print(new_nums)
