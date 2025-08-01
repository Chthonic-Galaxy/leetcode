def merge(nums1: list[int], m: int, nums2: list[int], n: int):
    p1 = m-1
    p2 = n-1
    p_w = m+n-1
    while p1 >= 0 and p2 >=0:
        if nums1[p1] > nums2[p2]:
            nums1[p_w] = nums1[p1]
            p1 -= 1
        else:
            nums1[p_w] = nums2[p2]
            p2 -= 1
        p_w -= 1
    
    while p2 >= 0:
        nums1[p_w] = nums2[p2]
        p2 -= 1
        p_w -= 1
    
    return nums1


print(merge([1,2,3,0,0,0], 3, [2,5,6], 3))
print(merge([4,5,6,0,0,0,0], 3, [1,2,3,5], 4))
print(merge([1], 1, [0], 0))
print(merge([0], 0, [1], 1))