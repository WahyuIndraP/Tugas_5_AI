# Sistem Pakar Untuk Mendiagnosa Gangguan WiFi

## Identitas

Nama : Wahyu Indra Purnama
NIM  : F1D02410099

---

## Topik dan Cara Menjalankan Program

### Topik

Topik yang digunakan pada tugas ini adalah 
## Sistem Pakar untuk Mendiagnosa Gangguan WiFi

Sistem pakar ini digunakan untuk memberikan saran awal mengenai kemungkinan gangguan pada koneksi WiFi berdasarkan fakta atau kondisi yang diberikan oleh pengguna. Sistem menggunakan metode Forward Chaining untuk mencocokkan fakta dengan aturan yang tersedia.

### Bahasa dan Versi

- Bahasa pemrograman: Python
- Versi Python: [VERSI PYTHON, contoh: Python 3.12]
- Format pengetahuan: JSON

### Cara Menjalankan Program

Pastikan Python sudah terpasang pada komputer.

Clone repository:

```bash
git clone [URL_REPOSITORY_GITHUB]
```


## 3. Daftar Sumber dan Tabel Aturan


Sistem pakar ini menggunakan sumber dari dokumentasi resmi yang membahas masalah koneksi WiFi dan Internet.

| ID | Judul | Penerbit | URL | Tanggal Akses |
|---|---|---|---|---|
| S1 | Memperbaiki masalah koneksi Wi-Fi di Windows | Microsoft Support | https://support.microsoft.com/id-id/windows/experience/connectivity-networking/fix-wi-fi-connection-issues-in-windows | 10 November 2026 |
| S2 | Memperbaiki masalah koneksi internet pada perangkat Android | Google Support | https://support.google.com/android/answer/2651367?hl=id | 10 November 2026 |

### Tabel Aturan

Aturan sistem pakar dibuat berdasarkan informasi dari sumber yang telah dicantumkan. Setiap aturan memiliki sumber agar dapat diketahui dasar informasi yang digunakan.

| ID | IF / Jika | Mode | THEN / Maka | Sumber |
|---|---|---|---|---|
| R1 | perangkat tersambung ke WiFi; tidak ada akses internet | dan | koneksi internet bermasalah | S1 |
| R2 | perangkat tidak bisa mengakses internet; perangkat lain bisa terhubung ke WiFi | dan | masalah kemungkinan berasal dari perangkat | S1 |
| R3 | indikator WiFi tidak muncul; bar sinyal WiFi kosong | atau | perangkat berada di luar jangkauan WiFi | S2 |
| R4 | perangkat berada di luar jangkauan WiFi; perangkat jauh dari router | dan | sinyal WiFi lemah | S2 |
| R5 | koneksi internet bermasalah; router belum direstart | dan | perlu restart router | S1 |

### Hubungan Antaraturan

Sistem menggunakan hasil aturan sebelumnya sebagai fakta baru. Contohnya, R1 menghasilkan koneksi internet bermasalah. Hasil tersebut kemudian digunakan sebagai salah satu kondisi pada R5.

```text
Fakta awal
    ↓
R1
    ↓
koneksi internet bermasalah
    ↓
R5
    ↓
perlu restart router
```

Dengan demikian, R5 menggunakan hasil dari R1 sehingga memenuhi ketentuan bahwa minimal satu aturan menggunakan hasil aturan lain.

---

## 4. Metode yang Dipilih

### Forward Chaining (FC)

Metode yang digunakan pada sistem pakar ini adalah Forward Chaining.

Forward Chaining dipilih karena proses diagnosis dimulai dari fakta atau kondisi yang diberikan oleh pengguna. Sistem kemudian mencocokkan fakta tersebut dengan bagian jika pada setiap aturan. Jika kondisi suatu aturan terpenuhi, bagian maka menjadi kesimpulan baru. Kesimpulan tersebut dapat digunakan kembali sebagai fakta untuk menjalankan aturan berikutnya.

Contoh prosesnya:

```text
Fakta awal:
- perangkat tersambung ke WiFi
- tidak ada akses internet
- router belum direstart

        ↓

R1 terpenuhi

        ↓

koneksi internet bermasalah

        ↓

R5 terpenuhi

        ↓

perlu restart router
```

Karena sistem menggunakan Forward Chaining berbasis aturan, tidak terdapat perhitungan numerik atau rumus seperti pada algoritma yang menggunakan nilai angka. Oleh karena itu, bagian perhitungan tangan dengan angka tidak diperlukan.

---

## 5. Tiga Kasus Uji dan Screenshot

Pengujian dilakukan dengan tiga kasus untuk memastikan aturan dapat menghasilkan kesimpulan yang sesuai. Salah satu kasus merupakan kasus yang tidak memenuhi aturan sehingga sistem tidak menghasilkan kesimpulan.

### Kasus Uji 1 — Koneksi Internet Bermasalah

Fakta yang diberikan:

```text
perangkat tersambung ke WiFi
tidak ada akses internet
router belum direstart
```

Aturan yang terpenuhi:

```text
R1
R5
```

Hasil yang diharapkan:

```text
koneksi internet bermasalah
perlu restart router
```

Screenshot hasil program:

![Screenshot Kasus Uji 1](Screenshot/Kasus%201.png)

---

### Kasus Uji 2 — Kemungkinan Masalah pada Perangkat

Fakta yang diberikan:

```text
perangkat tidak bisa mengakses internet
perangkat lain bisa terhubung ke WiFi
```

Aturan yang terpenuhi:

```text
R2
```

Hasil yang diharapkan:

```text
masalah kemungkinan berasal dari perangkat
```

Screenshot hasil program:

![Screenshot Kasus Uji 2](Screenshot/Kasus%202.png)

---

### Kasus Uji 3 — Tidak Ada Kesimpulan

Fakta yang diberikan:

```text
perangkat jauh dari router
```

Fakta tersebut tidak memenuhi kondisi pada aturan yang tersedia.

Hasil yang diharapkan:

```text
tidak ditemukan kesimpulan berdasarkan aturan yang tersedia
```

Screenshot hasil program:

![Screenshot Kasus Uji 3](Screenshot/Kasus%203.png)

---

## 4. Batas Keberlakuan

Sistem pakar ini menggunakan pengetahuan yang diperoleh dari dokumentasi resmi Microsoft Support dan Google Support mengenai pemecahan masalah koneksi WiFi dan Internet. Sistem digunakan untuk memberikan saran awal berdasarkan kondisi perangkat, koneksi WiFi, jangkauan sinyal, dan router yang telah dimasukkan ke dalam aturan. Sistem tidak mencakup seluruh kemungkinan gangguan jaringan dan tidak menggantikan pemeriksaan teknis secara langsung. Oleh karena itu, hasil yang diberikan merupakan hanyalah saran awal dan bukan keputusan akhir.


## 5. Penggunaan Alat Bantu AI

Membantu untuk mencari judul dan menjelaskan serta memberikan contoh seperti apa forward chaning itu dalam kode