# ============================================================
#  menu_si_mahasiswa.py
#  Program: Menu Interaktif Sistem Informasi Mahasiswa
#  Deskripsi: Menggabungkan 3 studi kasus dalam satu menu
#             interaktif dengan validasi input lengkap.
# ============================================================

# ─── Import logika dari modul lain ─────────────────────────
# (Semua logika disalin langsung agar program berdiri sendiri)

import os

# ══════════════════════════════════════════════════════════════
#  STUDI KASUS 1 — Status Mahasiswa
# ══════════════════════════════════════════════════════════════

def tentukan_status_mhs(ipk: float, sks: int) -> str:
    if ipk < 1.5:
        return "Tidak Aktif"
    elif 1.5 <= ipk < 2.0:
        return "Peringatan"
    else:
        return "Aktif" if sks >= 18 else "Peringatan"

def menu_status_mahasiswa():
    os.system("cls" if os.name == "nt" else "clear")
    print("=" * 65)
    print("          [1] CEK STATUS MAHASISWA")
    print("=" * 65)
    print("  Aturan:")
    print("  ✔ Aktif       : IPK >= 2.0 DAN SKS >= 18")
    print("  ⚠ Peringatan  : 1.5 <= IPK < 2.0  ATAU  SKS < 18")
    print("  ✘ Tidak Aktif : IPK < 1.5")
    print("=" * 65)

    while True:
        try:
            n = int(input("\n  Berapa mahasiswa yang ingin dicek? (1-20): "))
            if 1 <= n <= 20:
                break
            print("  [!] Masukkan angka antara 1 dan 20.")
        except ValueError:
            print("  [!] Masukkan angka bulat.")

    daftar = []
    for i in range(1, n + 1):
        print(f"\n  — Mahasiswa ke-{i} —")
        while True:
            nim = input("    NIM   : ").strip()
            if nim:
                break
            print("    [!] NIM tidak boleh kosong.")
        while True:
            nama = input("    Nama  : ").strip()
            if nama:
                break
            print("    [!] Nama tidak boleh kosong.")
        while True:
            try:
                ipk = float(input("    IPK   : "))
                if 0.0 <= ipk <= 4.0:
                    break
                print("    [!] IPK harus 0.0 – 4.0.")
            except ValueError:
                print("    [!] Angka tidak valid.")
        while True:
            try:
                sks = int(input("    SKS   : "))
                if 0 <= sks <= 24:
                    break
                print("    [!] SKS harus 0 – 24.")
            except ValueError:
                print("    [!] Angka tidak valid.")
        daftar.append({"nim": nim, "nama": nama, "ipk": ipk, "sks": sks})

    STATUS_ICON = {"Aktif": "✔", "Peringatan": "⚠", "Tidak Aktif": "✘"}
    rekap = {"Aktif": 0, "Peringatan": 0, "Tidak Aktif": 0}

    print("\n")
    print("=" * 70)
    print("  LAPORAN STATUS MAHASISWA")
    print("=" * 70)
    print(f"{'No':<4} {'NIM':<14} {'Nama':<22} {'IPK':<7} {'SKS':<6} {'Status'}")
    print("-" * 70)
    for i, m in enumerate(daftar, 1):
        status = tentukan_status_mhs(m["ipk"], m["sks"])
        rekap[status] += 1
        icon = STATUS_ICON[status]
        print(f"{i:<4} {m['nim']:<14} {m['nama']:<22} {m['ipk']:<7.2f} {m['sks']:<6} {icon} {status}")
    print("=" * 70)
    print(f"  Aktif: {rekap['Aktif']} | Peringatan: {rekap['Peringatan']} | Tidak Aktif: {rekap['Tidak Aktif']}")
    print("=" * 70)
    input("\n  Tekan Enter untuk kembali ke menu...")

# ══════════════════════════════════════════════════════════════
#  STUDI KASUS 2 — Hitung Diskon Biaya
# ══════════════════════════════════════════════════════════════

