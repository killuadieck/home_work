"""
题目：
    给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。
    你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

示例：
    给定 nums = [2, 7, 11, 15], target = 9
    因为 nums[0] + nums[1] = 2 + 7 = 9
    所以返回 [0, 1]

解题思路:
    方法一：
        因为n1 + n2 = target，并且n1 , n2都必须在nums中，
        所以只需要计算 n2 = target - nums[i] 中n2在nums中，用index()函数返回下角标
    方法二：
        参考大神解法，通过字典模拟哈希查询的过程
        将列表数据的值和下角标存储进字典，key为列表值，value为下角标。
        用get()函数判断n2 = target - n1，n2是否在存储过字典key中，存在则返回对应的value（下角标值），不存在就将当前的值存入字典等待下次比对判断
"""

# 方法一：
def twosum_one(nums,target):
    lens = len(nums)
    for i in range(lens):
        n1 = nums[i]
        n2 = target - n1
        if n2 in nums:
            j = nums.index(n2)
            if j != i:
                return [i, j]

#方法二
def twosum_two(nums,target):
    data = {}
    for i, num in enumerate(nums):
        if data.get(target - num) is not None: # 对data里进行key值查找，如果不存在则返回None，注意None和空值不一样
            return [data.get(target - num), i]
        data[num] = i

if __name__ == '__main__':

    nums = [2,3,1,2]
    target = 3
    result = twosum_two(nums,target)
    print(result)
