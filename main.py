#========EXERCISE 1 MARKET PROJECT========#

# Create the Price List of Fruit Purchases
Price_Apple = 10000
Price_Orange = 15000
Price_Grape = 20000

# Create user input 
Amount_Apple = input("Masukkan Jumlah Apel: ")
Amount_Orange = input("Masukkan Jumlah Jeruk: ")
Amount_Grape = input("Masukkan Jumlah Anggur: ")

# Convert user input to integer
Convert_Amount_Apple = int(Amount_Apple)
Convert_Amount_Orange = int(Amount_Orange)
Convert_Amount_Grape = int(Amount_Grape)

# Calculate the Price List of Fruit Purchases
Price_Apple_Total = Price_Apple * Convert_Amount_Apple
Price_Orange_Total = Price_Orange * Convert_Amount_Orange
Price_Grape_Total = Price_Grape * Convert_Amount_Grape

# Show the Shopping Detail of Fruit Purchases
print("Detail Belanja")
print(f"Apel: {Convert_Amount_Apple} x {Price_Apple} = {Price_Apple_Total}")
print(f"Jeruk: {Convert_Amount_Orange} x {Price_Orange} = {Price_Orange_Total}")
print(f"Anggur: {Convert_Amount_Grape} x {Price_Grape} = {Price_Grape_Total}")

print("Total: ", Price_Apple_Total + Price_Orange_Total + Price_Grape_Total)


#========EXERCISE 2 MARKET PROJECT========#

# Create the Price List of Fruit Purchases
Price_Apple = 10000
Price_Orange = 15000
Price_Grape = 20000

# Calculate the Price List of Fruit Purchases
Price_Apple_Total = Price_Apple * Convert_Amount_Apple
Price_Orange_Total = Price_Orange * Convert_Amount_Orange
Price_Grape_Total = Price_Grape * Convert_Amount_Grape

# Show the Shopping Detail of Fruit Purchases
print("Detail Belanja")
print(f"Apel: {Convert_Amount_Apple} x {Price_Apple} = {Price_Apple_Total}")
print(f"Jeruk: {Convert_Amount_Orange} x {Price_Orange} = {Price_Orange_Total}")
print(f"Anggur: {Convert_Amount_Grape} x {Price_Grape} = {Price_Grape_Total}")

# Show the Payment of Fruit Purchase
Payment = 160000
Amount_of_Money = input("Masukkan Jumlah Uang: ")
Amount_of_Money = int(Amount_of_Money)

# Condition 1 - "When the amount of money given is less"
if Amount_of_Money < Payment:
    Lack_of_Money = Payment - Amount_of_Money
    print(f"Transaksi Anda Dibatalkan Uangnya Kurang Sebesar: {Lack_of_Money}")

# Condition 2 - "When the money given is equal to the total amount to be paid"
elif Amount_of_Money == Payment:
    print("Terima kasih")

# Condition 3 - "When the money given is geater than the amount of money that must be paid"
else: 
    Return_of_Money = Amount_of_Money - Payment    # Amount_of_Money > Payment
    print(f"Uang Kembali Anda: {Return_of_Money}")


#========EXERCISE 3 MARKET PROJECT========#

# Create the Price List of Fruit Purchases
Price_Apple = 10000
Price_Orange = 15000
Price_Grape = 20000

# Stock of Fruit Purchases
Stock_Amount_Apple = 5
Stock_Amount_Orange = 7
Stock_Amount_Grape = 6

# Condition 1 - "When there are too many apples"
Amount_Apple = int(input("Masukkan Jumlah Apel: "))
while Amount_Apple > Stock_Amount_Apple:
    print("Jumlah yang dimasukkan terlalu banyak")
    print("Stok Apel tinggal : 5")
    Amount_Apple = int(input("Masukkan Jumlah Apel: "))
print()

# Condition 2 - "When there are too many oranges"
Amount_Orange = int(input("Masukkan Jumlah Jeruk: "))
while Amount_Orange > Stock_Amount_Orange:
    print("Jumlah yang dimasukkan terlalu banyak")
    print("Stok Jeruk tinggal : 7")
    Amount_Orange = int(input("Masukkan Jumlah Jeruk: "))
print()

# Condition 3 - "When there are too many grapes"
Amount_Grape = int(input("Masukkan Jumlah Anggur: "))
while Amount_Grape > Stock_Amount_Grape:
    print("Jumlah yang dimasukkan terlalu banyak")
    print("Stok Anggur tinggal : 6")
    Amount_Grape = int(input("Masukkan Jumlah Anggur: "))
print()

# Calculate the Price List of Fruit Purchases
Price_Apple_Total = Price_Apple * Amount_Apple
Price_Orange_Total = Price_Orange * Amount_Orange
Price_Grape_Total = Price_Grape * Amount_Grape

# Show the Shopping Detail of Fruit Purchases
print("Detail Belanja")
print(f"Apel: {Amount_Apple} x {Price_Apple} = {Price_Apple_Total}")
print(f"Jeruk: {Amount_Orange} x {Price_Orange} = {Price_Orange_Total}")
print(f"Anggur: {Amount_Grape} x {Price_Grape} = {Price_Grape_Total}")
print()
print("Total price: ", Price_Apple_Total + Price_Orange_Total + Price_Grape_Total)
print()

# Show the Payment of Fruit Purchase
Payment = 275000
Amount_of_Money = input("Masukkan Jumlah Uang: ")
Amount_of_Money = int(Amount_of_Money)
print()

# Condition - "When the amount of money given is less"

while Amount_of_Money < Payment:
    Lack_of_Money = Payment - Amount_of_Money
    print(f"Uang Anda Kurang Sebesar: {Lack_of_Money}")
    Amount_of_Money2 = int(input("Masukkan Jumlah Uang: "))
    if Amount_of_Money2 >= Payment:
        print("Terima kasih!")
        Return_of_Money = Amount_of_Money2 - Payment
        print(f"Uang Kembali Anda: {Return_of_Money}")
        break