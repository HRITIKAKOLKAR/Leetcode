"""
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.  Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.
"""
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        lst=[]
        for i in arr2:
            lst+=[i]*arr1.count(i)
        arr1_set=list(set(arr1))
        for i in arr2:
            if i in arr1_set:arr1_set.remove(i)
        arr1_set.sort()
        for i in arr1_set:
            lst+=[i]*arr1.count(i)
        return lst
