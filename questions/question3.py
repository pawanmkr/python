def multuple(nums):
    temp = list(nums)
    product = 1
    for x in temp:
        product *= x
    return product

nums = (4, 3, 2, 2, -1, 18)
print(nums)
print("Product: ",multuple(nums))
