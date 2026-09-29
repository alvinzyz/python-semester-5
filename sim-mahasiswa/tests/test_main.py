import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.models import Mahasiswa

def test_mahasiswa_attributes():
    mhs = Mahasiswa("20241320035", "Alvin", "A1", "Sistem Informasi", "Bojong Koneng", "Badminton")
    assert mhs.npm     == "20241320035"
    assert mhs.nama    == "Alvin"
    assert mhs.kelas   == "A1"
    assert mhs.jurusan == "Sistem Informasi"
    assert mhs.alamat  == "Bojong Koneng"
    assert mhs.hobby   == "Badminton"
    print("✅ Semua test berhasil!")

if __name__ == "__main__":
    test_mahasiswa_attributes()
