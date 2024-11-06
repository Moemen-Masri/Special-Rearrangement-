def special_rearrangement(nums):
    Even_nbs = [] #listbthat will store all the even numbers 
    Odd_nbs = [] #list that will store all the odd numbers
    for num in nums:
        #checking if the nb is even or odd
        if num % 2 == 0:
            Even_nbs.append(num)
        else:
            Odd_nbs.append(num)
    return Even_nbs + Odd_nbs #concatinating the two lists after sorting the values

List = input("Enter integers separated by spaces: ")
nums = list(map(int, List.split()))
print("Rearranged list:", special_rearrangement(nums))