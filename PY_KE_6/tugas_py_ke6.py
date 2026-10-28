# ============================================================================
# TUGAS PYTHON KE-6 - SEMUA SOAL DIGABUNG DALAM SATU FILE
# ============================================================================
# Soal 1: Fungsi hitung_statistik()
# Soal 2: Fungsi validasi_data()
# Soal 3: Module utilitas_akademik (hitung_ipk, konversi_nilai_huruf, generate_transkrip)
# Soal 4: Package sistem_informasi (CRUD Mahasiswa in-memory)
# Soal 5: REST API + lambda + higher-order functions + simpan ke JSON
# ============================================================================

import statistics
import math
import json
import os

# ============================================================================
# SOAL 1: Fungsi hitung_statistik()
# ============================================================================
# Fungsi yang menerima list angka dan mengembalikan dictionary berisi
# mean, median, modus, range (max-min), dan standard deviation.
# Menggunakan standard library (statistics, math).
# ============================================================================

def hitung_statistik(data):
    """
    Menghitung statistik dari list angka.

    Parameter:
        data (list): List berisi angka-angka.

    Return:
        dict: Dictionary berisi mean, median, modus, range, dan standard deviation.
    """
    if not data:
        return {
            "mean": 0,
            "median": 0,
            "modus": 0,
            "range": 0,
            "standard_deviation": 0
        }

    hasil = {
        "mean": statistics.mean(data),
        "median": statistics.median(data),
        "modus": statistics.mode(data),
        "range": max(data) - min(data),
        "standard_deviation": statistics.stdev(data) if len(data) > 1 else 0
    }
    return hasil


def demo_soal_1():
    """Demo untuk Soal 1: hitung_statistik()"""
    print("=" * 70)
    print(" SOAL 1: Fungsi hitung_statistik()")
    print("=" * 70)

    # Data contoh: nilai ujian mahasiswa
    nilai_ujian = [85, 90, 78, 92, 88, 76, 95, 85, 70, 85, 91, 82]

    print(f"\nData nilai ujian : {nilai_ujian}")
    print(f"Jumlah data      : {len(nilai_ujian)}")
    print("-" * 50)

    hasil = hitung_statistik(nilai_ujian)

    print(f"  Mean (Rata-rata)     : {hasil['mean']:.2f}")
    print(f"  Median               : {hasil['median']:.2f}")
    print(f"  Modus                : {hasil['modus']}")
    print(f"  Range (Max - Min)    : {hasil['range']}")
    print(f"  Standard Deviation   : {hasil['standard_deviation']:.4f}")

    # Data contoh kedua
    print("\n" + "-" * 50)
    data_tinggi_badan = [165, 170, 158, 175, 162, 180, 168, 172, 155, 170]
    print(f"Data tinggi badan : {data_tinggi_badan}")
    print(f"Jumlah data       : {len(data_tinggi_badan)}")
    print("-" * 50)

    hasil2 = hitung_statistik(data_tinggi_badan)

    print(f"  Mean (Rata-rata)     : {hasil2['mean']:.2f}")
    print(f"  Median               : {hasil2['median']:.2f}")
    print(f"  Modus                : {hasil2['modus']}")
    print(f"  Range (Max - Min)    : {hasil2['range']}")
    print(f"  Standard Deviation   : {hasil2['standard_deviation']:.4f}")

    print()


# ============================================================================
# SOAL 2: Fungsi validasi_data()
# ============================================================================
# Fungsi yang menerima dictionary data dan schema validasi (berupa dictionary
# dengan aturan tipe dan rentang). Mengembalikan tuple (is_valid, errors).
# Menggunakan *args dan **kwargs untuk fleksibilitas tambahan.
# ============================================================================

