# ============================================================
# TUGAS PYTHON KE-5
# Gabungan Soal 1 - 5 dalam satu program
# ============================================================

import string
import os

# ============================================================
# SOAL 1: Analisis Kalimat
# ============================================================

def hitung_jumlah_kata(kalimat):
    """Menghitung jumlah kata dalam kalimat."""
    kata_list = kalimat.split()
    return len(kata_list)

def hitung_jumlah_karakter(kalimat):
    """Menghitung jumlah karakter dalam kalimat (termasuk spasi)."""
    return len(kalimat)

def cari_kata_terpanjang(kalimat):
    """Mencari kata terpanjang dalam kalimat."""
    kata_list = kalimat.split()
    kata_terpanjang = ""
    for kata in kata_list:
        if len(kata) > len(kata_terpanjang):
            kata_terpanjang = kata
    return kata_terpanjang

def konversi_title_case(kalimat):
    """Mengubah setiap kata menjadi title case (huruf pertama kapital)."""
    return kalimat.title()

def soal_1():
    print("\n" + "=" * 55)
    print("  SOAL 1: ANALISIS KALIMAT")
    print("=" * 55)

    kalimat = input("\nMasukkan sebuah kalimat: ")

    if not kalimat.strip():
        print("Kalimat tidak boleh kosong!")
        return

    print("\n--- Hasil Analisis ---")

    # (a) Jumlah kata
    jumlah_kata = hitung_jumlah_kata(kalimat)
    print(f"(a) Jumlah kata          : {jumlah_kata}")

    # (b) Jumlah karakter
    jumlah_karakter = hitung_jumlah_karakter(kalimat)
    jumlah_tanpa_spasi = len(kalimat.replace(" ", ""))
    print(f"(b) Jumlah karakter      : {jumlah_karakter} (dengan spasi)")
    print(f"    Jumlah karakter      : {jumlah_tanpa_spasi} (tanpa spasi)")

    # (c) Kata terpanjang
    kata_terpanjang = cari_kata_terpanjang(kalimat)
    print(f"(c) Kata terpanjang      : '{kata_terpanjang}' ({len(kata_terpanjang)} karakter)")

    # (d) Title case
    kalimat_title = konversi_title_case(kalimat)
    print(f"(d) Kalimat (Title Case) : {kalimat_title}")


# ============================================================
# SOAL 2: Analisis Nilai Mahasiswa
# ============================================================

def hitung_rata_rata(nilai_list):
    """Menghitung rata-rata dari list nilai."""
    total = sum(nilai_list)
    rata_rata = total / len(nilai_list)
    return rata_rata

def cari_tertinggi_terendah(nilai_list):
    """Mencari nilai tertinggi dan terendah."""
    tertinggi = max(nilai_list)
    terendah = min(nilai_list)
    return tertinggi, terendah

def tentukan_kategori(nilai):
    """Menentukan kategori berdasarkan nilai.
    A = 80-100
    B = 70-79
    C = 60-69
    D = 50-59
    E = 0-49
    """
    if nilai >= 80:
        return "A"
    elif nilai >= 70:
        return "B"
    elif nilai >= 60:
        return "C"
    elif nilai >= 50:
        return "D"
    else:
        return "E"

def kelompokkan_kategori(nilai_list):
    """Mengelompokkan setiap nilai ke dalam kategori."""
    hasil = []
    for nilai in nilai_list:
        kategori = tentukan_kategori(nilai)
        hasil.append((nilai, kategori))
    return hasil

def hitung_frekuensi_kategori(nilai_list):
    """Menghitung frekuensi setiap kategori menggunakan dictionary."""
    frekuensi = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}
    for nilai in nilai_list:
        kategori = tentukan_kategori(nilai)
        frekuensi[kategori] += 1
    return frekuensi

