def resp(usr_in):
    if usr_in == '1':
        print("BOT: Menu is : Press 1 for Books \n Press 2 for Movies \n Press 3 for Recipe \n Press 4 to Quit!")
        usr_in = input(f"{USER}: ")
        if usr_in == '1': 
            val = book()
            if val == "QUIT":
                return "QUIT"
            else:
                return val
        elif usr_in == '2':
            val = movie()
            if val == "QUIT":
                return "QUIT"
            else:
                return val
        elif usr_in == '3':
            val = recipe()
            if val == "QUIT":
                return "QUIT"
            else:
                return val
        elif usr_in == '4':
            val = 'QUIT'
            if val == "QUIT":
                return "QUIT"
            else:
                return val
        

        
books = {'THE GUIDE':"LINK" , 'MALGUDI DAYS':"LINK",'TRAIN TO PAKISTAN':"LINK",'GODAN':"LINK",'COMBAT OF SHADOWS':"LINK"}
def book():
    print("BOT: Enter 1 : To get book list name \n Enter 2 : To search book by name \n Enter 3 : To Recommend book to add \n Enter 4 : To Quit ")
    inp = input(f"{USER}:")
    global books
    if inp == '1':
            print("BOT:")
            for i in books.keys():
                print(f" {i}")
    if inp == '2':
        name = input(f"{USER}: ")
        if name in books.keys():
            print("BOT: Available!")
            print("BOT: Want to Read? press Y to Read else 4 to QUIT")
            wtr = input(f"{USER}: ")
            if wtr == "Y" or wtr == 'y':
                print("BOT: " + name + " => " + books[name])
            else:
                return "QUIT"
    if inp == '3':
            print("BOT: I Would Like to Read New Book Please Recommend me!")
            rec = input(f"{USER}: ")
            print("BOT: Please provide link to Book!")
            rec_link = input(f"{USER}: ")
            books[rec] = rec_link
            print(books)
            return "Thankyou I've Added the book!"
    if inp == '4':
            return "QUIT"
          

def movie():
    print("BOT: We'r Working on It :)zzz ")
    return
def recipe():
    print("BOT: We'r Working on It :)zzz ")
    return
            
            
            
print("BOT: Welcome User: ")
print("BOT: By What Name Shall I address You ?")
USER = input("USER: ")
print(f"Hello {USER} :) ")
usr_in = "initial"
while usr_in != "QUIT":
    
    print(f"BOT: {USER} please \n Press 1 -> Menu \n Press 2 -> How To Use \n Press 3 -> About Us \n Press 4 -> Quit")
    
    usr_in = input(f"{USER}:")
    if usr_in == '1':
        bot_resp = resp(usr_in)
        if bot_resp == "QUIT":
            print("BOT: Thanks For using services!")
            usr_in = "QUIT"
            break
        elif bot_resp == None:
            print("Please let us know! :)")
        else:
            print("BOT: " ,bot_resp)
    elif usr_in == '2':
        print("BOT: Just follow instructions: ")
    elif usr_in == '3':
        print("BOT: We are Nothing 😜")
    elif usr_in == '4':
        usr_in = "QUIT"
        if usr_in == "QUIT":
            print("BOT: Thanks For using services!")
            break
        
    
