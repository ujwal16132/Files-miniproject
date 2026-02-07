#📘 Student Record Manager (File-Based)
#Features:
#Add student
#View all students
#Search student
#No data loss
#Uses only .txt file
#Uses:
#r / a / r+
#read(), write()
#seek(), tell()
#string operations
#👉 This will make file handling automatic for you.
"""while True:
    choice = print(
            "1.add student\n"
            "2.view all students\n"
            "3.serach student\n"
            "4.delete name"
            ""
        )
    click = input("Enter the choice: ").lower().strip()
    with open("data.txt","r") as file:
        content = file.read()
    #Add student
    if click == "add":
        name = input("Enter the name:").lower().strip()
        if name in content:
             print(f"name is already exists")
        else:
            with open("data.txt","a") as add_student:
                add_student.write(name+"\n")
                print("Name added successfully")
    #View all students
    if click =="view".lower().strip():
        with open("data.txt","r") as file:
            for line in file:
                print(line.strip())        
    if click == "Search".lower().strip():
        name = input("Enter the name:").lower().strip()
        with open("data.txt","r+") as search:
            for line in search:
                if line.strip() == name:
                    print(name)
                    break
            else:
                print("Name does not exist")
    if click == "delete".lower().strip():
        name_delete = input("Enter the name to delete").lower().strip()
        remain = []
        found = False
        with open("data.txt","r+") as file:
            for line in file:
                if line.strip() == name_delete:
                    found = True
                    continue
                remain.append(line)
        if found :
            with open("data.txt","w") as file:
                file.writelines(remain)
            print(f"{name_delete} deleted successfully")
        else:
            print(f"{name_delete} not found")
    if click == "exit".lower().strip():
        print("Exited successfully")
        break"""

#Refactor into functions (clean structure)

def add(name,dep,sec):
    with open("data.txt","a") as file:
        data = f"{name},{dep},{sec}\n"
        file.write(data)
        print(f"{name} {dep} {sec} added successfully")

def update(name):
    with open("data.txt","r+") as file:
        lines = file.readlines()
        remain = []
        found = False
        changes = input("Enter the changes you need:")
        if changes == "dep".lower().strip():
            dep = input("Enter the new dep:")
        elif changes == "sec":
            sec = input("Enter the  new sec:")
        elif changes == "both".lower().strip():
            dep = input("Enter the new dep:")
            sec = input("Enter the  new sec:")
        else:
            print("Invalid choice")
            return
        for line in lines:
            blocks = line.strip().split(",")
            if name == blocks[0]:
                found = True
                if changes == "dep".lower().strip():
                    blocks[1] = dep
                elif changes == "sec".lower().strip():
                     blocks[2] = sec 
                elif changes == "both".lower().strip():
                    blocks[1],blocks[2]= dep,sec
                  #blocks[2] = sec
                final_line = ",".join(blocks)+"\n"
                remain.append(final_line)
            else:
                remain.append(line)
        if found:
            with open("data.txt","w") as file:
                file.writelines(remain)
            print("updated successfully")
        else:
            print("the name you entered is new, cannot update it")

def view():
        with open("data.txt","r") as file:
            content = file.readlines()
        return content

def search(name):
        with open("data.txt","r") as file:
            for line in file:
                if name.strip() == line.strip().split(",")[0]:
                    return True
            else:
                 return False
            
def delete(del_name):
        with open("data.txt","r") as file:
            lines =file.readlines()
        remain = []
        found = False
        for line in lines:
            name = line.strip().split(",")[0]
            if name == del_name:
                found = True
                continue
            remain.append(line)
        if found:
            with open("data.txt","w") as file:
                file.writelines(remain)
            print(f" {del_name} deleted successfully")
        else:
            print(f"{del_name} not found")
while True:
    choice = print(
                "1.add\n"
                "2.update\n"
                "3.view\n"
                "4.search\n"
                "5.delete\n"
                "6.exit"
                ""
            )
    click = input("Enter the choice: ").lower().strip()      
    if click == "add".lower().strip():
        name = input("Enter the name:")
        dep = input("Enter the department:")
        sec = input("Enter the section:")
        if  not search(name):
             add(name,dep,sec)   
        else:
            print(f"{name} {dep} {sec} already exists")

    if click == "update".lower().strip():
        name = input("Enter the name that you want to edit:")
        update(name)
  
    if click == "view".lower().strip():
        if view():
            all_visit = view()
            for line in all_visit:
                print(line.strip())
        else:
            print(f"{line} name not found")

    if click == "search".lower().strip():
        name = input("Enter the name:")
        if search(name):
            print(f"{name} details found")
        else:
            print(f"{name} details not found")

    if click == "delete".lower().strip():
        delete_name = input("Enter the name:")
        delete(delete_name)

    if click == "exit".strip().lower():
        print("exited successfully")
        break
         

         



        


    
        
             
              


                          

            

        
