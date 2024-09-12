def addItem(x, list1, list2, list3):
    while (x == 1):
        itemName = input("Enter Item Name: ");
        list1.append(itemName);
        itemCategory = input("Enter Item Category: ");
        list2.append(itemCategory);
        itemExp = input("Enter Item Expiration Date: ");
        list3.append(itemExp);
        addMore = input("Would You Like To Add Another Item? Please Enter Yes (Y/y) or No (N/n): ");
        if(addMore == 'Y' or addMore == 'y'):
            return addItem(x, list1, list2, list3);
        elif (addMore == 'N' or addMore == 'n'):
            x == 0;
            return False;
        else:
            print("Invalid. Please Enter Y/y or N/n.");
            addMore = input("Would You Like To Add Another Item? Please Enter Yes (Y/y) or No (N/n): ");
            if(addMore == 'Y' or addMore == 'y'):
                return addItem(x, list1, list2, list3);
            elif (addMore == 'N' or addMore == 'n'):
                x == 0;
                return False;

def menu(length1, list1, list2, list3):
    print("You Currently Have a List of %d Items in Your Inventory. Would You Like to:" % length1);
    print("A) View Item List");
    print("B) Add New Item");
    print("C) Remove Item");
    userChoice = input("Enter Your Option Here: ");
    if(userChoice == 'A' or userChoice == 'a'):
        print("Item Name: | Item Category: | Expiration Date:");
        for x in range(length1):
            print(list1[x] + " | " + list2[x] + " | " + list3[x]);
    elif(userChoice == 'B' or userChoice == 'b'):
        y = 1;
        addItem(y, list1, list2, list3);
    elif(userChoice == 'C' or userChoice == 'c'):
        removal = input("Which Item Would You Like to Remove? ");
        for x in range(length1):
            if(list1[x] == removal):
                list1.remove(list1[x]);
                list2.remove(list2[x]);
                list3.remove(list3[x]);
        print("Item Successfully Removed.");
    else:
        print("Invalid. Please Enter a Letter From A-C/a-c.");
        userChoice = input("Enter Your Option Here: ");
    menu(length1, list1, list2, list3);


print("Hello! Please Enter An Item Name, Category, & Expiration Date*");
print("*If your item does not have an expiration date, enter 'N/A'.");

n = 1;
names = [];
categories = [];
expDates = [];
addItem(n, names, categories, expDates);

x = len(names);
menu(x, names, categories, expDates);