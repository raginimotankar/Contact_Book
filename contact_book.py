from contact import Contact
class ContactBook:
    def __init__(self):
        self.contact=[]
    def add_contact(self,contact):
        self.contact.append(contact) 
    def display_all_contacts(self):
        for contact in self.contact:
         print("............")
    def search_contact(self,name):
        for contact in self.contacts:
            if contact.name.lower()==name.lower():  
               return contact
            return None 
          