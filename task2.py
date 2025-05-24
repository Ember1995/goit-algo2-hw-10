# Визначення класу Teacher
class Teacher:
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = set()
        self.assigned_subjects = set()

def create_schedule(subjects, teachers):
    uncovered_subjects = subjects.copy()
    selected_teachers = []

    while uncovered_subjects:
        best_teacher = None
        best_coverage = set()

        for teacher in teachers:
            coverage = teacher.can_teach_subjects & uncovered_subjects
            if not coverage:
                continue

            if (not best_teacher or 
                len(coverage) > len(best_coverage) or 
                (len(coverage) == len(best_coverage) and teacher.age < best_teacher.age)):
                best_teacher = teacher
                best_coverage = coverage

        if not best_teacher:
            return None

        best_teacher.assigned_subjects = best_coverage
        uncovered_subjects -= best_coverage
        selected_teachers.append(best_teacher)
        teachers.remove(best_teacher)

    return selected_teachers

if __name__ == '__main__':
    # Множина предметів
    subjects = {'Математика', 'Фізика', 'Хімія', 'Інформатика', 'Біологія'}

    # Створення списку викладачів
    teachers = [
        Teacher("Олександр", "Іваненко", 45, "o.ivanenko@example.com"),
        Teacher("Марія", "Петренко", 38, "m.petrenko@example.com"),
        Teacher("Сергій", "Коваленко", 50, "s.kovalenko@example.com"),
        Teacher("Наталія", "Шевченко", 29, "n.shevchenko@example.com"),
        Teacher("Дмитро", "Бондаренко", 35, "d.bondarenko@example.com"),
        Teacher("Олена", "Гриценко", 42, "o.grytsenko@example.com"),
    ]

    # Призначення предметів, які може викладати кожен викладач
    teachers[0].can_teach_subjects = {'Математика', 'Фізика'}
    teachers[1].can_teach_subjects = {'Хімія'}
    teachers[2].can_teach_subjects = {'Інформатика', 'Математика'}
    teachers[3].can_teach_subjects = {'Біологія', 'Хімія'}
    teachers[4].can_teach_subjects = {'Фізика', 'Інформатика'}
    teachers[5].can_teach_subjects = {'Біологія'}

    # Виклик функції створення розкладу
    schedule = create_schedule(subjects, teachers)

    # Виведення розкладу
    if schedule:
        print("Розклад занять:")
        for teacher in schedule:
            print(f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}")
            print(f"   Викладає предмети: {', '.join(teacher.assigned_subjects)}\n")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")