def validasi_data(data, schema, *args, **kwargs):
    """
    Memvalidasi dictionary data berdasarkan schema yang diberikan.

    Parameter:
        data (dict)   : Dictionary data yang akan divalidasi.
        schema (dict) : Dictionary schema validasi. Setiap key berisi dict dengan:
                        - 'tipe'     : tipe data yang diharapkan (int, float, str, dll.)
                        - 'required' : apakah field wajib ada (True/False)
                        - 'min'      : nilai minimum (opsional, untuk int/float)
                        - 'max'      : nilai maksimum (opsional, untuk int/float)
                        - 'min_len'  : panjang minimum (opsional, untuk str)
                        - 'max_len'  : panjang maksimum (opsional, untuk str)
        *args         : Argumen tambahan (misal: list field yang di-skip).
        **kwargs      : Keyword arguments tambahan:
                        - strict (bool)  : jika True, field di data yang tidak ada
                                           di schema dianggap error.
                        - verbose (bool) : jika True, cetak proses validasi.

    Return:
        tuple: (is_valid: bool, errors: list of str)
    """
    errors = []
    strict = kwargs.get("strict", False)
    verbose = kwargs.get("verbose", False)

    # Ambil field yang di-skip dari *args (jika ada)
    skip_fields = list(args)

    if verbose:
        print("  [VERBOSE] Memulai validasi data...")
        print(f"  [VERBOSE] Mode strict: {strict}")
        if skip_fields:
            print(f"  [VERBOSE] Field yang di-skip: {skip_fields}")

    # Validasi setiap field di schema
    for field, aturan in schema.items():
        if field in skip_fields:
            if verbose:
                print(f"  [VERBOSE] Skip field '{field}'")
            continue

        required = aturan.get("required", False)
        tipe = aturan.get("tipe", None)

        # Cek apakah field wajib ada
        if required and field not in data:
            errors.append(f"Field '{field}' wajib diisi tetapi tidak ditemukan.")
            continue

        # Jika field tidak ada dan tidak required, lewati
        if field not in data:
            if verbose:
                print(f"  [VERBOSE] Field '{field}' tidak ada (opsional), dilewati.")
            continue

        nilai = data[field]

        # Cek tipe data
        if tipe and not isinstance(nilai, tipe):
            errors.append(
                f"Field '{field}': tipe data harus {tipe.__name__}, "
                f"tetapi ditemukan {type(nilai).__name__}."
            )
            continue

        # Cek rentang untuk tipe numerik (int/float)
        if isinstance(nilai, (int, float)):
            if "min" in aturan and nilai < aturan["min"]:
                errors.append(
                    f"Field '{field}': nilai {nilai} kurang dari minimum {aturan['min']}."
                )
            if "max" in aturan and nilai > aturan["max"]:
                errors.append(
                    f"Field '{field}': nilai {nilai} melebihi maksimum {aturan['max']}."
                )

        # Cek panjang untuk tipe string
        if isinstance(nilai, str):
            if "min_len" in aturan and len(nilai) < aturan["min_len"]:
                errors.append(
                    f"Field '{field}': panjang '{nilai}' ({len(nilai)}) kurang dari "
                    f"minimum {aturan['min_len']} karakter."
                )
            if "max_len" in aturan and len(nilai) > aturan["max_len"]:
                errors.append(
                    f"Field '{field}': panjang '{nilai}' ({len(nilai)}) melebihi "
                    f"maksimum {aturan['max_len']} karakter."
                )

    # Mode strict: cek field di data yang tidak ada di schema
    if strict:
        for field in data:
            if field not in schema:
                errors.append(
                    f"Field '{field}' tidak dikenali dalam schema (mode strict)."
                )

    is_valid = len(errors) == 0

    if verbose:
        status = "VALID" if is_valid else "TIDAK VALID"
        print(f"  [VERBOSE] Hasil validasi: {status} ({len(errors)} error)")

    return (is_valid, errors)


