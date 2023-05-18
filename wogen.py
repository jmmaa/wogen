# A WORDLIST GENERATOR TOOL DEDICATED FOR A SINGLE TARGET
# GATHER AVAILABLE DATA FROM THE TARGET
# THEN COMBINE ALL COLLECTED DATA
#
# EG.
#       DATA:
#           name, middlename, lastname,  age
#
# THEN COMBINE:
#       namemiddlename
#       namelastname
#       nameage
#       middlenamename
#       middlenamelastname
#       middlenameage
#       lastnamename
#       lastnamemiddlename
#       lastnameage
#       agename
#       agemiddlename
#       agelastname
#
# PUT ALL THE COMBINED DATA INTO A WORDLIST.TXT FILE
# GENERATING A WORDLIST MAY TAKE TIME 
# DEPENDING ON THE DATA COLLECTED
# THE MORE DATA THE LONGER IT TAKES
# 
#
#
#
#
# - GODFR3YP4DU4

import itertools
import threading
import datetime
import shutil
import time
import sys
import re
import os


# third party
import phonenumbers



class Color:
    # Class for coloring the font with the highlighted text format

    green = '\033[1;32;40m'
    red = '\033[1;31;40m'
    reset = '\033[0;37;40m'




# Make sure that the required module are in the system
# before running the whole program
# try importing the module if not found, install it





# REQUIRED MODULES
# modules = [
#             'phonenumbers',
#             're',
#             'random',
#             'datetime',
#             'itertools',
#             'shutil',
#             'threading',
#             'sys'
#             ]

# for module in modules:
#     try:
#         globals()[module] = importlib.import_module(module)
#     except:
#         print(f'{Color.red}\nModule not found!{Color.reset}')
#         print('\nInstalling required module')
#         time.sleep(3)
#         os.system(f'python3 -m pip install {module}')






# get width and height of terminal for future references
width, height = shutil.get_terminal_size()





class Validator:
    # Class of function to validate user input
    # in order to avoid any error while running the program
    # and enhance the result of this tool

    def invalid(self):
        # Print Invalid Message
        print(Color.red + 'Invalid input. Please try again.' + Color.reset)



    def name(self, data):
        # Get user input and
        # Filter it for a better result
        # Check name if two words and validate it
        # Check name if in alphabet
        # If not, repeat the question

        if 'username' in data:
            name = input(f'\n-》{data.capitalize()}: ')
        else:
            while True:
                name = input(f'\n-》{data.capitalize()}: ')
                if name:
                    name = name.replace(' ', '')
                    if name.isalpha():
                        break
                    else:
                        self.invalid()
                        continue
                else:
                    break
        return name



    def age(self, data):
        # Get user input and
        # Filter it for a better result
        # Check if age is valid
        # If not, repeat the question

        while True:
            age = input(f'\n-》{data.capitalize()}: ')
            if age:
                try:
                    age = int(age)
                    if age < 0 or len(str(age)) > 2:
                        self.invalid()
                        continue
                    else:
                        break
                except:
                    self.invalid()
                    continue
            else:
                break
        return age



    def dob(self, data):
        # Get the user input and
        # Filter it for a better result
        # Check if DOB is valid
        # If not, repeat the question

        while True:
            dob = input(f'\n-》{data.capitalize()} (MM/DD/YYYY): ')
            pattern = '(0[1-9]|1[012])/(0[1-9]|[12]\d|3[01])/(19|20)\d\d'
            if dob:
                if re.fullmatch(pattern, dob):
                    break
                else:
                    self.invalid()
                    continue
            else:
                break
        return dob



    def email(self, data):
        # Get the user input and
        # Filter it for a better result
        # Check if email is valid
        # If not, repeat the question

        while True:
            email = input(f'\n-》{data.capitalize()}: ')
            pattern = re.compile(r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])")
            if email:
                if re.fullmatch(pattern, email):
                    break
                else:
                    self.invalid()
                    continue
            else:
                break
        return email
    


    def phone(self, data):
        # Get the user input and
        # Filter it for a better result
        # Check if DOB is valid
        # If not, repeat the question

        while True:
            phone = input(f'\n-》{data.capitalize()} (+639123456789): ')
            if phone:
                try:
                    phone = phonenumbers.parse(f'{phone}')
                    if phonenumbers.is_valid_number(phone):
                        phone = phonenumbers.format_number(phone, phonenumbers.PhoneNumberFormat.NATIONAL).replace(' ', '')
                        break
                    else:
                        print(Color.red + 'Invalid number. Please try again.' + Color.reset)
                        continue
                except Exception as e:
                    print(e)

                    print(Color.red + 'Invalid number. Please try again.' + Color.reset)
                    continue
            else:
                break
        return phone



    def symbols(self, data):
        # Get the user input and
        # Filter it for a better result
        # Check if symbol is valid
        # If not, repeat the question
        
        print('\n')
        msg = 'Put some symbols to strengthen your wordlist'
        syms = '@#$_&-+()/'
        print(msg.center(width))
        print(syms.center(width))

        while True:
            symbols = input(f'\n-》{data.capitalize()}: ')
            if symbols:
                if re.match('\W', symbols):
                    break
                else:
                    self.invalid()
                    continue
            else:
                break
        
        symbol_list = []

        for symbol in iter(symbols):
            symbol_list.append(symbol)

        return symbol_list



    def additional_words(self, data):
        # Get the user input and
        # Filter it for a better result

        print('\n')
        msgs = ['Add some words that can be a possible password',
                'Like favorite food, place, pet name, etc',
                'Press enter to skip']
        
        for msg in msgs:
            print(msg.center(width))

        print('\n')

        words = []

        while True:
            word = input(f'\n-》{data.capitalize()}: ')
            if word:
                word = word.replace(' ', '')
                words.append(word)
            else:
                break

        return words





