import numpy as np
menu = {"Kopi": {"Espresso": 15000, "Cappuccino": 20000, "Latte": 25000}, "Non-kopi": {"Teh": 10000, "Jus": 15000, "Soda": 12000}}
jenis_pembelian = {'Dine-in' : 0, 'Take-away' : 2000, 'Delivery' : 5000}

def daftar_menu(menu, kategori) :
    for item, harga in menu[kategori].items():
        print(f"{item}: Rp {harga:,}")

while True :
    print("=============== 🍵 SELAMAT DATANG DI CAFE SONNTAG ☕ ================")
    print("1. Lihat Menu Kopi")
    print("2. Lihat Menu Non-Kopi")
    print("3. Membuat Menu Baru")
    print("4. Edit Harga Menu")
    print("5. Hapus Menu")
    print("6. Kasir")
    print("7. Keluar")
    inputan = int(input("Masukan input : "))
    if inputan == 1:
        print("\n=============== MENU KOPI ================")
        daftar_menu(menu, "Kopi")
        print("===========================================\n")
    elif inputan == 2:
        print("\n=============== MENU NON-KOPI ================")
        daftar_menu(menu, "Non-kopi")
        print("===========================================\n")
    elif inputan == 3:
        print("\n=============== MEMBUAT MENU BARU ================")
        kategori = input("Masukkan kategori (Kopi/Non-Kopi): ")
        nama_menu = input("Masukkan nama menu: ")
        harga_menu = int(input("Masukkan harga menu: "))
        if kategori.capitalize() in menu:
            menu[kategori.capitalize()][nama_menu.capitalize()] = harga_menu
            print(f"{nama_menu} berhasil ditambahkan ke menu {kategori}.")
        else:
            print("Kategori tidak valid.")
        print("===========================================\n")
    elif inputan == 4:
        print("\n=============== MENGEDIT MENU ================")
        kategori = input("Masukkan kategori (Kopi/Non-kopi): ")
        daftar_menu(menu, kategori.capitalize())
        nama_menu = input("Masukkan nama menu yang ingin diedit: ")
        if kategori.capitalize() in menu and nama_menu.capitalize() in menu[kategori.capitalize()]:
            harga_baru = int(input("Masukkan harga baru: "))
            menu[kategori.capitalize()][nama_menu.capitalize()] = harga_baru
            print(f"{nama_menu} berhasil diperbarui dengan harga baru Rp {harga_baru}.")
        else:
            print("Menu tidak ditemukan.")
        print("===========================================\n")
    elif inputan == 5:
        print("\n=============== MENGHAPUS MENU ================")
        kategori = input("Masukkan kategori (Kopi/Non-kopi): ")
        daftar_menu(menu, kategori.capitalize())
        nama_menu = input("Masukkan nama menu yang ingin dihapus: ")
        if kategori.capitalize() in menu and nama_menu.capitalize() in menu[kategori.capitalize()]:
            del menu[kategori.capitalize()][nama_menu.capitalize()]
            print(f"{nama_menu} berhasil dihapus dari menu {kategori}.")
        else:
            print("Menu tidak ditemukan.")
        print("===========================================\n")
    elif inputan == 6:
        keranjang = {"menu" : [], "banyak" : np.array([])}
        total_belanja = 0
        while True:  
            if len(keranjang["menu"]) > 0:
                print("\nKeranjang belanja Anda: ")
                for item, banyak in zip(keranjang["menu"], keranjang["banyak"]):
                    print(f"Jumlah {item}: {banyak.astype(int)}")
            else :
                print("\nKeranjang belanja Anda masih kosong. Ayo segera pesan!\n")
            kategori = input("Masukkan kategori (Kopi/Non-kopi), ketik lainnya agar perhitungan total dilakukan dan kembali ke halaman utama : ")
            if kategori.capitalize() in menu :
                print(f"\n=============== MENU {kategori.upper()} ================")
                daftar_menu(menu, kategori.capitalize())
            else :
                break
            nama_menu = input("Masukkan nama menu: ")
            if kategori.capitalize() in menu and nama_menu.capitalize() in menu[kategori.capitalize()]:
                keranjang["menu"].append(nama_menu.capitalize())
                banyak = int(input("Masukkan jumlah pesanan: "))
                keranjang["banyak"] = np.append(keranjang["banyak"], banyak)
                total_belanja += menu[kategori.capitalize()][nama_menu.capitalize()] * banyak
                print(f"{nama_menu} berhasil ditambahkan ke pesannan.")
            else:
                continue
        if len(keranjang["menu"]) > 0:
            print("\n=============== RINCIAN PESANAN ================")
            inputan_jenis_pembelian = input("Masukan jenis pembelian. Dine-in/Take-away/Delivery setiap jenis memiliki nominal tambahan berbeda: ")
            for item, banyak in zip(keranjang["menu"], keranjang["banyak"]):
                print(f"Jumlah {item}: {banyak.astype(int)}")
            print(f"Total belanja: Rp {total_belanja + jenis_pembelian[inputan_jenis_pembelian.capitalize()]}\n")
            inputan_pembayaran = float(input("Masukkan jumlah pembayaran: "))
            if inputan_pembayaran < total_belanja:
                print("Maaf, jumlah pembayaran kurang. Silakan coba lagi.")
            else:
                kembalian = inputan_pembayaran - total_belanja
                print(f"Kembalian: Rp {int(kembalian)}\n")
            print("=============== TERIMA KASIH TELAH BERBELANJA DI CAFE SONNTAG ===============\n\n")
        else :
            continue
    elif inputan == 7:
        print("Terima kasih telah berkunjung ke Cafe Sonntag! Jangan lupa datang lagi ya!")
        break