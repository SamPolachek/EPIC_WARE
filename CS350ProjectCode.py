def addItem(x, list1, list2, list3):
#This function is called when the user opens the application. It will allow the user to add an item into the database.
#Users must specify item name, category, and expiration date (If the item has one).
#Once an item is added, the program asks the user if they want to add another. Users must respond with Y/y or N/n, or the program will ask again.
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
#After the program exits function addItem(), the program calls this function to ask what the user wants to do with the list.
#Users can view the item list, add a new item, remove an item from the list, or exit the menu, which will end the program.
#After the program does want the user asks, the menu will appear again.
    print("You Currently Have a List of %d Items in Your Inventory. Would You Like to:" % length1);
    print("A) View Item List");
    print("B) Add New Item");
    print("C) Remove Item");
    print("D) Exit Menu");
    userChoice = input("Enter Your Option Here: ");
#If the user wishes to view the list, the program will call function tabulate() to format the list of items and then print it.
#After the list is printed, the program will ask if the user wants to sort the list, and call function filter() if the user says 'yes'.
    if(userChoice == 'A' or userChoice == 'a'):
        tabulate(list1, list2, list3);
        sortOption = input("Would You Like to Sort This List? Please Enter Yes (Y/y) or No (N/n): ");
        if (sortOption == 'Y' or sortOption == 'y'):
            filter(list1, list2, list3);
        menu(length1, list1, list2, list3);
#If the user wishes to add a new item to the list, the program simply calls function addItem(), repeating the starting process.
    elif(userChoice == 'B' or userChoice == 'b'):
        y = 1;
        addItem(y, list1, list2, list3);
        menu(length1, list1, list2, list3);
#If the user wishes to remove an item, the program asks the user to input the name of the item.
#If the item is in the list, the program will remove the item and its corresponding category and expiration date.
#Once the item is removed, the program calls tabulate() to re-print the new list.
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
#If the user wishes to exit the menu, the program simply exits out of menu(), not recursively calling back to the function.
    elif(userChoice == 'D' or userChoice == 'd'):
        print("Menu Exit Successful. Have a Good Day!");
        return False;
    else:
        print("Invalid. Please Enter a Letter From A-C/a-c.");
        userChoice = input("Enter Your Option Here: ");

def filter(list1, list2, list3):
#This function allows users to sort their list of items by either name, category, or expiration date, displaying a menu with options.
#If the user chooses to sort by name or expiration date, the program will use function sort_lists() to arrange each list in ascending order.
#If the user chooses to sort by category, the program will display a list of unique categories and print how many there are.
    print("You Can Sort Through Your List of Items by Name, Category, or Expiration Date.");
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
#This function takes the list that users want the program to sort, and sorts the two corresponding lists based on the user's choice.
    return zip(*sorted(zip(list1, list2, list3)));

def tabulate(list1, list2, list3):
#This function formats and prints the item list in a way that makes it more readable to users.
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

print("Thank You for Choosing Culinary Cache!");
