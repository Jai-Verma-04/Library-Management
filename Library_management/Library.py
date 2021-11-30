import lib_main

'''Creation of the registration and login interface'''

registered_users = {}       #* Dictionary os user and password

def register():         #* Function for registering a librarian

    print()
    
    user_name = input("Choose a nusername: ")       #* Entering the username for the librarian
    password = input("Choose a password: ")     #* Choosing a password for thr librarian
    
    print(f"{user_name} registered successfully..")     #* Confirms the registration
    
    registered_users[user_name]=password        #* Adds username as key and password as value in the dict



def login():        #* Function for logging in
    print()
    
    user = input("Enter your username: ")       #* Input the username   
    passwd = input("Enter the password: ")      #* Input the password
    
    if user in registered_users.keys():             #* If username is registered
        
        if registered_users.get(user) == passwd:    #* If password is also correct  
            print("Logged in successfully")
            lib_main.main()
        
        else:                                       #* If username is correct but password incorrect
            print("Wrong Passsword!!")
            main()
    
    else:                               #* Username not found the dictionary
        print("User not found!!")
        main()


def display_librarians():              #* Show the librarians who can access the library
    
    for user in registered_users.keys():    #* Fetch username from the dict
        print(user)


if __name__=='__main__':        
    
    def main():         #* Interface for the library
    
        while True:

            print()
            print("Welcome to the Library...")
            print("1. Register librarian")
            print("2. Login to library")
            print("3. Show librarians")
            
            choose = int(input("Enter a choice: "))    

            if choose==1:
                register()      #* Calling the register function
            
            elif choose==2:
                login()         #* calling the login function
            
            elif choose==3:
                display_librarians()    #* Calling the display librarian function
            
            else:
                print("wrong choice")
                main()
    main()