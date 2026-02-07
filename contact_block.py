"""
Docstring for contact_block
What to build
Store name → phone number
Search contact
Update contac
Delete contact
Concepts revised
Dictionaries
Functions
String handling
"""

def c_b(contacts):
    while True:
        try:
            press = input("Enter:").lower().strip()
        except ValueError:
            print("you can only enter strings as input")
        if press == "search contact":
            user_con = input("search the contact").lower().strip()
            if user_con in contacts.keys():
                    print(f"{user_con}:{contacts[user_con]} ")
            elif user_con not in contacts.keys():
                print("This contact is new contact\n cannot find the contact")
                print("Add this contact in new contact section")
        elif press == "add contact":
            new_name = input("Enter the new contact").lower().strip()
            new_contact = int(input(f"Enter the {new_name} number:"))
            if new_name  not in  contacts.keys():
                contacts[new_name] = new_contact 
                print(f"{new_name} contact updated sucessfully")
            elif new_name in contacts.keys():
                print(f"{new_name} already exists in contacts")
            else:
                print("contact already exists")
        elif press == "update contact":
            update_con = input("Enter the contact")
            if update_con in contacts:
                contacts[update_con] = input("Edit the contact")
                print(update_con,":",contacts[update_con])  
            else:
                print("The contact You entered is new") 
        elif press == "delete contact":
            delete_con = input("enter the contact that you want to delete:")
            if delete_con in contacts.keys():
                contacts.pop(delete_con)
                print(contacts)
            else:
                print("contact is not their to delete")
        elif press == "exit":
            print("Sucessfully excited")
            break
contact_block = ({"ajay":9421870802,
            "vijay":785777709,
            "suresh":872598768,
            "ramesh":594958383,
            "ujwal":8977463453,
                    })
c_b(contact_block)

