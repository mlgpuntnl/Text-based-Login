import json
from os import read

'''
User class that handles the login functionalities
'''

class User():

    db = 'db.json'

    # create a new user
    def create(self, uname, pwd):
        userdata = {
            'name': uname,
            'pwd': pwd,
            'is_admin': False
        }
        user_exists = self.getUser(uname)
        if user_exists == False:
            self.addUser(uname, userdata)
            return userdata
        else:
            return 'user_exists'


    # gets user and compares passwords
    def login(self, uname, pwd):
        user = self.getUser(uname)

        if user == False:
            return False
        elif user['pwd'] == pwd:
            return user
        else:
            return False


    # check if user exists
    # if so: return userdata
    # else: return False
    def getUser(self, uname):
        data = ''
        # get full json object from db file
        with open(self.db, 'r') as reader:
            data = reader.read()
        
        data = json.loads(data)
        if uname in data:
            return data[uname]
        else:
            return False
  
    
    # adds a new user to the db
    def addUser(self, uname, userdata):
        data = ''
        # open db and get data
        with open(self.db, 'r') as reader:
            data = reader.read()

        # add userdata to dataset
        data = json.loads(data)
        data[uname] = userdata
        data = json.dumps(data)

        # write to db
        with open(self.db, 'w') as writer:
            writer.write(data)

