#imports random integer
from random import randint

#Writes a a list to file name poem.txt
#A dream within a dream by edgar allen poe
poem_file = "poem.txt"
poem = [
"Take this kiss upon the brow!",
"And, in parting from you now,",
"Thus much let me avow:",
"You are not wrong who deem",
"That my days have been a dream;",
"Yet if hope has flown away",
"In a night, or in a day,",
"In a vision, or in none,",
"Is it therefore the less gone?",
"All that we see or seem",
"Is but a dream within a dream."
]

with open(poem_file,"w") as outfile:
    for i in poem:
        outfile.writelines(i + "\n")
outfile.close()


#gets filelines from poem.txt
def get_file_lines(filename):
    infile = open(poem_file,"r")
    poemlines = infile.readlines()
    infile.close()
    return poemlines

#This function gets the size of the list and uses it to calculate the length of the for loop
#by subtracting the length by the number of loops, the number is then used to make the
#the list appear as if going backwards.
def line_printed_backwards(line_list):
    size = len(line_list)-1

    for i in range(len(line_list)):
        print(f'{size-i + 1} {line_list[size - i]}')

#This function uses the size of the list to determine how many loops to run
#The for loop then uses a number between the length and 0 and prints that line out
def lines_printed_random(line_list):
    size = len(line_list)-1

    for i in range(len(line_list)):
        random = randint(0, size)
        print(line_list[random])

#This function prints out the even number first and then the odd
#By using if statements, the code checks if the number has a remainder
#If it has no remainder it prints out that line number
#the opposite is then done to print out the odd numbers
def lines_printed_custom(line_list):
    for i in range(len(line_list)):
        if (i % 2) == 0:
            pass
        else:
            print(line_list[i])

    for i in range(len(line_list)):
        if (i % 2) == 0:
            print(line_list[i])
        else:
            pass

    
#defines our variables
poemlist = get_file_lines(poem_file)
response = ''

#while loops until response = done
#the loop uses if statements to check what to print
while response != "done":
    print("How would you like your poem?")
    print("Type backwards for a backword reading,")
    print("Type random for random reading, ")
    print("Type custom for a even then odd reading")
    response = input("Type done to exit: " )
    if response == "backwards":
        line_printed_backwards(poemlist)
    if response == "random":
        lines_printed_random(poemlist)
    if response == "custom":
        lines_printed_custom(poemlist)

    
