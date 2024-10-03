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