def hitung_diskon_biaya(spp, anak_karyawan, ipk, tepat_waktu):
    diskon_list = []
    if anak_karyawan:
        diskon_list.append(("Anak Karyawan", 25))
    if ipk >= 3.8:
        diskon_list.append(("IPK >= 3.8", 20))
    elif ipk >= 3.5:
        diskon_list.append(("IPK >= 3.5", 15))
    elif ipk >= 3.0:
        diskon_list.append(("IPK >= 3.0", 10))
    if tepat_waktu:
        diskon_list.append(("Bayar Tepat Waktu", 5))
    total_persen = min(sum(p for _, p in diskon_list), 100)
    potongan = spp * (total_persen / 100)
    return diskon_list, total_persen, potongan, spp - potongan

def tanya_yn(pesan: str) -> bool:
    while True:
        jawaban = input(f"  {pesan} (y/n): ").strip().lower()
        if jawaban in ("y", "n"):
            return jawaban == "y"
        print("  [!] Ketik 'y' atau 'n'.")

def menu_hitung_diskon():
    os.system("cls" if os.name == "nt" else "clear")
    print("=" * 55)
    print("       [2] HITUNG DISKON BIAYA KULIAH")
    print("=" * 55)
    print("  Diskon: Karyawan 25% | IPK>=3.8: 20% | IPK>=3.5: 15%")
    print("          IPK>=3.0: 10% | Tepat Waktu: 5% (kumulatif)")
    print("=" * 55)

    while True:
        try:
            spp = float(input("\n  Biaya SPP (Rp): ").replace(",", "").replace(".", ""))
            if spp > 0:
                break
            print("  [!] SPP harus > 0.")
        except ValueError:
            print("  [!] Angka tidak valid.")

    anak_kar = tanya_yn("Anak karyawan?")

    while True:
        try:
            ipk = float(input("  IPK (0.0-4.0) : "))
            if 0.0 <= ipk <= 4.0:
                break
            print("  [!] IPK harus 0.0 – 4.0.")
        except ValueError:
            print("  [!] Angka tidak valid.")

    tepat = tanya_yn("Bayar tepat waktu?")

    diskon_list, total_persen, potongan, final = hitung_diskon_biaya(spp, anak_kar, ipk, tepat)

    print("\n" + "=" * 55)
    print("  HASIL PERHITUNGAN DISKON")
    print("=" * 55)
    print(f"  SPP Awal       : Rp {spp:>12,.0f}")
    if diskon_list:
        print("  Diskon Berlaku :")
        for nama, persen in diskon_list:
            print(f"    ✔ {nama:<22}: {persen}%  (Rp {spp * persen/100:>10,.0f})")
    else:
        print("  Diskon Berlaku : Tidak ada")
    print(f"  Total Diskon   : {total_persen}%")
    print(f"  Potongan       : Rp {potongan:>12,.0f}")
    print("-" * 55)
    print(f"  Biaya Final    : Rp {final:>12,.0f}")
    print("=" * 55)
    input("\n  Tekan Enter untuk kembali ke menu...")

# ══════════════════════════════════════════════════════════════
#  STUDI KASUS 3 — Cek Peringatan Stok
# ══════════════════════════════════════════════════════════════

INVENTARIS = [
    {"kode": "BK-001", "nama": "Buku Algoritma",   "stok": 45, "stok_min": 10, "harga": 125_000},
    {"kode": "AT-002", "nama": "Pulpen Pilot",      "stok":  8, "stok_min": 20, "harga":   8_500},
    {"kode": "KT-003", "nama": "Kertas A4 (Rim)",   "stok":  3, "stok_min": 10, "harga":  55_000},
    {"kode": "AT-004", "nama": "Spidol Whiteboard", "stok":  0, "stok_min":  5, "harga":  15_000},
    {"kode": "EL-005", "nama": "Kabel HDMI",        "stok": 12, "stok_min":  5, "harga":  85_000},
    {"kode": "BK-006", "nama": "Buku Basis Data",   "stok":  2, "stok_min":  8, "harga": 110_000},
    {"kode": "AT-007", "nama": "Penggaris 30cm",    "stok": 30, "stok_min": 10, "harga":   7_000},
    {"kode": "EL-008", "nama": "Flashdisk 32GB",    "stok":  6, "stok_min": 10, "harga":  95_000},
    {"kode": "KT-009", "nama": "Amplop Coklat",     "stok":100, "stok_min": 20, "harga":   1_200},
    {"kode": "EL-010", "nama": "Mouse Wireless",    "stok":  1, "stok_min":  5, "harga": 150_000},
]

