# Catatan peninjauan P01–P06

## P01 — Perjelas perhitungan persentase PASS

**P01-1 · Keterbacaan.** “Persentasenya dihitung dari tiga jawaban hasil pengulangan.” Kata “Persentasenya” mengharuskan pembaca kembali ke definisi Pi untuk mengenali apa yang dipersentasekan. Frasa “dihitung dari tiga jawaban” hanya menyatakan berapa jawaban yang tersedia.

**Syarat perbaikan.** Pembaca dapat menghitung persentase dengan membagi jumlah jawaban berstatus PASS (Pi) dengan tiga, lalu mengalikannya dengan 100%. Pertahankan arti i sebagai penanda kasus serta batas perhitungannya. Ketiga jawaban berasal dari pengulangan kasus yang sama pada model dan kondisi konteks bisnis yang sama.

## P02 — Hilangkan pengulangan aturan akses

**P02-1 · Keterbacaan dan penempatan.** “Pada kondisi dengan konteks bisnis, ketujuh dokumen tersebut tersedia untuk dibaca agen. Pada kondisi tanpa konteks bisnis, agen tidak memperoleh akses ke dokumen tersebut.” Menurut keterangan konteks, “Perbedaan akses dengan dan tanpa konteks bisnis sudah dijelaskan pada rancangan pengujian.” Paragraf sebelumnya juga sudah memperkenalkan SKILL.md dan enam dokumen referensi serta mengarahkan pembaca ke Tabel 3.7. Kedua kalimat mengulang aturan akses di bagian yang membahas isi dokumen.

**Syarat perbaikan.** Kedua kalimat dapat dihapus. Uraian sebelumnya tetap memperkenalkan ketujuh dokumen dan fungsi masing-masing melalui Tabel 3.7. Perbedaan hak akses tetap dijelaskan pada rancangan pengujian. Keterangan bahwa dokumen dapat dibaca hanya menyatakan ketersediaannya. Keterangan itu tidak membuktikan agen membaca semua dokumen.

## P03 — Pertahankan kedua cara penggabungan jawaban

**P03-1 · Tidak perlu perubahan.** “Untuk membandingkan hasil dengan dan tanpa konteks bisnis, jawaban kedua model digabungkan pada setiap kondisi. Untuk membandingkan kedua model, jawaban dengan dan tanpa konteks bisnis digabungkan pada setiap model.” Susunan yang sejajar membantu pembaca mengikuti perubahan dasar pengelompokan. Pada perbandingan kondisi, satu kelompok memuat jawaban kedua model. Pada perbandingan model, satu kelompok memuat jawaban dari kedua kondisi.

**Syarat jika redaksi diubah.** Pembaca tetap dapat menentukan jawaban mana yang masuk ke setiap kelompok untuk masing-masing perbandingan. Pertahankan kata kerja yang menyatakan penggabungan jawaban. Membandingkan model secara terpisah di setiap kondisi akan mengubah prosedur. Cuplikan ini cukup untuk meninjau penjelasannya. Pelaksanaan analisis tidak dapat diperiksa dari bahan yang diberikan.

## P04 — Hubungkan alasan FAIL dengan jawaban pada tiap kasus

**P04-1 · Keterbacaan.** “Nilai yang dicantumkan dalam jawaban T3-C1 yang gagal dan satu jawaban T7-C2 sesuai dengan expected result.” Pembaca harus menunggu kalimat berikutnya, “Jawaban tersebut dinilai FAIL karena rincian golongan kendaraan pada T3-C1 dan evaluasi indikator pada T7-C2 tidak lengkap”, untuk memastikan bahwa satu jawaban T7-C2 itu juga dinilai FAIL. Penyebutan kedua kode secara berpasangan dua kali membuat pembaca harus mencocokkan tiap kekurangan dengan kasusnya.

**Syarat perbaikan.** Hubungan antara nilai, kelengkapan, dan penilaian harus dapat diikuti untuk masing-masing kasus. Nilai yang tercantum sesuai dengan expected result. Pada jawaban T3-C1 yang dinilai FAIL, rincian golongan kendaraan tidak lengkap. Pada satu jawaban T7-C2 yang dinilai FAIL, evaluasi indikator tidak lengkap. Pertahankan pembatas “satu” pada T7-C2 dan istilah expected result. Cuplikan ini tidak menetapkan jumlah jawaban T3-C1 yang dimaksud.

## P05 — Bedakan kasus yang selalu gagal dari kasus yang bergantian gagal

**P05-1 · Ketepatan makna.** “Pada DeepSeek v4 tanpa konteks bisnis, kasus yang gagal berubah antarpengulangan meskipun jumlah PASS tetap sama.” Pernyataan ini dapat memberi kesan bahwa kedua kasus yang gagal selalu berganti, padahal “T3-C1 memperoleh FAIL pada ketiga pengulangan.” T7-C2 gagal pada pengulangan pertama dan ketiga. Pergantian hanya menyangkut kasus gagal yang kedua pada pengulangan kedua.

**Syarat perbaikan.** Pembaca dapat menunjukkan bagaimana DeepSeek v4 tetap mencatat 13/15 PASS di setiap pengulangan tanpa konteks bisnis. Jawaban untuk T3-C1 selalu dinilai FAIL. Jawaban lain yang dinilai FAIL berasal dari T7-C2 pada pengulangan pertama dan ketiga serta dari T7-C1 pada pengulangan kedua. Jadikan kode sebagai penanda kasus agar jelas bahwa evaluasi berlaku pada jawaban. Penjelasan ini juga menghilangkan kebutuhan akan kata “antarpengulangan”, yang pernah dipersoalkan dalam profil tesis.

**Pertahankan.** Pembuka sudah memberikan hasil untuk kedua kondisi. Dengan konteks bisnis, kedua model mencapai 15/15 PASS di setiap pengulangan. Tanpa konteks bisnis, urutan hasil Muse Spark 1.3 adalah 14/15, 13/15, dan 14/15 PASS. Pertahankan ejaan nama kedua model, urutan pengulangan, dan rujukan ke Tabel L1.2 dan Tabel L1.3 dalam Lampiran 1.

## P06 — Sumber belum cukup untuk memperjelas klaim

**P06-1 · Pertanyaan faktual terbuka.** “Kondisi ini membuat model gagal.” Tanpa paragraf sebelumnya, pembaca tidak dapat mengenali kondisi yang dirujuk, model yang mengalami kegagalan, atau apa yang gagal dilakukan. Kata “membuat” menyatakan hubungan sebab akibat. Cuplikan tidak memberikan dasar untuk menilai hubungan itu.

**Syarat perbaikan.** Minta kalimat yang memperkenalkan kondisi dan hasil yang dimaksud. Minta pula keterangan pengujian yang mendukung klaim sebab akibat jika hubungan itu hendak dipertahankan. Jika sumber hanya mencatat kegagalan saat kondisi tersebut berlaku, batasi uraian pada pengamatan itu. Tunda penggantian sampai rujukannya jelas. Jangan memindahkan nama model, kode kasus, atau status PASS/FAIL dari cuplikan lain ke P06.
