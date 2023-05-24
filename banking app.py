#bank app
#Antonio Garza
#5/22/2022
#Bank Account Update

#Name of the customer
customer_name = str(input('Enter the customer name: '))
account_number = int(input('Enter the account number: '))
account_balance = 0
displayBalanceSvngs = 0
displayBalanceChk = 0
account_type = input('choose from the following: s-savings, c-checking and, l-loans')
#varaibles input/outputs

if account_type == 's':
    print('The user has a savings balance of: ' + 'and a checking balanace of')
    accountInfo = input("""
    Welcome to the Savings Account if you would like to update your balance ty[e '+' followed by the amount the user
    would like to enter. If you would like to withdraw select'-' followed by the amount you would like to withdraw
    to exit this menu type 'return'
    """)
    if accountInfo == '+':
        #this will add to the module then print to the console
        updateBalance = int(input('How much would you like to deposit to your checking: '))
        displayBalance = account_balance + updateBalance
        print(f'you have a balance of: $ {displayBalance}')
        account_type = input('choose from the following: s-savings, c-checking and, l-loans: ')
        balanceQuestion = str(input('Would you like a balance TYPE Y/N: '))
        if balanceQuestion == 'Y':
            print(f'checking = {displayBalanceChk:.2f} savings = {displayBalanceSvngs:.2f}')
            #make sure you decide to change the name of display balance so you have one for both checking and savings
            #both variables have been initialized 5/22/2023**
        else:
             accountInfo = input("""
    Welcome to the Savings Account if you would like to update your balance type '+' followed by the amount the user
    would like to enter. If you would like to withdraw select'-' followed by the amount you would like to withdraw
    to exit this menu type 'return'
    """)
        
    if accountInfo == '-':
        #This function will 'withdraw' or subtract from the module
        updateBalance = int(input('How much would you like to withdraw: '))
        displayBalance = accountBalance - updateBalance
        print(f'You have a balanance of: $ {displayBalance}')
        account_type = input('choose from the following: s-savings, c-checking and, l-loans: ')
        balanceQuestion = str(input('Would you like a balance TYPE Y/N: ' ))
    else:
             accountInfo = input("""
    Welcome to the Savings Account if you would like to update your balance type '+' followed by the amount the user
    would like to enter. If you would like to withdraw select'-' followed by the amount you would like to withdraw
    to exit this menu type 'return'
    """)
        
if account_type == 'c':
    print('The user has a savings balance of: ' + 'and a checking balanace of: ')
    accountInfo = input("""
    Welcome to the Checking Account if you would like to update your balance type '+' followed by the amount the user
    would like to enter. If you would like to withdraw select'-' followed by the amount you would like to withdraw
    to exit this menu type 'return'
    """)
    if accountInfo == '+':
        #this will add to the module then print to the console
        updateBalance = int(input('How much would you like to deposit to your checking: '))
        displayBalance = account_balance + updateBalance
        print(f'you have a balance of: $ {displayBalance:.2f}')
        account_type = input('choose from the following: s-savings, c-checking and, l-loans: ')
        balanceQuestion = str(input('Would you like a balance TYPE Y/N: '))
    else:
         accountInfo = input("""
    Welcome to the Savings Account if you would like to update your balance type '+' followed by the amount the user
    would like to enter. If you would like to withdraw select'-' followed by the amount you would like to withdraw
    to exit this menu type 'return'
    """)
        
    if accountInfo == '-':
        #This function will 'withdraw' or subtract from the module
        updateBalance = int(input('How much would you like to withdraw: '))
        displayBalance = accountBalance - updateBalance
        print(f'You have a balanance of: $ {displayBalance:.2f}')
        account_type = input('choose from the following: s-savings, c-checking and, l-loans: ')
        balanceQuestion = str(input('Would you like a balance TYPE Y/N: '))
    else:
         accountInfo = input("""
    Welcome to the Savings Account if you would like to update your balance type '+' followed by the amount the user
    would like to enter. If you would like to withdraw select'-' followed by the amount you would like to withdraw
    to exit this menu type 'return'
    """)
        
if accountInfo == 'return':
    customer_name = str(input('Enter the customer name: '))
    account_number = int(input('Enter the account number: '))
    account_type = input('choose from the following: s-savings, c-checking and, l-loans: ')

if account_type == 'l':
    loans = input("""
a in order to recieve a loan you must make payments within 14 days and 10 hours of income from any job the loan user has. users can only make 40% of the initial payments from the loan requests each 2 day period.
    """)