def demo_soal_2():
    """Demo untuk Soal 2: validasi_data()"""
    print("=" * 70)
    print(" SOAL 2: Fungsi validasi_data()")
    print("=" * 70)

    # Schema validasi untuk data mahasiswa
    schema_mahasiswa = {
        "nama": {
            "tipe": str,
            "required": True,
            "min_len": 3,
            "max_len": 50
        },
        "nim": {
            "tipe": str,
            "required": True,
            "min_len": 8,
            "max_len": 15
        },
        "usia": {
            "tipe": int,
            "required": True,
            "min": 17,
            "max": 60
        },
        "ipk": {
            "tipe": float,
            "required": True,
            "min": 0.0,
            "max": 4.0
        },
        "semester": {
            "tipe": int,
            "required": False,
            "min": 1,
            "max": 14
        }
    }

    # --- Test 1: Data valid ---
    print("\n--- Test 1: Data Valid ---")
    data_valid = {
        "nama": "Budi Santoso",
        "nim": "20210001",
        "usia": 21,
        "ipk": 3.75,
        "semester": 5
    }
    print(f"  Data: {data_valid}")
    is_valid, errors = validasi_data(data_valid, schema_mahasiswa)
    print(f"  Valid: {is_valid}")
    if errors:
        for e in errors:
            print(f"  Error: {e}")

    # --- Test 2: Data tidak valid ---
    print("\n--- Test 2: Data Tidak Valid ---")
    data_invalid = {
        "nama": "AB",            # terlalu pendek (min 3)
        "nim": "123",            # terlalu pendek (min 8)
        "usia": 15,              # di bawah minimum (17)
        "ipk": 4.5,             # melebihi maksimum (4.0)
    }
    print(f"  Data: {data_invalid}")
    is_valid, errors = validasi_data(data_invalid, schema_mahasiswa)
    print(f"  Valid: {is_valid}")
    for e in errors:
        print(f"  Error: {e}")

    # --- Test 3: Data dengan tipe salah ---
    print("\n--- Test 3: Data Dengan Tipe Salah ---")
    data_tipe_salah = {
        "nama": 12345,           # seharusnya str
        "nim": "20210003",
        "usia": "dua puluh",     # seharusnya int
        "ipk": "tiga koma lima", # seharusnya float
    }
    print(f"  Data: {data_tipe_salah}")
    is_valid, errors = validasi_data(data_tipe_salah, schema_mahasiswa)
    print(f"  Valid: {is_valid}")
    for e in errors:
        print(f"  Error: {e}")

    # --- Test 4: Menggunakan *args (skip field) dan **kwargs (strict, verbose) ---
    print("\n--- Test 4: Dengan *args (skip 'semester') dan **kwargs (strict=True, verbose=True) ---")
    data_extra_field = {
        "nama": "Citra Dewi",
        "nim": "20210004",
        "usia": 22,
        "ipk": 3.50,
        "semester": 6,
        "alamat": "Jakarta"      # field ini tidak ada di schema
    }
    print(f"  Data: {data_extra_field}")
    is_valid, errors = validasi_data(
        data_extra_field, schema_mahasiswa,
        "semester",               # *args: skip field 'semester'
        strict=True,              # **kwargs
        verbose=True
    )
    print(f"  Valid: {is_valid}")
    for e in errors:
        print(f"  Error: {e}")

    print()


# ============================================================================
# SOAL 3: Module utilitas_akademik
# ============================================================================
# Berisi fungsi: hitung_ipk(), konversi_nilai_huruf(), generate_transkrip().
# (Dijadikan satu file sesuai instruksi)
# ============================================================================

def konversi_nilai_huruf(nilai_angka):
    """
    Mengkonversi nilai angka (0-100) menjadi nilai huruf.

    Parameter:
        nilai_angka (int/float): Nilai angka antara 0 sampai 100.

    Return:
        str: Nilai huruf (A, AB, B, BC, C, D, E).
    """
    if nilai_angka >= 85:
        return "A"
    elif nilai_angka >= 80:
        return "AB"
    elif nilai_angka >= 75:
        return "B"
    elif nilai_angka >= 70:
        return "BC"
    elif nilai_angka >= 60:
        return "C"
    elif nilai_angka >= 50:
        return "D"
    else:
        return "E"


def bobot_nilai(huruf):
    """
    Mengembalikan bobot numerik dari nilai huruf.

    Parameter:
        huruf (str): Nilai huruf (A, AB, B, BC, C, D, E).

    Return:
        float: Bobot numerik.
    """
    tabel_bobot = {
        "A": 4.0,
        "AB": 3.5,
        "B": 3.0,
        "BC": 2.5,
        "C": 2.0,
        "D": 1.0,
        "E": 0.0
    }
    return tabel_bobot.get(huruf.upper(), 0.0)


def hitung_ipk(daftar_mata_kuliah):
    """
    Menghitung IPK dari daftar mata kuliah.

    Parameter:
        daftar_mata_kuliah (list of dict): Setiap dict berisi:
            - 'nama_mk'     : nama mata kuliah (str)
            - 'sks'         : jumlah SKS (int)
            - 'nilai_angka' : nilai angka 0-100 (int/float)

    Return:
        float: Nilai IPK (skala 4.0).
    """
    total_bobot = 0
    total_sks = 0

    for mk in daftar_mata_kuliah:
        sks = mk["sks"]
        huruf = konversi_nilai_huruf(mk["nilai_angka"])
        total_bobot += bobot_nilai(huruf) * sks
        total_sks += sks

    if total_sks == 0:
        return 0.0

    ipk = total_bobot / total_sks
    return round(ipk, 2)


