# 5. Check for consecutive threes in a list
def consecutive_threes(list):
    for i in range(len(list)-1):
        if list[i] == 3 and list[i+1] == 3:
            return True
    return False

print(consecutive_threes([1, 3, 3])) 
print(consecutive_threes([1, 3, 1, 3]))  
