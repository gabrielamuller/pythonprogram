def show_menu():
    print("1. Add a person")
    print("2. View people")
    print("3. Stats")
    print("4. Exit")
    
    option = input("Enter option: ")
    return option
    
def data_loop():
    while True:
        option = show_menu()
        if option == "1":
            add_people()
        elif option == "2":
            view_people()
        elif option == "3":
            view_stats()
        elif option == "4":
            break
        else:
            print("Invalid Option")
        print(" ")
            
def add_people():
    print("")
    first_name = input("Enter your first name:\n ")
   
    print("")
    last_name = input("Enter your last name:\n ")
  
    print("")
    team = input("Enter your team:\n ")

    print("")
    age = int(input("Enter your age:\n "))

    line = first_name + " " + last_name + " " + team + " " + age + " "
    file = open("data.txt", "a")
    file.write(line + "\n")
    file.close()
    
def view_people():
    file = open("data.txt", "r")
    lines = file.read().splitlines()
    print(lines)
    file.close()
    
    
def view_stats():
    file = open("data.txt", "r")
    lines = file.read().splitlines()
    num_lines = sum(1 for line in open('data.txt'))
    print("Number of people: ", num_lines)
    file.close()
    
    file = open("data.txt", 'r')
    content = file.read()       
    file.close()

    lines = content.split() 
    total = 0
    for item in lines:
        if item.isnumeric():
            total += int(item)
    print("The average age is: ", (total)/(num_lines))
  
   

    
data_loop()