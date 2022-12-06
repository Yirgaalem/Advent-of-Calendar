'''
Lowercase item types a through z have priorities 1 through 26.
Uppercase item types A through Z have priorities 27 through 52.
'''
from string import ascii_letters

letters = {}
for key, char in enumerate(ascii_letters):
    letters[char] = key+1

def part1(line):
    middle = len(line)//2
    sumCommon = 0
    first = {}
    second = {}
    for i in range(len(line)):
        if i < middle:
            first[line[i]] = first.get(line[i],0)+1
        else:
            second[line[i]] = second.get(line[i],0)+1
    

    for i in first:
        if second.get(i):
            sumCommon += letters[i]
            

    return sumCommon

def part2(lines):
   
    for i in lines[0]:
        if i in lines[1] and i in lines[2]:
            print(i)
            return letters[i]



with open('C:\\Users\\Nahor Yirgaalem\\Projects\\Advent of Calendar\\Day3\\input.txt') as file:
    totalSum = 0
    badge = 0
    three_lines = []
    count = 0
    for line in file:
        totalSum += part1(line)

        if len(three_lines) == 3:
            count +=1
            badge+=part2(three_lines)
            three_lines = []

        three_lines.append(line.strip())

  
    badge+=part2(three_lines)
    badge+=part2(three_lines)
    badge+=part2(three_lines)

    print(totalSum)
    print(badge)