def generate_transkrip(nama_mahasiswa, nim, daftar_mata_kuliah):
    """
    Membuat transkrip nilai mahasiswa dalam bentuk string terformat.

    Parameter:
        nama_mahasiswa (str)           : Nama mahasiswa.
        nim (str)                      : NIM mahasiswa.
        daftar_mata_kuliah (list of dict): List mata kuliah dengan sks dan nilai.

    Return:
        str: String berisi transkrip nilai lengkap.
    """
    lebar = 70
    garis = "=" * lebar

    transkrip = []
    transkrip.append(garis)
    transkrip.append("  TRANSKRIP NILAI AKADEMIK".center(lebar))
    transkrip.append(garis)
    transkrip.append(f"  Nama : {nama_mahasiswa}")
    transkrip.append(f"  NIM  : {nim}")
    transkrip.append("-" * lebar)
    transkrip.append(
        f"  {'No':<4} {'Mata Kuliah':<30} {'SKS':>5} {'Nilai':>7} {'Huruf':>7} {'Bobot':>7}"
    )
    transkrip.append("-" * lebar)

    total_sks = 0
    total_bobot = 0

    for i, mk in enumerate(daftar_mata_kuliah, 1):
        nama_mk = mk["nama_mk"]
        sks = mk["sks"]
        nilai = mk["nilai_angka"]
        huruf = konversi_nilai_huruf(nilai)
        bbt = bobot_nilai(huruf)

        total_sks += sks
        total_bobot += bbt * sks

        transkrip.append(
            f"  {i:<4} {nama_mk:<30} {sks:>5} {nilai:>7.1f} {huruf:>7} {bbt:>7.1f}"
        )

    transkrip.append("-" * lebar)
    ipk = total_bobot / total_sks if total_sks > 0 else 0
    transkrip.append(f"  Total SKS : {total_sks}")
    transkrip.append(f"  IPK       : {ipk:.2f}")
    transkrip.append(garis)

    return "\n".join(transkrip)


def demo_soal_3():
    """Demo untuk Soal 3: utilitas_akademik"""
    print("=" * 70)
    print(" SOAL 3: Module utilitas_akademik")
    print("=" * 70)

    # Data mata kuliah contoh
    daftar_mk = [
        {"nama_mk": "Algoritma & Pemrograman",   "sks": 3, "nilai_angka": 88},
        {"nama_mk": "Struktur Data",             "sks": 3, "nilai_angka": 82},
        {"nama_mk": "Basis Data",                "sks": 3, "nilai_angka": 76},
        {"nama_mk": "Jaringan Komputer",         "sks": 3, "nilai_angka": 90},
        {"nama_mk": "Sistem Operasi",            "sks": 3, "nilai_angka": 71},
        {"nama_mk": "Matematika Diskrit",        "sks": 3, "nilai_angka": 65},
        {"nama_mk": "Kalkulus",                  "sks": 2, "nilai_angka": 78},
        {"nama_mk": "Bahasa Inggris",            "sks": 2, "nilai_angka": 92},
    ]

    # Demo konversi_nilai_huruf
    print("\n--- Konversi Nilai Huruf ---")
    contoh_nilai = [95, 82, 76, 71, 65, 52, 40]
    for n in contoh_nilai:
        print(f"  Nilai {n:>3} -> {konversi_nilai_huruf(n)}")

    # Demo hitung_ipk
    print("\n--- Hitung IPK ---")
    ipk = hitung_ipk(daftar_mk)
    print(f"  IPK Mahasiswa: {ipk}")

    # Demo generate_transkrip
    print("\n--- Generate Transkrip ---")
    transkrip = generate_transkrip("Andi Pratama", "20210001", daftar_mk)
    print(transkrip)

    print()


# ============================================================================
# SOAL 4: Package sistem_informasi (CRUD Mahasiswa)
# ============================================================================
# Berisi subpackage: model, service, utils.
# Implementasi CRUD sederhana untuk entitas Mahasiswa
# menggunakan dictionary sebagai penyimpanan in-memory.
# (Semua dijadikan satu file sesuai instruksi)
# ============================================================================

# --- model (entitas Mahasiswa) ---

class MahasiswaModel:
    """
    Representasi model data Mahasiswa.
    Menyimpan data dalam dictionary in-memory.
    """

    def __init__(self):
        """Inisialisasi storage sebagai dictionary kosong."""
        self._storage = {}
        self._next_id = 1

    def get_storage(self):
        """Mengembalikan seluruh data storage."""
        return self._storage.copy()

    def get_next_id(self):
        """Mengembalikan ID berikutnya."""
        return self._next_id

    def increment_id(self):
        """Menaikkan counter ID."""
        self._next_id += 1


