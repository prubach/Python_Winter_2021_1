class Customer:
    last_id = 0

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        Customer.last_id += 1
        self.id = Customer.last_id

    def __repr__(self):
        return 'Customer[{},{},{}]'.format(self.id, self.firstname, self.lastname)


class Account:
    last_id = 0

    def __init__(self, customer):
        self.customer = customer
        Account.last_id += 1
        self.id = Account.last_id
        self._balance = 0

    def deposit(self, amount):
        #TODO
        self._balance = self._balance + amount

    def charge(self, amount):
        #TODO
        if amount > self._balance:
            print('Not enough money')
            raise NotEnoughMoneyError('Not enough, amount requested: {} balance: {}'.format(amount, self._balance))
        if amount < 0:
            print('negative amount')
            raise NegativeAmountError('Negative amount provided')
        self._balance = self._balance - amount

    def __repr__(self):
        return '{}[{},{},{}]'.format(self.__class__.__name__, self.id, self.customer.lastname, self._balance)


class SavingsAccount(Account):
    pass


class CheckingAccount(Account):
    pass


class Bank:
    def __init__(self):
        self.account_list = []
        self.customer_list = []

    def create_customer(self, firstname, lastname):
        c = Customer(firstname, lastname)
        self.customer_list.append(c)
        return c

    def create_account(self, customer, is_savings=False):
        a = SavingsAccount(customer) if is_savings else CheckingAccount(customer)
        self.account_list.append(a)
        return a

    def transfer(self, from_acc_id, to_acc_id, amount):
        #TODO
        from_acc = self.account_list[from_acc_id-1]
        to_acc = self.account_list[to_acc_id-1]
        #try:
        from_acc.charge(amount)
        to_acc.deposit(amount)
        #except NotEnoughMoneyError as ne:
        #    print('Charge unsucceful: ' + str(ne))

    def __repr__(self):
        return 'Bank[{},{}]'.format(self.customer_list, self.account_list)


class BankError(Exception):
    pass

class NotEnoughMoneyError(BankError):
    pass

class NegativeAmountError(BankError):
    pass


b = Bank()
c = b.create_customer('Anne', 'Smith')
a = b.create_account(c)
c2 = b.create_customer('John', 'Brown')
b.create_account(c2, is_savings=True)


try:
    a.deposit(200)
    #a.charge(300)
    print(b)
    b.transfer(1, 2, 150)
    b.trn(333)
    print(b)
# except (NotEnoughMoneyError, NegativeAmountError) as ne:
#     print('Charge unsucceful: ' + str(ne))
except BankError as ne:
    print('Charge unsucceful: ' + str(ne))
# Not good to use it
# except Exception as e:
#     print(str(e))






#b.transfer(1, 2, 100)
#print(b)