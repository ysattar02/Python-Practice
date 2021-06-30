



class Person:
  # Constructor - Dunder method
  def __init__(self, first_name, last_name, number, email):
    self.first_name = first_name
    self.last_name = last_name
    self.number = number
    self.email = email
    
  
  def __str__(self):
    return f"Name: {self.first_name} {self.last_name} \nPhone Number: {self.number} \nEmail: {self.email}"

  # Create method that returns just the full name. 
  def only_name(self):
    return f"Name: {self.first_name} {self.last_name}"
  # Method that takes a new email as a parameter and changes the current email
  def new_email(self, new_email):
    self.email = new_email
    return f"The email has been updated to: {new_email}"
  
  def new_number(self, new_number):
    self.number = new_number
    return f"The number has been updated to: {new_number}"

  def new_name(self):
    first = input("Enter first name: ")
    last = input("Enter last name: ")
    self.first_name = first
    self.last_name = last
    print(f"The name has been updated to {first} {last}")
    
contacts = []

prevContacts = open('myContacts.txt', 'r')

for line in prevContacts:
  split_line = line.split(",")
  # Using data in split_line, assign values to proper variables
  first_name = split_line[0].strip()
  last_name = split_line[1].strip()
  phone = split_line[2].strip()
  email = split_line[3].strip() 
  # Using the variables create a Person class object.
  contact = Person(first_name, last_name, phone, email)
  # Add contact to contacts 
  contacts.append(contact)

prevContacts.close()

def display():
  print('''
  Options:
  1) Enter new contact
  2) Display all contacts 
  3) Search by name 
  4) Update contact
  5) Quit program
  ''') 

running = True

while running:
  display()
  user_action = input("What do you want to do? (Enter Number 1-5): ") 

  if user_action == '1':
    first_name_input = input("First name: ")
    last_name_input = input("Last name: ")
    number_input = input("Phone Number: ")
    email_input = input("Email Address: ")
  
    # Create a new Person class object
    my_contact = Person(first_name_input, last_name_input, number_input, email_input)

    # Sace contact to text file:
    new_contact = f"{first_name_input}, {last_name_input}, {number_input}, {email_input}\n"
    prevContacts = open("myContacts.txt", "a")
    prevContacts.write(new_contact)
    # close() file to free up memory that it is UserWarning
    prevContacts.close()

    # Save contact to contacts list
    contacts.append(my_contact)

    print("Your contacts have been updated")

  if user_action == '2':
    print("CONTACTS:\n")
    print("-----------------------")
    print("\n")
    for i in contacts:
      print(i)
      print("\n")

    print("-----------------------")

  if user_action == '3':
    search = input("Enter the first name of a person: ").lower()
    for contact in contacts:
      if search == contact.first_name.lower(): 
        print("-----------------------")
        print(contact)
        print("-----------------------")
      else:
        print("That contact is not in the list! ")

  if user_action == '4':
    first = input("Enter the first name of a person: ").lower().strip()
    last = input("Enter the last name of a person: ").lower().strip()
  
    for contact in contacts:
      if first == contact.first_name.lower() and last == contact.last_name.lower():
        contact.new_name()
      else:
        print("That contact is not in the list! ")
        
      

  if user_action == '5':
    running = False
    print("Thanks for using my program! ")
  
    



    

  





