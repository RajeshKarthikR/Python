

with open("text.txt", "r+") as write_file:

    write_file.read()
    write_file.write("h")


with open("text.txt", "w") as write_file:

    write_file.write("abc")
