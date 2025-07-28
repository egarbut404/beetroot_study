#Task 1

def count_local_var(func):
    return func.__code__.co_nlocals

def first_func():
    a = 10
    b = 10
    return a + b

def second_func(a, b, c):
    return a + b + c

print(count_local_var(first_func))
print(count_local_var(second_func))

#Task 2

def return_func(mult):
    def local_func(num):
        return num * mult
    return local_func

mult = return_func(2)
print(mult(5))

print(return_func(3)(10))

#Task 3

def choose_func(nums: list, func1, func2):
    if all(num > 0 for num in nums):
        return func1(nums)
    return func2(nums)

def square_nums(nums):
    return [num ** 2 for num in nums]

def remove_negatives(nums):
    return [num for num in nums if num > 0]


nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]

assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]
assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]
