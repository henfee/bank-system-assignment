#Program starts here
class Bank(object):
    def __init__(self,BankId,name,location):
        self.BankId = BankId
        self.name = name
        self.location = location

    def detail(self):
        print("\n+++++ Name:",self.name,"\n+++++ Location:",self.location,"\n+++++ BANK#:",self.BankId,"\n",'*'*50,"\n\n")

 #Teller class inherits from the bank class   
class Teller(Bank):
    
    def __init__(self,Bank,Id,Name):
        self.Bank = Bank
        self.Id = Id
        self.Name = Name
        
    def detail(self):
        print("\n++++++++BANK: ",self.Bank.name,
              "\n++++++++TELLER ID: ",self.Id,
              "\n++++++++TELLER NAME:",self.Name)
        
    def CollectMoney(Customer,amt):
        if(Customer.Bank.bankId == self.Bank.bankId):
            Customer.AccountBal+=amt
            print("Collecting Money")
        else:
            print("Look For Your BANK")

    def OpenAccount():
        print("Account is Opening")

    def CloseAcount():
        print("Account is closing")

    def loanRequest():
        print("Loan request is loading")

    def ProvideInfo():
        print("Provide Info")

    def IssueCard():
        print("Issue Card")


#Customer class inherits from the bank class        
class Customer(Bank):
    AccountBal = 0
    LoanAmt = 0
    def __init__(self,Bank,Id,Name,Address,PhoneNo,AcctNo):
        self.Bank = Bank
        self.Name = Name
        self.Id = Id
        self.Address = Address
        self.PhoneNo = PhoneNo
        self.AcctNo = AcctNo

    def detail(self):
        print("*"*60,
              "\n******** Customer ID:",self.Id,
              "\n******** BANK:",self.Bank.name,
              "\n******** NAME:",self.Name,
              "\n******** ADDRESS:",self.Address,
              "\n******** PHONE NO:",self.PhoneNo,
              "\n******** AC\\NO:",self.AcctNo+"\n"+"*"*60
              )

    def GeneralInquiry(self):
        print("General Inquiry")

    def DepositMoney(self, amt):
        self.AccountBal += amt
        print("deposit of ",amt," UGX\n")
    
    def WithdrawMoney(self, amt):
        if(amt < self.AccountBal):
            self.AccountBal -= amt
            print("withdraw of ",amt," UGX\n")
        else:
            print("** OOPS YOU HAVE INSUFFICIENT BALANCE **")

    def OpenAccount(self):
        print("open account")

    def CloseAcount(self):
        print("Close account")

    def ApplyForLoan(self, amt):
        print("apply for loan")

    def RequestCard(self):
        print("request card")
        
#ACCOUNT AND LOAN INHERIT FROM CUSTOMER CLASS
class Account(Customer):
    def __init__(self, Customer,Id,CustomerId):
        self.Customer = Customer
        self.Id = Id
        self.CustomerId = CustomerId

class Loan(Customer):
    def __init__(self, Customer,Id,CustomerId):
        self.Customer = Customer
        self.Id = Id
        self.CustomerId = CustomerId
        
#SAVINGS AND CHECKING INHERIT FROM ACCOUNT CLASS
class Savings(Account):
    def __init__(self,Account,Id,CustomerId):
        self.Account = Account
        self.Id = Id
        self.CustomerId = CustomerId
        print("SAVINGS: ",self.Account.AccountBal)
              
class Checking(Account):
    def __init__(self,Account,Id,CustomerId):
        self.Account = Account
        self.Id = Id
        self.CustomerId = CustomerId
        print("checking... \n BALANCE: ",self.Account.AccountBal)
#banks 1 and 2    
B1 = Bank(1001234,"bank 001","Mbarara")
B2 = Bank(1006225,"bank 002","Masaka") 

#details of bank 1 and 2
B1.detail() 
B2.detail() 

# BANK 1 TELLERS
B1_T1 = Teller(B1,1123456,"Kirabo Sophie")
B1_T2 = Teller(B1,1305342,"Nagaba Catherine")
B1_T3 = Teller(B1,102023,"Kansiime Racheal")

B1_T1.detail()
B1_T2.detail()
B1_T3.detail()

# BANK 2 TELLERS
B2_T1 = Teller(B2,202245,"Nyangoma Immaculate")
B2_T2 = Teller(B2,233424,"Namaganda Christine")
B2_T3 = Teller(B2,213023,"Amanya Juliet")

B2_T1.detail()
B2_T2.detail()
B2_T3.detail()



### CUSTOMERS BANK 1
print("CUSTOMERS of ",B1.name,"\n","_"*40)
CS_B1 = [
    Customer(B1,100001,"NATWIJUKA EVALYNE","KABIRA MITOOMA","0754294567","0211547877"),
    Customer(B1,100002,"MUSINGUZI EVALISTO","ISHAKA PLOT 123 MBARARA_ KASESE ROAD ","0786578743","0415432166"),
    Customer(B1,100003,"MUHUMUZA VICENT","BUSHENYI","0750978213","0411234590"),
    Customer(B1,100004,"MUHWEZI GILBERT","RUBANGA KABIRA","078340696","0311545467"),
    Customer(B1,100005,"ABAHO FELIX","BUNYONYI ","0758737542","0470545434"),
    Customer(B1,100006,"AHEREZA COLLINS","MBARARA NYAMITANGA","0775025334","0411845498"),
    Customer(B1,100007,"AKAMWESIGA EVANS","MWIZI ISINGIRO","0756525780","0711546465"),
    Customer(B1,100008,"ATUKWASE COMFORT","IBANDA","0772345453","0611545423"),
    Customer(B1,100009,"AINOMUGISHA JULIAN","BUNYARUGURU","0789035766","0413547870"),
    Customer(B1,100010,"TUHAISE PATITENCE","BUSHENYI","0702338888","021548804547")
    ]

for sc in CS_B1:    
    print(sc.detail())

#CUSTOMERS OF BANK 2
print("CUSTOMERS of ",B2.name,"\n","_"*40)
CS_B2 = [
    Customer(B2,200001,"KEMBABAZI ANGELLA","KINONI MBARARA","0754225335","7771540854576"),
    Customer(B2,200002,"KYARISIIMA CHARITY","ISINGIRO ","0788268767","45654381567888"),
    Customer(B2,200003,"MPAMIRE MODERN","RUKUNGIRI","0740678177","0777239567767"),
    Customer(B2,200004,"MUGUME ALLAN","RUBANGA KABIRA","0788507999","7777547452889"),
    Customer(B2,200005,"MUGUME ISAAC ","NTUNGAMO RWASHAMIIRE","0775507778","6780566454221"),
    Customer(B2,200006,"BYARUHANGA CHRIS","KABIRA MITOOMA","0709530356","9081847494332"),
    Customer(B2,200007,"ASHABA ANNITA","RUBARE NTUNGAMO","07453911678","5564546457876"),
    Customer(B2,200008,"KATUSHABE VIOLA","ISHAKA","07023458567","452565474342"),
    Customer(B2,200009,"MUGUMYA JOSHUA","RUBANGA KABIRA","07560817332","24444505857OOO0"),
    Customer(B2,200010,"KEMIGISHA DOREEN","NYAMITANGA MBARARA","0788607865","86524880384564")
    ]

for sc in CS_B2:    
    print(sc.detail())

#### withdraw and deposit
# ACCOUNT
CB1 = Customer(B1,55848,"KATUSHABE EUNICE","MBARARA","0757831138","889282663340892")
CB1_A = Account(CB1,25004,1)



