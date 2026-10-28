# ============================================================
#  ringkasan_algoritma.py
#  Program: Ringkasan Algoritma dari Ketiga Studi Kasus
#  Deskripsi: Menghitung dan menampilkan statistik gabungan
#             dari studi kasus mahasiswa, diskon, dan stok.
# ============================================================

# ─── Data Contoh Mahasiswa ───────────────────────────────────
DATA_MAHASISWA = [
    {"nama": "Aldi Firmansyah",  "ipk": 3.80, "sks": 20},
    {"nama": "Bintang Cahaya",   "ipk": 2.10, "sks": 18},
    {"nama": "Citra Dewi",       "ipk": 1.70, "sks": 16},
    {"nama": "Dian Pratama",     "ipk": 1.40, "sks": 12},
    {"nama": "Eka Saputra",      "ipk": 3.50, "sks": 22},
    {"nama": "Fajar Nugroho",    "ipk": 2.80, "sks": 20},
    {"nama": "Gita Lestari",     "ipk": 0.90, "sks":  8},
    {"nama": "Hendra Wijaya",    "ipk": 3.20, "sks": 19},
    {"nama": "Indah Permata",    "ipk": 1.60, "sks": 14},
    {"nama": "Joko Santoso",     "ipk": 2.50, "sks": 17},
]

# ─── Data Contoh Diskon ─────────────────────────────────────
DATA_DISKON = [
    {"spp": 5_000_000, "anak_karyawan": True,  "ipk": 3.9, "tepat_waktu": True},
    {"spp": 5_000_000, "anak_karyawan": False, "ipk": 3.6, "tepat_waktu": True},
    {"spp": 5_000_000, "anak_karyawan": False, "ipk": 3.2, "tepat_waktu": False},
    {"spp": 5_000_000, "anak_karyawan": True,  "ipk": 2.8, "tepat_waktu": False},
    {"spp": 5_000_000, "anak_karyawan": False, "ipk": 2.1, "tepat_waktu": True},
    {"spp": 5_000_000, "anak_karyawan": False, "ipk": 1.5, "tepat_waktu": False},
    {"spp": 5_000_000, "anak_karyawan": True,  "ipk": 3.5, "tepat_waktu": True},
    {"spp": 5_000_000, "anak_karyawan": False, "ipk": 3.8, "tepat_waktu": False},
]

# ─── Data Inventaris ────────────────────────────────────────
DATA_INVENTARIS = [
    {"nama": "Buku Algoritma",   "stok": 45, "stok_min": 10},
    {"nama": "Pulpen Pilot",     "stok":  8, "stok_min": 20},
    {"nama": "Kertas A4 (Rim)",  "stok":  3, "stok_min": 10},
    {"nama": "Spidol Whiteboard","stok":  0, "stok_min":  5},
    {"nama": "Kabel HDMI",       "stok": 12, "stok_min":  5},
    {"nama": "Buku Basis Data",  "stok":  2, "stok_min":  8},
    {"nama": "Penggaris 30cm",   "stok": 30, "stok_min": 10},
    {"nama": "Flashdisk 32GB",   "stok":  6, "stok_min": 10},
    {"nama": "Amplop Coklat",    "stok":100, "stok_min": 20},
    {"nama": "Mouse Wireless",   "stok":  1, "stok_min":  5},
]

# ══════════════════════════════════════════════════════════════
#  FUNGSI HITUNG
# ══════════════════════════════════════════════════════════════

def hitung_status_mahasiswa(data: list) -> dict:
    """(a) Hitung persentase mahasiswa aktif vs tidak aktif."""
    rekap = {"Aktif": 0, "Peringatan": 0, "Tidak Aktif": 0}
    for m in data:
        ipk, sks = m["ipk"], m["sks"]
        if ipk < 1.5:
            rekap["Tidak Aktif"] += 1
        elif 1.5 <= ipk < 2.0:
            rekap["Peringatan"] += 1
        else:
            if sks >= 18:
                rekap["Aktif"] += 1
            else:
                rekap["Peringatan"] += 1

    total = len(data)
    return {
        "rekap": rekap,
        "total": total,
        "persen_aktif"      : rekap["Aktif"]       / total * 100,
        "persen_peringatan" : rekap["Peringatan"]  / total * 100,
        "persen_tidak_aktif": rekap["Tidak Aktif"] / total * 100,
    }

