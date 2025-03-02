class Mahasiswa:
    def __init__(self, nama, nim, mata_kuliah, ipk):
        self.nama = nama
        self.nim = nim
        self.mata_kuliah = mata_kuliah  # List of subjects
        self.ipk = ipk

    def __str__(self):
        return f"Nama: {self.nama}, NIM: {self.nim}, Mata Kuliah: {', '.join(self.mata_kuliah)}, IPK: {self.ipk}"

# Contoh objek mahasiswa
mahasiswa1 = Mahasiswa("Alice", "123456", ["Matematika", "Fisika", "Kimia", "Biologi", "Statistika", "Pemrograman"], 3.5)
mahasiswa2 = Mahasiswa("Bob", "123457", ["Matematika", "Fisika", "Kimia", "Biologi", "Statistika", "Pemrograman"], 3.6)
mahasiswa3 = Mahasiswa("Charlie", "123458", ["Matematika", "Fisika", "Kimia", "Biologi", "Statistika", "Pemrograman"], 3.7)

# Menampilkan informasi mahasiswa
mahasiswa_list = [mahasiswa1, mahasiswa2, mahasiswa3]

for mhs in mahasiswa_list:
    print(mhs)