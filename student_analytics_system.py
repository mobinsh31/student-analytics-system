"""
Mini Project
Author: Mobina Shokouhi
Topic: Student Analytics System
Date: 2026-07-3
"""

import numpy as np

scores = np.array([
    [18,17,19],
    [15,14,16],
    [20,19,20],
    [12,13,11],
    [17,18,16]
])

course_names = ["Math", "Programming", "Statistics"]

student_names = [
    "Student 1",
    "Student 2",
    "Student 3",
    "Student 4",
    "Student 5"
]

# ===== Student Analytics System =====

# Number of Students:

print( f" Number of Students: {scores.shape[0]} ")

# Number of Courses:

print( f" Number of Courses: {scores.shape[1]} ")

# Dataset Shape:

print(f" Dataset Shape: {scores.shape} ")

# Scores of Student 1

print(f" Student 1 :{scores[0,:]} ")

# Scores of Student 3

print(f" Student 3 :{scores[2,:]} ")

# Scores of Last Student

print(f" Last Student :{scores[-1,:]} ")

# All Math Scores

print(f" Math scores : {scores[: , 0 ]}")

# All Programming Scores

print(f" Programming Scores : {scores[: , 1 ]}")

# All Statistics Scores

print(f" Statistics Scores : {scores[: , -1 ]}")


#==== average of scores =====

student_averages = np.mean(scores , axis= 1)

# Average Score of Student 1

print(f" Average Score of Student 1: {student_averages [0]} " ) 

# Average Score of Student 2

print(f" Average Score of Student 2: {student_averages [1]} " ) 

# Average Score of Student 3

print(f" Average Score of Student 3: {student_averages [2]} " ) 

# Average Score of Student 4

print(f" Average Score of Student 4: {student_averages [3]} " ) 

# Average Score of Student 5

print(f" Average Score of Student 5: {student_averages [4]} " ) 

#==== average of courses =====

course_averages = np.mean (scores , axis= 0 )  

best_course_index = np.argmax(course_averages)

worst_course_index = np.argmin(course_averages)

# Average Math Score:

print (f" Average Math Score : {course_averages [0] } ")

# Average Programming Score:

print (f" Average Programming Score : {course_averages [1] } ")

# Average Statistics Score:

print (f" Average Statistics Score : {course_averages [2] } ")

# ===== best & worst =====

best_student = np.max(student_averages)

best_student_index = np . argmax(student_averages)

worst_student = np.min(student_averages)

worst_student_index = np.argmin(student_averages)

# Best Student Average:

print(f" Best Student Average : {best_student} " )

print(f"{ student_names[best_student_index] } is  best student")

# Worst Student Average:

print(f" Worst Student Average : {worst_student} " )

print(f"{ student_names[worst_student_index] } is  worst student")

# Best courses :

print(f"{ course_names[best_course_index] } is best course . ")

# Worst courses :

print(f"{ course_names[worst_course_index] } is worst course . ")