#!/usr/bin/env python
# coding: utf-8

# In[18]:


class BankAccount() :
    def __init__(self, name, age, gender, job) :
        self.name = name
        self.age = age
        self.gender = gender
        self.job = job
        
    def showinfo(self) :
        if self.gender == "f" :
            title = "Ms."
        else:
            title = "Mr."
        print("Hello", title, self.name)
        print("You are a", self.age,"year-old", self.job)
        
        
        


# In[32]:


class Banktrans(BankAccount) :
    def __init__(self, name, age, gender, job) :
        super(). __init__(name, age, gender, job)
        self.balance = 0
        
    def deposit(self) :
        addamount = int(input("Enter the amount you want to deposit"))
        self.balance = self.balance + addamount
        print("Transaction successful!\n Your new balance is", self.balance)
        
    def withdraw(self) :
        wdamount = int(input("Enter the amount you want to withdraw"))
        if wdamount < self.balance :
            self.balance = self.balance - wdamount
            print("Transaction successful!\n Your new balance is", self.balance)
        else :
            print("Transaction failed!\n There is not enough balance amount")
            
    def viewbalance(self) :
        self.showinfo()
        print("Your account balance is", self.balance)
        


# In[24]:


#defining an instance with user-entered attribute values

user1 = Banktrans(input("enter you name"),int(input("enter you age")), input("F or M"), input("enter your job"))


# In[28]:


user1.viewbalance()


# In[29]:


user1.deposit()


# In[31]:


user1.withdraw()


# In[ ]:




