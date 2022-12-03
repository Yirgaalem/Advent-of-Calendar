'''
PART 1
Appreciative of your help yesterday, one Elf gives you an encrypted strategy guide (your puzzle input) that they say will be sure to help you win. "The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors. The second column--" Suddenly, the Elf is called away to help with someone's tent.

The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors. Winning every time would be suspicious, so the responses must have been carefully chosen.
The winner of the whole tournament is the player with the highest score. Your total score is the sum of your scores for each round. The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

Since you can't be sure if the Elf is trying to help you or trick you, you should calculate the score you would get if you were to follow the strategy guide.

For example, suppose you were given the following strategy guide:

A Y
B X
C Z
This strategy guide predicts and recommends the following:

In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends in a loss for you with a score of 1 (1 + 0).
The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.
In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).

What would your total score be if everything goes exactly according to your strategy guide?
-----------------------------------------------------------------------------------------------------------

Rock > Paper > Scissors > Rock
COLUMN 1
A - Rock
B - Paper
C - Scissors

COLUMN 2
X - Rock
Y - Paper
Z - Scissors

Selection - Rock is 1 point, Paper is 2 points, Scissors is 3 points
Outcome - Win is 6 points, Draw is 3 points, Loss is 0 point

The score of one round is the sum of the selection + outcome

------------------------------------------------------------------------------------------------------------------------------------- 
PART 2
The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column says how the round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"

The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round ends as indicated. The example above now goes like this:

In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you also choose Rock. This gives you a score of 1 + 3 = 4.
In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a score of 1 + 0 = 1.
In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.
Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12.

Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?
'''

def part1(opponent, user):
    # A function that will determine who wins
    roundSum = 0 
    if user == 'X':
        roundSum +=1
        if opponent == 'A':
            roundSum+=3
        elif opponent == 'B':
            roundSum+=0
        else:
            roundSum+=6
    
    elif user == 'Y':
        roundSum +=2
        if opponent == 'A':
            roundSum+=6
        elif opponent == 'B':
            roundSum+=3
        
        else:
            roundSum+=0
    
    else:
        roundSum +=3
        if opponent == 'A':
            roundSum += 0
        elif opponent == 'B':
            roundSum += 6
        
        else:
            roundSum += 3
    
    return roundSum

def part2(opponent, required):

    '''
    X means we need a lose +0 points, Y means we need a draw +3 points, Z means we need a win +6 points
    '''
    roundSum = 0

    if required == 'X':
        roundSum+=0

        # Opponent chose rock, to lose we need to choose scissors
        if opponent == 'A':
            roundSum += 3
        # Opponnent chose Paper, to lose we need Rock
        elif opponent == 'B':
            roundSum += 1
        # Opponent chose Scissors, to lose we need Paper
        else:
            roundSum +=2

    elif required == 'Y':
        roundSum += 3
        # Opponent chose rock, to draw we need to choose rock
        if opponent == 'A':
            roundSum += 1
        # Opponnent chose Paper, to draw we need paper
        elif opponent == 'B':
            roundSum += 2
        # Opponent chose Scissors, to draw we need paper
        else:
            roundSum +=3
    
    else:
        roundSum+=6
        # Opponent chose rock, to win we need to choose paper
        if opponent == 'A':
            roundSum += 2
        # Opponnent chose Paper, to win we need scissors
        elif opponent == 'B':
            roundSum += 3
        # Opponent chose Scissors, to win we need rock
        else:
            roundSum +=1
    return roundSum


with open('C:\\Users\\Nahor Yirgaalem\\Projects\\Advent of Calendar\\Day2\\input.txt') as file:
    part1_score = part2_score = 0
    for line in file:
        data = line.rsplit()
        opp = data[0]
        me = data[1]

        part1_score += part1(opp, me)
        part2_score += part2(opp, me)
        
    
    print(part1_score)
    print(part2_score)
