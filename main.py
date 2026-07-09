#Expence Tracker Project
expensesList = [] # List of expenses in form of dictionary
print("Welcome to EXPENSES Tracker :")

while True :
    print("=============MENU===============")
    print("1. Add Expenses")
    print("2. View All Expenses")
    print("3. View Total Spending")
    print("4. EXIT")
    print("-----------------------------")
    choice = int(input("Please enter your choic : "))

    #Add Expenses
    if(choice==1):
        date = input("Enter DATE : ")
        category = input("Enter the CATEGORY : (food,travel,grocery etc..)")
        description = input("Enter short DESCRIPTION :")
        amount = float(input("Enter AMOUNT :"))

        expenses = {
            "DATE": date,
            "CATEGORY" : category,
            "DESCRIPTION" : description,
            "AMOUNT" :amount
        }
        expensesList.append(expenses)
        print("✅Expenses added successfully")
        #2.VEIW ALL EXPENSES
    elif(choice==2):
        if(len(expensesList)==0):
           print("No Expenses Found")
        else:
           print("-------------All Expenses----------------")
           count = 1
           for expenses in expensesList:
               print(f"expens no.{count} : {expenses["DATE"]},{expenses["CATEGORY"]},{expenses["DESCRIPTION"]},{expenses["AMOUNT"]}")
               count = count + 1

    #3.view total spending
    elif(choice==3):
        totalSpending = 0
        for expenses in expensesList:
            totalSpending = totalSpending + expenses["AMOUNT"]
        print("\nTotal Spending :",totalSpending)

   #4.EXIT
    elif(choice==4):
        print("Thank you for using Expenses Tracker")    
        break

    else:
        print("INVALID CHOICE,Please enter valid choice")

       