def soal_2():
    print("\n" + "=" * 55)
    print("  SOAL 2: ANALISIS NILAI MAHASISWA")
    print("=" * 55)

    input_nilai = input("\nMasukkan nilai mahasiswa (pisahkan dengan spasi): ")
    nilai_list = list(map(float, input_nilai.split()))

    if not nilai_list:
        print("List nilai tidak boleh kosong!")
        return

    print(f"\nData nilai: {nilai_list}")
    print(f"Jumlah mahasiswa: {len(nilai_list)}")
    print("\n--- Hasil Analisis ---")

    # (a) Rata-rata
    rata_rata = hitung_rata_rata(nilai_list)
    print(f"(a) Rata-rata nilai      : {rata_rata:.2f}")

    # (b) Nilai tertinggi dan terendah
    tertinggi, terendah = cari_tertinggi_terendah(nilai_list)
    print(f"(b) Nilai tertinggi      : {tertinggi}")
    print(f"    Nilai terendah       : {terendah}")

    # (c) Kategori setiap nilai
    print(f"\n(c) Kategori setiap nilai:")
    print(f"    {'Nilai':<10} {'Kategori':<10}")
    print(f"    {'-'*20}")
    kategori_list = kelompokkan_kategori(nilai_list)
    for nilai, kategori in kategori_list:
        print(f"    {nilai:<10} {kategori:<10}")

    # (d) Frekuensi kategori
    print(f"\n(d) Frekuensi setiap kategori:")
    frekuensi = hitung_frekuensi_kategori(nilai_list)
    keterangan = {
        "A": "Sangat Baik (80-100)",
        "B": "Baik (70-79)",
        "C": "Cukup (60-69)",
        "D": "Kurang (50-59)",
        "E": "Sangat Kurang (0-49)"
    }
    print(f"    {'Kategori':<10}| {'Frekuensi':<10}| Keterangan")
    print(f"    {'-'*42}")
    for kategori in ["A", "B", "C", "D", "E"]:
        jumlah = frekuensi[kategori]
        ket = keterangan[kategori]
        bar = "#" * jumlah
        print(f"    {kategori:<10}| {jumlah:<10}| {ket} {bar}")


# ============================================================
# SOAL 3: Operasi Set - Beasiswa Mahasiswa
# ============================================================

def mahasiswa_kedua_beasiswa(set_a, set_b):
    """Mencari mahasiswa yang menerima kedua beasiswa (irisan/intersection)."""
    return set_a & set_b

def hanya_beasiswa_a(set_a, set_b):
    """Mencari mahasiswa yang hanya menerima beasiswa A (selisih/difference)."""
    return set_a - set_b

def beasiswa_b_tidak_a(set_a, set_b):
    """Mencari mahasiswa yang menerima beasiswa B tapi tidak A."""
    return set_b - set_a

def semua_mahasiswa_unik(set_a, set_b):
    """Mencari semua mahasiswa unik yang menerima beasiswa (gabungan/union)."""
    return set_a | set_b

def soal_3():
    print("\n" + "=" * 55)
    print("  SOAL 3: OPERASI SET - BEASISWA MAHASISWA")
    print("=" * 55)

    # Data contoh penerima beasiswa
    beasiswa_a = ["MHS001", "MHS002", "MHS003", "MHS004", "MHS005", "MHS007"]
    beasiswa_b = ["MHS002", "MHS004", "MHS006", "MHS007", "MHS008", "MHS009"]

    print(f"\nPenerima Beasiswa A: {beasiswa_a}")
    print(f"Penerima Beasiswa B: {beasiswa_b}")

    # Konversi ke set
    set_a = set(beasiswa_a)
    set_b = set(beasiswa_b)

    print("\n--- Hasil Operasi Set ---")

    # (a) Intersection
    kedua = mahasiswa_kedua_beasiswa(set_a, set_b)
    print(f"\n(a) Menerima KEDUA beasiswa (A & B / intersection):")
    for mhs in sorted(kedua):
        print(f"    - {mhs}")
    print(f"    Jumlah: {len(kedua)} mahasiswa")

    # (b) Hanya beasiswa A
    hanya_a = hanya_beasiswa_a(set_a, set_b)
    print(f"\n(b) HANYA menerima Beasiswa A (A - B / difference):")
    for mhs in sorted(hanya_a):
        print(f"    - {mhs}")
    print(f"    Jumlah: {len(hanya_a)} mahasiswa")

    # (c) Beasiswa B tapi tidak A
    b_tidak_a = beasiswa_b_tidak_a(set_a, set_b)
    print(f"\n(c) Menerima Beasiswa B tapi TIDAK A (B - A / difference):")
    for mhs in sorted(b_tidak_a):
        print(f"    - {mhs}")
    print(f"    Jumlah: {len(b_tidak_a)} mahasiswa")

    # (d) Semua mahasiswa unik
    semua_unik = semua_mahasiswa_unik(set_a, set_b)
    print(f"\n(d) SEMUA mahasiswa unik penerima beasiswa (A | B / union):")
    for mhs in sorted(semua_unik):
        print(f"    - {mhs}")
    print(f"    Jumlah: {len(semua_unik)} mahasiswa")


