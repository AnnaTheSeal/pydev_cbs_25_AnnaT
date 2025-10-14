import os

"""
### Робота з файлами та папками — завдання

1. **Створення файлу**
   Створи текстовий файл `hello.txt` і запиши в нього рядок:

   ```
   Hello, Python!
   ```
"""
with open("hello.txt", "w", encoding="utf-8") as f:
    f.write("Hello, Python!\n")

"""
2. **Читання файлу**
   Відкрий файл `hello.txt` і виведи його вміст на екран.
"""
with open("hello.txt", "r", encoding="utf-8") as f:
    print(f.read())

"""   
3. **Дозапис у файл**
   Додай у файл `hello.txt` ще один рядок:

   ```
   Learning file operations.
   ```
"""
with open("hello.txt", "a", encoding="utf-8") as f:
    f.write("Learning file operations.\n")


"""
4. **Читання кількох рядків**
   Виведи всі рядки з файлу `hello.txt` по одному рядку (без додаткових символів `\n`).
"""
with open("hello.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())

"""
5. **Підрахунок символів**
   Прочитай файл `hello.txt` і виведи кількість символів у ньому.
"""

with open("hello.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print("Кількість символів:", len(content))

"""
6. **Створення папки**
   Створи папку з назвою `data`. Усередині неї створи файл `notes.txt` із текстом:

   ```
   My first note.
   ```
"""
os.makedirs("data", exist_ok=True)
with open("data/notes.txt", "w", encoding="utf-8") as f:
    f.write("My first note.\n")

"""
7. **Список файлів у папці**
   Виведи на екран список усіх файлів у папці `data`.
"""
files = os.listdir("data")
print("Файли в папці data:", files)

"""
8. **Копіювання вмісту**
   Прочитай вміст файлу `notes.txt` і запиши його у файл `copy.txt` (у тій же папці `data`).
"""
with open("data/notes.txt", "r", encoding="utf-8") as src:
    content = src.read()
with open("data/copy.txt", "w", encoding="utf-8") as dst:
    dst.write(content)

"""
9. **Об’єднання файлів**
   Створи два файли: `a.txt` і `b.txt`, кожен із будь-яким текстом.
   Запиши їхній вміст у новий файл `ab.txt`.
"""
with open("a.txt", "w", encoding="utf-8") as f:
    f.write("Це файл A.\n")
with open("b.txt", "w", encoding="utf-8") as f:
    f.write("Це файл B.\n")

with open("ab.txt", "w", encoding="utf-8") as f:
    for filename in ["a.txt", "b.txt"]:
        with open(filename, "r", encoding="utf-8") as src:
            f.write(src.read())

"""
10. **Пошук слова у файлі**
    У файлі `notes.txt` перевір, чи є слово `"note"`.
    Якщо є — виведи `"Знайдено"`, інакше `"Не знайдено"`.
"""
with open("data/notes.txt", "r", encoding="utf-8") as f:
    text = f.read()
if "note" in text:
    print("Знайдено")
else:
    print("Не знайдено")