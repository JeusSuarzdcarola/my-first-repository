# Furniture.py - This program calculates profits and sales prices for a furniture company.

itemname = "TV Stand"
retailprice = 325.00
wholesaleprice = 200.00
profit = 0
saleprice = 0
saleprofit = 0

# Write assignment statements here for profit, saleprice, and saleprofit
profit = retailprice - wholesaleprice
saleprice = retailprice - (retailprice * .25)
saleprofit = saleprice - wholesaleprice

#output statements
print("Item Name: " + itemname)
print("Retail Price: $" + str(retailprice))
print("Wholesale Price: $" + str(wholesaleprice))
print("Profit: $" + str(profit))
print("Sale Price: $" + str(saleprice))
print("Sale Profit: $" + str(saleprofit))

