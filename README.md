# Kalkulator Desktop PyQt6 - UTS Pemrograman Desktop

Aplikasi kalkulator berbasis GUI desktop yang dibangun menggunakan Python dan PyQt6 sesuai spesifikasi tugas UTS Pemrograman Desktop.

---

## Checklist Fitur (Sesuai Ketentuan PPT UTS)

### Sudah Dibuat
- [x] Menggunakan framework PyQt6.
- [x] Struktur proyek terpisah secara modular (folder assets, logic, ui).
- [x] File entri utama aplikasi (main.py).
- [x] Window utama (QMainWindow) dengan judul "Kalkulator" dan icon aplikasi.
- [x] Layar display hasil (ui/display.py) menggunakan QLineEdit dengan status read-only dan alignment teks rata kanan.
- [x] Susunan tombol kalkulator dengan QGridLayout (ui/keypad.py).
- [x] Tombol angka sudah disesuaikan hanya memakai digit NIM kelompok (0, 1, 4, 5, 8, 9) tanpa angka yang tidak diperlukan.
- [x] Tombol operasi matematika pada keypad (+, -, *, /, =, C, akar kuadrat, x kuadrat, 1/x).
- [x] Pewarnaan tombol (tombol C merah, tombol = biru, tombol angka gelap).
- [x] Tampilan tombol rapat dan padat (sudah diatur dengan spacing 8px di keypad dan margin minimal di display).

### Perlu Dibuat dan Dibenahi
- [ ] Implementasi QTabWidget:
  - Tab 1: Layout Grid (QGridLayout).
  - Tab 2: Kombinasi Layout (QVBoxLayout dan QHBoxLayout).
- [ ] Kombinasi Layout VBox dan HBox (Tab 2):
  - Menyusun tombol kalkulator menggunakan kombinasi baris QHBoxLayout di dalam QVBoxLayout.
  - Menampilkan panel informasi NIM dan daftar angka yang digunakan.
- [ ] Menu Bar dan Shortcut:
  - Menu operasi matematika pada menu bar (Tambah, Kurang, Kali, Bagi, Kuadrat, Akar, Invers, Clear).
  - Shortcut akselerator pada menu menggunakan tanda & (contoh: &Operasi, &Tambah, &Kurang, &Kali, &Bagi, &File, &Keluar).
- [ ] Logika Perhitungan (logic/calculator.py):
  - Mengimplementasikan proses perhitungan aritmatika (+, -, *, /).
  - Mengimplementasikan operasi fungsi khusus (akar kuadrat, kuadrat, invers 1/x).
  - Fungsi Clear All (C) dan evaluasi ekspresi sama dengan (=).
  - Penanganan error pembagian dengan nol dan format salah.
- [ ] Menghubungkan Signal dan Slot dari klik tombol mouse ke logika dan layar display.

---

## Struktur Folder dan File

```text
UTS/
|-- assets/
|   `-- icons/
|       `-- calculator.png    # File gambar ikon aplikasi
|-- logic/
|   `-- calculator.py         # Modul logika dan komputasi perhitungan matematika
|-- ref/
|   |-- ChatGPT Image ...png  # Referensi rancangan tata letak antarmuka
|   |-- Gemini_Generated...jpg# Referensi visual kalkulator
|   `-- image.png             # Referensi visual kalkulator standar
|-- ui/
|   |-- display.py            # Komponen widget layar penampil hasil (QLineEdit)
|   |-- keypad.py             # Komponen widget papan tombol berbasis QGridLayout
|   `-- main_window.py        # Komponen jendela utama (QMainWindow, menu, dan tab)
|-- .gitignore                # Konfigurasi file yang diabaikan oleh Git
|-- main.py                   # File entri utama eksekusi program
|-- requirements.txt          # Daftar dependensi library (PyQt6==6.11.0)
|-- setup.ps1                 # Skrip setup virtual environment otomatis
`-- README.md                 # Dokumentasi proyek dan checklist tugas
```

### Penjelasan Fungsi Folder

