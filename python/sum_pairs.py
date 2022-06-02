# Write a method that takes an integer array and a desired sum. The output will be pairs of numbers from the inputed integer array that equal that desired sum. If there are no pairs that work, return 'unable to find pairs'


def sum_pairs(int_list, des_sum):
    ans_list = []
    for idx,value in enumerate(int_list):
        for i in range(1, len(int_list), 1):
            if (value + int_list[i] == des_sum) and idx < i:
                ans_list.append([value, int_list[i]])
    if not ans_list:
        return 'unable to find pairs'
    return ans_list

print(sum_pairs([1,2,3,4,5], 9)) # [[4,5]]
print(sum_pairs([1,2,3,4,5], 7)) # [[2,5], [3,4]]
print(sum_pairs([3, 1, 5, 8, 2], 27)) # 'unable to find pairs'
