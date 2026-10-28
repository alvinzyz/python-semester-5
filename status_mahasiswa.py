# ============================================================
#  status_mahasiswa.py
#  Program: Laporan Status Mahasiswa
#  Deskripsi: Menerima data 5 mahasiswa dan menampilkan status
#             berdasarkan IPK dan SKS.
# ============================================================

def tentukan_status(ipk: float, sks: int) -> str:
    """Menentukan status mahasiswa berdasarkan IPK dan SKS."""
    if ipk < 1.5:
        return "Tidak Aktif"
    elif 1.5 <= ipk < 2.0:
        return "Peringatan"
    else:  # ipk >= 2.0
        if sks >= 18:
            return "Aktif"
        else:
            return "Peringatan"  # IPK oke tapi SKS kurang

def input_mahasiswa(nomor: int) -> dict:
    """Menerima input data satu mahasiswa dari pengguna."""
    print(f"\n{'─'*40}")
    print(f"  Data Mahasiswa ke-{nomor}")
    print(f"{'─'*40}")

    while True:
        nim = input("  NIM           : ").strip()
        if nim:
            break
        print("  [!] NIM tidak boleh kosong.")

    while True:
        nama = input("  Nama          : ").strip()
        if nama:
            break
        print("  [!] Nama tidak boleh kosong.")

    while True:
        try:
            ipk = float(input("  IPK (0.0-4.0) : "))
            if 0.0 <= ipk <= 4.0:
                break
            print("  [!] IPK harus antara 0.0 dan 4.0.")
        except ValueError:
            print("  [!] Masukkan angka desimal yang valid.")

    while True:
        try:
            sks = int(input("  SKS (0-24)    : "))
            if 0 <= sks <= 24:
                break
            print("  [!] SKS harus antara 0 dan 24.")
        except ValueError:
            print("  [!] Masukkan angka bulat yang valid.")

    return {"nim": nim, "nama": nama, "ipk": ipk, "sks": sks}

def tampilkan_laporan(daftar_mahasiswa: list) -> None:
    """Menampilkan laporan status seluruh mahasiswa."""
    STATUS_ICON = {
        "Aktif"      : "✔",
        "Peringatan" : "⚠",
        "Tidak Aktif": "✘",
    }

    print("\n")
    print("=" * 75)
    print("                   LAPORAN STATUS MAHASISWA")
    print("=" * 75)
    print(f"{'No':<4} {'NIM':<14} {'Nama':<22} {'IPK':<7} {'SKS':<6} {'Status':<14}")
    print("-" * 75)

    rekap = {"Aktif": 0, "Peringatan": 0, "Tidak Aktif": 0}

    for i, mhs in enumerate(daftar_mahasiswa, start=1):
        status = tentukan_status(mhs["ipk"], mhs["sks"])
        icon   = STATUS_ICON.get(status, " ")
        rekap[status] += 1
        print(
            f"{i:<4} {mhs['nim']:<14} {mhs['nama']:<22} "
            f"{mhs['ipk']:<7.2f} {mhs['sks']:<6} {icon} {status}"
        )

    print("=" * 75)
    print("\n  RINGKASAN:")
    print(f"  {'Aktif'      :<14}: {rekap['Aktif']} mahasiswa")
    print(f"  {'Peringatan' :<14}: {rekap['Peringatan']} mahasiswa")
    print(f"  {'Tidak Aktif':<14}: {rekap['Tidak Aktif']} mahasiswa")
    print("=" * 75)

def main():
    print("=" * 75)
    print("          SISTEM INFORMASI STATUS MAHASISWA")
    print("=" * 75)
    print("  Aturan Status:")
    print("  ✔ Aktif       : IPK >= 2.0 DAN SKS >= 18")
    print("  ⚠ Peringatan  : 1.5 <= IPK < 2.0  ATAU  IPK >= 2.0 dan SKS < 18")
    print("  ✘ Tidak Aktif : IPK < 1.5")
    print("=" * 75)

    JUMLAH_MAHASISWA = 5
    daftar_mahasiswa = []

    for i in range(1, JUMLAH_MAHASISWA + 1):
        data = input_mahasiswa(i)
        daftar_mahasiswa.append(data)

    tampilkan_laporan(daftar_mahasiswa)

if __name__ == "__main__":
    main()