# ============================================================
# SOAL 4: Dictionary Inventaris Toko
# ============================================================

def tampilkan_inventaris(inventaris):
    """Menampilkan seluruh data inventaris dalam format tabel."""
    if not inventaris:
        print("    Inventaris kosong.")
        return
    print(f"    {'No':<4} {'Nama Barang':<20} {'Harga (Rp)':<15} {'Stok':<8} {'Subtotal (Rp)':<15}")
    print(f"    {'-'*62}")
    no = 1
    for nama, (harga, stok) in inventaris.items():
        subtotal = harga * stok
        print(f"    {no:<4} {nama:<20} {harga:<15,.0f} {stok:<8} {subtotal:<15,.0f}")
        no += 1

def tambah_barang(inventaris, nama, harga, stok):
    """(a) Menambah barang baru ke inventaris."""
    if nama in inventaris:
        print(f"    ! Barang '{nama}' sudah ada di inventaris!")
        return False
    inventaris[nama] = (harga, stok)
    print(f"    + Barang '{nama}' berhasil ditambahkan (Harga: Rp{harga:,.0f}, Stok: {stok})")
    return True

def update_stok(inventaris, nama, jumlah_tambah):
    """(b) Mengupdate stok barang yang sudah ada."""
    if nama not in inventaris:
        print(f"    ! Barang '{nama}' tidak ditemukan di inventaris!")
        return False
    harga, stok_lama = inventaris[nama]
    stok_baru = stok_lama + jumlah_tambah
    if stok_baru < 0:
        print(f"    ! Stok tidak boleh negatif! Stok saat ini: {stok_lama}")
        return False
    inventaris[nama] = (harga, stok_baru)
    print(f"    ~ Stok '{nama}' diupdate: {stok_lama} -> {stok_baru} (perubahan: {jumlah_tambah:+d})")
    return True

def cari_barang_rentang_harga(inventaris, harga_min, harga_max):
    """(c) Mencari barang dengan harga dalam rentang tertentu."""
    hasil = {}
    for nama, (harga, stok) in inventaris.items():
        if harga_min <= harga <= harga_max:
            hasil[nama] = (harga, stok)
    return hasil

def hitung_total_nilai_inventaris(inventaris):
    """(d) Menghitung total nilai inventaris (harga x stok untuk semua barang)."""
    total = 0
    for nama, (harga, stok) in inventaris.items():
        total += harga * stok
    return total

