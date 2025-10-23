import csv
import random


def read_line(reader):
    fields = next(reader)
    print(" | ".join(fields))
    return fields


def slice(book_list, start, end):
    book_list.seek(0)
    reader = csv.reader(book_list, delimiter=",")
    for i in range(end):
        if i >= start:
            read_line(reader)
        else:
            next(reader)


def find_popular(book_list):
    book_list.seek(0)
    reader = csv.DictReader(book_list, delimiter=",")
    c = 0
    for r in reader:
        largeword = r["Book-Title"]
        if len(largeword) > 30:
            c += 1
    print(c)
    return c






if __name__ == '__main__':
    with open("books-en.csv") as book_list:
        reader = csv.reader(book_list, delimiter=",")
        read_line(reader)
        find_popular(book_list)
