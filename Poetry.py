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

infile = open(poem_file,"r")
print(infile.read())
infile.close()