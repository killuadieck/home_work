"""
题目：
    给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。
    请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
    你可以假设 nums1 和 nums2 不会同时为空。
示例：
    不需要

解题思路:
    方法一：
        将2个list合并成一个，并且排序。然后取合并后的list长度。奇数则中位数，如果是偶数则取 n//2 和 n//2 - 1 两个的平均数
    方法二：
        采用二分查找的方法
"""


# 方法一
def motsa(nums1, nums2):
    l = nums1 + nums2
    l.sort()
    s = len(l)
    if s % 2 == 0:
        return (l[s // 2] + l[s // 2 - 1]) / 2
    else:
        return l[s // 2]


#方法二
