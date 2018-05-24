#!python27
import os, random, time
'''
ATM Simulator 
Author : S.Haseeb
Registered Account: 1111111111111111
Passwd: 1234
'''
class ATM:
    def __init__(self):
        self.AMOUNT = random.randint(500, 100000)
        self.USERS = {'1111111111111111':'1234'}
    def run(self):
        os.system('cls')
        while True:
            print ('        ATM V1.0')
            print ('[ Welcome to Python Bank ]\n')
            print ('    Enter your Debit Card No.')
            self.NO = raw_input('<<< ')
            os.system('cls')
            if len(self.NO) == 16:
                break
            else:
                print ('[Error]:\nATM number is 16 digits long.\n') 

        while True:
            os.system('cls')
            print ('     Enter the 4 digit PIN')
            self.PIN = raw_input('<<< ')
            if len(self.PIN) == 4:
                break
            else:
                print ('[Error]:\nPIN must be 4 digits long.\n')

        if self.NO in self.USERS:
            if self.USERS[self.NO] == self.PIN:
                self.logged()
            
    def logged(self):
        os.system('cls')
        print ('Logged in as %s' %self.NO)
        print ('Current Balance: %s $\n' %self.AMOUNT)
        print ('     1) Withdraw')
        print ('     2) Change PIN')
        print ('     3) Logout')
        selection = raw_input('<<< ')
        
        if selection == '1':
            os.system('cls')
            print ('     Amount ($) :')
            cash = raw_input('<<< ')
            if int(cash) <= self.AMOUNT:
                self.AMOUNT -= int(cash)
                print ('Withdrawl Successful')
            elif int(cash) > self.AMOUNT:
                print ('We don\'t give Loans.')

            time.sleep(2)
            os.system('cls')
            self.logged()
            
        if selection == '2':
            while True:
                print ('     Enter New PIN:')
                pin = raw_input('<<< ')
                if len(pin) == 4:
                    self.USERS[self.NO] = pin
                    print ('PIN change successful.')
                    break
                else:
                    print ('[Error]:\nPIN must be 4 digit long.\n')
                    time.sleep(2)
                time.sleep(2)
                os.system('cls')
            self.logged()
        
        if selection == '3':
            os.system('cls')
            print (' Logout Succesful ')
            time.sleep(2)
            self.run()
            
if __name__ == '__main__':
    import platform
    if platform.system().lower() == 'windows':
        ATM().run()
    else:
        print('This program can only run on windows.')
        print('To run on other OS be brave enough to change')
        print('os.system(\'cls\')')
time.sleep(4)
