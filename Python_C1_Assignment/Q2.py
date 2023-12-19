# Given a string with multiple occurrences of the word "book," write a Python program to replace only the first two occurrences with "notebook."

input_string = "I have a book, a pen, and another book in my bag and book."

res=input_string.replace("book","notebook",2)
print(res)