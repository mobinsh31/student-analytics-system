import numpy as np

# Student Average
def calculate_student_averages (scores) :
 averages = np.mean(scores , axis= 1)
 return averages

#Course Average
def calculate_course_averages (scores) :
 course_averages = np.mean (scores , axis= 0 )  
 return course_averages

#Best Student
def get_best_student (scores , student_names) :
 averages = calculate_student_averages(scores)
 best_student_index = np.argmax(averages)
 return student_names[best_student_index], averages[best_student_index]

#Worst Student
def get_worst_student (scores, student_names):
  averages = calculate_student_averages(scores)
  worst_student_index = np.argmin(averages)
  return student_names[worst_student_index], averages[worst_student_index]

#Best Course
def get_best_course(scores , course_names) :
 course_averages=calculate_course_averages (scores)
 best_course_index = np.argmax(course_averages)
 return course_names[best_course_index], course_averages[best_course_index]

#Worst Course
def get_worst_course(scores, course_names) :
  course_averages=calculate_course_averages (scores)
  worst_course_index = np.argmin(course_averages)
  return course_names[worst_course_index], course_averages[worst_course_index]
#Failed Students
def get_failed_student(scores, student_names):
    averages = calculate_student_averages(scores)

    failed_students = []

    for i in range(len(averages)):
        if averages[i] < 12:
            failed_students.append((student_names[i], averages[i]))

    return failed_students

def get_student_ranking(scores, student_names):

    averages = calculate_student_averages(scores)

    students = list(zip(student_names, averages))

    students.sort(key=lambda x: x[1], reverse=True)

    return students

#Top N Students
def get_top_N_students(scores, student_names, n):

    ranking = get_student_ranking(scores, student_names)

    return ranking[:n]

#Student Report
def student_report(scores, student_names, course_names, student_name):

    student_index = student_names.index(student_name)

    student_scores = scores[student_index]

    averages = calculate_student_averages(scores)
    student_average = averages[student_index]

    ranking = get_student_ranking(scores, student_names)

    rank = 1

    for name, average in ranking:
        if name == student_name:
            break
        rank += 1


    report = {
        "name": student_name,
        "scores": dict(zip(course_names, student_scores)),
        "average": student_average,
        "rank": rank
    }

    return report