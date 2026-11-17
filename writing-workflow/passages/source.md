# Bagian naskah

Sunting hanya teks pada setiap bagian. Konteks merupakan bahan baca, bukan teks pengganti. Pertahankan identitas bagian.

## P01

Konteks: Bagian metode menjelaskan penyajian hasil per kasus. Setiap kasus dijalankan tiga kali pada setiap model, dengan dan tanpa konteks bisnis.

Teks:

Untuk satu kasus pada model dan kondisi konteks bisnis yang sama, jumlah jawaban PASS ditulis sebagai Pi, dengan i menunjukkan kasus yang dinilai. Persentasenya dihitung dari tiga jawaban hasil pengulangan.

## P02

Konteks: Paragraf sebelumnya: Konteks bisnis diberikan dalam bentuk skill business-context, yang terdiri atas SKILL.md dan enam dokumen referensi dalam folder references. Tabel 3.7 merangkum isi setiap dokumen dan fungsinya bagi agen. Bagian ini menjelaskan dokumen konteks bisnis. Perbedaan akses dengan dan tanpa konteks bisnis sudah dijelaskan pada rancangan pengujian.

Teks:

Pada kondisi dengan konteks bisnis, ketujuh dokumen tersebut tersedia untuk dibaca agen. Pada kondisi tanpa konteks bisnis, agen tidak memperoleh akses ke dokumen tersebut.

## P03

Konteks: Bagian analisis data menjelaskan ringkasan hasil menurut ketersediaan konteks bisnis dan menurut model. Masing-masing model menghasilkan jumlah jawaban yang sama pada kedua kondisi. Tidak ada tabel hasil atau implementasi analisis tambahan dalam paket ini.

Teks:

Untuk membandingkan hasil dengan dan tanpa konteks bisnis, jawaban kedua model digabungkan pada setiap kondisi. Untuk membandingkan kedua model, jawaban dengan dan tanpa konteks bisnis digabungkan pada setiap model.

## P04

Konteks: Bagian pembahasan ketepatan jawaban. expected result adalah jawaban yang menjadi dasar penilaian PASS atau FAIL. T3-C1 dan T7-C2 adalah identitas kasus yang telah diperkenalkan sebelumnya.

Teks:

Kelengkapan jawaban ikut menentukan hasil evaluasi. Nilai yang dicantumkan dalam jawaban T3-C1 yang gagal dan satu jawaban T7-C2 sesuai dengan expected result. Jawaban tersebut dinilai FAIL karena rincian golongan kendaraan pada T3-C1 dan evaluasi indikator pada T7-C2 tidak lengkap.

## P05

Konteks: Bagian hasil pengulangan. Tiap model mengerjakan 15 kasus pada setiap pengulangan. T3-C1, T7-C1, dan T7-C2 adalah identitas kasus yang telah diperkenalkan sebelumnya. Penamaan model mengikuti teks sumber.

Teks:

Dengan konteks bisnis, kedua model memperoleh 15/15 PASS pada setiap pengulangan. Tanpa konteks bisnis, Muse Spark 1.3 memperoleh 14/15, 13/15, dan 14/15 PASS, sedangkan DeepSeek v4 memperoleh 13/15 PASS pada masing-masing pengulangan.
Pada DeepSeek v4 tanpa konteks bisnis, kasus yang gagal berubah antarpengulangan meskipun jumlah PASS tetap sama. T3-C1 memperoleh FAIL pada ketiga pengulangan. T7-C2 memperoleh FAIL pada pengulangan pertama dan ketiga, sedangkan T7-C1 memperoleh FAIL pada pengulangan kedua. Rekap hasil per kasus dan pengulangan disajikan pada Tabel L1.2 dan Tabel L1.3 dalam Lampiran 1.

## P06

Konteks: Cuplikan pembahasan yang terlepas dari paragraf sebelumnya. Catatan pengujian tidak tersedia dalam paket ini.

Teks:

Kondisi ini membuat model gagal.
