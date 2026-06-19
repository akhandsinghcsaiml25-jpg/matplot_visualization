import matplotlib.pyplot as plt


students = ["A", "B", "C", "D", "E", "F", "G"]
marks = [25, 45, 78, 90, 20, 35, 60]


passing_marks = 30

average_marks = sum(marks) / len(marks)

print("Average Marks =", round(average_marks, 2))

plt.figure(figsize=(8, 5))
plt.bar(students, marks)


plt.axhline(y=average_marks,
            linestyle='--',
            label=f'Average = {average_marks:.2f}')


plt.axhline(y=passing_marks,
            linestyle=':',
            label='Passing Marks = 30')

plt.title("Student Marks - Bar Graph")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.legend()
plt.show()


plt.figure(figsize=(8, 5))
plt.scatter(students, marks)


plt.axhline(y=average_marks,
            linestyle='--',
            label=f'Average = {average_marks:.2f}')


plt.axhline(y=passing_marks,
            linestyle=':',
            label='Passing Marks = 30')

plt.title("Student Marks - Scatter Plot")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.legend()
plt.show()
