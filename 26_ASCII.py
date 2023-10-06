print("enter a string: ",end= " ")
text = input()
textlength = len(text)
for char in text:
    ascii = ord(char)
    print(char,"/t",ascii)