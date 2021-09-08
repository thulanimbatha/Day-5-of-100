# get highest score from a list

hscores = input("Please enter a list of scores: ")
scores = hscores.split(" ")

highest_score = -1
for score in scores:
    score = int(score)
    if highest_score < score:
        highest_score = score

print(f"The highest score is {highest_score}")
