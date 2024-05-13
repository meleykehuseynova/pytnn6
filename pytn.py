import random
import math

def funk():
    nums_list = []
    for _ in range(5):
        nums_list.append(random.randint(20, 50))
    
    print("Əsas list:", nums_list)
    
    for i in range(len(nums_list)):
        if nums_list[i] % 2 == 0:
            nums_list[i] = math.pow(nums_list[i], 2)
    
    print("Dəyişdirilmiş list:", nums_list)

funk()
