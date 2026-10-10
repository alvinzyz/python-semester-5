# ============================================================
#  diskon_biaya.py
#  Program: Kalkulator Diskon Biaya Kuliah
#  Deskripsi: Menghitung diskon SPP berdasarkan status karyawan,
#             IPK, dan ketepatan waktu pembayaran.
# ============================================================

def hitung_diskon(spp: float, anak_karyawan: bool, ipk: float, tepat_waktu: bool) -> dict:
    """
    Menghitung rincian diskon biaya kuliah.

    Returns:
        dict berisi daftar diskon yang berlaku, total persen diskon,
        potongan biaya, dan biaya final.
    """
    diskon_list = []

    # 1. Diskon anak karyawan
    if anak_karyawan:
        diskon_list.append(("Anak Karyawan", 25))

    # 2. Diskon berdasarkan IPK (hanya satu level yang berlaku)
    if ipk >= 3.8:
        diskon_list.append(("IPK >= 3.8 (Cumlaude)", 20))
    elif ipk >= 3.5:
        diskon_list.append(("IPK >= 3.5", 15))
    elif ipk >= 3.0:
        diskon_list.append(("IPK >= 3.0", 10))

    # 3. Diskon pembayaran tepat waktu
    if tepat_waktu:
        diskon_list.append(("Pembayaran Tepat Waktu", 5))

    total_persen  = sum(persen for _, persen in diskon_list)
    # Diskon tidak melebihi 100%
    total_persen  = min(total_persen, 100)
    potongan      = spp * (total_persen / 100)
    biaya_final   = spp - potongan

    return {
        "diskon_list"  : diskon_list,
        "total_persen" : total_persen,
        "potongan"     : potongan,
        "biaya_final"  : biaya_final,
    }

def tanya_ya_tidak(pertanyaan: str) -> bool:
    """Meminta input y/n dari pengguna hingga valid."""
    while True:
        jawaban = input(f"  {pertanyaan} (y/n): ").strip().lower()
        if jawaban in ("y", "n"):
            return jawaban == "y"
        print("  [!] Masukkan 'y' untuk Ya atau 'n' untuk Tidak.")

def format_rupiah(nilai: float) -> str:
    """Memformat angka menjadi string Rupiah."""
    return f"Rp {nilai:>14,.2f}"

def main():
    print("=" * 60)
    print("       KALKULATOR DISKON BIAYA KULIAH")
    print("=" * 60)
    print("  Tabel Diskon yang Tersedia:")
    print("  ─────────────────────────────────────────────")
    print("  Anak Karyawan              : 25%")
    print("  IPK >= 3.8                 : 20%")
    print("  IPK >= 3.5                 : 15%")
    print("  IPK >= 3.0                 : 10%")
    print("  Pembayaran Tepat Waktu     :  5%")
    print("  ─────────────────────────────────────────────")
    print("  *Semua diskon bersifat kumulatif (maks. 100%)")
    print("=" * 60)

    # --- Input ---
    print("\n  Masukkan Data:")
    while True:
        try:
            spp_str = input("  Biaya SPP (Rp) : ").replace(",", "").replace(".", "").strip()
            spp = float(spp_str)
            if spp > 0:
                break
            print("  [!] Biaya SPP harus lebih dari 0.")
        except ValueError:
            print("  [!] Masukkan angka yang valid.")

    anak_karyawan = tanya_ya_tidak("Apakah anak karyawan?")

    while True:
        try:
            ipk = float(input("  IPK (0.0-4.0)  : "))
            if 0.0 <= ipk <= 4.0:
                break
            print("  [!] IPK harus antara 0.0 dan 4.0.")
        except ValueError:
            print("  [!] Masukkan angka desimal yang valid.")

    tepat_waktu = tanya_ya_tidak("Bayar tepat waktu?")

    # --- Hitung ---
    hasil = hitung_diskon(spp, anak_karyawan, ipk, tepat_waktu)

    # --- Tampilkan ---
    print("\n")
    print("=" * 60)
    print("          HASIL PERHITUNGAN DISKON")
    print("=" * 60)
    print(f"  Biaya SPP Awal         : {format_rupiah(spp)}")
    print()

    if hasil["diskon_list"]:
        print("  Diskon yang Berlaku:")
        for nama_diskon, persen in hasil["diskon_list"]:
            potongan_item = spp * (persen / 100)
            print(f"    ✔ {nama_diskon:<26}: {persen:>3}%  ({format_rupiah(potongan_item)})")
    else:
        print("  Diskon yang Berlaku    : Tidak ada diskon")

    print("  " + "─" * 56)
    print(f"  Total Diskon           : {hasil['total_persen']:>3}%")
    print(f"  Total Potongan         : {format_rupiah(hasil['potongan'])}")
    print("  " + "─" * 56)
    print(f"  Biaya Final yang Dibayar: {format_rupiah(hasil['biaya_final'])}")
    print("=" * 60)

if __name__ == "__main__":
    main()
