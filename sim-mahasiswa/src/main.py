import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.models import Mahasiswa

def main():
    print("=" * 45)
    print("       PROGRAM BIODATA MAHASISWA")
    print("=" * 45)

    mahasiswa = Mahasiswa(
        npm     = "20241320035",
        nama    = "Muhamad Alvin Ramdhan",
        kelas   = "A1",
        jurusan = "Sistem Informasi",
        alamat  = "Jln Bojong Koneng",
        hobby   = "Badminton"
    )

    mahasiswa.tampilkan()
    print("  Terima kasih sudah mengisi biodata!")
    print("=" * 45)

if __name__ == "__main__":
    main()
