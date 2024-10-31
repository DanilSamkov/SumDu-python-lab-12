import json
from datetime import datetime

# Дані про учнів
students = [
    {"прізвище": "Щоголів", "ім'я": "Кирило", "по_батькові": "Радимович", "дата_народження": "2001-01-15",
     "стать": "чоловіча"},
    {"прізвище": "Цар", "ім'я": "Еммануїла", "по_батькові": "Олегівна", "дата_народження": "2005-02-25",
     "стать": "жіноча"},
    {"прізвище": "Дикий", "ім'я": "Юрій", "по_батькові": "Златович", "дата_народження": "2009-03-10",
     "стать": "чоловіча"},
    {"прізвище": "Юринець", "ім'я": "Роксолан", "по_батькові": "Леонідович", "дата_народження": "2002-04-30",
     "стать": "чоловіча"},
    {"прізвище": "Франчук", "ім'я": "Орися", "по_батькові": "Северинівна", "дата_народження": "1999-05-22",
     "стать": "жіноча"},
    {"прізвище": "Їжак", "ім'я": "Чеслава", "по_батькові": "Костянтинівна", "дата_народження": "2003-06-12",
     "стать": "чоловіча"},
    {"прізвище": "Посікіра", "ім'я": "Божена", "по_батькові": "Вікторівна", "дата_народження": "2009-07-07",
     "стать": "жіноча"},
    {"прізвище": "Гучок", "ім'я": "Шарль", "по_батькові": "Арсенович", "дата_народження": "2001-08-14",
     "стать": "чоловіча"},
    {"прізвище": "Хижняк", "ім'я": "Жадан", "по_батькові": "Юхимович", "дата_народження": "2006-09-17",
     "стать": "чоловіча"},
    {"прізвище": "Удовиченко", "ім'я": "Світолик", "по_батькові": "Костянтинович", "дата_народження": "2000-10-29",
     "стать": "чоловіча"}
]


# Функція для перевірки вводу
def validate_name_field(field_name, input_str):
    if not input_str.isalpha():
        raise ValueError(f"{field_name} не повинно містити цифри або спеціальні символи.")
    return input_str


# Перевірка статі
def validate_gender(gender):
    if gender not in ["чоловіча", "жіноча"]:
        raise ValueError("Стать повинна бути 'чоловіча' або 'жіноча'.")
    return gender


# Перевірка дати народження
def validate_birthdate(birthdate):
    try:
        datetime.strptime(birthdate, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Дата народження повинна бути у форматі рррр-мм-дд.")
    return birthdate


# Функція запису даних у JSON файл
def write_students_to_json(filename="students.json"):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump({"students": students}, file, ensure_ascii=False, indent=4)


# Функція зчитування та виведення вмісту JSON файлу у вигляді таблиці
def read_students_from_json(filename="students.json"):
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)
        students = data.get("students", [])  # Извлекаем список студентов

        header = f"{'Прізвище':<12} {'Ім\'я':<10} {'По батькові':<15} {'Дата народження':<15} {'Стать':<10}"
        print(header)
        print("=" * len(header))

        for student in students:
            print(
                f"{student['прізвище']:<12} {student['ім\'я']:<10} {student['по_батькові']:<15} {student['дата_народження']:<15} {student['стать']:<10}"
            )


# Функція додавання нового запису
def add_student_to_json(new_student, filename="students.json"):
    with open(filename, "r+", encoding="utf-8") as file:
        data = json.load(file)
        students_list = data.get("students", [])
        students_list.append(new_student)
        data["students"] = students_list
        file.seek(0)
        json.dump(data, file, ensure_ascii=False, indent=4)
        file.truncate()


# Функція видалення запису
def delete_student_from_json(prizvische, filename="students.json"):
    with open(filename, "r+", encoding="utf-8") as file:
        data = json.load(file)
        students_list = data.get("students", [])
        initial_count = len(students_list)
        students_list = [student for student in students_list if student['прізвище'] != prizvische]

        if len(students_list) == initial_count:
            print(f"Учня з прізвищем {prizvische} не знайдено.")
        else:
            print(f"Учня з прізвищем {prizvische} успішно видалено.")

        data["students"] = students_list
        file.seek(0)
        json.dump(data, file, ensure_ascii=False, indent=4)
        file.truncate()


