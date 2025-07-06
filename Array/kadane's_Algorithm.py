# maximum subarray problem
# OR find a nonempty subarray with largest sum

'''  Bruteforce --- 0(n*n) Time complexity '''

def bruteforce(nums:list) -> int:
    max_sum = nums[0]

    for i in range(len(nums)):
        cur_sum = 0
        for j in range(i,len(nums)):
            cur_sum += nums[j]
            max_sum = max(cur_sum,max_sum)
           # print(f'Current Sum:{cur_sum}|| Max Sum: {max_sum}')
    return max_sum

#print(bruteforce([4,-1,2,-7,3,4]))


'''  Kadanes Algorithm --- 0(n) Time complexity '''

def Kadanes(nums:list)->int:
    max_sum = nums[0]
    cur_sum = 0

    for num in nums:
        # cur_sum = max(cur_sum,0)
        # cur_sum += num
        cur_sum = max(cur_sum,0)+num
        max_sum = max(cur_sum,max_sum)

    return max_sum


# print(Kadanes([4, -1, 2, -7, 3, 4]))


'''  Slding Window Approach (returning two intexes of the subarray) --- 0(n) Time complexity '''

def sliding_window(nums:list)-> int:
    cur_sum = 0
    max_sum = nums[0]
    max_L = max_R = L = 0

    for R in range(len(nums)):
        if cur_sum<0:
            cur_sum = 0
            L = R

        cur_sum += nums[R]

        if cur_sum > max_sum:
            max_sum = cur_sum
            max_L = L
            max_R = R

    #return nums[max_L] + nums[max_R]
    return max_L,max_R



print(sliding_window([4, -1, 2, -7, 3, 4]))
