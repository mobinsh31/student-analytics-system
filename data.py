"""
Mini Project
Author: Mobina Shokouhi
Topic: Student Analytics System
Date: 2026-07-3
"""

import numpy as np

student_names = [
    "Paul Casey",
    "Danielle Sandoval",
    "Tina Andrews",
    "Tara Clark",
    "Anthony Campos",
    "Kelly Wade",
    "Anthony Smith",
    "George Short",
    "Stanley Gutierrez",
    "Audrey Simpson",
    "Gabrielle White",
    "Clinton Randolph",
    "Patricia Gomez",
    "Pamela Jackson",
    "Laura Jackson",
    "Roger Wiley",
    "Vicki Thompson",
    "Maxwell Davidson",
    "Jonathan Werner",
    "Angela Rios",
    "Tim Nichols",
    "Kyle Willis",
    "Shannon Simpson",
    "Sean Griffin",
    "Cassandra West",
    "Patricia Chavez",
    "Jason Williams",
    "Peter Gibbs",
    "Jeffrey Blanchard",
    "Carol Hill"
]

course_names = [
    "Programming Fundamentals",
    "Discrete Mathematics",
    "Physics",
    "Data Structures",
    "Database Systems",
    "English",
    "Probability & Statistics"
]

scores = np.array([
    [73, 81, 93, 97, 63, 80, 87],
    [90, 86, 96,100, 90, 88, 90],
    [81, 97, 95, 96, 65, 77, 94],
    [71, 74, 88, 80, 89, 63, 86],
    [84, 77, 65, 65, 80, 74, 76],
    [93,100, 67, 78, 72, 80, 84],
    [99, 96, 97, 73, 88, 76, 64],
    [95, 95, 82, 63, 84, 70, 85],
    [94, 68, 94, 85, 81, 74, 72],
    [98, 69, 88, 71, 67, 71, 73],
    [65, 60, 97, 94, 71, 81, 66],
    [80, 61,100, 65, 87, 64, 61],
    [94, 59, 69, 67, 89, 65, 73],
    [66, 94, 86,100, 57, 90, 63],
    [96, 90, 86, 92, 92, 95, 87],
    [94, 50, 78, 64, 79, 74, 84],
    [92, 64, 93, 91, 80, 89, 72],
    [86, 83, 85, 79, 93, 76, 77],
    [92, 87, 92, 99, 97, 87, 86],
    [99, 65, 98, 75, 66, 72,100],
    [100,90, 72, 98, 73, 97, 72],
    [57, 55, 78, 94, 83, 88, 88],
    [89, 72, 68, 72, 71, 54, 90],
    [50, 76, 81, 55, 56, 80, 79],
    [87, 91, 90, 88, 95, 88, 93],
    [92, 86, 87, 81, 93, 90, 99],
    [100,77, 80, 94, 63, 90, 90],
    [64, 75, 93, 79, 81, 96, 85],
    [79, 65, 99, 71, 76, 77, 83],
    [82,100, 61, 97, 30, 74, 73]
])
