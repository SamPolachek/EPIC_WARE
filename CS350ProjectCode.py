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
    print("D) Exit Menu");
    userChoice = input("Enter Your Option Here: ");
    if(userChoice == 'A' or userChoice == 'a'):
        tabulate(list1, list2, list3);
        filter(list1, list2, list3);
        menu(length1, list1, list2, list3);
    elif(userChoice == 'B' or userChoice == 'b'):
        y = 1;
        addItem(y, list1, list2, list3);
        menu(length1, list1, list2, list3);
    elif(userChoice == 'C' or userChoice == 'c'):
        removal = input("Which Item Would You Like to Remove? ");
        found = False;
        for x in range(length1 - 1, -1, -1):
            if(list1[x] == removal):
                del list1[x];
                del list2[x];
                del list3[x];
                found = True;
        if(found == True):
            print("Item Successfully Removed.");
        else:
            print("The Item You Entered Does Not Appear to be in Your List. Please Try Again.");
            removal = input("Which Item Would You Like to Remove? ");
        tabulate(list1, list2, list3);
        menu(length1, list1, list2, list3);
    elif(userChoice == 'D' or userChoice == 'd'):
        print("Menu Exit Successful. Have a Good Day!");
        return False;
    else:
        print("Invalid. Please Enter a Letter From A-C/a-c.");
        userChoice = input("Enter Your Option Here: ");

def filter(list1, list2, list3):
    print("This is a Complete List of All Items You Have Added.");
    print("You Can Sort Through this List by Name, Category, and Expiration Date.");
    print("Filter By:");
    print("A) Alphabetical Order (Name)");
    print("B) Category");
    print("C) Expiration Date");
    filtChoice = input("Please Select an Option for Filtering: ");
    if(filtChoice == 'A' or filtChoice == 'a'):
        list1, list2, list3 = sort_lists(list1, list2, list3);
        print("Here is the List of Items Sorted in Alphabetical Order.");
        tabulate(list1, list2, list3);
    elif(filtChoice == 'B' or filtChoice == 'b'):
        categories = [];
        seen = set();
        for y in list2:
            if y not in seen:
                categories.append(y);
                seen.add(y);
        print(categories);
        uc = len(categories)
        print("You Have %d Unique Categories in Your List of Items." % uc);
    elif(filtChoice == 'C' or filtChoice == 'c'):
        list3, list1, list2 = sort_lists(list3, list1, list2);
        print("Here is the List of Items Sorted by Expiration Date.");
        tabulate(list1, list2, list3);

def sort_lists(list1, list2, list3):
    return zip(*sorted(zip(list1, list2, list3)));

def tabulate(list1, list2, list3):
    max_width1 = max(len("Item Name:"), max(len(item) for item in list1));
    max_width2 = max(len("Item Category:"), max(len(item) for item in list2));
    max_width3 = max(len("Expiration Date:"), max(len(item) for item in list3));
    formatting = f"{{:<{max_width1}}} | {{:<{max_width2}}} | {{:<{max_width3}}}";
    print(formatting.format("Item Name:", "Item Category:", "Expiration Date:"));
    print("-" * (max_width1 + max_width2 + max_width3 + 6));
    for x, y, z in zip(list1, list2, list3):
        print(formatting.format(x, y, z));

print("Welcome to Culinary Cache! Please Enter An Item Name, Category, & Expiration Date*.");
print("*If your item does not have an expiration date, enter 'N/A'.");

n = 1;
names = [];
categories = [];
expDates = [];
addItem(n, names, categories, expDates);

x = len(names);
menu(x, names, categories, expDates);

print("Thank You For Choosing Culinary Cache!");
