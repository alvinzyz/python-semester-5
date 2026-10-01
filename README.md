Sistem Informasi Mahasiswa (SIM)
Aplikasi console-based untuk mengelola data mahasiswa pada Program Studi Sistem Informasi.

Identitas
Nama: Muhamad Alvin Ramdhan
NIM: 20241320035
Kelas: A1
Fitur
Tambah data mahasiswa (NIM, nama, prodi, angkatan, IPK)
Tampilkan seluruh data dalam tabel
Cari mahasiswa berdasarkan NIM
Hapus data mahasiswa
Validasi data input
Prasyarat
Python 3.10+
pip
Instalasi
git clone https://github.com/alvinzyz/python-semester-5.git
cd python-semester-5/sim-mahasiswa
python -m venv venv
venv\Scripts\activate       # Windows
# source venv/bin/activate  # Linux/macOS
pip install -r requirements.txt
Penggunaan
python -m src.main
Pengujian
pytest tests/ -v
Struktur Proyek
sim-mahasiswa/
├── src/
│   ├── __init__.py
│   ├── main.py        # Program utama & menu interaktif
│   └── models.py      # Model data Mahasiswa & DaftarMahasiswa
├── tests/
│   ├── __init__.py
│   └── test_main.py   # Unit test
├── docs/              # Dokumentasi
├── requirements.txt   # Dependensi
├── .gitignore
└── README.md
Setup Checklist
 Python terinstal (versi: 3.10.6)
 Virtual environment dibuat & diaktivasi
 Paket terinstal via requirements.txt
 Program berjalan tanpa error
 Unit test lulus (5/5 passed)
 Repositori Git diinisiasi
 Push ke GitHub berhasil
 README.md lengkap
