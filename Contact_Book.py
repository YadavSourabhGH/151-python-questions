# 2. Contact Book - Stores and manages contact information
class ContactBook:
    def __init__(self):
        self.contacts = {}  # Store contacts in dictionary
        
    def add_contact(self, name, phone, email):
        # Save contact details
        self.contacts[name] = {
            "phone": phone,
            "email": email
        }
        
    def find_contact(self, name):
        # Return contact if found, else return None
        return self.contacts.get(name)
