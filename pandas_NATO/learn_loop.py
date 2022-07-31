
### dictionary comprehension
names = ['Alex', 'Beth', 'Cal', 'Dalling', 'Eleanor', 'Freddie']
import random
students_scores = {students:random.randint(80,100) for students in names}
passed_students = {name: value for (name, value) in students_scores.items() if value >= 80} # ★
print(passed_students)


### Loop through data frame
import pandas as pd
stduent_dict = {"student": ["Alex", "Beth", "Caroline"],
"score": [56,76,98]}
data = pd.DataFrame(stduent_dict)

for index, row in data.iterrows():
#   print(row.student)
#   print(row.score)
    if row.student == 'Alex':
        print(row.score)