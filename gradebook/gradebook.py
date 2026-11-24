import csv
from statistics import mean, median
def load_students(filename= "students.csv"):
    students_list=[]
    scores=[]

    with open(filename, "r") as file:
        reader= csv.DictReader(file)
        for students in reader:
            try:
                name=(students["name"])
                course=(students["course"])
                score=int(students["score"])
            except ValueError:
                print(f"Invalid score for student {students['name']}: {students['score']}")
                continue
            if score>=90:
                grade="A"
            elif score>=80:
                grade="B"
            elif score>=70:
                grade="C"
            elif score>=60:
                grade= "D"
            else:
                grade="F"
            students_list.append({
                "name": name,
                "course": course,
                "score": score,
                "grade": grade
            })
            scores.append(score)
            print(f"{name} -{course}- {score} - {grade}")
    return students_list, scores
def compute_stats(students_list, scores):
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

    return class_count, class_mean, class_median, highest, lowest
        
def write_report(students_list, class_count, class_mean, class_median, highest, lowest, filename= "report.txt"):
    sorted_students = sorted (
        students_list,
        key=lambda student:["score"],
        reverse= True
    )       
    with open("report.txt", "w") as report:
        report.write("GRADEBOOK REPORT\n")
        report.write("")
        report.write(f"Class count: {class_count}\n")
        report. write (f" Class median: {class_median}\n")
        report.write(f"Class mean: {class_mean}\n")
        if highest is not None and lowest is not None:
            report.write(f"Class highest score: {highest["name"]} - {highest ["score"]}\n")
            report.write(f"Class lowest score: {lowest ["name"]} - {lowest ["score"]}\n")

        report.write("\nSTUDENT RESULTS\n")

        for student in  sorted_students:
            report.write(
                f"{student["name"]} - {student["course"]} -"
                f"{student['score']} - {student["grade"]}\n"
            )

def main():
    students_list, scores = load_students()
    class_count, class_mean, class_median, highest, lowest= compute_stats(students_list, scores)
    write_report(students_list, class_count, class_mean, class_median, highest, lowest)

if __name__ == "__main__":
    main()
