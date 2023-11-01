'''
Lookup O(1)
Push O(1)
insert O(n)
Delete O(n)
'''

import random
import datetime


# nums_1 = [random.randint(1,100000) for x in range(1)]
# nums_2 = [random.randint(1,100000) for x in range(10)]
# nums_3 = [random.randint(1,100000) for x in range(100)]
# nums_4 = [random.randint(1,100000) for x in range(1000)]
# nums_5 = [random.randint(1,100000) for x in range(10000)]
# nums_6 = [random.randint(1,100000) for x in range(100000)]
# nums_7 = [random.randint(1,100000) for x in range(1000000)]
# nums_8 = [random.randint(1,100000) for x in range(10000000)]
# nums_9 = [random.randint(1,100000) for x in range(100000000)]

# def evaul_insert_time(l: list[int]):
#     insert_target = len(l)//2
#     start = datetime.datetime.utcnow()
#     l.insert(insert_target, 1234)
#     end = datetime.datetime.utcnow()

#     dif = end-start
#     return dif.microseconds

# print(evaul_insert_time(nums_1))
# print(evaul_insert_time(nums_2))
# print(evaul_insert_time(nums_3))
# print(evaul_insert_time(nums_4))
# print(evaul_insert_time(nums_5))
# print(evaul_insert_time(nums_6))
# print(evaul_insert_time(nums_7))
# print(evaul_insert_time(nums_8))
# print(evaul_insert_time(nums_9))
# #print(evaul_insert_time(nums_10))


# Reverse A String

# s = 'andy'
# o = []
# for i in range(len(s)-1,-1, -1):
#     o.append(s[i])
# print(''.join(o))


# Merge sorted arrays
def merge_sorted_arrays(l1: list[int], l2: list[int]) -> list[int]:
    merged_list = []
    while len(l1)>0 or len(l2)>0:
        if len(l1)==0:
            merged_list.append(l2.pop(0))
        elif len(l2)==0:
            merged_list.append(l1.pop(0))
        elif l1[0] <= l2[0]:
            merged_list.append(l1.pop(0))
        else:
            merged_list.append(l2.pop(0))
    return merged_list



print(merge_sorted_arrays([0,3,4,31], [4,6,30]))

