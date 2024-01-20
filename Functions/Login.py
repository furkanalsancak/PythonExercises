
#Simple Login System, matching the credentials of the users username and password

def login():


    #for visuals
    print("----------------------")
    print("==== Login System ====")
    print("----------------------")

    #Declaring variables and storing password and username
    username = "Khan345"
    password = "k345"

    #Declaring variables and taking input from user
    input_user = input("Enter your username : ")
    input_pass = input("Enter your password : ")

    #Checking username and password
    if input_user == username and input_pass==password:
        print("Redirecting...")
    else:
        print("Invalid username or password!!!")


login()