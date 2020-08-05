number = input("Phone: ")
phone = {
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "7":"seven",
    "8":"eight",
    "9":"nine"
}
output=""
for x in number:
    output += phone.get(x, "!") + " "
print(output)


