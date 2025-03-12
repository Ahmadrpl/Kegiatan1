import webbrowser

# Inisialisasi variabel
playlist = []  # List untuk menyimpan lagu (dalam bentuk dictionary)

# Fungsi untuk menambahkan lagu ke playlist
def tambah_lagu():
    nama_lagu = input("Masukkan nama lagu: ")
    link_lagu = input("Masukkan link lagu (URL): ")
    if len(nama_lagu) > 100:  # Batasan panjang nama lagu
        print("Nama lagu terlalu panjang! Maksimal 100 karakter.")
    else:
        lagu = {"nama": nama_lagu, "link": link_lagu}
        playlist.append(lagu)
        print(f"Lagu '{nama_lagu}' berhasil ditambahkan ke playlist!")

# Fungsi untuk melihat daftar lagu dalam playlist
def lihat_playlist():
    if not playlist:
        print("Playlist kosong. Tidak ada lagu untuk ditampilkan.")
    else:
        print("Daftar Lagu dalam Playlist:")
        for index, lagu in enumerate(playlist):
            print(f"{index + 1}: {lagu['nama']}")

# Fungsi untuk menghapus lagu dari playlist
def hapus_lagu():
    lihat_playlist()
    if playlist:
        try:
            index = int(input("Masukkan nomor lagu yang ingin dihapus: ")) - 1
            if 0 <= index < len(playlist):
                lagu_terhapus = playlist.pop(index)
                print(f"Lagu '{lagu_terhapus['nama']}' berhasil dihapus dari playlist!")
            else:
                print("Nomor lagu tidak valid.")
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")

# Fungsi untuk memutar lagu
def putar_lagu():
    lihat_playlist()
    if playlist:
        try:
            index = int(input("Masukkan nomor lagu yang ingin diputar: ")) - 1
            if 0 <= index < len(playlist):
                lagu = playlist[index]
                print(f"Memutar lagu: {lagu['nama']}")
                webbrowser.open(lagu["link"])  # Membuka link lagu di browser
            else:
                print("Nomor lagu tidak valid.")
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")

# Fungsi utama untuk menjalankan aplikasi
def main():
    # Menampilkan judul "Selamat Datang di Playlist Lagu Kamu"
    print("====================================")
    print(" Selamat Datang di Playlist Lagu Kamu")
    print("====================================")
    
    while True:
        print("\nMenu Playlist Musik:")
        print("1. Tambah Lagu")
        print("2. Lihat Playlist")
        print("3. Hapus Lagu")
        print("4. Putar Lagu")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == '1':
            tambah_lagu()
        elif pilihan == '2':
            lihat_playlist()
        elif pilihan == '3':
            hapus_lagu()
        elif pilihan == '4':
            putar_lagu()
        elif pilihan == '5':
            print("Terima kasih telah menggunakan aplikasi playlist musik!")
            break
        else:
            print("Pilihan tidak valid. Harap pilih antara 1-5.")

# Menjalankan aplikasi
if __name__ == "__main__":
    main()
