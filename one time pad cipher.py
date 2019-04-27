###This program uses the one time pad cipher concept with the ascii value as its number for text
global cipher

def enc():
    data = str(input("Enter the char"))
    key = str(input("Enter the key"))
    cipher = ord(data) + ord(key)
    cipher = chr(cipher)
    print(cipher)
def dec():
    cipher = input("enter the cipher text :")
    key = input("enter key :")
    msg = ord(cipher) - ord(key)
    msg = chr(msg)
    print("the message is :" + str(msg))
def main():
    ch = int(input("Press 1 to encrypt\n2 to decrypt\n0 to exit"))
    if ch == 1:
        enc()
    elif ch == 2:
        dec()
    else:
        print("Project exited")
main()