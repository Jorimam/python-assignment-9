import random

class Bank_account:

	promo_prize = 2000
	def __init__(self, name, balance, hasPromo = False, isAdmin = False,isFreeze = False, text = False, email = False):
		self.account_name = name
		self.account_balance = balance
		if hasPromo:
			self.account_balance += self.promo_prize
			self.number =random.randint(100,90000000)
			self.isAdmin = isAdmin
			self.isFreeze = isFreeze
			self.text = text
			self.email = email

	def detail(self):
		return f"name: {self.account_name}, balance: {self.account_balance}, number: {self.number}, admin: {self.isAdmin}, freezed {self.isFreeze}"

	def deposit(self,amount):
		if self.isFreeze:
			return "Frozen account"
		if amount > 0:
			self.account_balance += amount
			msg1 = f"CREDIT,\nAmount: #{amount}.\nAvailable balance: {self.account_balance}"
			msg2 = f"Dear {self.account_name},\nDeposit of #{amount} successful. Available balance: #{self.account_balance}"
		if self.text == True:
			self.send_text(msg1)
			print( f"SMS: {msg1}")
		if self.email == True:
			self.send_email(msg2)
			return f"EMAIL: {msg2}"
		else:
			return "invalid amount"

	def withdraw(self,amount):
		if self.isFreeze:
			return "Frozen account"
		if self.account_balance >= amount:
			self.account_balance -= amount
			msg1 = f"DEBIT,\nAmount: #{amount}.\nAvailable balance: {self.account_balance}"
			msg2 = f"Dear {self.account_name},\nWithdrawal of #{amount} successful. Available balance: #{self.account_balance}"
		if self.text == True:
			self.send_text(msg1)
			print(f"SMS: {msg1}")
			
		if self.email == True:
			self.send_email(msg2)
			return f"EMAIL: {msg2}"
		else:
			return "insufficient"

			    
	def transfer(self,recipient,amount_to_send):
		if self.isFreeze:
			return "Account frozen"
		if amount_to_send < self.account_balance:
			self.withdraw(amount_to_send)
			recipient.deposit(amount_to_send)
			msg1 = f"DEBIT,\nAmount: #{amount_to_send}.\nRecipient: {recipient.account_name}\nAvailable balance: #{self.account_balance}"
			msg2 = f"Dear {self.account_name},\nTRANSFER of #{amount_to_send} successful.\nRecipient: {recipient.account_name}. Available balance: #{self.account_balance}"


#To reciever
			msg3 = f"CREDIT,\nAmount: #{amount_to_send}.Sender: {self.account_name}\nAvailable balance: #{amount_to_send}"
			msg4 = f"Dear {recipient.account_name},\nCREDIT of #{amount_to_send} successful.\nSender: {amount_to_send}"
		if self.text == True:
			self.send_text(msg1)
			print(f"SMS: {msg1}\nSMS: {msg3}")
			
		if self.email == True:
			self.send_email(msg2)
			return f"EMAIL: {msg2}\nEMAIL: {msg4}" 
		else:
			return "insufficient"

	def freeze_account(self, user):
		if user.isFfreeze == True:
			return f"{user.account_name} account has been frozen"
			       
	def unfreeze_account(self, user):
		if user.isFreeze == False:
			return f"{user.account_name} account has been frozen"
			
        
	def send_text(self, msg):
		if self.text:
			pass

	def send_email(self, msg):
		if self.email:
			pass

jo  = Bank_account("Jo Max", 2000, True, True, text = True, email = True)
pip = Bank_account("Pip Doe ", 1000, False)
print(jo.withdraw(1500))