def soal_4():
    print("\n" + "=" * 65)
    print("  SOAL 4: DICTIONARY INVENTARIS TOKO")
    print("=" * 65)

    # Inisialisasi data inventaris awal
    inventaris = {
        "Beras 5kg":        (65000, 50),
        "Minyak Goreng 1L": (18000, 30),
        "Gula Pasir 1kg":   (14000, 45),
        "Telur 1kg":        (28000, 25),
        "Mie Instan":       (3500, 100),
        "Kopi Sachet":      (2000, 200),
        "Sabun Mandi":      (5000, 60),
        "Susu UHT 1L":      (16000, 35),
    }

    print("\nData Inventaris Awal:")
    tampilkan_inventaris(inventaris)

    # (a) Menambah barang baru
    print("\n--- (a) Menambah Barang Baru ---")
    tambah_barang(inventaris, "Roti Tawar", 15000, 20)
    tambah_barang(inventaris, "Air Mineral 1.5L", 5000, 80)
    tambah_barang(inventaris, "Beras 5kg", 65000, 10)  # duplikat, harusnya gagal

    # (b) Mengupdate stok
    print("\n--- (b) Mengupdate Stok ---")
    update_stok(inventaris, "Beras 5kg", 20)        # tambah 20
    update_stok(inventaris, "Mie Instan", -30)       # kurangi 30
    update_stok(inventaris, "Susu UHT 1L", 15)      # tambah 15
    update_stok(inventaris, "Snack Coklat", 10)      # barang tidak ada

    # (c) Mencari barang dengan harga dalam rentang tertentu
    print("\n--- (c) Mencari Barang dalam Rentang Harga ---")
    harga_min = 5000
    harga_max = 20000
    print(f"    Rentang harga: Rp{harga_min:,.0f} - Rp{harga_max:,.0f}")
    hasil_cari = cari_barang_rentang_harga(inventaris, harga_min, harga_max)
    if hasil_cari:
        print(f"    Ditemukan {len(hasil_cari)} barang:")
        for nama, (harga, stok) in hasil_cari.items():
            print(f"      - {nama}: Rp{harga:,.0f} (Stok: {stok})")
    else:
        print("    Tidak ada barang dalam rentang harga tersebut.")

    # (d) Menghitung total nilai inventaris
    print("\n--- (d) Total Nilai Inventaris ---")
    total = hitung_total_nilai_inventaris(inventaris)
    print(f"    Total nilai inventaris: Rp{total:,.0f}")

    # Tampilkan inventaris akhir
    print("\nData Inventaris Akhir:")
    tampilkan_inventaris(inventaris)


# ============================================================
# SOAL 5: Analisis Teks dari File
# ============================================================

def baca_file(nama_file):
    """Membaca teks dari file dan mengembalikan sebagai string."""
    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            teks = file.read()
        return teks
    except FileNotFoundError:
        print(f"    ! File '{nama_file}' tidak ditemukan!")
        return None

def bersihkan_teks(teks):
    """Membersihkan teks: ubah ke huruf kecil dan hapus tanda baca."""
    teks_lower = teks.lower()
    teks_bersih = ""
    for char in teks_lower:
        if char not in string.punctuation:
            teks_bersih += char
        else:
            teks_bersih += " "
    return teks_bersih

def hitung_frekuensi_kata(teks):
    """(a) Menghitung frekuensi setiap kata menggunakan dictionary."""
    kata_list = teks.split()  # list
    frekuensi = {}            # dict
    for kata in kata_list:
        if kata in frekuensi:
            frekuensi[kata] += 1
        else:
            frekuensi[kata] = 1
    return frekuensi, kata_list

def kata_paling_sering(frekuensi, n=10):
    """(b) Menampilkan n kata paling sering muncul."""
    kata_terurut = sorted(frekuensi.items(), key=lambda x: x[1], reverse=True)
    return kata_terurut[:n]

def cari_hapax_legomena(frekuensi):
    """(c) Mengidentifikasi kata yang hanya muncul sekali (hapax legomena)."""
    hapax = set()  # menggunakan set
    for kata, jumlah in frekuensi.items():
        if jumlah == 1:
            hapax.add(kata)
    return hapax

def hitung_type_token_ratio(frekuensi, total_kata):
    """(d) Menghitung rasio kata unik terhadap total kata (type-token ratio)."""
    kata_unik = len(frekuensi)  # jumlah kata unik (types)
    ratio = kata_unik / total_kata if total_kata > 0 else 0
    return kata_unik, total_kata, ratio

