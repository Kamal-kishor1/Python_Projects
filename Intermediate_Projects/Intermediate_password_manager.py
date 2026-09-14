from cryptography.fernet import Fernet

"""def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:  # 'wb' - write bytes
        key_file.write(key)

write_key()"""


def load_key():
    file = open("key.key", "rb")  # 'rb' - read bytes
    key = file.read()
    file.close()
    return key


# master_pwd = input("enter your master password: ")

key = load_key()  # + master_pwd.encode()
# .encode convert to bytes or use master_pwd.bytes
fer = Fernet(key)


def view():
    with open("user_details.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.rsplit("|")

            decrypt_passw = fer.decrypt(passw.encode()).decode()

            print("user : ", user, "| password:", decrypt_passw)


def add():
    user_name = input("Account Name: ")
    user_password = input("Account Password: ")

    encrypt_password = fer.encrypt(user_password.encode())

    with open("user_details.txt", "a") as f:
        f.write(
            user_name + "|" + encrypt_password.decode() + "\n"
        )  # it provide the byte string - b'passw'  so decode it


while True:
    mode = input(
        "Would you like to add password or view old passwords: (view/add) or press 'q' to Quit: "
    )
    if mode == "q":
        break

    if mode == "view":
        view()

    elif mode == "add":
        add()

    else:
        print("invalid argument!")
