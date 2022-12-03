# Find the elf carrying the most calories, how many total calories is that elf holding
# Context manager, always will close file
with open('C:\\Users\\Nahor Yirgaalem\\Projects\\Advent of Calendar\\Day1\\input.txt') as file:
    calories = []
    curr = []
    for line in file:
        try:
            curr.append(int(line.rstrip()))
        except:
            calories.append(curr)
            curr = []
    
    fatestElf = 0
    for elf in calories:
        countCalories = 0
        for eCals in elf:
            countCalories += int(eCals)
        
        if fatestElf < countCalories:
            fatestElf = countCalories
    
    print(fatestElf)