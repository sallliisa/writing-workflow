# Penilaian struktur pada baseline

**§2.7, §2.7.1, dan §2.7.2 perlu diperbaiki.** T153–157 sudah menjelaskan cara LLM menggunakan konteks dan keterbatasan konteks panjang. T159–176 mengidentifikasi model, pengembang, akses, dan batas token. Pembaca masih perlu mengetahui kemampuan terdokumentasi dari setiap versi yang relevan ketika agen meminta data, menggunakan hasilnya, dan menyusun jawaban yang dapat dinilai. Kesamaan batas token belum menjelaskan mengapa ketepatan jawaban perlu diperiksa pada masing-masing kondisi ketersediaan dokumen.

| Pertanyaan pembaca | Bukti dan penempatan |
|---|---|
| Model mana yang diuji? | Nama, pengembang, dan kapasitas sudah tercatat di §2.7. T387–401 melaporkan lingkungan dan pengaturan studi. |
| Apa yang dapat dilakukan tiap versi dalam tugas ini? | §2.7.1 pada baseline menyebut dukungan panggilan alat. §2.7.2 menyebut versi, API, dan bobot terbuka. Profil pertama perlu menjelaskan bagaimana hasil satu permintaan berguna untuk langkah berikutnya. Profil kedua perlu menjelaskan kemampuan versi yang relevan untuk meminta data dan menyediakan keluaran terstruktur. |
| Apa yang dibandingkan? | Dalam §3.1 kedua model menerima tugas dan alat yang sama. §2.7 perlu menghubungkan fungsi model dalam agen dengan pertanyaan tentang ketepatan jawaban ketika dokumen aturan tersedia dan ketika dokumen tersebut tidak tersedia. |
| Mengapa penulis memilih kedua versi tersebut? | T19–27, 151–176, 204–226, 385–405 dan 479–487 memberi identitas, rancangan dan lingkungan. Alasan historis pemilihan belum tercatat. Penjelasannya memerlukan keterangan penulis di §3.4.1 (A04). |

Di referensi, §2.7 membangun perbandingan melalui profil, kendala dan arti masing-masing model bagi tugasnya. Penutup R215 dan R231 menyatakan peran model dalam perbandingan. Perbedaan antara inferensi lokal dan layanan cloud menjadi dasar bagi rancangan referensi. Kedua model sasaran digunakan dalam lingkungan agen yang sama. Uraian visi dan arsitektur yang panjang pada referensi juga tidak menjawab pertanyaan tentang hasil perhitungan operasional. [Peta fungsi lengkap](reference-functions.md) · [Pemeriksaan silang](challenge.md)

## Putusan lain yang berubah

Selain keluarga §2.7, §3.3 dan §3.3.2 memerlukan keterangan tentang bagaimana dokumen tersedia bagi sesi baru dan bagaimana akses dibatasi pada kondisi pembanding. §3.4.1 memerlukan alasan pemilihan serta penelusuran sumber batas keluaran. §3.5 dan §3.5.1 menjelaskan aturan dan contoh keputusan, tetapi belum menyebut cara 180 keputusan aktual ditetapkan. Bagian-bagian tersebut sebelumnya dinilai cukup. BAB II juga berubah sebagai induk §2.7. §3.5.3 tetap membutuhkan penjelasan sumber observasi tindakan agen. Pertanyaan itu sudah muncul pada peninjauan sebelumnya.

Status §3.2.2, §4.8, dan §4.8.3 berubah dari cukup menjadi menunggu bukti T9-C2. Tabel kasus dan contoh indikator keempat dapat merujuk pada indikator yang berbeda. Perubahan status ini mencatat perlunya memeriksa hasil per indikator sebelum mengambil keputusan. [Semua perbedaan putusan terhadap peninjauan terdahulu](historical-judgment-changes.json)

## Bagian ringkas yang memenuhi fungsinya

- §2.8 menjelaskan arti kecocokan struktur dan nilai, persentase keberhasilan, serta rentang 0/3–3/3. §3.5.1 memperlihatkan mengapa satu atribut tambahan dan perbedaan frekuensi menghasilkan FAIL. Rumus kemiripan teks dalam referensi tidak diperlukan untuk memahami putusan itu.
- §3.3.2 memperlihatkan isi ketujuh berkas dan satu petunjuk untuk pertanyaan lintas topik. Pertanyaan A05 menyangkut mekanisme akses pada saat pengujian. Contoh isi dan pemilihan referensinya sudah menjalankan fungsi tersendiri.
- Bagian hasil per tugas mengurutkan perbandingan menurut konteks, model, lalu kombinasinya. §3.5.3 menetapkan penyebut masing-masing perbandingan. Pada kelompok dengan seluruh jawaban PASS, tabel dan keterangan singkat mencukupi.
- Tabel dan uraian T7-C1 serta T7-C2 membedakan nilai sebelum pembulatan, nilai yang ditampilkan, batas indikator, dan status keluaran. Penulis melaporkan urutan tindakan untuk pengulangan tertentu. Untuk satu jawaban Muse, uraian hanya menyebut status keluaran. Putusan akhir A06 mempertahankan perbedaan ini.

Kedua akar dan semua turunannya diperiksa. Dari 106 simpul sasaran pada baseline, 86 cukup untuk fungsi setempat, 13 memerlukan perubahan, dan 7 menunggu bukti. Tujuh temuan diterima, tiga temuan bergantung pada bukti yang belum tersedia. Sebagian temuan yang diterima juga memerlukan keterangan penulis untuk diperbaiki. [Evaluasi dan 22 hubungan antarbagiannya](evaluation.json) · [Cakupan menurut kedalaman](coverage.json) · [Rencana revisi](structural-plan.md)