def soal_5():
    print("\n" + "=" * 60)
    print("  SOAL 5: ANALISIS TEKS DARI FILE")
    print("=" * 60)

    # Cari file sample_text.txt di direktori yang sama dengan script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    nama_file = os.path.join(script_dir, "sample_text.txt")

    print(f"\nMembaca file: 'sample_text.txt'...")

    teks = baca_file(nama_file)
    if teks is None:
        return

    print(f"    File berhasil dibaca ({len(teks)} karakter)")

    # Bersihkan teks
    teks_bersih = bersihkan_teks(teks)

    # (a) Hitung frekuensi setiap kata
    print("\n--- (a) Frekuensi Setiap Kata ---")
    frekuensi, kata_list = hitung_frekuensi_kata(teks_bersih)
    print(f"    Total kata dalam teks   : {len(kata_list)}")
    print(f"    Jumlah kata unik        : {len(frekuensi)}")
    print(f"\n    Daftar frekuensi kata (semua):")
    for kata in sorted(frekuensi.keys()):
        jumlah = frekuensi[kata]
        bar = "#" * jumlah
        print(f"      {kata:<20} : {jumlah:>3}x {bar}")

    # (b) 10 kata paling sering muncul
    print("\n--- (b) 10 Kata Paling Sering Muncul ---")
    top_10 = kata_paling_sering(frekuensi, 10)
    print(f"    {'No':<4} {'Kata':<20} {'Frekuensi':<10}")
    print(f"    {'-'*34}")
    for i, (kata, jumlah) in enumerate(top_10, 1):
        bar = "#" * jumlah
        print(f"    {i:<4} {kata:<20} {jumlah:<10} {bar}")

    # (c) Hapax legomena
    print("\n--- (c) Hapax Legomena (Kata Muncul 1 Kali) ---")
    hapax = cari_hapax_legomena(frekuensi)
    print(f"    Jumlah hapax legomena: {len(hapax)} kata")
    print(f"    Daftar hapax legomena:")
    for i, kata in enumerate(sorted(hapax), 1):
        print(f"      {i:>3}. {kata}")

    # (d) Type-Token Ratio
    print("\n--- (d) Type-Token Ratio (TTR) ---")
    kata_unik, total_kata, ttr = hitung_type_token_ratio(frekuensi, len(kata_list))
    print(f"    Jumlah kata unik (types)  : {kata_unik}")
    print(f"    Total kata (tokens)       : {total_kata}")
    print(f"    Type-Token Ratio (TTR)    : {ttr:.4f} ({ttr*100:.2f}%)")
    if ttr > 0.7:
        print(f"    Interpretasi: Variasi kosa kata TINGGI")
    elif ttr > 0.4:
        print(f"    Interpretasi: Variasi kosa kata SEDANG")
    else:
        print(f"    Interpretasi: Variasi kosa kata RENDAH (banyak pengulangan)")


# ============================================================
# MENU UTAMA
# ============================================================
def main():
    while True:
        print("\n" + "=" * 55)
        print("      TUGAS PYTHON KE-5 - MENU UTAMA")
        print("=" * 55)
        print("  [1] Analisis Kalimat")
        print("  [2] Analisis Nilai Mahasiswa")
        print("  [3] Operasi Set - Beasiswa Mahasiswa")
        print("  [4] Dictionary Inventaris Toko")
        print("  [5] Analisis Teks dari File")
        print("  [0] Keluar")
        print("=" * 55)

        pilihan = input("Pilih soal (0-5): ").strip()

        if pilihan == "1":
            soal_1()
        elif pilihan == "2":
            soal_2()
        elif pilihan == "3":
            soal_3()
        elif pilihan == "4":
            soal_4()
        elif pilihan == "5":
            soal_5()
        elif pilihan == "0":
            print("\nTerima kasih! Program selesai.")
            break
        else:
            print("\nPilihan tidak valid! Masukkan angka 0-5.")

        input("\nTekan Enter untuk kembali ke menu...")

if __name__ == "__main__":
    main()
