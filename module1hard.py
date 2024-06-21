grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}


def average(args):
    return [sum(i) / len(i) for i in args]              # среднее значение баллов каждого студента


average_grades = list(average(grades))                  # средние баллы студентов записали в список

students_sort = sorted(students)                        # отсортировали множество по алфавиту
average_students = {key: value for (key, value)
                    in zip(students_sort, average_grades)}     # генерируем словарь: студент: средний балл
print(average_students)
