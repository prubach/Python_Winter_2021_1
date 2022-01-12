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

    def charge(self, amount):
        #TODO

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

    def __repr__(self):
        return 'Bank[{},{}]'.format(self.customer_list, self.account_list)


b = Bank()
c = b.create_customer('Anne', 'Smith')
b.create_account(c)
c2 = b.create_customer('John', 'Brown')
b.create_account(c2, is_savings=True)

print(b)