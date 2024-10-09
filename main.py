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


#========EXERCISE 4 MARKET PROJECT========#

# Create a list menu to produce a list of fruits
while True:
    print("\nSelamat Datang di Pasar Buah") # Create a title
    print("\nList Menu: ")
    print("1. Menampilkan Daftar Buah")
    print("2. Menambahkan Buah")
    print("3. Menghapus Buah")
    print("4. Membeli Buah")
    print("5. Exit Program")
    print()
    choice = int(input("Masukkan angka Menu yang ingin dijalankan: "))
    
    # Create a list of fruit purchases
    list_of_fruits = { "Index" : ["0", "1", "2"],
                       "Nama" : ["Apel", "Jeruk", "Anggur"],
                       "Stock": [20, 15, 25],
                       "Harga": [10_000, 15_000, 20_000]}
    if choice == 1 :
        print("\nDaftar Buah")
        print("Index\t|Nama\t|Stock\t|Harga")
        for choice in range(len(list_of_fruits["Index"])):
            print(f"{list_of_fruits["Index"][choice]}\t|{list_of_fruits["Nama"][choice]}\t|{list_of_fruits["Stock"][choice]}\t|{list_of_fruits["Harga"][choice]}")
    
    # Add fruit to the list
    elif choice == 2:
        AddFruit = input("Masukkan Nama Buah\t:")
        StockFruit = int(input("Masukkan Stock Buah\t:"))
        Price = int(input("Masukkan Harga Buah\t:"))
        Index = "3"
        list_of_fruits["Index"].append(Index)
        list_of_fruits["Nama"].append(AddFruit)
        list_of_fruits["Stock"].append(StockFruit)
        list_of_fruits["Harga"].append(Price)
        print("\nDaftar Buah")
        print("Index\t|Nama\t|Stock\t|Harga")
        for choice in range(len(list_of_fruits["Index"])):
            print(f"{list_of_fruits["Index"][choice]}\t|{list_of_fruits["Nama"][choice]}\t|{list_of_fruits["Stock"][choice]}\t|{list_of_fruits["Harga"][choice]}")
    
    # Remove the fruit in the list
    elif choice == 3:
        print("\nDaftar Buah")
        print("Index\t|Nama\t|Stock\t|Harga")
        for choice in range(len(list_of_fruits["Index"])):
            print(f"{list_of_fruits["Index"][choice]}\t|{list_of_fruits["Nama"][choice]}\t|{list_of_fruits["Stock"][choice]}\t|{list_of_fruits["Harga"][choice]}")
        index_remove = int(input("\nMasukkan Index Buah yang Akan Dihapus: "))
        list_of_fruits ["Nama"].pop(index_remove)
        list_of_fruits ["Stock"].pop(index_remove)
        list_of_fruits ["Harga"].pop(index_remove)
        for choice in range(len(list_of_fruits["Nama"])):
            print(f"{list_of_fruits["Index"][choice]}\t|{list_of_fruits["Nama"][choice]}\t|{list_of_fruits["Stock"][choice]}\t|{list_of_fruits["Harga"][choice]}")
        
    # Create a purchases list
    elif choice == 4:
        print("\nDaftar Buah")
        print("Index\t|Nama\t|Stock\t|Harga")
        for choice in range(len(list_of_fruits["Nama"])):
            print(f"{list_of_fruits["Index"][choice]}\t|{list_of_fruits["Nama"][choice]}\t|{list_of_fruits["Stock"][choice]}\t|{list_of_fruits["Harga"][choice]}")
        option = "Ya"
        total_payment = 0
        list_buy = {"Nama" : [], "Stock" : [], "Harga" : []}
        while option == "Ya":
            index_buy = int(input("Masukkan Index Buah yang Ingin Dibeli: "))
            if index_buy <= len(list_of_fruits["Nama"])-1:
                buy_fruit = int(input("Masukkan Jumlah Buah yang Ingin Dibeli: "))
                if buy_fruit <= list_of_fruits["Stock"][index_buy]:
                    list_of_fruits["Stock"][index_buy] = list_of_fruits["Stock"][index_buy] - buy_fruit
                    list_buy["Nama"].append(list_of_fruits["Nama"][index_buy])
                    list_buy["Harga"].append(list_of_fruits["Harga"][index_buy])
                    list_buy["Stock"].append(buy_fruit)
                else:
                    print(f"Stock buah tidak cukup, stock {list_of_fruits["Nama"][index_buy]} tinggal {list_of_fruits["Stock"][index_buy]}")

            else:
                print("Index Tidak Ada Didalam Daftar")
            print("Isi Chart: ")
            print("Nama\t|Qty\t|Harga\t")
            for choice in range(len(list_buy["Nama"])):
                print(f"{list_buy["Nama"][choice]}\t|{list_buy["Stock"][choice]}\t|{list_buy["Harga"][choice]}")
            option = input("Mau beli yang Lain? (Ya/Tidak): ")
        else:
            for choice in range(len(list_buy["Nama"])):
                total_payment = total_payment + (list_buy["Harga"][choice] * list_buy["Stock"][choice])
            print("Total Yang Harus Dibayar: ", total_payment)
            payment = 0
            while total_payment > payment:
                payment = int(input("\nMasukkan Jumlah Uang: "))
                if total_payment > payment:
                    lack_of_money = total_payment - payment
                    print("Transaksi Anda Dibatalkan")
                    print("Uang Anda Kurang Sebesar", lack_of_money)
                    print()
                elif total_payment == payment:
                    print("Terimakasih!")
                    print()
                else:
                    return_of_money = payment - total_payment
                    print("Terimakasih!")
                    print("Uang Kembalian Anda", return_of_money)
        
    elif choice == 5:
        print("Exit Program")
        break
    else:
        print("Menu Tidak Tersedia")
        break





