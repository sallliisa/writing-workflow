# BAB I
## Pertanyaan penelitian
Seberapa tepat jawaban dua model atas pertanyaan analitis dengan dan tanpa dokumen aturan bisnis? Jawaban diperiksa terhadap nilai acuan. Penelitian menggunakan model Nusa dan Cakra melalui API, dengan data, tool, dan pertanyaan yang sama.
# BAB II
## 2.7 Model bahasa
Dokumentasi Nusa dan Cakra menyatakan bahwa kedua model dapat mengeluarkan permintaan pemanggilan tool dan menggunakan hasilnya untuk menyusun jawaban (S1, S2). Dalam penelitian ini kemampuan tersebut digunakan untuk mengambil data sebelum menghasilkan jawaban analitis. Kedua dokumentasi juga menjelaskan bahwa keluaran terstruktur tidak menjamin kebenaran nilainya. Oleh karena itu, penelitian menilai kesesuaian nilai jawaban dengan acuan. Kedua model menggunakan API; perbandingan ini menilai jawaban dari dua model pada kondisi yang sama, tanpa menguji perbedaan antara layanan cloud dan model lokal. Kedua sumber tidak menjelaskan arsitektur internal.
### 2.7.1 Nusa
Nusa dikembangkan oleh Penyedia N dan diakses melalui API dengan context window 32.000 token.
### 2.7.2 Cakra
Cakra dikembangkan oleh Penyedia C dan diakses melalui API dengan context window 32.000 token.
# BAB III
## 3.4 Pemilihan dan pengaturan
Catatan penelitian menyebutkan bahwa kedua model dipilih karena akses API keduanya tersedia pada masa pengujian dan keduanya mendukung tool yang diperlukan. Keduanya menerima tool, data, pertanyaan, serta batas jumlah pemanggilan yang sama. Perbedaan yang diuji adalah model dan ada atau tidaknya dokumen aturan bisnis.