# --- utils (fungsi utilitas) ---

def format_mahasiswa(mhs_data):
    """
    Memformat data mahasiswa menjadi string yang rapi.

    Parameter:
        mhs_data (dict): Data mahasiswa.

    Return:
        str: String terformat.
    """
    return (
        f"  ID: {mhs_data['id']} | "
        f"NIM: {mhs_data['nim']} | "
        f"Nama: {mhs_data['nama']} | "
        f"Jurusan: {mhs_data['jurusan']} | "
        f"IPK: {mhs_data['ipk']}"
    )


def validasi_nim(nim):
    """
    Memvalidasi format NIM (harus digit, minimal 8 karakter).

    Parameter:
        nim (str): NIM yang akan divalidasi.

    Return:
        bool: True jika valid.
    """
    return isinstance(nim, str) and nim.isdigit() and len(nim) >= 8


# --- service (CRUD operations) ---

class MahasiswaService:
    """
    Service layer untuk operasi CRUD pada entitas Mahasiswa.
    """

    def __init__(self):
        """Inisialisasi model."""
        self.model = MahasiswaModel()

    def create(self, nim, nama, jurusan, ipk):
        """
        Menambahkan data mahasiswa baru (CREATE).

        Parameter:
            nim (str)     : NIM mahasiswa.
            nama (str)    : Nama mahasiswa.
            jurusan (str) : Jurusan mahasiswa.
            ipk (float)   : IPK mahasiswa.

        Return:
            dict: Data mahasiswa yang baru dibuat, atau None jika gagal.
        """
        if not validasi_nim(nim):
            print(f"  [ERROR] NIM '{nim}' tidak valid (harus digit, min 8 karakter).")
            return None

        # Cek duplikat NIM
        for mhs in self.model.get_storage().values():
            if mhs["nim"] == nim:
                print(f"  [ERROR] NIM '{nim}' sudah terdaftar.")
                return None

        mhs_id = self.model.get_next_id()
        data_mhs = {
            "id": mhs_id,
            "nim": nim,
            "nama": nama,
            "jurusan": jurusan,
            "ipk": ipk
        }
        self.model._storage[mhs_id] = data_mhs
        self.model.increment_id()
        return data_mhs

    def read(self, mhs_id=None):
        """
        Membaca data mahasiswa (READ).

        Parameter:
            mhs_id (int, optional): ID mahasiswa. Jika None, return semua data.

        Return:
            dict atau list: Data mahasiswa tunggal atau list semua mahasiswa.
        """
        if mhs_id is not None:
            data = self.model.get_storage()
            if mhs_id in data:
                return data[mhs_id]
            else:
                print(f"  [ERROR] Mahasiswa dengan ID {mhs_id} tidak ditemukan.")
                return None
        else:
            return list(self.model.get_storage().values())

    def update(self, mhs_id, **kwargs):
        """
        Memperbarui data mahasiswa (UPDATE).

        Parameter:
            mhs_id (int)  : ID mahasiswa yang akan diupdate.
            **kwargs      : Field yang akan diupdate (nama, jurusan, ipk, nim).

        Return:
            dict: Data mahasiswa yang sudah diupdate, atau None jika gagal.
        """
        if mhs_id not in self.model._storage:
            print(f"  [ERROR] Mahasiswa dengan ID {mhs_id} tidak ditemukan.")
            return None

        allowed_fields = {"nim", "nama", "jurusan", "ipk"}
        for key, value in kwargs.items():
            if key in allowed_fields:
                if key == "nim" and not validasi_nim(value):
                    print(f"  [ERROR] NIM '{value}' tidak valid.")
                    return None
                self.model._storage[mhs_id][key] = value
            else:
                print(f"  [WARNING] Field '{key}' tidak dikenali, dilewati.")

        return self.model._storage[mhs_id]

    def delete(self, mhs_id):
        """
        Menghapus data mahasiswa (DELETE).

        Parameter:
            mhs_id (int): ID mahasiswa yang akan dihapus.

        Return:
            dict: Data mahasiswa yang dihapus, atau None jika gagal.
        """
        if mhs_id not in self.model._storage:
            print(f"  [ERROR] Mahasiswa dengan ID {mhs_id} tidak ditemukan.")
            return None

        data_dihapus = self.model._storage.pop(mhs_id)
        return data_dihapus

    def search_by_name(self, keyword):
        """
        Mencari mahasiswa berdasarkan nama (partial match).

        Parameter:
            keyword (str): Kata kunci pencarian.

        Return:
            list: List data mahasiswa yang cocok.
        """
        hasil = []
        for mhs in self.model._storage.values():
            if keyword.lower() in mhs["nama"].lower():
                hasil.append(mhs)
        return hasil