def hitung_rata_diskon(data: list) -> dict:
    """(b) Hitung rata-rata diskon yang diberikan."""
    total_diskon = []
    for d in data:
        persen = 0
        if d["anak_karyawan"]:
            persen += 25
        ipk = d["ipk"]
        if ipk >= 3.8:
            persen += 20
        elif ipk >= 3.5:
            persen += 15
        elif ipk >= 3.0:
            persen += 10
        if d["tepat_waktu"]:
            persen += 5
        total_diskon.append(min(persen, 100))

    rata = sum(total_diskon) / len(total_diskon) if total_diskon else 0
    return {
        "detail"     : total_diskon,
        "rata_rata"  : rata,
        "maks_diskon": max(total_diskon) if total_diskon else 0,
        "min_diskon" : min(total_diskon) if total_diskon else 0,
    }

def hitung_restock(data: list) -> dict:
    """(c) Hitung persentase item yang perlu restock."""
    perlu_restock = 0
    rekap_status  = {"AMAN": 0, "PERINGATAN": 0, "RENDAH": 0, "HABIS": 0}

    for item in data:
        stok, stok_min = item["stok"], item["stok_min"]
        if stok == 0:
            status = "HABIS"
        elif stok <= stok_min * 0.25:
            status = "RENDAH"
        elif stok <= stok_min * 0.75:
            status = "PERINGATAN"
        else:
            status = "AMAN"

        rekap_status[status] += 1
        if status != "AMAN":
            perlu_restock += 1

    total = len(data)
    return {
        "rekap"            : rekap_status,
        "total"            : total,
        "perlu_restock"    : perlu_restock,
        "persen_restock"   : perlu_restock / total * 100,
        "persen_aman"      : rekap_status["AMAN"] / total * 100,
    }

# ══════════════════════════════════════════════════════════════
#  TAMPILKAN TABEL
# ══════════════════════════════════════════════════════════════

def cetak_baris_tabel(kolom_kiri, kolom_tengah, kolom_kanan, lebar=(40, 18, 18)):
    l1, l2, l3 = lebar
    print(f"  │ {str(kolom_kiri):<{l1}} │ {str(kolom_tengah):>{l2}} │ {str(kolom_kanan):>{l3}} │")

def cetak_separator(lebar=(40, 18, 18), char="─"):
    l1, l2, l3 = lebar
    print(f"  ├─{'─'*l1}─┼─{'─'*l2}─┼─{'─'*l3}─┤")

def cetak_header(lebar=(40, 18, 18)):
    l1, l2, l3 = lebar
    print(f"  ┌─{'─'*l1}─┬─{'─'*l2}─┬─{'─'*l3}─┐")

def cetak_footer(lebar=(40, 18, 18)):
    l1, l2, l3 = lebar
    print(f"  └─{'─'*l1}─┴─{'─'*l2}─┴─{'─'*l3}─┘")

