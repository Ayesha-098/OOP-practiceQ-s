# Understanding Attributes & Visibility (Public, Private, Protected)
# Problem: Secure File Manager
# Create a SecureFile class with:
# A public filename attribute.
# A protected _size attribute (stores file size in KB).
# A private __password attribute (used for securing file access).
# A method get_file_info() that returns the filename and size.
# A method set_password(password) that updates the private password.
# A method authenticate(password) that checks if the password matches.

class SecureFile:
    def __init__(self, filename, size, password):
        self.filename = filename
        self._size = size 
        self.__password = password

    def get_file_info(self):
        return f"Filename: {self.filename}, Size: {self._size}KB"

    def set_password(self, new_password):
        self.__password = new_password

    def authenticate(self, password):
        if password == self.__password:
            print("Access granted.")
            return True
        else:
            print("Access denied.")
            return False

file = SecureFile("project.docx", "120", "secret123")
print(file.get_file_info())  
file.set_password("newSecret123")
if file.authenticate("newSecret123"):
    print("You can open the file!")
else:
    print("Incorrect password. Try again.")