def tentukan_status_stok(stok, stok_min):
    if stok == 0:
        return "HABIS",      1, "🔴"
    elif stok <= stok_min * 0.25:
        return "RENDAH",     2, "🟠"
    elif stok <= stok_min * 0.75:
        return "PERINGATAN", 3, "🟡"
    else:
        return "AMAN",       4, "🟢"

def menu_peringatan_stok():
    os.system("cls" if os.name == "nt" else "clear")
    print("=" * 90)
    print("              [3] CEK PERINGATAN STOK INVENTARIS")
    print("=" * 90)

    data = []
    for item in INVENTARIS:
        status, prioritas, ikon = tentukan_status_stok(item["stok"], item["stok_min"])
        nilai = item["stok"] * item["harga"]
        data.append({**item, "status": status, "prioritas": prioritas, "ikon": ikon, "nilai": nilai})

    data_sorted = sorted(data, key=lambda x: x["prioritas"])
    total_nilai  = sum(d["nilai"] for d in data)
    rekap = {"AMAN": 0, "PERINGATAN": 0, "RENDAH": 0, "HABIS": 0}
    for d in data:
        rekap[d["status"]] = rekap.get(d["status"], 0) + 1

    print(f"\n{'No':<4} {'Kode':<8} {'Nama':<24} {'Stok':>5} {'Min':>5} {'Status':<14} {'Nilai Stok':>16}")
    print("-" * 90)
    for i, d in enumerate(data_sorted, 1):
        print(f"{i:<4} {d['kode']:<8} {d['nama']:<24} {d['stok']:>5} {d['stok_min']:>5} "
              f"{d['ikon']} {d['status']:<12} Rp {d['nilai']:>12,.0f}")
    print("=" * 90)
    print(f"  Total Nilai Inventaris: Rp {total_nilai:,.0f}")
    print(f"  🟢 Aman: {rekap['AMAN']} | 🟡 Peringatan: {rekap['PERINGATAN']} | "
          f"🟠 Rendah: {rekap['RENDAH']} | 🔴 Habis: {rekap['HABIS']}")
    item_restock = sum(1 for d in data if d["status"] != "AMAN")
    print(f"  Perlu Restock: {item_restock}/{len(data)} item ({item_restock/len(data)*100:.1f}%)")
    print("=" * 90)
    input("\n  Tekan Enter untuk kembali ke menu...")

# ══════════════════════════════════════════════════════════════
#  MENU UTAMA
# ══════════════════════════════════════════════════════════════

def tampilkan_menu():
    os.system("cls" if os.name == "nt" else "clear")
    print("╔" + "═" * 51 + "╗")
    print("║       SISTEM INFORMASI MAHASISWA (SIM)          ║")
    print("╠" + "═" * 51 + "╣")
    print("║                                                 ║")
    print("║   [1]  Cek Status Mahasiswa                     ║")
    print("║   [2]  Hitung Diskon Biaya Kuliah               ║")
    print("║   [3]  Cek Peringatan Stok Inventaris           ║")
    print("║                                                 ║")
    print("║   [0]  Keluar                                   ║")
    print("║                                                 ║")
    print("╚" + "═" * 51 + "╝")

def main():
    while True:
        tampilkan_menu()
        pilihan = input("\n  Pilih menu [0-3]: ").strip()

        if pilihan == "1":
            menu_status_mahasiswa()
        elif pilihan == "2":
            menu_hitung_diskon()
        elif pilihan == "3":
            menu_peringatan_stok()
        elif pilihan == "0":
            os.system("cls" if os.name == "nt" else "clear")
            print("  Terima kasih telah menggunakan SIM. Sampai jumpa!")
            break
        else:
            print("  [!] Pilihan tidak valid. Masukkan angka 0-3.")
            input("  Tekan Enter untuk melanjutkan...")

if __name__ == "__main__":
    main()
