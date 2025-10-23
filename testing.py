import csv
import random

def read_line(reader):
    """Читает и выводит одну строку из CSV файла"""
    fields = next(reader)
    print(" | ".join(fields))
    return fields

def slice(book_list, start, end):
    """Выводит срез строк из файла"""
    book_list.seek(0)
    reader = csv.reader(book_list, delimiter=",")
    for i in range(end):
        if i >= start:
            read_line(reader)
        else:
            next(reader)

def count_long_titles(book_list):
    """Подсчитывает количество книг с названиями длиннее 30 символов"""
    book_list.seek(0)
    reader = csv.DictReader(book_list, delimiter=",")
    c = 0
    for r in reader:
        largeword = r["Book-Title"]
        if len(largeword) > 30:
            c += 1
    
    # ВЫВОДИМ результат!
    print(f'📊 Количество книг с названиями длиннее 30 символов: {c}')
    return c

def find_books_by_author(book_list, author_name):
    """Ищет книги указанного автора за 1991 и 1996 годы"""
    book_list.seek(0)
    reader = csv.DictReader(book_list, delimiter=",")
    found_books = []
    
    for row in reader:
        if (row["Book-Author"].lower() == author_name.lower() and 
            row["Year-Of-Publication"] in ['1991', '1996']):
            found_books.append(row)
    
    print(f"\n🔍 Найдено книг автора '{author_name}' за 1991-1996 годы: {len(found_books)}")
    for book in found_books:
        print(f"   - '{book['Book-Title']}' ({book['Year-Of-Publication']})")
    
    return found_books

def generate_bibliography(book_list, num_entries=20):
    """Генерирует библиографические ссылки для случайных книг"""
    book_list.seek(0)
    reader = csv.DictReader(book_list, delimiter=",")
    
    # Собираем все подходящие книги
    all_books = [row for row in reader if row["Book-Author"] and row["Book-Title"]]
    
    # Выбираем случайные
    selected_books = random.sample(all_books, min(num_entries, len(all_books)))
    
    # Создаем библиографические ссылки
    bibliography = []
    for i, book in enumerate(selected_books, 1):
        citation = f"{book['Book-Author']}. {book['Book-Title']} - {book['Year-Of-Publication']}"
        bibliography.append(f"{i}. {citation}")
    
    # Сохраняем в файл
    with open("bibliography.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(bibliography))
    
    print(f"\n✅ Сгенерировано {len(bibliography)} библиографических ссылок")
    print("📁 Сохранено в файл: bibliography.txt")
    
    return bibliography

if __name__ == '__main__':
    try:
        with open("books-en.csv", encoding='utf-8') as book_list:
            print("=" * 50)
            print("📚 СИСТЕМА АНАЛИЗА БИБЛИОТЕКИ")
            print("=" * 50)
            
            reader = csv.reader(book_list, delimiter=",")
            read_line(reader)  # Читаем заголовок
            
            # ЗАДАЧА 1: Подсчет длинных названий
            print("\n1. ПОДСЧЕТ КНИГ С ДЛИННЫМИ НАЗВАНИЯМИ")
            count_long_titles(book_list)
            
            # ЗАДАЧА 2: Поиск книг по автору
            print("\n2. ПОИСК КНИГ ПО АВТОРУ")
            author = input("Введите имя автора для поиска: ").strip()
            if author:
                find_books_by_author(book_list, author)
            else:
                print("❌ Имя автора не введено")
            
            # ЗАДАЧА 3: Генерация библиографии
            print("\n3. ГЕНЕРАЦИЯ БИБЛИОГРАФИЧЕСКИХ ССЫЛОК")
            generate_bibliography(book_list)
            
    except FileNotFoundError:
        print("❌ Ошибка: Файл 'books-en.csv' не найден!")
    except Exception as e:
        print(f"❌ Произошла ошибка: {e}")