- **assets/**: Folder penyimpanan file aset statis aplikasi seperti file gambar dan icon.
- **assets/icons/**: Subfolder khusus menyimpan icon aplikasi (`calculator.png`) yang ditampilkan pada title bar jendela dan taskbar.
- **logic/**: Folder khusus untuk menempatkan kode logika bisnis/perhitungan matematika secara terpisah dari tampilan antarmuka (UI).
- **ui/**: Folder yang berisi seluruh file komponen tampilan antarmuka grafis (PyQt6 widgets).
- **ref/**: Folder tempat menyimpan file referensi desain antarmuka dan ketentuan layout tugas UTS.

### Penjelasan Fungsi Setiap File

- **main.py**:
  File utama yang dieksekusi pertama kali. Berfungsi menginisialisasi `QApplication`, memanggil instance `MainWindow`, menampilkan GUI ke layar, dan menjalankan event loop aplikasi.

- **ui/main_window.py**:
  Mengatur kerangka jendela utama (`QMainWindow`), properti window (judul, ukuran, icon), menu bar dengan shortcut `&`, serta menampung widget utama (seperti `QTabWidget` untuk tab Grid dan tab Kombinasi Layout).

- **ui/display.py**:
  Mengatur tampilan layar kalkulator dengan class `Display` (`QWidget`). Berisi `QLineEdit` berstatus read-only (agar input murni dari klik mouse), alignment rata kanan, font ukuran 48pt, dan tanpa border.

- **ui/keypad.py**:
  Mengatur tata letak papan tombol kalkulator dengan class `Keypad` (`QWidget`) menggunakan `QGridLayout`. Mengatur posisi koordinat baris/kolom tombol angka, operator aritmatika, tombol C, dan tombol sama dengan (=).

- **logic/calculator.py**:
  Modul komputasi backend kalkulator untuk memproses perhitungan angka, menjalankan operasi matematika (+, -, *, /, akar, kuadrat, invers), menyimpan status operasi, dan mengembalikan hasil hitung ke display.

- **requirements.txt**:
  Menentukan versi pustaka Python yang wajib digunakan, yaitu `PyQt6==6.11.0`.

- **setup.ps1**:
  Skrip otomasi PowerShell untuk membuat environment `.venv`, melakukan upgrade pip, dan memasang seluruh dependencies dari `requirements.txt`.

- **.gitignore**:
  Menyaring file yang tidak perlu diunggah ke repositori, seperti folder `.venv`, cache `__pycache__`, dan file temporer.

---

## Penjelasan Alur Kode (Codingan)

1. **Inisialisasi Aplikasi (main.py)**:
   Program dimulai dari fungsi `main()`. Membuat objek `app = QApplication(sys.argv)`, kemudian menginstansiasi `window = MainWindow()`, menampilkan window dengan `window.show()`, dan mengunci eksekusi pada `sys.exit(app.exec())`.

2. **Penyusunan Jendela Utama (ui/main_window.py)**:
   Class `MainWindow` mengonfigurasi judul "Kalkulator", memuat ikon dari `assets/icons/calculator.png`, mengatur ukuran awal 500x600 piksel, membuat menu bar dasar, lalu menggabungkan widget `Display` dan `Keypad` ke dalam `QVBoxLayout` pada central widget.

3. **Komponen Layar (ui/display.py)**:
   Class `Display` menyusun `QLineEdit` di dalam `QVBoxLayout`. Teks default bernilai "0", diset read-only agar pengguna hanya memasukkan input melalui klik kursor mouse, diset format teks rata kanan, dan diberi styling CSS transparan tanpa border.

4. **Komponen Tombol (ui/keypad.py)**:
   Class `Keypad` menggunakan `QGridLayout` dengan spasi antar tombol. Tombol-tombol disimpan dalam daftar tuple `(teks, baris, kolom)`. Tombol C diberi warna latar merah `#e74c3c`, tombol angka diberi warna `#363636`, dan tombol `=` diletakkan pada baris 3 kolom 2 dengan ukuran membentang 2 kolom berwarna biru `#2878d4`.

5. **Modul Logika (logic/calculator.py)**:
   File ini disiapkan untuk menerima masukan angka dan operator dari interaksi UI, melakukan validasi perhitungan aritmatika dan fungsi matematika, serta mengembalikan string hasil ke layar display.

---

## Cara Menjalankan

1. Setup environment dan install dependensi:
   ```powershell
   .\setup.ps1
   ```
2. Jalankan aplikasi:
   ```powershell
   python main.py
   ```
