from control import clear
from login import User

'''
View class
- generates different views with static methods
'''
class View:

    options = {}

    # shows the welcome view
    def welcome(self):
        clear()
        print('hello, welcome to my Login system! ')
        print('What do you want to do? ')

        print('===========================')
        # self.clearOptions()
        self.addOption(1, 'login', 'Log in')
        self.addOption(2, 'create_acount','Create acount')
        self.addOption(3, 'exit_view', 'Exit')
        print('===========================')

        self.handleInput()
    
    # confirm if want to exit
    def exit_view(self):
        clear()
        print('are you shure you want to exit?')
        print('===========================')
        self.clearOptions()
        self.addOption(1, 'close_app', 'Yes')
        self.addOption(2, 'welcome', 'No')
        print('===========================')

        self.handleInput()

    # login view
    def login(self, msg=False):
        clear()
        print('---Log in---')
        if msg is not False:
            print(f"!! {str(msg)} !!")
        uname = input('Username: ')
        pwd = input('password: ')

        user = User()
        res = user.login(uname, pwd)
        if res == False:
            self.login('Username or password incorrect')
        else:
            self.logged_in(res)

    # create account view
    def create_acount(self, msg=False):
        clear()
        print('---Create acount---')
        if msg is not False:
            print(f"!! {str(msg)} !!")
        
        uname = input('Username: ')
        pwd = input('password: ')

        user = User()
        res = user.create(uname, pwd)
        if res == 'user_exists':
            # try again
            self.create_acount('User already exists')
        else:
            self.logged_in(res)

    def logged_in(self, user):
        print(f"welcome {user['name']}")
        pass

    # adds new option to object and prints the option out
    def addOption(self, key, action, msg):
        key = str(key)
        msg = str(msg)
        print(f'{key}: {msg}')
        self.options[key] = action

    # empties all the options saved in object
    def clearOptions(self):
        self.options = {}

    # calls function based on input
    def handleInput(self):
        inp = input('')

        if inp in self.options:
            getattr(self, self.options[inp])()

        else:
            print('Incorrect input')
            self.handleInput()
    
    def close_app(self):
        print('Goodbye')