def demo_soal_4():
    """Demo untuk Soal 4: Package sistem_informasi (CRUD Mahasiswa)"""
    print("=" * 70)
    print(" SOAL 4: Package sistem_informasi - CRUD Mahasiswa")
    print("=" * 70)

    service = MahasiswaService()

    # --- CREATE ---
    print("\n--- CREATE: Menambahkan Mahasiswa ---")
    m1 = service.create("20210001", "Andi Pratama", "Teknik Informatika", 3.75)
    if m1:
        print(f"  Berhasil ditambahkan: {format_mahasiswa(m1)}")

    m2 = service.create("20210002", "Budi Santoso", "Sistem Informasi", 3.50)
    if m2:
        print(f"  Berhasil ditambahkan: {format_mahasiswa(m2)}")

    m3 = service.create("20210003", "Citra Dewi", "Teknik Informatika", 3.90)
    if m3:
        print(f"  Berhasil ditambahkan: {format_mahasiswa(m3)}")

    m4 = service.create("20210004", "Doni Setiawan", "Manajemen Informatika", 3.20)
    if m4:
        print(f"  Berhasil ditambahkan: {format_mahasiswa(m4)}")

    # Test duplikat NIM
    print("\n  Test duplikat NIM:")
    service.create("20210001", "Test Duplikat", "Test", 3.00)

    # Test NIM tidak valid
    print("  Test NIM tidak valid:")
    service.create("123", "Test Invalid", "Test", 3.00)

    # --- READ ---
    print("\n--- READ: Membaca Data Mahasiswa ---")
    print("  Semua mahasiswa:")
    semua_mhs = service.read()
    for mhs in semua_mhs:
        print(format_mahasiswa(mhs))

    print("\n  Mahasiswa dengan ID 2:")
    mhs2 = service.read(2)
    if mhs2:
        print(format_mahasiswa(mhs2))

    print("\n  Mahasiswa dengan ID 99 (tidak ada):")
    service.read(99)

    # --- UPDATE ---
    print("\n--- UPDATE: Memperbarui Data Mahasiswa ---")
    updated = service.update(2, nama="Budi Setiawan", ipk=3.65)
    if updated:
        print(f"  Setelah update ID 2: {format_mahasiswa(updated)}")

    # --- DELETE ---
    print("\n--- DELETE: Menghapus Data Mahasiswa ---")
    deleted = service.delete(4)
    if deleted:
        print(f"  Berhasil dihapus: {format_mahasiswa(deleted)}")

    print("\n  Data setelah penghapusan:")
    semua_mhs = service.read()
    for mhs in semua_mhs:
        print(format_mahasiswa(mhs))

    # --- SEARCH ---
    print("\n--- SEARCH: Mencari Mahasiswa ---")
    hasil = service.search_by_name("budi")
    print(f"  Pencarian 'budi': {len(hasil)} ditemukan")
    for mhs in hasil:
        print(format_mahasiswa(mhs))

    print()


# ============================================================================
# SOAL 5: REST API + Lambda + Higher-Order Functions + JSON
# ============================================================================
# Menggunakan library requests untuk mengambil data dari JSONPlaceholder API,
# kemudian menggunakan lambda dan higher-order function (map, filter, sorted)
# untuk memproses data. Hasilnya disimpan ke file JSON.
# ============================================================================