def tampilkan_ringkasan(mhs_hasil, diskon_hasil, restock_hasil):
    print("\n")
    print("═" * 85)
    print("                     RINGKASAN ALGORITMA — TIGA STUDI KASUS")
    print("═" * 85)

    # ─── Tabel (a): Status Mahasiswa ───────────────────────────
    print("\n  (a) PERSENTASE STATUS MAHASISWA")
    cetak_header()
    cetak_baris_tabel("Kategori", "Jumlah", "Persentase")
    cetak_separator()
    cetak_baris_tabel("✔  Aktif",       f"{mhs_hasil['rekap']['Aktif']} mhs",       f"{mhs_hasil['persen_aktif']:.1f}%")
    cetak_baris_tabel("⚠  Peringatan",  f"{mhs_hasil['rekap']['Peringatan']} mhs",  f"{mhs_hasil['persen_peringatan']:.1f}%")
    cetak_baris_tabel("✘  Tidak Aktif", f"{mhs_hasil['rekap']['Tidak Aktif']} mhs", f"{mhs_hasil['persen_tidak_aktif']:.1f}%")
    cetak_separator()
    cetak_baris_tabel("TOTAL",          f"{mhs_hasil['total']} mhs",                "100.0%")
    cetak_footer()

    # ─── Tabel (b): Rata-rata Diskon ───────────────────────────
    print("\n  (b) STATISTIK DISKON BIAYA KULIAH")
    cetak_header()
    cetak_baris_tabel("Metrik", "Nilai", "Keterangan")
    cetak_separator()
    cetak_baris_tabel("Rata-rata Diskon",   f"{diskon_hasil['rata_rata']:.1f}%",   "Dari seluruh sampel")
    cetak_baris_tabel("Diskon Tertinggi",   f"{diskon_hasil['maks_diskon']}%",     "Penerima terbaik")
    cetak_baris_tabel("Diskon Terendah",    f"{diskon_hasil['min_diskon']}%",      "Penerima terkecil")
    cetak_baris_tabel("Jumlah Data",        f"{len(diskon_hasil['detail'])} data", "")
    cetak_separator()
    cetak_baris_tabel("Detail per data",
                      ", ".join(f"{p}%" for p in diskon_hasil["detail"][:5]),
                      "5 data pertama")
    cetak_footer()

    # ─── Tabel (c): Restock Inventaris ─────────────────────────
    print("\n  (c) PERSENTASE ITEM YANG PERLU RESTOCK")
    cetak_header()
    cetak_baris_tabel("Status Stok", "Jumlah Item", "Persentase")
    cetak_separator()
    cetak_baris_tabel("🟢 Aman",       f"{restock_hasil['rekap']['AMAN']} item",       f"{restock_hasil['persen_aman']:.1f}%")
    cetak_baris_tabel("🟡 Peringatan", f"{restock_hasil['rekap']['PERINGATAN']} item", f"{restock_hasil['rekap']['PERINGATAN']/restock_hasil['total']*100:.1f}%")
    cetak_baris_tabel("🟠 Rendah",     f"{restock_hasil['rekap']['RENDAH']} item",     f"{restock_hasil['rekap']['RENDAH']/restock_hasil['total']*100:.1f}%")
    cetak_baris_tabel("🔴 Habis",      f"{restock_hasil['rekap']['HABIS']} item",      f"{restock_hasil['rekap']['HABIS']/restock_hasil['total']*100:.1f}%")
    cetak_separator()
    cetak_baris_tabel("Total Perlu Restock",
                      f"{restock_hasil['perlu_restock']} item",
                      f"{restock_hasil['persen_restock']:.1f}%")
    cetak_baris_tabel("TOTAL INVENTARIS",
                      f"{restock_hasil['total']} item",
                      "100.0%")
    cetak_footer()

    print("\n" + "═" * 85)
    print("  KESIMPULAN EKSEKUTIF:")
    print("═" * 85)
    print(f"  • {mhs_hasil['persen_aktif']:.1f}% mahasiswa berstatus Aktif, "
          f"{mhs_hasil['persen_tidak_aktif']:.1f}% Tidak Aktif.")
    print(f"  • Rata-rata diskon yang diberikan adalah {diskon_hasil['rata_rata']:.1f}% "
          f"(maks {diskon_hasil['maks_diskon']}%, min {diskon_hasil['min_diskon']}%).")
    print(f"  • {restock_hasil['persen_restock']:.1f}% item inventaris "
          f"({restock_hasil['perlu_restock']} dari {restock_hasil['total']}) perlu segera di-restock.")
    print("═" * 85)

def main():
    print("=" * 85)
    print("             RINGKASAN ALGORITMA — TIGA STUDI KASUS")
    print("=" * 85)
    print("  Menggunakan data contoh yang telah ditentukan...")

    mhs_hasil     = hitung_status_mahasiswa(DATA_MAHASISWA)
    diskon_hasil  = hitung_rata_diskon(DATA_DISKON)
    restock_hasil = hitung_restock(DATA_INVENTARIS)

    tampilkan_ringkasan(mhs_hasil, diskon_hasil, restock_hasil)

if __name__ == "__main__":
    main()
