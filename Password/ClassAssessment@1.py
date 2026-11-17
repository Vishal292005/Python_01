user = {}
print("_____Set Username&Password_____")
num = int(input("Enter the number of records:"))
for i in range(num):
    print(f"Enter the Users details:{i+1}")
    uname = input("set username:")
    while True:
        pwd = input("set password:")
        upper = 0
        lower = 0
        digit = 0
        special = 0
        special_chars = "!@#$%^&*(),.?\":{}|<>_-+=[];'`~/\\"

        if len(pwd) >= 8:
            for j in pwd:
                if j.isupper():
                    upper += 1
                elif j.islower():
                    lower += 1
                elif j.isdigit():
                    digit += 1
                elif j in special_chars:
                    special += 1

            if upper >= 1 and lower >= 1 and digit >= 1 and special >= 1:
                while True:
                    cpwd = input("Confirm password:")
                    if pwd==cpwd:
                        user[uname] = pwd
                        print("User is Registered Successfully")
                        break
                    else:
                        print("Password not matched,Retry the Confirm Password")
                break
            else:
                print("Password needs upper, lower, digit & special char. Re-enter.")
        else:
            print("Password must be at least 8 characters. Re-enter.")



print("\n_____Login_____")
att = 5
for k in range(att):
    luser = input("Enter username:")
    lpassword = input("Enter password:")
    if luser in user:
        if lpassword == user[luser]:
            print("Login Successful",luser,"Hi")
        else:
            print("Login Failed,Retry")
    else:
        print("Username invalid,Retry")

print("Access Denied! you have maximum login attempts exceeded")