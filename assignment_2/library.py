'''
CS1026a 2023
Assignment 02
Rosaline Scully
250966670
rscully5
October 18, 2023
'''

'''
This code is a virtual library where you can add books, borrow books,
return books, and see a list of all the books in the library.
'''
#start function that is the main part of the program
def start():
    #list of starting books
    all_books = [
        ['9780596007126', "The Earth Inside Out", "Mike B", 2, ['Ali']],
        ['9780134494166', "The Human Body", "Dave R", 1, []],
        ['9780321125217', "Human on Earth", "Jordan P", 1, ['David', 'b1', 'user123']]
    ]
    #empty list of rented isbns waiting to be filled!
    rented_ISBNs = []
    done = False

    #first choice before entering the loop
    print_menu()
    selection = input("Your selection> ").lower()

    #main menu
    while not done:
        if selection == 'a' or selection == "1":
            new_book(all_books)
            print_menu()
        elif selection == 'r' or selection == "2":
            borrow(all_books, rented_ISBNs)
            print_menu()
        elif selection == 't' or selection == "3":
            return_book(all_books, rented_ISBNs)
            print_menu()
        elif selection == 'l' or selection == "4":
            list_books(all_books, rented_ISBNs)
            print_menu()
        elif selection == 'x' or selection == "5":
            print("$$$$$$$$ FINAL LIST OF BOOKS $$$$$$$$")
            list_books(all_books, rented_ISBNs)
            done = True
            break
        else:
            print("Wrong selection! Please select a valid option.")
            print_menu()
        selection = input("Your selection> ").lower()


#this is the menu function
def print_menu():
    print('\n######################')
    print('1: (A)dd a new book.')
    print('2: Bo(r)row books.')
    print('3: Re(t)urn a book.')
    print('4: (L)ist all books.')
    print('5: E(x)it.')
    print('######################\n')

#this function will add a new book to all_books
def new_book(one_new_book):
    done = False
    book_name = input("Book name> ")
    #after receiving user input, ensure the user enters a valid book name by prompting the user
    while not done:
        if "%" in book_name:
            print("Invalid book name!")
            book_name = input("Book name> ")
        elif "*" in book_name:
            print("Invalid book name!")
            book_name = input("Book name> ")
        else:
            done = True
    #author name has no further checking
    author = input("Author name> ")

    edition = input("Edition> ")
    done_2 = False
    #after receiving user input, ensure the edition is digits only by prompting the user
    while not done_2:
        if edition.isdigit() == False:
            print("Invalid edition number!")
            edition = input("Edition> ")
        else:
            edition = int(edition)
            done_2 = True

    isbn = input("ISBN> ")
    done_3 = False
    #after receiving user input, prompt the user to type in all digits and a 13 digit number
    while not done_3:
        if isbn.isdigit() == False:
            print("Invalid ISBN!")
            isbn = input("ISBN> ")
        elif len(isbn) != 13:
            print("Invalid ISBN!")
            isbn = input("ISBN> ")
        else:
            done_3 = True

    sum = 0
    counter = 1
    #starts mathematical verification to the isbn
    for i in isbn:
        if counter % 2 != 0:
            sum = sum + (int(i)*1)
            counter += 1
        elif counter % 2 == 0:
            sum = sum + (int(i)*3)
            counter += 1

    counter_2 = 0
    #check if isbn calculation is divisable by 10, if not, exit to main menu
    if sum % 10 == 0:
        for i in one_new_book:
            #check if there is a duplicate isbn
            if i[0] != isbn:
                counter_2 += 1
            else:
                print("Duplicate ISBN is found! Cannot add the book.")
                return one_new_book
        #add new book if everything looks good
        if counter_2 == len(one_new_book):
            one_new_book.append([isbn, book_name, author, edition, []])
            print("A new book is added successfully.")
    else:
        print("Invalid ISBN!")
    return one_new_book

#borrowing books function
def borrow(books,rented):
    #input from user
    name = input("Enter the borrower name> ")
    search = input("Search term> ").lower()
    books_found = 0
    #test if there's a "*" in the search term so it can search all books
    if "*" in search:
        search = search.replace("*","")
        counter_1 = 0
        for one_book in books:
            #search all the books and check if it's rented. if not rented borrow all books with search term.
            if search in one_book[1].lower():
                if one_book[0] not in rented:
                    rented.append(one_book[0])
                    books[counter_1][4].append(name)
                    books_found += 1
                    print(f" -\"{one_book[1]}\" is borrowed!")
            counter_1 += 1
        if books_found == 0:
            print("No books found!")
    #test if there's a "%" at the beginning of the search so it can search first words only.
    elif search[0] == "%":
        search = search.replace("%", "")
        counter_2 = 0
        for one_book in books:
            b = one_book[1].split(" ")
            #search all books and check if it's rented. if not rented, borrow all books with search term.
            if search == b[0].lower():
                if one_book[0] not in rented:
                    rented.append(one_book[0])
                    books[counter_2][4].append(name)
                    books_found += 1
                    print(f" -\"{one_book[1]}\" is borrowed!")
            counter_2 += 1
        if books_found == 0:
            print("No books found!")
    else:
        counter_3 = 0
        #test if the search term exactly matches a book title
        for one_book in books:
            if search == one_book[1].lower():
                #search all books and check if it's rented. if not rented, borrow all books with search term.
                if one_book[0] not in rented:
                    rented.append(one_book[0])
                    books[counter_3][4].append(name)
                    books_found += 1
                    print(f" -\"{one_book[1]}\" is borrowed!")
            counter_3 += 1
        if books_found == 0:
            print("No books found!")
    return books, rented

#returning books function
def return_book(books,rented):
    isbn = input("ISBN> ")
    #check if book isbn matches any in the rented list
    for book in rented:
        if book == isbn:
            for b in books:
                #if there is a match remove it and return to main menu
                if b[0] == isbn:
                    rented.remove(isbn)
                    print(f'\"{b[1]}\" is returned.')
                    r = list(rented)
                    return r
    #if there is no match, return to main menu
    print("No book is found!")
    return list(rented)

#list all books function
def list_books(books,rented):
    for one_book in books:
        #check if the book is in rented list so it can be labelled "unavailable"
        if one_book[0] in rented:
            print("---------------")
            print("[Unavailable]")
            print(f"{one_book[1]} - {one_book[2]}")
            print(f"E: {one_book[3]} ISBN: {one_book[0]}")
            print(f"borrowed by: {one_book[4]}")
        else:
            #if not in rented list, it will print "available"
            print("---------------")
            print("[Available]")
            print(f"{one_book[1]} - {one_book[2]}")
            print(f"E: {one_book[3]} ISBN: {one_book[0]}")
            print(f"borrowed by: {one_book[4]}")

start()