# Versions for editorial review

[DIHAPUS] means deletion of the assigned passage only. Read source.md for the original and context.

## P01

### X

Untuk setiap kasus, tiga pengulangan pada model dan kondisi konteks bisnis yang sama menghasilkan tiga jawaban. Persentase PASS dihitung dengan membagi jumlah jawaban berstatus PASS dengan tiga, lalu mengalikan hasilnya dengan 100%.

### Y

Untuk satu kasus pada model dan kondisi konteks bisnis yang sama, jumlah jawaban PASS ditulis sebagai Pi, dengan i menunjukkan kasus yang dinilai. Persentasenya dihitung dari tiga jawaban hasil pengulangan.

## P02

### X

[DIHAPUS]

### Y

[DIHAPUS]

## P03

### X

Untuk membandingkan kedua kondisi pengujian, seluruh jawaban yang dihasilkan dengan konteks bisnis dibandingkan dengan seluruh jawaban yang dihasilkan tanpa konteks bisnis. Masing-masing kelompok mencakup jawaban dari kedua model. Untuk membandingkan model, jawaban Muse Spark 1.3 dari kedua kondisi digabungkan, lalu dibandingkan dengan gabungan jawaban DeepSeek v4 dari kedua kondisi yang sama.

### Y

Untuk membandingkan hasil dengan dan tanpa konteks bisnis, jawaban kedua model digabungkan pada setiap kondisi. Untuk membandingkan kedua model, jawaban dengan dan tanpa konteks bisnis digabungkan pada setiap model.

## P04

### X

Kelengkapan jawaban ikut menentukan hasil evaluasi. Nilai yang dicantumkan dalam jawaban T3-C1 yang gagal dan satu jawaban T7-C2 sesuai dengan expected result. Jawaban tersebut dinilai FAIL karena rincian golongan kendaraan pada T3-C1 dan evaluasi indikator pada T7-C2 tidak lengkap.

### Y

Kelengkapan jawaban ikut menentukan hasil evaluasi. Nilai yang dicantumkan dalam jawaban T3-C1 yang gagal dan satu jawaban T7-C2 sesuai dengan expected result. Jawaban tersebut dinilai FAIL karena rincian golongan kendaraan pada T3-C1 dan evaluasi indikator pada T7-C2 tidak lengkap.

## P05

### X

Dengan konteks bisnis, kedua model memperoleh 15/15 PASS pada setiap pengulangan. Tanpa konteks bisnis, Muse Spark 1.3 memperoleh 14/15, 13/15, dan 14/15 PASS, sedangkan DeepSeek v4 memperoleh 13/15 PASS pada masing-masing pengulangan.
Pada DeepSeek v4 tanpa konteks bisnis, kasus yang gagal berubah antarpengulangan meskipun jumlah PASS tetap sama. T3-C1 memperoleh FAIL pada ketiga pengulangan. T7-C2 memperoleh FAIL pada pengulangan pertama dan ketiga, sedangkan T7-C1 memperoleh FAIL pada pengulangan kedua. Rekap hasil per kasus dan pengulangan disajikan pada Tabel L1.2 dan Tabel L1.3 dalam Lampiran 1.

### Y

Dengan konteks bisnis, kedua model memperoleh 15/15 PASS pada setiap pengulangan. Tanpa konteks bisnis, Muse Spark 1.3 memperoleh 14/15, 13/15, dan 14/15 PASS, sedangkan DeepSeek v4 memperoleh 13/15 PASS pada masing-masing pengulangan.
Pada DeepSeek v4 tanpa konteks bisnis, kasus yang gagal berubah antarpengulangan meskipun jumlah PASS tetap sama. T3-C1 memperoleh FAIL pada ketiga pengulangan. T7-C2 memperoleh FAIL pada pengulangan pertama dan ketiga, sedangkan T7-C1 memperoleh FAIL pada pengulangan kedua. Rekap hasil per kasus dan pengulangan disajikan pada Tabel L1.2 dan Tabel L1.3 dalam Lampiran 1.

## P06

### X

Kondisi ini membuat model gagal.

### Y

Kondisi ini membuat model gagal.
