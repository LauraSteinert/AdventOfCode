# Advent of Code day 1!

# Importing!
import os

#File path to input.txt in a raw form!
filepath=os.path.normpath(r'input.txt')

#Function that does the pretty things!

#First, we open the file as f
with open(filepath) as f:
    all_calories = []  #Creating a list to put all the calories in it;
    for calories in f.read().split('\n\n'): #We separate the file in small calories groups whenever it finds an "\n\n";
        total = sum(int(calorie) for calorie in calories.split('\n')) #Then, we sum up the calories in the group of calories whenever we see a breakline;
        all_calories.append(total) #Then we append the total at the end of our list
    all_calories.sort(reverse=True) #Then, we sort it a descending order, so that the greatest one is in the first place.

def count_them_all(total): #Now, we just made a function to invoke the result of the things we did above
    return all_calories[0]

def top_three_gourmands(total): #Then, for the second part, we will take the range between 0 and 3 to make the sum of the top 3 gourmands of holiday season
    return sum(all_calories[0:3])

print(count_them_all(all_calories)) #Print the result of the call to the function!
print(top_three_gourmands(all_calories))#Print the result of the call to the function!
