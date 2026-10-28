# ============================================================
#  validasi_data.py
#  Program: Validasi Data Mahasiswa
#  Deskripsi: Fungsi validasi NIM, IPK, SKS, dan Semester
#             yang mengembalikan list error jika data tidak valid.
# ============================================================

import re
from datetime import date

# ─── Konstanta ───────────────────────────────────────────────
TAHUN_MIN  = 2000
TAHUN_MAX  = 2037
IPK_MIN    = 0.0
IPK_MAX    = 4.0
SKS_MIN    = 0
SKS_MAX    = 24
SEM_MIN    = 1
SEM_MAX    = 14

# ══════════════════════════════════════════════════════════════
#  FUNGSI VALIDASI
# ══════════════════════════════════════════════════════════════

def validasi_nim(nim: str) -> list[str]:
    """
    Memvalidasi NIM mahasiswa.

    Aturan:
    - Harus tepat 10 digit angka
    - 4 digit pertama adalah tahun masuk (2000–2037)

    Returns:
        List pesan error (kosong jika valid).
    """
    errors = []

    if not nim:
        errors.append("NIM tidak boleh kosong.")
        return errors

    if not re.fullmatch(r"\d{10}", nim):
        errors.append(f"NIM harus tepat 10 digit angka (saat ini: '{nim}' = {len(nim)} karakter).")
        return errors  # tidak perlu cek tahun jika format salah

    tahun = int(nim[:4])
    if not (TAHUN_MIN <= tahun <= TAHUN_MAX):
        errors.append(
            f"Tahun pada NIM ({tahun}) harus antara {TAHUN_MIN} dan {TAHUN_MAX}."
        )

    return errors


def validasi_ipk(ipk_str: str) -> list[str]:
    """
    Memvalidasi IPK mahasiswa.

    Aturan:
    - Harus berupa angka desimal
    - Rentang 0.0 – 4.0

    Returns:
        List pesan error (kosong jika valid).
    """
    errors = []

    if not ipk_str:
        errors.append("IPK tidak boleh kosong.")
        return errors

    try:
        ipk = float(ipk_str)
    except ValueError:
        errors.append(f"IPK harus berupa angka desimal (contoh: 3.75), bukan '{ipk_str}'.")
        return errors

    if not (IPK_MIN <= ipk <= IPK_MAX):
        errors.append(f"IPK ({ipk}) harus antara {IPK_MIN} dan {IPK_MAX}.")

    return errors


def validasi_sks(sks_str: str) -> list[str]:
    """
    Memvalidasi jumlah SKS yang diambil.

    Aturan:
    - Harus berupa angka bulat
    - Rentang 0 – 24

    Returns:
        List pesan error (kosong jika valid).
    """
    errors = []

    if not sks_str:
        errors.append("SKS tidak boleh kosong.")
        return errors

    try:
        sks = int(sks_str)
    except ValueError:
        errors.append(f"SKS harus berupa angka bulat, bukan '{sks_str}'.")
        return errors

    if not (SKS_MIN <= sks <= SKS_MAX):
        errors.append(f"SKS ({sks}) harus antara {SKS_MIN} dan {SKS_MAX}.")

    return errors


def validasi_semester(sem_str: str) -> list[str]:
    """
    Memvalidasi semester mahasiswa.

    Aturan:
    - Harus berupa angka bulat
    - Rentang 1 – 14

    Returns:
        List pesan error (kosong jika valid).
    """
    errors = []

    if not sem_str:
        errors.append("Semester tidak boleh kosong.")
        return errors

    try:
        sem = int(sem_str)
    except ValueError:
        errors.append(f"Semester harus berupa angka bulat, bukan '{sem_str}'.")
        return errors

    if not (SEM_MIN <= sem <= SEM_MAX):
        errors.append(f"Semester ({sem}) harus antara {SEM_MIN} dan {SEM_MAX}.")

    return errors


