#using remove() to remove the largest and smallest function and then find the average of the rest
def centered_average(nums):
  nums.remove(min(nums))
  total =0
  nums.remove(max(nums))
  for i in nums:
    total += i
  return total/(len(nums))

print('centered_average([1, 2, 3, 4, 100]):', centered_average([1, 2, 3, 4, 100]))
print('centered_average([1, 1, 5, 5, 10, 8, 7]):',centered_average([1, 1, 5, 5, 10, 8, 7]))
print('centered_average([-10, -4, -2, -4, -2, 0]):',centered_average([-10, -4, -2, -4, -2, 0]))
print('centered_average([5, 3, 4, 6, 2]):',centered_average([5, 3, 4, 6, 2]))
print('centered_average([5, 3, 4, 0, 100]):',centered_average([5, 3, 4, 0, 100]))
print('centered_average([100, 0, 5, 3, 4]):',centered_average([100, 0, 5, 3, 4]))
print('centered_average([4, 0, 100]):',centered_average([4, 0, 100]))
print('centered_average([0, 2, 3, 4, 100]):',centered_average([0, 2, 3, 4, 100]))
print('centered_average([1, 1, 100]):',centered_average([1, 1, 100]))
print('centered_average([7, 7, 7]):',centered_average([7, 7, 7]))
print('centered_average([1, 7, 8]):',centered_average([1, 7, 8]))
print('centered_average([1, 1, 99, 99]):',centered_average([1, 1, 99, 99]))
print('centered_average([1000, 0, 1, 99]):',centered_average([1000, 0, 1, 99]))
print('centered_average([4, 4, 4, 4, 5]):',centered_average([4, 4, 4, 4, 5]))
print('centered_average([4, 4, 4, 1, 5]):',centered_average([4, 4, 4, 1, 5]))
print('centered_average([6, 4, 8, 12, 3]):',centered_average([6, 4, 8, 12, 3]))
