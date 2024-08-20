# coreman book
#
# def max_crossing_subarray(arr,low,mid,high):
#     left_sum = -9_99_999
#     cur_sum = 0
#     for i in range(mid,low-1,-1):
#         cur_sum += arr[i]
#         if cur_sum > left_sum:
#             left_sum = cur_sum
#             max_left = i
#
#     right_sum = -9_99_999
#     cur_sum = 0
#     for i in range(mid+1,high):
#         cur_sum += arr[i]
#         if cur_sum > right_sum:
#             right_sum = cur_sum
#             max_right = i
#     return (max_left,max_right,left_sum+right_sum)
#
#
# def find_max_subarray(arr,low,high):
#     if low == high:
#         return (low,high,arr[low])
#     else:
#         mid = (low+high)//2
#         print('first condition')
#         (left_low,left_high,left_sum) = find_max_subarray(arr,low,mid)
#         print('second condition')
#         (right_low,right_high,right_sum) = find_max_subarray(arr,mid+1,high)
#         print('third condition')
#         (cross_low,cross_high,cross_sum) = find_max_subarray(arr,low,mid,high)
#
#         if left_sum >= right_sum and left_sum >= cross_sum:
#             return (left_low,left_high,left_sum)
#         elif right_sum >= left_sum and right_sum >= cross_sum:
#             return (right_low,right_high,right_sum)
#         else:
#             return (cross_low, cross_high, cross_sum)
# A Divide and Conquer based program
# for maximum subarray sum problem

# Find the maximum possible sum in
# arr[] auch that arr[m] is part of it


def maxCrossingSum(arr, l, m, h):
    # Include elements on left of mid.
    cur_sum = 0
    left_sum = -9_99_999
    max_left = m
    for i in range(m, l - 1, -1):
        cur_sum += arr[i]
        if cur_sum > left_sum:
            left_sum = cur_sum
            max_left = i
            print(left_sum,max_left)

    cur_sum = 0
    right_sum = -9_99_999
    max_right = m + 1
    for i in range(m+1, h):
        cur_sum = cur_sum + arr[i]
        if cur_sum > right_sum:

            right_sum = cur_sum
            max_right = i

    return [max_left, max_right, left_sum + right_sum]


# Returns sum of maximum sum subarray in aa[l..h]
# def maxSubArraySum(arr, l, h):
#     # Invalid Range: low is greater than high
#     if l > h:
#         return -10000
#     # Base Case: Only one element
#     if l == h:
#         return [l, h, arr[l]]
#
#     # Find middle point
#     m = (l + h) // 2
#
#     left = maxSubArraySum(arr, l, m - 1)
#     right = maxSubArraySum(arr, m + 1, h)
#     cross = maxCrossingSum(arr, l, m, h)
#
#     if left[2] >= (right[2] and cross[2]):
#         return left
#     elif right[2] >= (left[2] and cross[2]):
#         return right
#     else:
#         return cross







# Driver Code
arr = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
n = len(arr)
m = ((0 + n) // 2)
print(maxCrossingSum(arr,0,m,n))

# max_sum = maxSubArraySum(arr, 0, n - 1)
# print("Maximum contiguous sum is ", max_sum)

# This code is contributed by Nikita Tiwari.


# A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
#
# low, high = 0, len(A)
#
# print(find_max_subarray(A, low, high))
