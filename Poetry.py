from random import randint

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


def get_file_lines(filename):
    infile = open(poem_file,"r")
    poemlines = infile.readlines()
    infile.close()
    return poemlines

def line_printed_backwards(line_list):
    size = len(line_list)-1

    for i in range(len(line_list)):
        print(f'{size-i + 1} {line_list[size - i]}')

def lines_printed_random(line_list):
    size = len(line_list)-1

    for i in range(len(line_list)):
        random = randint(0, size)
        print(line_list[random])

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

    

poemlist = get_file_lines(poem_file)
lines_printed_custom(poemlist)

#line_printed_backwards(get_file_lines(poem_file))

