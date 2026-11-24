import csv
from statistics import mean, median

students_list=[]
scores=[]

with open("score.csv", "r") as file:
    reader= csv.DictReader(file)
    for student in reader:
        name=(student["name"])
        score=int(student["score"])

        students_list.append({"name": name, "score": score})
        scores.append(score)

        print(f"{name} - {score}")
        
if scores:
    class_count = len(scores)
    class_mean= mean(scores)
    class_median= median(scores)
    highest = max(students_list, key=lambda student: student ["score"])
    lowest= min(students_list, key= lambda student: student ["score"])

    print(f"Class_count is: {class_count}")
    print(f"Class_mean is: {class_mean}")
    print(f"Class_median is: {class_median}")
    print(f"Highest score is: {highest ["name"]} - {highest ["score"]}")
    print(f"Lowest score is: {lowest ["name"]} - {lowest ["score"]}")
else:
    print("No score")
