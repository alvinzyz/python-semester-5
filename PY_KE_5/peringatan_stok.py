# ============================================================
#  peringatan_stok.py
#  Program: Sistem Peringatan Stok Inventaris
#  Deskripsi: Mengevaluasi status stok item, menampilkan laporan
#             lengkap dengan prioritas, total nilai, dan statistik.
# ============================================================

# ─── Data Inventaris ─────────────────────────────────────────
INVENTARIS = [
    {"kode": "BK-001", "nama": "Buku Algoritma",      "stok": 45,  "stok_min": 10, "harga": 125_000},
    {"kode": "AT-002", "nama": "Pulpen Pilot",         "stok": 8,   "stok_min": 20, "harga":   8_500},
    {"kode": "KT-003", "nama": "Kertas A4 (Rim)",      "stok": 3,   "stok_min": 10, "harga":  55_000},
    {"kode": "AT-004", "nama": "Spidol Whiteboard",    "stok": 0,   "stok_min": 5,  "harga":  15_000},
    {"kode": "EL-005", "nama": "Kabel HDMI",           "stok": 12,  "stok_min": 5,  "harga":  85_000},
    {"kode": "BK-006", "nama": "Buku Basis Data",      "stok": 2,   "stok_min": 8,  "harga": 110_000},
    {"kode": "AT-007", "nama": "Penggaris 30cm",        "stok": 30,  "stok_min": 10, "harga":   7_000},
    {"kode": "EL-008", "nama": "Flashdisk 32GB",       "stok": 6,   "stok_min": 10, "harga":  95_000},
    {"kode": "KT-009", "nama": "Amplop Coklat",        "stok": 100, "stok_min": 20, "harga":   1_200},
    {"kode": "EL-010", "nama": "Mouse Wireless",       "stok": 1,   "stok_min": 5,  "harga": 150_000},
]

# ─── Konstanta Batas Stok ────────────────────────────────────
BATAS_RENDAH_PERSEN   = 0.25   # stok <= 25% dari stok_min  → Rendah
BATAS_PERINGATAN_PERSEN = 0.75 # stok <= 75% dari stok_min  → Peringatan

def tentukan_status_stok(stok: int, stok_min: int) -> tuple[str, int, str]:
    """
    Menentukan status, prioritas, dan ikon stok item.

    Returns:
        (status, prioritas, ikon)
        Prioritas: 1 (kritis) → 4 (aman), digunakan untuk sorting.
    """
    if stok == 0:
        return "HABIS",      1, "🔴"
    elif stok <= stok_min * BATAS_RENDAH_PERSEN:
        return "RENDAH",     2, "🟠"
    elif stok <= stok_min * BATAS_PERINGATAN_PERSEN:
        return "PERINGATAN", 3, "🟡"
    elif stok >= stok_min:
        return "AMAN",       4, "🟢"
    else:
        return "PERINGATAN", 3, "🟡"

def evaluasi_inventaris(inventaris: list) -> list:
    """Menambahkan field status, prioritas, ikon, dan nilai ke setiap item."""
    hasil = []
    for item in inventaris:
        status, prioritas, ikon = tentukan_status_stok(item["stok"], item["stok_min"])
        nilai = item["stok"] * item["harga"]
        hasil.append({**item, "status": status, "prioritas": prioritas, "ikon": ikon, "nilai": nilai})
    return hasil

def format_rupiah(nilai: float) -> str:
    return f"Rp {nilai:>15,.0f}"

def tampilkan_laporan(data: list) -> None:
    """Menampilkan laporan inventaris diurutkan berdasarkan prioritas."""
    data_sorted = sorted(data, key=lambda x: x["prioritas"])

    print("\n")
    print("=" * 95)
    print("                         LAPORAN PERINGATAN STOK INVENTARIS")
    print("=" * 95)
    print(f"{'No':<4} {'Kode':<8} {'Nama Item':<24} {'Stok':>6} {'Min':>6} {'Harga':>14} {'Nilai Stok':>17} {'Status':<14}")
    print("-" * 95)

    for i, item in enumerate(data_sorted, start=1):
        print(
            f"{i:<4} {item['kode']:<8} {item['nama']:<24} "
            f"{item['stok']:>6} {item['stok_min']:>6} "
            f"Rp {item['harga']:>10,.0f} "
            f"Rp {item['nilai']:>13,.0f} "
            f"{item['ikon']} {item['status']}"
        )

    print("=" * 95)

def tampilkan_statistik(data: list) -> None:
    """Menampilkan ringkasan statistik inventaris."""
    total_item   = len(data)
    total_nilai  = sum(d["nilai"] for d in data)

    rekap = {"AMAN": 0, "PERINGATAN": 0, "RENDAH": 0, "HABIS": 0}
    for d in data:
        rekap[d["status"]] = rekap.get(d["status"], 0) + 1

    item_kritis  = [d for d in data if d["status"] in ("RENDAH", "HABIS")]
    item_restock = [d for d in data if d["status"] != "AMAN"]

    print("\n  RINGKASAN STATISTIK:")
    print("  " + "─" * 50)
    print(f"  Total Item Inventaris : {total_item}")
    print(f"  Total Nilai Inventaris: {format_rupiah(total_nilai)}")
    print()
    print(f"  🟢 Aman               : {rekap['AMAN']:>2} item")
    print(f"  🟡 Peringatan         : {rekap['PERINGATAN']:>2} item")
    print(f"  🟠 Rendah             : {rekap['RENDAH']:>2} item")
    print(f"  🔴 Habis              : {rekap['HABIS']:>2} item")
    print()

    if item_kritis:
        print("  ⚠  ITEM PERLU SEGERA DITANGANI:")
        for item in sorted(item_kritis, key=lambda x: x["prioritas"]):
            print(f"     {item['ikon']} [{item['kode']}] {item['nama']} — Stok: {item['stok']}")

    print(f"\n  Persentase Item Perlu Restock : "
          f"{len(item_restock)/total_item*100:.1f}% ({len(item_restock)} dari {total_item} item)")
    print("=" * 95)

def main():
    print("=" * 95)
    print("              SISTEM PERINGATAN STOK INVENTARIS")
    print("=" * 95)
    print("  Keterangan Status:")
    print("  🟢 AMAN       : Stok >= stok minimum")
    print("  🟡 PERINGATAN : Stok 25% - 75% dari stok minimum")
    print("  🟠 RENDAH     : Stok <= 25% dari stok minimum")
    print("  🔴 HABIS      : Stok = 0")
    print("=" * 95)

    data = evaluasi_inventaris(INVENTARIS)
    tampilkan_laporan(data)
    tampilkan_statistik(data)

if __name__ == "__main__":
    main()