class WoGen(Validator):
    # The main group of function to generate a wordlist

    def __init__(self):
        self.run_loading = None



    def banner(self):
        # Show the banner
        # clear the terminal before showing the WOGEN banner

        os.system('printf "\033c" ')
        print('\n' * 4)
        b = [
                f"......................................................",
                f"'##:::::'##::'#######:::'######:::'########:'##::: ##:",
                f" ##:'##: ##:'##.... ##:'##... ##:: ##.....:: ###:: ##:",
                f" ##: ##: ##: ##:::: ##: ##:::..::: ##::::::: ####: ##:",
                f" ##: ##: ##: ##:::: ##: ##::'####: ######::: ## ## ##:",
                f" ##: ##: ##: ##:::: ##: ##::: ##:: ##...:::: ##. ####:",
                f" ##: ##: ##: ##:::: ##: ##::: ##:: ##::::::: ##:. ###:",
                f". ###. ###::. #######::. ######::: ########: ##::. ##:",
                f":...::...::::.......::::......::::........::..::::..::",
                f"'''''''''''''’''''''''''''''''''''''''''''''''''''''''",
            ]

        for i in b:
            print(Color.green + i.center(width) + Color.reset)

        print(Color.red + '- GODFR3Y'.center(width+30) + Color.reset )



    def data(self):
        # Collect data from user and
        # Validate it using Validator module
        
        info = []
    
        print('\n\n\n\nPut everything you know then press enter')
        print("Press enter to skip\n")
    
        # get the target personal info
        firstname = self.name('firstname')
        middlename = self.name('middlename')
        lastname = self.name('lastname')
        nickname = self.name('nickname')
        age = self.age('age')
        dob = self.dob('dob').replace('/', '')
        dob_mm = dob[:2]
        dob_dd = dob[2:4]
        dob_yyyy = dob[4:]
        phone = self.phone('phonenumber')
        email = self.email('email')
        username = self.name('username')

    
        # get the target life partner info
        print('\n')
        msgs = ['Some additional information base on the',
                'target life partner can be useful',
                'to enhance your wordlist']
        for msg in msgs:
            print(msg.center(width))
    
        partner_firstname = self.name('partner\'s firstname')
        partner_middlename = self.name('partner\'s middlename')
        partner_lastname = self.name('partner\'s lastname')
        partner_nickname = self.name('partner\'s nickname')
        partner_age = self.age('partner\'s age')
        partner_dob = self.dob('dob').replace('/', '')
        partner_dob_mm = partner_dob[:2]
        partner_dob_dd = partner_dob[2:4]
        partner_dob_yyyy = partner_dob[4:]
        partner_phone = self.phone('partner\'s phonenumber')
        partner_email = self.email('partner\'s email')
        partner_username = self.name('partner\'s username') 
        date_engaged = self.dob('date engaged')
        date_engaged_mm = date_engaged[:2]
        date_engaged_dd = date_engaged[3:5]
        date_engaged_yyyy = date_engaged[6:]

        # additional words can also be useful
        words = self.additional_words('words')
        
        # additional symbols can also be useful
        symbols = self.symbols('symbols')
     
        # put all collected data into a list
        info.extend([
            firstname, 
            middlename,
            lastname,
            nickname,
            age,
            dob,
            dob_mm,
            dob_dd,
            dob_yyyy,
            phone,
            email,
            username,
            partner_firstname,
            partner_middlename,
            partner_lastname,
            partner_nickname,
            partner_age,
            partner_dob,
            partner_dob_mm,
            partner_dob_dd,
            partner_dob_yyyy,
            partner_phone,
            partner_email,
            partner_username,
            date_engaged,
            date_engaged_mm,
            date_engaged_dd,
            date_engaged_yyyy
            ])
        info.extend(symbols)
        info.extend(words)
        
    
        data = set()

        # filter info list to remove None value item
        # and store it to a new list then return
        for value in info:
            if value:
                data.add(str(value))



        return data

    

    def min_pass_len(self):
        # Get a minimum password length
        # Validate the user input to avoid any error

        while True:
            try:
                min_char= int(input('\nMinimum password length: '))
                if min_char <= 0:
                    self.invalid()
                    continue
                else:
                    break
            except:
                self.invalid()

        return min_char



    def max_pass_len(self, min_char):
        # Get a maximum password length
        # Validate the user input and check if not less from
        # minimum password length to avoid any error

        while True:
            try:
                max_char = int(input('\nMaximum password length: '))
                if max_char <= 0 or max_char <= min_char:
                    self.invalid()
                    continue
                else:
                    break
            except:
                self.invalid()
        
        return max_char



    def word_to_combine(self):
        # get the maximum number of data to combined
        # validate it for a better result

        msgs = [
                '\n',
                '\b',
                'Data:  a b c d',
                '\n',
                '2       3       4',
                'ab      abc     abcd',
                'ac      abd     abdc',
                'ad      acb     acbd',
                'ba      acd     acdb',
            ]
        
        for msg in msgs:
            print(msg.center(width))
        print('\n\n' + 'WARNING! The higher the number, the longer it takes to create and the more storage it gets.'.center(width))
        
        while True:
            try:
                num = int(input('\nUp to how many data to combine: '))
            except:
                self.invalid()
                continue
            break
        return num



    def create(self, min_char, max_char, data, word_to_combine):
        # Open a new Wordlist.txt file
        # Then put all created possible password
        # Using permutation from the data gathered

        data = sorted(data, key=len)
        
        with open('Wordlist.txt', 'w+') as wordlist:
            for num in range(1, word_to_combine + 1):
                for datas in itertools.permutations(data, num+1):
                    # join data in lowercase
                    passw = ''.join(datas)
                    
                    if len(passw) <= max_char and len(passw) >= min_char:
                        # join data in capitalize
                        cap_passw = ''.join(datas).capitalize()

                        # join data in title
                        title_passw = ''.join(dat.title() for dat in datas)

                        if passw != cap_passw and passw != title_passw and cap_passw != title_passw:
                            wordlist.write(passw + '\n')
                            wordlist.write(cap_passw + '\n')
                            wordlist.write(title_passw + '\n')
                        




    def finish(self, timer):
        # Open the Wordlist.txt and read
        # to determined how many passwords are created

        timer = datetime.timedelta(seconds=timer)

        with open('Wordlist.txt') as wordlist:
            count = sum(1 for line in wordlist)
            print(f'\n\n{Color.green}{count:,} password has been successfuly created and saved to {Color.reset}\'Wordlist.txt\'{Color.green} in the same directory{Color.reset}\n\n')

            print(f"{Color.red}The developer of this code is not liable for any misuse of this tools. You have been warn! {Color.reset}")


            print(f'\nFinish in {timer} seconds')



    def loading(self):
        # Display loading icon while generating

        for icon in itertools.cycle(['|', '/', '-', '\\', '-']):
            if not self.run_loading:
                break
            sys.stdout.write('\rGenerating ... ' + icon)
            sys.stdout.flush()
            time.sleep(0.1)



    def main(self):
        # Get the target info from the user by calling data() func
        # Ask the user for minimum and maximum password length
        # While creating show some motivational message
        # If done, show how many password has been create
        
        # start timer
        timer_start = time.time()

        # get data from user
        data = self.data()

        # get the minimum password length of chatacter
        min_char = self.min_pass_len()

        # get the maximum password length of character
        max_char = self.max_pass_len(min_char)

        # get the max number of data to combine
        word_to_combine = self.word_to_combine()

        # ask the user to generate or not
        # if y generate elif n quit else ask again
        while True:
            generate = input('\n\nGenerate a wordlist? [Y|N]: ').upper()
            print('\n')
            if generate == 'Y': 
                self.run_loading = True
                loading = threading.Thread(target=self.loading)
                loading.start()
                
                self.create(min_char, max_char, data, word_to_combine)

                self.run_loading = False
     
                break

            elif generate == 'N':
                exit()
            else:
                self.invalid()
        
        # timer end
        timer_end = time.time()

        timer = round(timer_end - timer_start)
        self.finish(timer)





if '__main__' == __name__:
    wogen = WoGen()
    wogen.banner()
    wogen.main()












