# Question 4 - codesignal style practice
# https://codesignal.com/blog/interview-prep/example-codesignal-questions/

lst = [{1,3}, {2,4}, {3,6}]
if {3,1} in lst:
    print("yes")


numbers = [1, -1, 2, 3]
# if len(numbers) < 2:
#     return 
numbers.sort() # [-1,1,2,3]
max_sum = numbers[-1] + numbers[-2] # 5
power_checker = -1
for i in range(100): 
    power_end = 2**i # 1, 2, 4, 8, 16, 32...
    if max_sum < power_end:
        power_checker = i

def question_four(numbers):
    hash_map = {}
    lst = []
    for number in numbers:
        hash_map[number] = hash_map.get(number, 0) + 1
    # hash_map = {1: 1, -1: 1, 2: 1, 3: 1}
    for i in range (power_checker):
        power_val = 2**i
        for number in numbers:
            finding_val = power_val - number
            if finding_val in hash_map:
                if {finding_val, number} not in lst: 
                    lst.append({finding_val, number})
    return len(lst)

print(question_four(numbers))


    
		

		

