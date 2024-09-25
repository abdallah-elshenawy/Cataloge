import os

library = {}

def clear_screen():
   os.system("cls" if os.name == "nt" else "clear")

def add_book():
   while True:
      clear_screen()
      isbn = input("Please enter the isbn: ")
      if (isbn not in library):
         title = input("Please enter the title: ")
         author = input("Please enter the author: ")
         # library[isbn] = {}
         # library[isbn]["title"] = title
         # library[isbn]["author"] = author
         # library[isbn]["available"] = True
         # library[isbn] = {"title": title, "author": author, "available": True}
         print(f"Book '{title}' by {author} added to the catalog with ISBN {isbn}.")
      else:
         print(f"the book with ISBN {isbn} is already existed in the library!")
      choice = input("Do you want to add another book (y/n)? ").lower()
      if choice != "y":
         break

def check_out_book():
   while True:
      clear_screen()
      isbn = input("Enter ISBN to check out: ")
      if (isbn in library):
         if (library[isbn]["available"]):
            library[isbn]["available"] = False
            print(f"Book {library[isbn]["title"]} is checked out successfully.")
         else:
            print(f"The book with ISBN {isbn} is currently checked out.")
      else:
         print(f"The book with ISBN {isbn} not found in the library!")
      choice = input("Do you want to check out another book (y/n)? ").lower()
      if choice != "y":
         break

def check_in_book():
   while True:
      clear_screen()
      isbn = input("Enter ISBN to check in: ")
      if (isbn in library):
         if not library[isbn]["available"]:
            library[isbn]["available"] = True
            print(f"Book '{library[isbn]["author"]}' Checked in Successfully.")
         else:
            print(f"The book with ISBN {isbn} is already available in the library!")
      else:
         print(f"The book with ISBN {isbn} not found in the library!")

      choice = input("Do you want to check in another book (y/n)? ").lower()
      if choice != "y":
         break

def list_library():
   clear_screen()
   for isbn in library:
      book_info = library[isbn]
      print(f"ISBN: {isbn}, Title: {book_info["title"]}, Author: {book_info["author"]}, Available: {book_info["available"]}")
   input("Press any key to go back to the menu ....")

while True:
   print("\nMenu:")
   print("1. Add Book")
   print("2. Check Out Book")
   print("3. Check In Book")
   print("4. List Book")
   print("5. Exit")
   choice = int(input("Enter Your Choice (1-5): "))
   if (choice == 1):
      add_book()
   elif (choice == 2):
      check_out_book()
   elif (choice == 3):
      check_in_book()
   elif (choice == 4):
      list_library()
   elif (choice == 5):
      print("\nExiting the program ... \n")
      break
   else:
      print("Invalid input! Please enter a number from 1 to 5.")