class Mahasiswa:
    """Model data mahasiswa."""

    def __init__(self, npm, nama, kelas, jurusan, alamat, hobby):
        self.npm     = npm
        self.nama    = nama
        self.kelas   = kelas
        self.jurusan = jurusan
        self.alamat  = alamat
        self.hobby   = hobby

    def tampilkan(self):
        """Menampilkan biodata mahasiswa."""
        print("=" * 45)
        print("        DATA BIODATA MAHASISWA")
        print("=" * 45)
        print(f"  NPM     : {self.npm}")
        print(f"  Nama    : {self.nama}")
        print(f"  Kelas   : {self.kelas}")
        print(f"  Jurusan : {self.jurusan}")
        print(f"  Alamat  : {self.alamat}")
        print(f"  Hobby   : {self.hobby}")
        print("=" * 45)
