import mysql.connector as sqltor
mycon = sqltor.connect(host ="localhost", user = "root", passwd = "lalit2106", database = "Database_04")
print()
print("                                    'GARDEN OF TASTE'                                      ")
print()
print("Welcome to the 'GARDEN OF TASTE' ")
print()
print()
print("Select one to continue.....")
print("1. See Menu ")
print("2. Place Order ")
print("3. Bill ")
choice  = int(input("Enter a number to continue : ")) 
if choice >3:
    print("Invalid, please choose a valid number")
else :
    if choice == 1:
        ctgy = input("Select a meal of your choice Veg/Non-Veg/Dessert : ") 
        print()
        print ("Menu for",ctgy," meal")
        if ctgy.lower() == "veg":
            print()
            query1= "select * from Menu"
            cursor1 = mycon.cursor(buffered=True)
            cursor1.execute(query1)
            for row in cursor1:
                print ("Dish No : ",row[0])
                print ("Dish Name : ",row[1])
                print ("Dish Category : ",row[2])
                print ("Dish Price : ",row[3])
                print()
            mycon.commit()
        elif ctgy.lower() == "non-veg":
            print()
            query2 = "select * from Menu_00"
            cursor2 = mycon.cursor(buffered=True)
            cursor2.execute(query2)
            for row in cursor2:
                print ("Dish No : ",row[0])
                print ("Dish Name : ",row[1])
                print ("Dish Category : ",row[2])
                print ("Dish Price : ",row[3])
                print()
            mycon.commit()
        elif ctgy.lower() == "dessert":
            print()
            query3 = "select * from Menu_0000"
            cursor3 = mycon.cursor(buffered=True)
            cursor3.execute(query3)
            for row in cursor3:
                print ("Dish No : ",row[0])
                print ("Dish Name : ",row[1])
                print ("Dish Category : ",row[2])
                print ("Dish Price : ",row[3])
                print()
            mycon.commit()
    if choice == 2:
        query4 = "create table Place_Order(Dish_Name char(40), Dish_Price int(10))"
        cursor4 = mycon.cursor(buffered=True)
        cursor4.execute(query4)
        mycon.commit()
        while (True):
            print()
            print("Enter 'y' if you want to order and ")
            still_order = input("Enter 'n' if you don't want to order : ")
            print()
            if still_order.lower() == 'y':
                dish_name = input("Enter name of the Dish you want to order : ")
                if dish_name.lower() == "shahi paneer":
                    dish_price = 400
                    print("Shahi paneer price : 400")
                elif dish_name.lower() == "pizza":
                    dish_price = 600
                    print("Pizza price : 600")
                elif dish_name.lower() == "manchurian":
                    dish_price = 320
                    print("Manchurian price : 320")
                elif dish_name.lower() == "hara-bhara kabab":
                    dish_price = 450
                    print("Hara-Bhara Kabab price : 450")
                elif dish_name.lower() == "malai chaap":
                    dish_price = 350
                    print("Malai Chaap price : 350")
                elif dish_name.lower() == "butter chicken":
                    dish_price = 550
                    print("Butter Chicken price : 550")
                elif dish_name.lower() == "murgh musallam":
                    dish_price = 750
                    print("Murgh musallam price : 750")
                elif dish_name.lower() == "mughlai parantha":
                    dish_price = 300
                    print("Mughlai Parantha price : 300")
                elif dish_name.lower() == "dry fish fry":
                    dish_price = 450
                    print("Dry Fish Fry price : 450")
                elif dish_name.lower() == "hyderabadi biryani":
                    dish_price = 500
                    print("Hyderabadi Biryani price : 500")
                elif dish_name.lower() == "shahi gulab jamun":
                    dish_price = 75
                    print("Shahi Gulab Jamun price : 75")
                elif dish_name.lower() == "blue berry cake":
                    dish_price = 220
                    print("Blue Berry Cake price : 220")
                elif dish_name.lower() == "apple pie bread":
                    dish_price = 180
                    print("Apple Pie Bread price : 180")
                elif dish_name.lower() == "shrikhand":
                    dish_price = 350
                    print("Shrikhand price : 350")
                elif dish_name.lower() == "rasmalai":
                    dish_price = 120
                    print("Rasmalai price : 120")
                query5 = "insert into Place_Order values('{}', {})".format(dish_name,dish_price)
                cursor5 = mycon.cursor(buffered=True)
                cursor5.execute(query5)
                mycon.commit()
            elif still_order.lower() == 'n': 
                print("Your order has been confirmed ")
                print("Thank you")
                break
    if choice ==3:
        Name= input("Enter You good name please : ")
        print()
        print("                                     'GARDEN OF TASTE'                                   ")
        print("                                       Customer Bill                                     ")
        print() 
        from datetime import date
        Bill_date = date.today()
        print("Date : ", Bill_date )
        print()
        print(Name)
        print()
        query6 = "select * from place_order"
        cursor6 = mycon.cursor(buffered=True)
        cursor6.execute(query6)
        print("Your orders :")
        print()
        for row in cursor6:
            print ("Dish Name : ",row[0])
            print ("Dish Price : ",row[1])
            print()
        mycon.commit()
        print()
        query7 = "select sum(Dish_Price) from place_order"
        cursor7 = mycon.cursor(buffered=True)
        cursor7.execute(query7)
        print("Discount - 0")
        for row in cursor7:
            print("Total amount to be paid : ", row[0])
        mycon.commit()
        print()
        query8= "drop table place_order"
        cursor8=mycon.cursor(buffered=True)
        cursor8.execute(query8)
        print("Thank you, Vist again")
        print()



# Limitations :-
'''
1. You have to run the program multiple times for seeing menu, placing order and bill.
2. The Menu is not in the table form.
3. You can see Menu of a single category of meal at a time (either veg, non-veg or desserts).
4. The program will fail if you ask for a bill without ordering anythig.
5. There is no option for quantity.
'''