def demo_soal_5():
    """Demo untuk Soal 5: REST API + Lambda + Higher-Order Functions"""
    print("=" * 70)
    print(" SOAL 5: REST API + Lambda + Higher-Order Functions + JSON")
    print("=" * 70)

    try:
        import requests
    except ImportError:
        print("\n  [INFO] Library 'requests' tidak terinstall.")
        print("  Install dengan: pip install requests")
        print("  Menggunakan data offline sebagai alternatif...\n")
        requests = None

    # --- Ambil data dari API atau gunakan data offline ---
    if requests:
        print("\n--- Mengambil data dari JSONPlaceholder API ---")
        try:
            # Ambil data posts
            response_posts = requests.get(
                "https://jsonplaceholder.typicode.com/posts", timeout=10
            )
            posts = response_posts.json()
            print(f"  Berhasil mengambil {len(posts)} posts")

            # Ambil data users
            response_users = requests.get(
                "https://jsonplaceholder.typicode.com/users", timeout=10
            )
            users = response_users.json()
            print(f"  Berhasil mengambil {len(users)} users")

        except Exception as e:
            print(f"  [ERROR] Gagal mengambil data: {e}")
            print("  Menggunakan data offline...\n")
            requests = None

    # Data offline sebagai fallback
    if not requests:
        posts = [
            {"userId": 1, "id": 1, "title": "sunt aut facere repellat provident occaecati", "body": "quia et suscipit recusandae consequuntur"},
            {"userId": 1, "id": 2, "title": "qui est esse", "body": "est rerum tempore vitae sequi sint nihil reprehenderit dolor"},
            {"userId": 1, "id": 3, "title": "ea molestias quasi exercitationem repellat", "body": "et iusto sed quo iure voluptatem occaecati"},
            {"userId": 2, "id": 4, "title": "eum et est occaecati", "body": "ullam et saepe reiciendis voluptatem adipisci sit amet"},
            {"userId": 2, "id": 5, "title": "nesciunt quas odio", "body": "repudiandae veniam quaerat sunt sed alias aut fugiat"},
            {"userId": 3, "id": 6, "title": "dolorem eum magni eos aperiam quia", "body": "ut aspernatur corporis harum nihil quis provident sequi"},
            {"userId": 3, "id": 7, "title": "magnam facilis autem", "body": "dolore placeat quibusdam ea quo vitae magni quis"},
            {"userId": 4, "id": 8, "title": "dolorem dolore est ipsam", "body": "dignissimos aperiam dolorem qui eum facilis quibusdam"},
            {"userId": 4, "id": 9, "title": "nesciunt iure omnis dolorem tempora et accusantium", "body": "consectetur animi nesciunt iure dolore enim quia ad"},
            {"userId": 5, "id": 10, "title": "optio molestias id quia eum", "body": "quo et expedita modi cum officia vel magni doloribus"},
        ]
        users = [
            {"id": 1, "name": "Leanne Graham", "username": "Bret", "email": "Sincere@april.biz", "company": {"name": "Romaguera-Crona"}},
            {"id": 2, "name": "Ervin Howell", "username": "Antonette", "email": "Shanna@melissa.tv", "company": {"name": "Deckow-Crist"}},
            {"id": 3, "name": "Clementine Bauch", "username": "Samantha", "email": "Nathan@yesenia.net", "company": {"name": "Romaguera-Jacobson"}},
            {"id": 4, "name": "Patricia Lebsack", "username": "Karianne", "email": "Julianne@kory.org", "company": {"name": "Robel-Corkery"}},
            {"id": 5, "name": "Chelsey Dietrich", "username": "Kamren", "email": "Lucio_Hettinger@annie.ca", "company": {"name": "Keebler LLC"}},
        ]
        print(f"\n  Menggunakan {len(posts)} posts (offline)")
        print(f"  Menggunakan {len(users)} users (offline)")

    # --- Menggunakan Lambda + Higher-Order Functions ---
    print("\n--- Menggunakan Lambda & Higher-Order Functions ---")

    # 1. MAP: Menambahkan panjang title pada setiap post
    print("\n  1. MAP - Menambahkan 'title_length' pada setiap post:")
    posts_with_length = list(map(
        lambda post: {**post, "title_length": len(post["title"])},
        posts
    ))
    for p in posts_with_length[:5]:
        print(f"     ID {p['id']:>2}: title_length={p['title_length']:>3} | \"{p['title'][:40]}...\"")
    if len(posts_with_length) > 5:
        print(f"     ... dan {len(posts_with_length) - 5} post lainnya")

    # 2. FILTER: Menyaring post berdasarkan userId tertentu
    print("\n  2. FILTER - Post milik userId=1:")
    posts_user1 = list(filter(
        lambda post: post["userId"] == 1,
        posts
    ))
    for p in posts_user1:
        print(f"     ID {p['id']:>2}: \"{p['title'][:50]}\"")
    print(f"     Total: {len(posts_user1)} posts")

    # 3. FILTER: Menyaring post dengan title panjang (> 30 karakter)
    print("\n  3. FILTER - Post dengan title > 30 karakter:")
    long_title_posts = list(filter(
        lambda post: len(post["title"]) > 30,
        posts
    ))
    for p in long_title_posts[:5]:
        print(f"     ID {p['id']:>2}: (len={len(p['title']):>2}) \"{p['title'][:50]}\"")
    print(f"     Total: {len(long_title_posts)} posts")

    # 4. SORTED: Mengurutkan post berdasarkan panjang title (descending)
    print("\n  4. SORTED - Post diurutkan berdasarkan panjang title (terpanjang dulu):")
    sorted_posts = sorted(
        posts,
        key=lambda post: len(post["title"]),
        reverse=True
    )
    for p in sorted_posts[:5]:
        print(f"     ID {p['id']:>2}: (len={len(p['title']):>2}) \"{p['title'][:50]}\"")

    # 5. MAP + FILTER + SORTED: Kombinasi
    print("\n  5. KOMBINASI MAP + FILTER + SORTED:")
    print("     (Post userId=1, ditambah title_length, diurutkan ascending)")
    hasil_kombinasi = sorted(
        map(
            lambda p: {"id": p["id"], "title": p["title"], "title_length": len(p["title"])},
            filter(lambda p: p["userId"] == 1, posts)
        ),
        key=lambda p: p["title_length"]
    )
    for p in hasil_kombinasi:
        print(f"     ID {p['id']:>2}: (len={p['title_length']:>2}) \"{p['title'][:50]}\"")

    # 6. MAP: Gabungkan data user ke post
    print("\n  6. MAP - Gabungkan data user ke setiap post:")
    user_dict = {u["id"]: u["name"] for u in users}
    posts_with_user = list(map(
        lambda p: {**p, "author_name": user_dict.get(p["userId"], "Unknown")},
        posts
    ))
    for p in posts_with_user[:5]:
        print(f"     ID {p['id']:>2}: Author: {p['author_name']:<20} | \"{p['title'][:35]}...\"")

    # 7. Analisis: Hitung jumlah post per user menggunakan lambda + map
    print("\n  7. ANALISIS - Jumlah post per user:")
    user_ids = set(map(lambda p: p["userId"], posts))
    post_count_per_user = sorted(
        map(
            lambda uid: {
                "userId": uid,
                "nama": user_dict.get(uid, "Unknown"),
                "jumlah_post": len(list(filter(lambda p: p["userId"] == uid, posts)))
            },
            user_ids
        ),
        key=lambda x: x["jumlah_post"],
        reverse=True
    )
    for pc in post_count_per_user:
        print(f"     User {pc['userId']} ({pc['nama']:<20}): {pc['jumlah_post']} posts")

    # --- Simpan hasil ke file JSON ---
    print("\n--- Menyimpan Hasil ke File JSON ---")

    hasil_analisis = {
        "metadata": {
            "total_posts": len(posts),
            "total_users": len(users),
            "sumber": "JSONPlaceholder API (https://jsonplaceholder.typicode.com)"
        },
        "posts_dengan_title_length": posts_with_length,
        "posts_user_1": posts_user1,
        "posts_title_panjang": long_title_posts,
        "posts_sorted_by_title_length": [
            {"id": p["id"], "title": p["title"], "title_length": len(p["title"])}
            for p in sorted_posts
        ],
        "posts_dengan_author": posts_with_user,
        "analisis_post_per_user": post_count_per_user
    }

    # Simpan ke file JSON
    output_dir = os.path.dirname(os.path.abspath(__file__))
    output_file = os.path.join(output_dir, "hasil_analisis_api.json")

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(hasil_analisis, f, indent=4, ensure_ascii=False)

    print(f"  File berhasil disimpan: {output_file}")
    print(f"  Ukuran file: {os.path.getsize(output_file):,} bytes")

    print()


# ============================================================================
# MAIN PROGRAM
# ============================================================================

if __name__ == "__main__":
    print()
    print("*" * 70)
    print("  TUGAS PYTHON KE-6 - SEMUA SOAL".center(70))
    print("*" * 70)
    print()

    # Jalankan semua demo
    demo_soal_1()
    demo_soal_2()
    demo_soal_3()
    demo_soal_4()
    demo_soal_5()

    print("*" * 70)
    print("  SELESAI - SEMUA SOAL TELAH DIJALANKAN".center(70))
    print("*" * 70)
