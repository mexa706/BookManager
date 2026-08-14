from asyncio.windows_events import NULL
from multiprocessing.process import active_children
from pydoc import text
from typing import List

bookList = [[1,"Meha","Say",2004],[2,"Valera","Garaj",2000],[3,"Artemka","Da",2003]]


def show_menu():
    print("==========================")
    print("        BOOK MANAGER      ")
    print("==========================")
    print("|1---Добавить книгу------|")
    print("|2---Показать все книги--|")
    print("|3---Найти книгу---------|")
    print("|4---Удалить книгу-------|")
    print("|5---Статистика----------|")
    print("|0---Выход---------------|")


def add_book(title, author, year,bookNumber):
    bookList.append([ bookNumber , title, author, year])
    print("Книга добавлена")
    return None


def show_books():
    print("Все Книги: ")
    for book in bookList:
        print(book)
    return None


def find_book(title):
    for book in bookList:
        if title in book[1]: print(book)
    print("Книга не найдена")


def delete_book(number):
    for book in bookList:
        if number == book[0]:
            bookList.remove(book)
            print("Книга Удалена")
    print("Книга не найдена")


def show_statistics():
    if len((bookList))==0 :
        print("Книг нет ")
        return None
    print("Статистика: ")
    print("Всего книг: ", len(bookList))
    oldBook=bookList[0][3]
    newBook=bookList[0][3]
    for book in bookList:
        if oldBook < book[3]:oldBook=book[3]
        elif newBook > book[3]:newBook=book[3]
    print("Самая старая книга: ", oldBook)
    print("Самая новая книга: ", newBook)
    return None


def main():
    stop = True
    bookNumber = 3
    while stop:
        show_menu()
        a = int(input("Выберите команду: "))
        match a:
            case 1:
                title = input("Введите название книги: ")
                author = input("Введите автора книги: ")
                if title != "" and author != "" :
                    year = input("Введите год книги: ")
                    if year != "":
                        year = int(year)
                        bookNumber=bookNumber+1
                        add_book(title, author, year,bookNumber)
                    else:
                        print("Не корректный ввод")
                        continue
                else:
                    print("Не корректный ввод")
                    continue

            case 2:
                show_books()
            case 3:
                title = input("Введите название книги: ")
                if title != "" :
                    find_book(title)
                else: print("Не корректный ввод")
            case 4:
                number = input("Введите номер книги: ")
                if number != "":
                    number = int(number)
                    delete_book(number)
                else: print("Не корректный ввод")
            case 5:
                show_statistics()
            case 0:
                stop = False
            case _:
                print("Ввод не корректный, попробуйте заново ")


main()
