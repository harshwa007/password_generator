import random as rd
import string as st
import secrets as se
import time


def site_name(txt_file_name):
    with open("passlist.txt", "a+") as file_object:
        # Move read cursor to the start of file.
        file_object.seek(0)
        # If file is not empty then append '\n'
        data = file_object.read(1000)
        if len(data) > 0:
            file_object.write("\n")
        # Append text at the end of file
        file_object.write(txt_file_name)
        return txt_file_name


def save_site_name():
    z=input('type site or title to save\t')
    site_name(z)
    return z


def add_username_in_text_file(txt_file_name):
    with open("passlist.txt", "a+") as file_object:
        # Move read cursor to the start of file.
        file_object.seek(0)
        # If file is not empty then append '\n'
        data = file_object.read(1000)
        if len(data) > 0:
            file_object.write("\t\t")
        # Append text at the end of file
        file_object.write(txt_file_name)
        return txt_file_name


def add_password_in_text_file(txt_file_name):
    with open("passlist.txt", "a+") as file_object:
        # Move read cursor to the start of file.
        file_object.seek(0)
        # If file is not empty then append '\n'
        data = file_object.read(1000)
        if len(data) > 0:
            file_object.write("\t\t")
        # Append text at the end of file
        file_object.write(txt_file_name)
        return txt_file_name


def secure_username(length_of_username):
    temp_username = st.ascii_lowercase+st.digits
    username = se.choice(st.ascii_lowercase)
    for x in range(length_of_username):
        username+=se.choice(temp_username)
    username_list = list(username)
    se.SystemRandom().shuffle(username_list)
    username = ''.join(username_list)
    b = username
    add_username_in_text_file(b)
    return username


def create_username():
    print("Create & save your own username!")
    c=input("type your username: ")
    add_username_in_text_file(c)
    return c


def secure_password(lenths_of_password):
    temppass = st.ascii_letters + st.digits + st.punctuation
    password = se.choice(st.ascii_uppercase)
    password += se.choice(st.ascii_lowercase)
    password += se.choice(st.digits)
    password += se.choice(st.punctuation)
    for i in range(lenths_of_password):
        password += se.choice(temppass)
    password_list = list(password)
    se.SystemRandom().shuffle(password_list)
    password = ''.join(password_list)
    a = password
    add_password_in_text_file(a)
    return password


def create_password():
    print("Create & your own password")
    d=input("type your password: ")
    add_password_in_text_file(d)
    return d


def ts():
    time.sleep(1)


while True:
    print("*******************************username and password generation*********************** ")
    save_site_name()
    ts()
    print("selection:\t1:Generate Username \t2:Generate Password")
    selection=int(input("Enter your selection:  "))
    if selection ==1 or selection==2:
        ans1 = input("Do you want Random username? type Yes or No\t")
        if ans1 in('Yes','yes','Y','YES','y'):
            ts()
            print("choices for username creation are\n1= 8 length \n2=10 length\n3=12 length\n4=15 length")
            choice1 = int(input("enter your choice: "))
            if choice1 == 1:
                ts()
                print("your username is successfully generated & saved!!")
                print("your 8 length username is    ", secure_username(7))

            if choice1 == 2:
                ts()
                print("your password is successfully generated & saved!!")
                print("your 10 length username is    ", secure_username(9))

            if choice1 == 3:
                ts()
                print("your password is successfully generated & saved!!")
                print("your 12 length username is    ", secure_username(11))
            if choice1 == 4:
                ts()
                print("your password is successfully generated & saved!!")
                print("your 15 length username is    ", secure_username(14))
            if choice1 not in ('1', '2', '3', '4'):
                ts()
                print("please enter valid choices")
        elif ans1 in('No','No','n','N','no'):
            ts()
            create_username()

    if selection == 2 or selection==1:
        ans2 = input("Do you want Random Password? type Yes or No\t")
        if ans2 in ('Yes', 'yes', 'Y', 'YES', 'y'):
            ts()
            print("choices for password generation are \n1= 8 length\n2=10 length \n3=12 length \n4=15 length")
            choices = int(input("enter your choice: "))
            if choices == 1:
                ts()
                print("your password is successfully generated & saved!!")
                print("your 8 length password is    ", secure_password(4))

            if choices == 2:
                ts()
                print("your password is successfully generated & saved!!")
                print("your 10 length password is    ", secure_password(6))

            if choices == 3:
                ts()
                print("your password is successfully generated!! & saved")
                print("your 12 length password is    ", secure_password(8))
            if choices == 4:
                ts()
                print("your password is successfully generated & saved!!")
                print("your 15 length password is    ", secure_password(11))
            if choices not in('1','2','3','4'):
                print("please enter valid choices")
        if ans2 in ('No','No','n','N','no'):
            ts()
            create_password()
    key=input("press key Q or q or E or e to exit  ")
    if key in('Q','q','E','e'):
        ts()
        break
    else:
        continue