def validasi_mahasiswa(nim: str, ipk_str: str, sks_str: str, sem_str: str) -> list[str]:
    """
    Menggabungkan seluruh validasi data mahasiswa.

    Returns:
        List semua pesan error (kosong jika semua data valid).
    """
    errors = []
    errors.extend(validasi_nim(nim))
    errors.extend(validasi_ipk(ipk_str))
    errors.extend(validasi_sks(sks_str))
    errors.extend(validasi_semester(sem_str))
    return errors

# ══════════════════════════════════════════════════════════════
#  PROGRAM UTAMA
# ══════════════════════════════════════════════════════════════

def tampilkan_aturan():
    print("=" * 65)
    print("           VALIDASI DATA MAHASISWA")
    print("=" * 65)
    print("  Aturan Validasi:")
    print(f"  • NIM      : 10 digit angka, tahun {TAHUN_MIN}–{TAHUN_MAX}")
    print(f"  • IPK      : {IPK_MIN} – {IPK_MAX} (angka desimal)")
    print(f"  • SKS      : {SKS_MIN} – {SKS_MAX} (angka bulat)")
    print(f"  • Semester : {SEM_MIN} – {SEM_MAX} (angka bulat)")
    print("=" * 65)

def main():
    tampilkan_aturan()

    print("\n  Masukkan data mahasiswa (kosongkan untuk menguji validasi):")
    nim      = input("  NIM         : ").strip()
    nama     = input("  Nama        : ").strip()
    ipk_str  = input("  IPK         : ").strip()
    sks_str  = input("  SKS         : ").strip()
    sem_str  = input("  Semester    : ").strip()

    errors = validasi_mahasiswa(nim, ipk_str, sks_str, sem_str)

    print("\n" + "=" * 65)
    print("  HASIL VALIDASI")
    print("=" * 65)

    # Tampilkan data yang diinput
    print("  Data yang Dimasukkan:")
    print(f"    NIM         : {nim      or '(kosong)'}")
    print(f"    Nama        : {nama     or '(kosong)'}")
    print(f"    IPK         : {ipk_str  or '(kosong)'}")
    print(f"    SKS         : {sks_str  or '(kosong)'}")
    print(f"    Semester    : {sem_str  or '(kosong)'}")
    print()

    if not errors:
        print("  ✅ Status   : VALID — Semua data mahasiswa sudah benar!")
    else:
        print(f"  ❌ Status   : TIDAK VALID — Ditemukan {len(errors)} kesalahan:")
        for i, err in enumerate(errors, 1):
            print(f"    {i}. {err}")

    print("=" * 65)

    # Demo mode: uji beberapa skenario secara otomatis
    lanjut = input("\n  Jalankan demo validasi otomatis? (y/n): ").strip().lower()
    if lanjut == "y":
        demo_kasus = [
            ("Valid",       "20231001001", "3.75", "18", "3"),
            ("NIM pendek",  "202310010",   "3.75", "18", "3"),
            ("IPK terlalu tinggi", "20231001002", "4.5", "20", "4"),
            ("SKS negatif", "20231001003", "2.50", "-1",  "5"),
            ("Sem > 14",    "20231001004", "3.10", "20", "15"),
            ("Tahun lama",  "19991001005", "3.10", "20",  "6"),
            ("Semua salah", "abc",          "xyz",  "99", "99"),
        ]

        print("\n" + "=" * 65)
        print("  DEMO VALIDASI OTOMATIS")
        print("=" * 65)
        for label, nim_d, ipk_d, sks_d, sem_d in demo_kasus:
            errs = validasi_mahasiswa(nim_d, ipk_d, sks_d, sem_d)
            status = "✅ VALID" if not errs else f"❌ {len(errs)} error"
            print(f"\n  [{label}]  NIM={nim_d}, IPK={ipk_d}, SKS={sks_d}, Sem={sem_d}")
            print(f"    → {status}")
            for e in errs:
                print(f"       • {e}")
        print("=" * 65)

if __name__ == "__main__":
    main()
