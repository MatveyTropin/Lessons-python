with open("File.txt") as file:
    text=file.read()
    print(text)
with open("File.txt",mode="w") as file:
    file.write("Hello")

    