import numpy as np
from data import scores, student_names, course_names
from analytics import (
    calculate_student_averages,
    calculate_course_averages,
    get_best_student,
    get_worst_student,
    get_best_course,
    get_worst_course
)

student_averages = calculate_student_averages(scores)
course_averages = calculate_course_averages(scores)

best_student = get_best_student(scores, student_names)
worst_student = get_worst_student(scores, student_names)

best_course = get_best_course(scores, course_names)
worst_course = get_worst_course(scores, course_names)


print(best_student)