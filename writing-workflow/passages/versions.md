# Versions for editorial review

[DIHAPUS] means deletion of the assigned passage only. Read source.md for the original and its context.

## P01

### X

Untuk setiap model dan kondisi konteks bisnis, \(P_i\) menyatakan jumlah jawaban PASS pada kasus ke-\(i\) dalam tiga pengulangan. Persentase jawaban PASS pada kasus tersebut dihitung dengan membagi \(P_i\) dengan tiga, lalu mengalikan hasilnya dengan 100%.

### Y

Untuk satu kasus pada model dan kondisi konteks bisnis yang sama, jumlah jawaban PASS ditulis sebagai Pi, dengan i menunjukkan kasus yang dinilai. Persentase jawaban PASS dari tiga pengulangan dihitung dengan membagi Pi dengan tiga, lalu mengalikan hasilnya dengan 100%.

## P02

### X

[DIHAPUS]

### Y

[DIHAPUS]

## P03

### X

Untuk membandingkan hasil dengan dan tanpa konteks bisnis, jawaban kedua model digabungkan pada setiap kondisi. Untuk membandingkan kedua model, jawaban dengan dan tanpa konteks bisnis digabungkan pada setiap model.

### Y

Untuk membandingkan hasil dengan dan tanpa konteks bisnis, jawaban kedua model digabungkan pada setiap kondisi. Untuk membandingkan kedua model, jawaban dengan dan tanpa konteks bisnis digabungkan pada setiap model.

## P04

### X

Kelengkapan jawaban ikut menentukan hasil evaluasi. Pada T3-C1, jawaban yang dinilai FAIL memuat nilai yang sesuai dengan expected result, tetapi rincian golongan kendaraannya tidak lengkap. Satu jawaban T7-C2 juga memuat nilai yang sesuai dengan expected result. Jawaban itu dinilai FAIL karena evaluasi indikatornya tidak lengkap.

### Y

Kelengkapan jawaban ikut menentukan hasil evaluasi. Pada T3-C1, nilai yang tercantum dalam jawaban yang gagal sesuai dengan *expected result*. Jawaban tersebut dinilai FAIL karena rincian golongan kendaraan tidak lengkap. Pada T7-C2, satu jawaban juga memuat nilai yang sesuai dengan *expected result*, tetapi dinilai FAIL karena evaluasi indikator tidak lengkap.

## P05

### X

Dengan konteks bisnis, kedua model memperoleh 15/15 PASS pada setiap pengulangan. Tanpa konteks bisnis, Muse Spark 1.3 memperoleh 14/15, 13/15, dan 14/15 PASS, sedangkan DeepSeek v4 memperoleh 13/15 PASS pada setiap pengulangan.

Dari dua kasus yang gagal pada setiap pengulangan DeepSeek v4 tanpa konteks bisnis, satu kasus selalu sama, yaitu T3-C1. Kasus lain yang gagal adalah T7-C2 pada pengulangan pertama dan ketiga serta T7-C1 pada pengulangan kedua. Rekap hasil per kasus dan pengulangan disajikan pada Tabel L1.2 dan Tabel L1.3 dalam Lampiran 1.

### Y

Dengan konteks bisnis, kedua model memperoleh 15/15 PASS pada setiap pengulangan. Tanpa konteks bisnis, Muse Spark 1.3 memperoleh 14/15, 13/15, dan 14/15 PASS, sedangkan DeepSeek v4 memperoleh 13/15 PASS pada masing-masing pengulangan.

Tanpa konteks bisnis, jawaban DeepSeek v4 untuk T3-C1 dinilai FAIL pada ketiga pengulangan. Jawaban lain yang dinilai FAIL berasal dari kasus T7-C2 pada pengulangan pertama dan ketiga serta dari kasus T7-C1 pada pengulangan kedua. Rekap hasil per kasus dan pengulangan disajikan pada Tabel L1.2 dan Tabel L1.3 dalam Lampiran 1.

## P06

### X

Kondisi ini membuat model gagal.

### Y

Kondisi ini membuat model gagal.
