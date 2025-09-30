"""
Завдання 0
Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
Створіть об'єкт цього класу, представляючи студента. Потім додайте метод до класу "Студент",
який дозволяє змінювати середній бал студента. Виведіть інформацію про студента та змініть
його середній бал.
"""

class Student:
    def __init__(self, name, surname, age, gpa):
        self.name = name
        self.surname = surname
        self.age = age
        self.gpa = gpa
    def change_gpa(self):
        new_gpa = input("Введіть новий середній бал: ")
        self.gpa = float(new_gpa)
        return self.gpa

student_1 = Student("Vasil","Shevchenko",19,8)
print(f"Ім'я: {student_1.name} {student_1.surname}     Вік: {student_1.age}    Cередній бал: {student_1.gpa}")
student_1.change_gpa()
print("Новий середній бал:", student_1.gpa)





"""
Завдання 1
Створіть клас, який описує книгу. Він повинен містити інформацію про автора, назву, рік видання та
жанр. Створіть кілька різних книжок. Визначте для нього методи __repr__ та __str__.
"""

class Book:
    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.reviews = []

    def add_review(self, review_obj):
        if isinstance(review_obj, Review):
            self.reviews.append(review_obj)
        else:
            print("Помилка: Спроба додати невалідий об'єкт як відгук.")

    def __str__(self):

        base_info = (f"*** КНИГА: '{self.title}' ({self.year}) ***\n"
                     f"Автор: {self.author}, Жанр: {self.genre}\n")

        if not self.reviews:
            reviews_info = "  (Відгуків поки що немає)"
        else:
            reviews_info = f"--- Список відгуків ({len(self.reviews)}) ---"
            for review in self.reviews:
                reviews_info += f"\n{review}"
            reviews_info += "\n------------------------------------"

        return base_info + reviews_info

    def __repr__(self):
        return (f"Book(author='{self.author}', title='{self.title}', "
                f"year={self.year}, genre='{self.genre}')")

book1 = Book("Джордж Орвелл", "1984", 1949, "Антиутопія")
book2 = Book("Леся Українка", "Лісова пісня", 1911, "Драма-феєрія")
book3 = Book("Рей Бредбері", "451° за Фаренгейтом", 1953, "Наукова фантастика")


print(book1)
print(book2)

bookshelf = [book1, book2, book3]
print(bookshelf)


"""
Завдання 2
Створіть клас, який описує відгук до книги. Додайте до класу книги поле(атрибут) – список_відгуків. Зробіть так,
щоб при виведенні обєкту классу книги на екран за допомогою функції print (__str__) також виводилися відгуки до неї.
"""

class Review:
    def __init__(self, user_name, text):
        self.user_name = user_name
        self.text = text

    def __str__(self):
        return f"  > Від {self.user_name}: \"{self.text}\""
