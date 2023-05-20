import datetime
import sqlite3


class supermarketapp:
    con = sqlite3.connect("market.db")
    cursor = con.cursor()

    def __init__(self):
        print("Welcome to managing panel")

    def createTable(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS managepanel 
                            (ProductID INT,ProductBrand TEXT,ProductModel TEXT,ProductAmount INT, ProductPrice INT )""")
        self.con.commit()

    def addProduct(self):
        print(">>adding command")
        productID = input("Product ID:")
        productBrand = input("Product Brand:")
        productModel = input("Product Model:")
        productAmount = input("Product Amount:")
        productPrice = input("Product Price:")
        self.cursor.execute("INSERT INTO managepanel VALUES (?,?,?,?,?)",
                            (productID, productBrand, productModel, productAmount, productPrice))
        self.con.commit()

    def updateDatas(self):
        print(">>update command")
        print("Please enter the necessary parameter for updating")
        choosing = input(" 1-Brand\n 2-Model\n 3-Amount\n 4-Price\n What's the change attribute:")
        if (choosing == "1"):
            productID = input("Please enter the change products ID:")
            new_brand = input("Please enter the new brand:")
            self.cursor.execute("UPDATE managepanel SET productBrand = ? WHERE productID = ?", (new_brand, productID))
            self.con.commit()
            print("Product updated")
        elif (choosing == "2"):
            productID = input("Please enter the change products ID:")
            new_model = input("Please enter the new model:")
            self.cursor.execute("UPDATE managepanel SET productModel = ? WHERE productID = ?", (new_model, productID))
            self.con.commit()
            print("Product updated")
        elif (choosing == "3"):
            productID = input("Please enter the change products ID:")
            new_amount = input("Please enter the new amount:")
            self.cursor.execute("UPDATE managepanel SET productAmount = ? WHERE productID = ?", (new_amount, productID))
            self.con.commit()
            print("Product updated")
        elif (choosing == "4"):
            productID = input("Please enter the change products ID:")
            new_price = input("Please enter the new price:")
            self.cursor.execute("UPDATE managepanel SET productPrice = ? WHERE productID = ?", (new_price, productID))
            self.con.commit()
            print("Product updated")
        else:
            print("Please make a valid choosing for updating")

    def makeInterestTOPrice(self):
        print(">>makeInterest command")
        ProductID = input("Please enter the ProductID for interest:")
        InterestRate = float(input("Please enter the percent rate for interest:"))
        self.cursor.execute("SELECT ProductPrice FROM managepanel WHERE ProductID = ?", (ProductID,))
        current_price = self.cursor.fetchone()[0]
        new_price = current_price * InterestRate / 100 + current_price
        new_price = round(new_price, 2)  # round to 2 decimal places
        new_price = abs(new_price)
        self.cursor.execute("UPDATE managepanel SET ProductPrice = ? WHERE ProductID = ?", (new_price, ProductID))
        self.con.commit()
        print("Product price updated with interest rate. New price: {}".format(new_price))

    def makeDiscountTOPrice(self):
        print(">>makeDiscount command")
        ProductID = input("Please enter the ProductID for discount:")
        DiscountRate = float(input("Please enter the percent rate for discount:"))
        self.cursor.execute("SELECT ProductPrice FROM managepanel WHERE ProductID = ?", (ProductID,))
        current_price = self.cursor.fetchone()[0]
        new_price = current_price * DiscountRate / 100 - current_price
        new_price = round(new_price, 2)
        new_price = abs(new_price)
        self.cursor.execute("UPDATE managepanel SET ProductPrice = ? WHERE ProductID = ?", (new_price, ProductID))
        self.con.commit()
        print("Product price updated with discount rate. New price: {}".format(new_price))

    def deleteProduct(self):
        print(">>delete command")
        ProductID = input("Please enter Product ID for delete:")
        self.cursor.execute("Delete from managepanel where ProductID = ?", (ProductID,))
        self.con.commit()
        print("The product deleted that is have ID :{} ".format(ProductID))

    def getAllProductInformations(self):
        print(">>terminal command")
        self.cursor.execute("PRAGMA table_info(managepanel)")
        column_info = self.cursor.fetchall()
        column_names = [column[1] for column in column_info]

        productAttributes = self.cursor.execute("SELECT * FROM managepanel")
        self.con.commit()

        for data in productAttributes:
            for i, attribute in enumerate(data):
                print("{}: {}".format(column_names[i], attribute))
            print("-----------------------")

    def getBillAsFormatingTXT(self):
        print(">>printing command")
        from datetime import datetime
        current_datetime = datetime.now()
        current_date = current_datetime.date()
        current_time = current_datetime.time()

        product_information = self.getAllProductInformations()

        fileGettingPreference = input("How do you want to take your bill: \n1-Current Bill \n2-Disposable "
                                      "Bill\nPreference:")
        if(fileGettingPreference == "1"):
           with open("storeBillCurrentData.txt", "w", encoding="UTF-8") as file:
                file.write(product_information)

        elif(fileGettingPreference == "2"):
            with open("storeBill.txt","a",encoding="UTF-8") as file:
                file.write(product_information)

supermarketapp = supermarketapp()


while True:
    mpcs = input("""
    1-Add Product
    2-Delete Product
    3-Update Product
    4-Make Interest
    5-Make discount
    6-Print Bill
    7-Print to Terminal
    8-Create Table
    q-Quit
    Please making choose for use the manage panel:""")
    if (mpcs == "q"):
        break
    elif (mpcs == "1"):
        supermarketapp.addProduct()
    elif (mpcs == "2"):
        supermarketapp.deleteProduct()
    elif (mpcs == "3"):
        supermarketapp.updateDatas()
    elif (mpcs == "4"):
        supermarketapp.makeInterestTOPrice()
    elif (mpcs == "5"):
        supermarketapp.makeDiscountTOPrice()
    elif (mpcs == "6"):
        supermarketapp.getBillAsFormatingTXT()
    elif (mpcs == "7"):
        supermarketapp.getAllProductInformations()
    elif (mpcs == "8"):
        supermarketapp.createTable()
    else:
        print("Please make valid a chose")
        continue