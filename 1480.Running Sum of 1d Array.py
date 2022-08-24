nums = [1, 2, 3 , 4]
    
res = []
aux = 0

for i in len(nums):
    aux += nums[i]
    res.append(aux)

print(res)