# Функція пошуку учнів за полем з перевіркою
# Функция поиска учеников по указанному полю
def search_student_by_field(field, value, filename="students.json"):
    valid_fields = ['ім\'я', 'прізвище', 'по_батькові', 'дата_народження', 'стать']
    if field not in valid_fields:
        raise ValueError(f"Невірне поле для пошуку. Допустимі поля: {', '.join(valid_fields)}.")

    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)
        students_list = data.get("students", [])
        result = [student for student in students_list if student.get(field) == value]
        return result


# Функція запису результатів у JSON файл
def write_results_to_json(results, filename="results.json"):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump({"results": results}, file, ensure_ascii=False, indent=4)


# Функція знаходження учнів з днями народження у заданому місяці
def find_students_by_birth_month(month, filename="students.json", results_filename="results.json"):
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file).get("students", [])
        result = []
        for student in data:
            birth_month = datetime.strptime(student["дата_народження"], "%Y-%m-%d").month
            if birth_month == month:
                result.append(f"{student['ім\'я']} {student['прізвище']}")
        write_results_to_json(result, results_filename)
        return result


def main():
    write_students_to_json()
    print("Дані записані у JSON файл.")

    while True:
        print("\nМеню:")
        print("1. Показати всіх учнів")
        print("2. Додати учня")
        print("3. Видалити учня")
        print("4. Пошук учня за полем")
        print("5. Знайти учнів з днями народження у вказаному місяці")
        print("6. Вийти")

        choice = input("Виберіть опцію: ")

        if choice == "1":
            read_students_from_json()
        elif choice == "2":
            try:
                prizvische = validate_name_field("Прізвище", input("Введіть прізвище: "))
                imya = validate_name_field("Ім'я", input("Введіть ім'я: "))
                po_batkovi = validate_name_field("По батькові", input("Введіть по батькові: "))
                data_narodzhennya = validate_birthdate(input("Введіть дату народження (рррр-мм-дд): "))
                stat = validate_gender(input("Введіть стать (чоловіча/жіноча): "))
                new_student = {"прізвище": prizvische, "ім'я": imya, "по_батькові": po_batkovi,
                               "дата_народження": data_narodzhennya, "стать": stat}
                add_student_to_json(new_student)
                print("Учня додано.")
            except ValueError as e:
                print(f"Помилка: {e}")
        elif choice == "3":
            prizvische = input("Введіть прізвище учня, якого хочете видалити: ")
            delete_student_from_json(prizvische)
        elif choice == "4":
            try:
                field = input("Введіть поле для пошуку (ім'я, прізвище, по_батькові, дата_народження, стать): ")
                value = input(f"Введіть значення для поля {field}: ")
                results = search_student_by_field(field, value)
                if results:
                    print("Знайдено такі записи:")
                    header = f"{'Прізвище':<12} {'Ім\'я':<10} {'По батькові':<15} {'Дата народження':<15} {'Стать':<10}"
                    print(header)
                    print("=" * len(header))
                    for student in results:
                        print(
                            f"{student['прізвище']:<12} {student['ім\'я']:<10} {student['по_батькові']:<15} {student['дата_народження']:<15} {student['стать']:<10}")
                else:
                    print("Записів не знайдено.")
            except ValueError as e:
                print(f"Помилка: {e}")
        elif choice == "5":
            try:
                month = int(input("Введіть номер місяця (1-12): "))
                if 1 <= month <= 12:
                    results = find_students_by_birth_month(month)
                    if results:
                        print("Учні з днями народження у цьому місяці:")
                        for student in results:
                            print(student)
                            write_results_to_json(results)
                            print("Результати записані у results.json.")
                    else:
                        print("Немає учнів з днями народження у цьому місяці.")
                else:
                    print("Помилка: номер місяця повинен бути між 1 та 12.")
            except ValueError:
                print("Помилка: введіть коректний номер місяця.")
        elif choice == "6":
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
