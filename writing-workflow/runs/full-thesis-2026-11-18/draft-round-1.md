# BAB I — PENDAHULUAN

Bab pendahuluan ini membahas latar belakang penelitian, rumusan masalah, tujuan dan manfaat penelitian, batasan penelitian, serta sistematika penulisan skripsi.

## 1.1. Latar Belakang

*Business Intelligence* (BI) menyediakan laporan dan analisis agar pengguna dapat memahami data organisasi dan menggunakannya untuk mengambil keputusan (Chaudhuri dkk., 2011). BI digunakan untuk kebutuhan strategis ataupun operasional. Melalui *self-service* BI, pengguna bisnis dapat membuat laporan dan menganalisis data dengan lebih sedikit bantuan dari spesialis BI (Alpar dan Schulz, 2016).

Pengguna dapat menyampaikan pertanyaan melalui antarmuka bahasa alami, sehingga tidak perlu menulis *query* secara langsung. Namun, sistem masih kesulitan menjawab pertanyaan analitis yang kompleks serta memahami konteks dan istilah bisnis yang digunakan (Sawant dan Sonawane, 2024).

Pertanyaan pengguna juga dapat dijawab melalui agen berbasis *Large Language Model* (LLM). Agen merencanakan langkah analisis, memilih tool, lalu memeriksa hasil setiap langkah sebelum memberikan jawaban (Wang dkk., 2024). Dalam penelitian ini, Agentic *Business Intelligence* merupakan pendekatan BI yang menggunakan agen untuk membaca data, melakukan perhitungan, dan menjawab pertanyaan pengguna secara *on-demand*.

HKA TROM merupakan sistem internal HK Aston yang mengelola data transaksi, lalu lintas, insiden, inspeksi, serta pengukuran Standar Pelayanan Minimal (SPM) dan Service Level Agreement (SLA). Nama tabel dan kolom belum tentu menjelaskan apa yang diukur oleh suatu indikator, rumus yang digunakan, syarat berlakunya aturan, atau arti status. Sebagai contoh, Lalu Lintas Harian Rata-rata (LHR) pada HKA TROM dihitung dengan membagi total volume kendaraan dengan jumlah hari kalender dalam periode yang diminta. Jika total volume hanya dibagi dengan jumlah hari yang memiliki laporan, nilai LHR dapat berbeda.

Rumiantsau dan Fokeev (2026) menguji *semantic layer* pada analisis berbasis LLM menggunakan dokumen yang menjelaskan apa yang dihitung dan aturan yang digunakan serta memperjelas istilah bisnis. Ketika dokumen tersebut diberikan kepada model, akurasi meningkat sebesar 17 sampai 23 poin persentase. Dalam penelitian ini, konteks bisnis yang diberikan ke agen menjelaskan arti data dan aturan analisis HKA TROM.

Kasus uji dipilih untuk melihat bagaimana agen menggunakan informasi dan aturan bisnis dalam beberapa jenis analisis. Pada sebagian kasus, agen perlu menggabungkan informasi dari beberapa laporan atau mempertimbangkan tindakan yang berkaitan dengan suatu kejadian untuk menentukan statusnya. Pada kasus lain, agen perlu memperhitungkan data yang tidak tersedia atau membandingkan status pemenuhan setiap indikator SPM/SLA pada dua periode.

Penelitian ini membandingkan ketepatan jawaban Muse Spark 1.3 dan DeepSeek v4 Flash pada kasus analisis operasional HKA TROM. Setiap model diuji dengan dan tanpa konteks bisnis menggunakan kasus dan *expected result* yang sama. *Expected result* dihitung dari data setiap kasus sesuai aturan bisnis HKA TROM, lalu digunakan untuk menilai jawaban agen. Hasil perbandingan dapat menjadi pertimbangan saat membuat dokumentasi bisnis untuk analisis berbasis agen.

## 1.2. Rumusan Masalah

Penelitian ini berfokus pada ketepatan jawaban agen dalam analisis transaksi, lalu lintas, insiden, inspeksi, serta SPM/SLA pada HKA TROM. Rumusan masalah yang dikaji adalah bagaimana ketepatan jawaban Muse Spark 1.3 dan DeepSeek v4 Flash ketika diuji dengan dan tanpa konteks bisnis, berdasarkan kesesuaian jawaban masing-masing model dengan *expected result* pada setiap kasus.

## 1.3. Tujuan Penelitian

Penelitian ini bertujuan untuk mengevaluasi ketepatan jawaban *Agentic Business Intelligence* pada kasus analisis operasional HKA TROM dengan membandingkan Muse Spark 1.3 dan DeepSeek v4 Flash, masing-masing dengan dan tanpa konteks bisnis. Perbandingan menggunakan tingkat keberhasilan, yaitu persentase jawaban yang sesuai dengan *expected result*, serta rincian hasil pada setiap kasus dan pengulangan.

## 1.4. Manfaat Penelitian

Manfaat penelitian bagi kajian akademik dan pengembangan sistem analitik adalah sebagai berikut:

1. Memberikan bukti empiris tentang ketepatan jawaban *Agentic Business Intelligence* pada kasus analisis operasional HKA TROM.
2. Memberikan contoh cara mengevaluasi agen analisis data dan membuat konteks bisnis. Hasil penelitian dapat menjadi pertimbangan saat memilih model dan menyiapkan dokumentasi bisnis untuk kebutuhan analisis yang sejenis.

## 1.5. Batasan Penelitian

Batasan penelitian ini adalah sebagai berikut:

1. Pengujian terbatas pada 15 kasus dari sembilan jenis tugas analisis operasional HKA TROM, yang mencakup transaksi, lalu lintas, insiden, inspeksi, serta SPM/SLA.
2. Sebanyak 237 baris data sintetis digunakan untuk kasus uji dan perhitungan *expected result*. Data ini dibuat berdasarkan struktur, relasi tabel, konfigurasi, dan aturan bisnis HKA TROM.
3. Pada kedua kondisi pengujian, agen dapat membaca sumber data, data master, dan konfigurasi melalui layanan yang sama. Agen tidak diberi kode fitur analitik, query yang digunakan oleh fitur tersebut, hasil dashboard, *expected result*, atau data yang sudah diolah menjadi jawaban untuk kasus uji.
4. Tujuh dokumen konteks bisnis hanya tersedia pada kondisi dengan konteks bisnis dan diberikan bersama kepada agen. Pengaruh tiap dokumen atau aturan tidak diuji secara terpisah.
5. Evaluasi membandingkan 180 jawaban terstruktur dari kedua model dengan *expected result*. Hasil penilaian digunakan untuk membandingkan tingkat keberhasilan kedua model dan melihat apakah hasil setiap kasus berubah antara pengulangan.

## 1.6. Sistematika Penulisan

Laporan skripsi ini disusun dalam lima bab dengan sistematika penulisan sebagai berikut:

| BAB I | PENDAHULUAN |
| :---- | :---- |
|  | Bab ini menyajikan latar belakang, rumusan masalah, tujuan penelitian, manfaat penelitian, batasan penelitian, serta sistematika penulisan. |
| BAB II | TINJAUAN PUSTAKA |
|  | Bab ini membahas penelitian terdahulu serta teori *Business Intelligence*, agen berbasis *Large Language Model*, analisis melalui bahasa alami, konteks bisnis, dan evaluasi hasil analisis. |
| BAB III | METODOLOGI PENELITIAN |
|  | Bab ini menjelaskan data dan kasus uji, prompt dan konteks bisnis yang digunakan, cara agen menghasilkan jawaban, serta evaluasi hasil. Pengujian membandingkan kedua model dengan dan tanpa konteks bisnis. |
| BAB IV | HASIL DAN PEMBAHASAN |
|  | Bab ini menyajikan hasil evaluasi Muse Spark 1.3 dan DeepSeek v4 Flash dengan dan tanpa konteks bisnis. Pembahasan mencakup ketepatan jawaban menurut kelompok tugas, hasil pengulangan, perbandingan kedua model, serta interpretasi dan keterbatasan penelitian. |
| BAB V | PENUTUP |
|  | Bab ini berisi kesimpulan yang menjawab rumusan masalah berdasarkan hasil evaluasi serta saran untuk pengembangan dan penelitian selanjutnya. |

# BAB II — TINJAUAN PUSTAKA

Bab ini membahas penelitian terdahulu dan konsep yang digunakan dalam evaluasi *Agentic Business Intelligence*. Pembahasan meliputi *Business Intelligence*, agen berbasis LLM, analisis data melalui bahasa alami, *prompt* dan konteks bisnis, model yang digunakan, serta evaluasi hasil analisis.

## 2.1. State-of-the-art

Penelitian terkait *Agentic Business Intelligence* mencakup penggunaan bahasa alami untuk mengakses data, agen berbasis LLM untuk menjalankan analisis, dan evaluasi agen pada tugas bisnis. Perbandingan penelitian tersebut disajikan pada Tabel 2.1.

**Tabel 2.1 Perbandingan Penelitian Terkait**

| No | Penelitian | Fokus | Data / Lingkungan | Evaluasi dan Temuan | Relevansi / Keterbatasan |
| ----- | ----- | ----- | ----- | ----- | ----- |
| 1 | Sawant & Sonawane (2024) | Antarmuka bahasa alami untuk basis data dan visualisasi | Kajian NLIDB, NLIV, dan BI | Antarmuka bahasa alami memudahkan akses ke data. Kendalanya mencakup pertanyaan analitis yang kompleks serta pemahaman konteks dan semantik. | Memberikan dasar bagi conversational analytics melalui kajian antarmuka bahasa alami untuk basis data dan visualisasi. |
| 2 | X. Liu dkk. (2024) - AgentBench | Evaluasi LLM sebagai agen pada lingkungan interaktif | 8 lingkungan dan 29 model API ataupun open-source | Menemukan kendala utama pada penalaran jangka panjang, pengambilan keputusan, dan kepatuhan terhadap instruksi. | Mendukung evaluasi berbasis tugas interaktif pada beragam lingkungan umum. |
| 3 | Hong dkk. (2025) - Data Interpreter | Agen LLM untuk *workflow* data science dengan beberapa tahap | InfiAgent-DABench, tugas machine learning, dan tugas open-ended | Perencanaan berbasis graph dan verifikasi bertahap meningkatkan kinerja pada beberapa *benchmark* analisis data. | Menunjukkan penggunaan agen untuk merencanakan dan memeriksa analisis data secara bertahap. |
| 4 | Sahu dkk. (2025) - InsightBench | Evaluasi business analytics end-to-end | 100 dataset bisnis dengan insight yang sengaja disisipkan dan dikurasi | Mengevaluasi perumusan pertanyaan, analisis, interpretasi, dan penyusunan insight menggunakan evaluator berbasis LLM. | Mengevaluasi insight dari analisis bisnis yang bersifat open-ended dengan penilaian berbasis LLM. |
| 5 | Lei dkk. (2025) - Spider 2.0 | *Workflow* *Text-to-SQL* tingkat enterprise | 632 tugas dengan basis data besar, metadata, dokumentasi, dan beberapa sistem basis data | Code agent yang diuji menyelesaikan 21,3% tugas, dibandingkan 91,2% pada Spider 1.0. | Menunjukkan kesulitan menyelesaikan tugas SQL pada lingkungan enterprise. |
| 6 | Vishwakarma dkk. (2025) - EnterpriseBench | Evaluasi agen pada lingkungan enterprise | 500 tugas pada software engineering, HR, finance, dan administrasi | Lingkungan pengujian mencakup data yang tersebar, kontrol akses, dan workflow lintas fungsi. Hasil penyelesaian tugas bervariasi menurut model, framework, dan strategi perencanaan. | Mencakup tugas dari beberapa fungsi organisasi dalam satu lingkungan pengujian. |
| 7 | Rumiantsau & Fokeev (2026) | Pengaruh semantic layer pada analisis berbasis LLM | 100 pertanyaan retail. Sebanyak 99 dinilai setelah satu query referensi gagal dieksekusi | Analytical Pass Rate meningkat 17,2–23,2 poin persentase berdasarkan penilaian Claude Sonnet 4.6 sebagai judge. | Menguji pemberian dokumen konteks bisnis melalui protokol *single-shot* pada satu dataset retail. Studi ini masih berupa preprint. |
| 8 | Egg dkk. (2025) — DABstep | Evaluasi agen pada tugas analisis data bertahap | Data CSV/JSON dan dokumentasi bisnis untuk 450 pertanyaan analisis pembayaran | Jawaban akhir dibandingkan dengan *expected result* menggunakan normalisasi dan toleransi sesuai tipe jawaban | Mencakup analisis dari beberapa sumber data dan penerapan aturan bisnis. Perbandingan dengan dan tanpa dokumen konteks tidak diuji. |

Sawant dan Sonawane (2024) membahas antarmuka bahasa alami yang memungkinkan pengguna mengakses data tanpa menulis *query* sendiri. Salah satu kesulitannya adalah memahami pertanyaan analitis yang kompleks, termasuk konteks dan arti data yang dimaksud pengguna. Pada penggunaan agen, pekerjaan ini juga mencakup pemilihan sumber data dan langkah analisis yang diperlukan untuk menjawab pertanyaan.

Kemampuan agen menjalankan tugas diuji dalam AgentBench pada berbagai lingkungan interaktif. Pengujian tersebut menemukan kendala dalam penalaran, pengambilan keputusan, dan kepatuhan terhadap instruksi (X. Liu dkk., 2024). Untuk tugas *data science*, Data Interpreter menggunakan perencanaan berbasis graf dan verifikasi bertahap selama analisis berlangsung (Hong dkk., 2025).

Tugas bisnis yang digunakan dalam evaluasi agen cukup beragam. InsightBench menilai *insight* dan ringkasan hasil analisis yang bersifat *open-ended* (Sahu dkk., 2025), sedangkan EnterpriseBench mencakup pekerjaan dari beberapa fungsi organisasi (Vishwakarma dkk., 2025). Spider 2.0 menguji *workflow Text-to-SQL* pada lingkungan *enterprise*, yang memerlukan pemahaman terhadap metadata dan dokumentasi data (Lei dkk., 2025).

DABstep menggunakan pertanyaan analisis dari kegiatan operasional Adyen, perusahaan penyedia layanan pembayaran (Adyen, n.d.). Agen perlu membaca data terstruktur dan dokumentasi bisnis, lalu menjalankan beberapa langkah analisis. Jawaban akhirnya dibandingkan dengan *expected result*, yaitu jawaban yang diharapkan untuk pertanyaan tersebut. Aturan perbandingannya disesuaikan dengan tipe jawaban (Egg dkk., 2025).

Rumiantsau dan Fokeev (2026) membandingkan model yang hanya menerima skema data dengan model yang juga menerima dokumen konteks bisnis. Pada 99 pertanyaan *retail*, penambahan dokumen tersebut meningkatkan *Analytical Pass Rate* sebesar 17,2–23,2 poin persentase. Penilaian dilakukan berdasarkan hasil eksekusi dan Claude Sonnet 4.6 sebagai *judge*.

Dalam penelitian ini, Muse Spark 1.3 dan DeepSeek v4 Flash digunakan untuk menjawab pertanyaan analisis operasional HKA TROM. Kedua model diuji dengan dan tanpa konteks bisnis. Agen membaca data melalui *tool* dan menghasilkan jawaban dalam format *JavaScript Object Notation* (JSON). Struktur dan nilai jawaban kemudian dibandingkan dengan *expected result*.

## 2.2. Business Intelligence

*Business Intelligence* (BI) adalah kumpulan teknologi, proses, dan aplikasi untuk mengolah data organisasi menjadi informasi yang membantu pengambilan keputusan. BI mencakup komponen seperti *data warehouse*, *Online Analytical Processing* (OLAP), *reporting server*, *dashboard*, *ad hoc query*, dan *analytical engine*. Komponen tersebut digunakan untuk menyimpan dan mengolah data, menyajikan laporan, serta melakukan analisis sesuai kebutuhan pengguna (Chaudhuri dkk., 2011).

Dalam analisis BI, pengguna menentukan nilai yang ingin dihitung dan cara mengelompokkan hasilnya. Nilai yang dihitung disebut *measure*, sedangkan pengelompokannya menggunakan *dimension*, seperti waktu atau kategori data (Quamar dkk., 2020). Melalui *self-service BI*, pengguna bisnis dapat melakukan analisis tersebut dengan lebih sedikit bantuan dari pengembang atau unit BI (Alpar dan Schulz, 2016).

## 2.3. Agentic Business Intelligence

*Agentic Business Intelligence* dalam penelitian ini adalah penggunaan agen untuk menjalankan analisis data bisnis. Pengguna menyampaikan pertanyaan, kemudian agen membaca data melalui *tool*, melakukan perhitungan, dan menyusun jawaban.

Untuk menjawab suatu pertanyaan, agen dapat memerlukan informasi dari beberapa sumber. Pada DABstep, agen memilih data yang diperlukan, menghubungkan informasi dari sumber yang berbeda, dan menerapkan aturan bisnis dalam perhitungan (Egg dkk., 2025). Dalam penelitian ini, data insiden HKA TROM perlu dihubungkan dengan data tindakan penanganan yang tersimpan dalam tabel terpisah. Insiden dinyatakan selesai jika memiliki minimal satu tindakan penanganan dan seluruh tindakan tersebut sudah selesai.

Setelah memperoleh data, agen dapat menjumlahkan nilai, menghitung banyaknya data, atau mencari rata-rata. Jika pertanyaan meminta hasil per kategori atau per periode, perhitungan dilakukan untuk setiap kelompok data. InfiAgent-DABench mencakup perhitungan rata-rata pada seluruh data dan pada setiap kelompok, termasuk tugas dengan nilai yang tidak tersedia (Hu dkk., 2024). TableBench juga mencakup perhitungan total, jumlah data, dan perbandingan hasil antar periode (Wu dkk., 2025).

Untuk menentukan status berdasarkan suatu batas, agen perlu memeriksa operator pembanding dan syarat yang berlaku. Syarat *lebih dari* tidak mencakup nilai yang tepat pada batas, sedangkan *lebih dari atau sama dengan* mencakup nilai tersebut. NumericBench menguji perbandingan lebih besar, lebih kecil, atau sama dengan, termasuk perbandingan yang digabungkan dengan kondisi tertentu (Li dkk., 2025).

## 2.4. Agen Berbasis Kecerdasan Buatan

Agen berbasis LLM menggunakan model bahasa untuk merencanakan dan memilih tindakan sesuai tugas yang diberikan. Melalui *tool*, agen dapat membaca data atau menjalankan fungsi di luar model. Hasil dari tindakan tersebut digunakan untuk menentukan langkah berikutnya (Wang dkk., 2024).

Interaksi ini dapat berlangsung dalam *tool call loop*. Agen memilih *tool* dan parameter *input*, menerima hasilnya, lalu menentukan apakah masih ada informasi yang perlu diperoleh (Wang dkk., 2024). Sebagai contoh, agen membaca skema untuk mengetahui kolom yang tersedia sebelum mengambil data yang sesuai dengan pertanyaan. Jika data tersebut belum cukup, agen dapat melakukan *tool call* berikutnya. Pada Data Interpreter, rencana analisis juga dapat disesuaikan berdasarkan hasil yang diperoleh selama pengerjaan tugas (Hong dkk., 2025).

Kesalahan dapat terjadi ketika agen memilih data atau memahami hasil *tool call*, sehingga perhitungan berikutnya menggunakan informasi yang keliru. AgentBench menemukan bahwa penalaran dan kepatuhan terhadap instruksi masih menjadi kendala dalam penyelesaian tugas interaktif (X. Liu dkk., 2024).

### 2.4.1. Tool dan Model Context Protocol

*Tool* adalah fungsi yang dapat dipanggil agen, misalnya untuk membaca skema atau mengambil data. Deskripsi *tool* menjelaskan fungsi, parameter *input*, dan *output* yang dikembalikan. Fungsi setiap *tool* perlu mudah dibedakan agar agen dapat memilih *tool* yang sesuai. Penggunaannya juga perlu diuji pada tugas yang relevan (Anthropic, 2025).

Pada LongDA, agen LongTA menggunakan read_doc untuk membaca bagian dokumen, search_doc untuk mencari kata kunci, dan retriever untuk menemukan informasi yang relevan. Agen ini menjalankan perhitungan melalui eksekusi Python (Li dkk., 2026).

*Model Context Protocol* (MCP) menghubungkan aplikasi yang menjalankan agen dengan server penyedia *tool* dan sumber informasi. Dalam MCP, *host* mengelola interaksi dengan model dan konteks percakapan. *Client* di dalam *host* menangani komunikasi dengan server. Setiap *client* terhubung dengan satu server, sedangkan satu *host* dapat menjalankan beberapa *client* (Model Context Protocol, 2026).

## 2.5. Analisis Data melalui Bahasa Alami

Antarmuka bahasa alami memungkinkan pengguna meminta analisis melalui pertanyaan atau instruksi. Sawant dan Sonawane (2024) membahas *Natural Language Interface to Databases* (NLIDB) untuk mengakses basis data dan *Natural Language Interface to Visualization* (NLIV) untuk membuat visualisasi. Sistem perlu memahami istilah dalam pertanyaan dan menghubungkannya dengan data yang tersedia.

Untuk menjawab pertanyaan tentang total volume kendaraan per bulan, misalnya, sistem perlu mengelompokkan data berdasarkan bulan dan menjumlahkan volume pada setiap kelompok. Jika pengguna juga menyebut ruas atau rentang tanggal, sistem hanya menggunakan data yang sesuai dengan keterangan tersebut. Dalam *conversational BI*, istilah dalam pertanyaan dihubungkan dengan pengetahuan tentang domain, *measure*, dan *dimension* agar sistem dapat menentukan analisis yang diminta (Quamar dkk., 2020).

Istilah bisnis juga perlu memiliki definisi yang jelas. Nama kolom belum tentu menjelaskan kapan suatu pekerjaan dianggap selesai atau bagaimana rata-rata harian dihitung (Quamar dkk., 2020).

## 2.6. Prompt dan Konteks Bisnis

*Prompt* adalah instruksi atau pertanyaan yang diberikan kepada model untuk mengarahkan jawabannya. Selain menjelaskan tugas, *prompt* dapat memuat informasi tambahan, contoh, dan format jawaban yang diminta. Brown dkk. (2020) menunjukkan bahwa GPT-3 dapat menjalankan berbagai tugas melalui instruksi atau contoh dalam *prompt* tanpa *fine-tuning* khusus untuk setiap tugas.

Dalam analisis data, agen dapat menggunakan dokumen konteks bisnis untuk memahami arti data dan aturan perhitungannya. Pada DABstep, dokumentasi bisnis disertakan bersama data dari beberapa sumber agar agen dapat menjalankan analisis sesuai aturan yang berlaku (Egg dkk., 2025). Dalam penelitian ini, agen diuji dengan dan tanpa akses ke dokumen konteks bisnis.

### 2.6.1. Struktur dan Isi Konteks Bisnis

Dokumen konteks bisnis dapat memuat arti setiap baris data, hubungan antartabel, satuan, dan arti nilai status. Istilah yang digunakan perlu konsisten agar objek atau proses yang sama tidak dijelaskan dengan arti yang berbeda. Dalam *ontology engineering*, pengetahuan suatu bidang dijelaskan melalui konsep, relasi, dan fungsi yang didefinisikan secara eksplisit (Gruber, 1993).

Untuk menentukan cakupan dan tingkat perincian ontologi, Noy dan McGuinness (2001) menggunakan pertanyaan yang perlu dijawab. Dokumen konteks bisnis dalam penelitian ini menjelaskan cara memilih data, hubungan antartabel, dan ketentuan perhitungan sesuai aturan HKA TROM.

Aturan perhitungan menjelaskan, misalnya, cara memperlakukan nilai null dan jumlah hari yang digunakan untuk menghitung rata-rata harian. Rata-rata volume kendaraan per hari dapat berbeda jika total volume dibagi dengan jumlah seluruh hari kalender atau hanya jumlah hari yang memiliki data. Dokumen konteks juga perlu menjelaskan kapan suatu batas atau syarat berlaku. Dalam penelitian ini, penjelasan tersebut dikelompokkan menurut topik analisis.

### 2.6.2. Skills

*Skill* adalah kumpulan instruksi dan bahan pendukung untuk membantu agen menjalankan tugas tertentu. Dalam format Agent Skills, SKILL.md memuat nama, deskripsi kegunaan, dan instruksi utama. Informasi yang lebih rinci dapat disimpan dalam dokumen referensi dan dibaca saat diperlukan (Agent Skills, n.d.).

Dalam penelitian ini, instruksi utama digunakan untuk mengarahkan agen ke referensi yang sesuai dengan pertanyaan. Dokumen ini disebut dokumen *routing*. Dokumen referensi memuat penjelasan istilah dan aturan bisnis untuk setiap topik. Agen dapat membaca lebih dari satu referensi apabila pertanyaannya memerlukan informasi dari beberapa topik.

## 2.7. Large Language Models

*Large Language Model* (LLM) adalah model bahasa berskala besar yang dilatih menggunakan kumpulan teks untuk mempelajari pola bahasa dan menghasilkan *output* berdasarkan konteks (Brown dkk., 2020). Pada agen, LLM digunakan untuk memilih tindakan dan menyusun jawaban dari informasi yang tersedia (Wang dkk., 2024).

Selama pengerjaan tugas, konteks yang diterima model dapat berisi *prompt*, hasil *tool call*, dan isi dokumen yang telah dibaca. Jumlah token yang dapat diproses dalam konteks tersebut dibatasi oleh *context window*.

N. F. Liu dkk. (2024) menguji model dengan informasi yang ditempatkan pada bagian berbeda dalam konteks panjang. Pada tugas pencarian informasi, hasil model dipengaruhi oleh letak informasi yang dibutuhkan. Shi dkk. (2023) juga menemukan bahwa informasi yang tidak relevan dapat mengganggu model dalam menyelesaikan soal aritmetika.

Penelitian ini menggunakan Muse Spark 1.3 dari Meta dan DeepSeek v4 Flash dari DeepSeek. Pengembang dan *context window* kedua model disajikan pada Tabel 2.2.

**Tabel 2.2 Karakteristik Model yang Digunakan**

| Aspek | Muse Spark 1.3 | DeepSeek v4 Flash |
| :---- | :---- | :---- |
| Pengembang | Meta | DeepSeek |
| Context window (token) | 1.048.576 | 1.048.576 |

Sumber: Meta (2026c) dan DeepSeek-AI (2026).

### 2.7.1. Muse Spark 1.3

Muse Spark 1.3 diperkenalkan oleh Meta pada September 2026 dan tersedia melalui Meta Model API serta Muse Code (Meta, 2026a). Model ini mendukung *tool calling* dan memiliki *context window* sebesar 1.048.576 token (Meta, 2026b, 2026c).

### 2.7.2. DeepSeek v4 Flash

DeepSeek v4 Flash yang digunakan dalam penelitian ini adalah versi DeepSeek-V4.1-Flash-1017, dengan *context window* sebesar 1.048.576 token (DeepSeek-AI, 2026). Model ini tersedia melalui API DeepSeek, dan *weights*-nya dapat diakses secara terbuka (DeepSeek, 2026a).

## 2.8. Evaluasi Hasil Analisis

Evaluasi hasil analisis dilakukan dengan memeriksa jawaban yang dihasilkan agen. Untuk tugas yang memiliki jawaban pasti, hasilnya dapat dibandingkan dengan *expected result*, seperti pada InfiAgent-DABench (Hu dkk., 2024) dan DABstep (Egg dkk., 2025). Dalam penelitian ini, evaluasi mencakup kesesuaian struktur dan nilai jawaban, tingkat keberhasilan, serta konsistensi hasil pengulangan.

### 2.8.1. Kesesuaian Struktur dan Nilai Jawaban

Pada jawaban berbentuk JSON, pemeriksaan mencakup struktur dan nilai yang dihasilkan. Struktur meliputi atribut yang diminta, tipe nilai, dan urutan elemen *array*. Dalam evaluasi *in-context learning*, DataBench memeriksa apakah *output* merupakan JSON yang valid dan memuat atribut yang diperlukan sebelum menilai ketepatan isinya (Osés Grijalba dkk., 2024).

Nilai jawaban dibandingkan dengan *expected result* yang disusun berdasarkan data dan aturan perhitungan untuk setiap pertanyaan. Pada InfiAgent-DABench, seluruh bagian jawaban harus benar agar tugas dinilai berhasil (Hu dkk., 2024). Dalam penelitian ini, jawaban diberi status PASS jika struktur dan seluruh nilainya sesuai dengan *expected result*. Jika ada bagian yang tidak sesuai, jawaban dinilai FAIL.

### 2.8.2. Tingkat Keberhasilan

Tingkat keberhasilan adalah persentase jawaban yang benar (Hu dkk., 2024). Dalam penelitian ini, persentase PASS dihitung untuk setiap model pada kondisi dengan dan tanpa konteks bisnis. Seluruh jawaban dari ketiga pengulangan ikut dihitung.

### 2.8.3. Konsistensi Hasil Pengulangan

Pada τ-bench, tugas yang sama dijalankan beberapa kali untuk menilai konsistensi agen. Hasil pengujian menunjukkan bahwa keberhasilan agen dapat berbeda pada setiap pengulangan (Yao dkk., 2025).

Dalam penelitian ini, konsistensi dilihat dari jumlah PASS pada tiga pengulangan untuk kasus, model, dan kondisi konteks bisnis yang sama. Hasilnya ditulis sebagai 0/3 hingga 3/3. Nilai 3/3 berarti ketiga pengulangan berhasil, sedangkan 0/3 berarti seluruh pengulangan gagal.

# BAB III — METODOLOGI PENELITIAN

Bab ini menjelaskan data, rancangan pengujian, dan prosedur evaluasi hasil analisis Agentic Business Intelligence pada HKA TROM. Uraian metode mengikuti proses penyiapan data, penyusunan prompt dan konteks bisnis, generasi jawaban, serta evaluasi hasil.

## 3.1. Gambaran Umum Penelitian

Penelitian ini menggunakan pendekatan kuantitatif komparatif untuk mengevaluasi ketepatan jawaban agen pada HKA TROM. Setiap kasus berisi pertanyaan analisis dan ketentuan jawaban, sedangkan jawaban akhir agen dibandingkan dengan *expected result* (Egg dkk., 2025).

Muse Spark 1.3 dan DeepSeek v4 Flash masing-masing diuji dengan dan tanpa konteks bisnis. Kedua model menggunakan kasus, data, *tool*, *prompt*, dan *expected result* yang sama, dengan akses ke dokumen konteks bisnis yang dibedakan.

Penelitian dimulai dengan menyiapkan data dan *expected result* untuk 15 kasus berdasarkan aturan HKA TROM. Setelah itu, prompt dan dokumen konteks bisnis dibuat. Prompt berisi pertanyaan dalam bahasa Indonesia dan ketentuan jawaban JSON, sedangkan dokumen konteks bisnis menjelaskan data dan aturan analisis.

Pada tahap generasi jawaban, agen membaca data dan menghasilkan jawaban berdasarkan prompt. Jawaban tersebut kemudian dibandingkan dengan *expected result* untuk menentukan PASS atau FAIL. Pada tahap analisis hasil, tingkat keberhasilan kedua model dibandingkan pada pengujian dengan dan tanpa konteks bisnis. Jawaban yang gagal serta perbedaan hasil pada tiga pengulangan juga diperiksa. Gambar 3.1 merangkum kelima tahap penelitian.

*Gambar 3.1 Alur Tahapan Penelitian*

Kelima belas kasus dalam penelitian ini dikelompokkan ke dalam sembilan jenis tugas, yaitu T1 hingga T9. Kode setiap kasus mengikuti pola T[n]-C[m], dengan n menunjukkan nomor jenis tugas dan m menunjukkan nomor kasus dalam tugas tersebut. Sebagai contoh, T1-C2 adalah kasus kedua pada jenis tugas T1.

Untuk setiap model, 15 kasus dijalankan tiga kali dengan konteks bisnis dan tiga kali tanpa konteks bisnis. Pengujian ini menghasilkan 45 jawaban pada masing-masing kondisi, sehingga terdapat 90 jawaban per model dan 180 jawaban dari kedua model. Rincian pengujian dapat dilihat pada Tabel 3.1.

**Tabel 3.1 Rancangan Pengujian Kedua Model**

| Model | Konteks bisnis | Kasus | Pengulangan | Jumlah jawaban |
| ----- | ----- | ----- | ----- | ----- |
| Muse Spark 1.3 | Dengan konteks bisnis | 15 | 3 | 45 |
| Muse Spark 1.3 | Tanpa konteks bisnis | 15 | 3 | 45 |
| DeepSeek v4 Flash | Dengan konteks bisnis | 15 | 3 | 45 |
| DeepSeek v4 Flash | Tanpa konteks bisnis | 15 | 3 | 45 |
| Total | Seluruh pengujian | – | – | 180 |

## 3.2. Data Penelitian

Data penelitian mencakup data HKA TROM yang digunakan agen untuk menjawab pertanyaan serta *expected result* untuk menilai ketepatan jawaban agen.

### 3.2.1. Sumber dan Cakupan Data

Basis data penelitian menggunakan skema HKA TROM dan diisi dengan data sintetis.

Kumpulan data uji berisi 237 baris pada 15 tabel operasional. Baris tersebut mencakup laporan pemantauan transaksi beserta rincian durasi, laporan lalu lintas dan jumlah kendaraan, data insiden berikut tindakan penanganan, laporan kecelakaan, serta jadwal dan hasil inspeksi. Data master dan konfigurasi berisi identitas ruas, gerbang, golongan kendaraan, aset, serta parameter SPM/SLA yang diperlukan dalam analisis. Tabel 3.2 merangkum sumber data utama untuk setiap kelompok analisis.

**Tabel 3.2 Kelompok Analisis dan Sumber Data Utama**

| Kelompok | Sumber data |
| ----- | ----- |
| Transaksi | monitoring_transactions, monitoring_transaction_details |
| Lalu lintas | toll_volume_revenue, toll_traffic_volumes |
| Insiden | incidents, incident_actions, accident_reports |
| Inspeksi | inspection_schedules, inspections, inspection_elements, inspection_items |
| SPM/SLA | monitoring_transactions, monitoring_transaction_details, view_section_spm_sla |

Ruas, tanggal, gerbang, *shift*, atau periode dalam setiap prompt menentukan data yang harus dianalisis. Agen juga dapat membaca data di luar cakupan tersebut, sehingga perlu memilih data yang sesuai sebelum melakukan perhitungan.

### 3.2.2. Pemilihan Kasus Uji

Penelitian ini menggunakan 15 kasus dari sembilan jenis tugas, T1 hingga T9. Kasus dipilih dari analisis operasional yang dapat dikerjakan dengan data HKA TROM dan memerlukan kemampuan yang dijelaskan pada Bagian 2.3.

Laporan transaksi dan lalu lintas digunakan untuk menguji pemilihan data, perhitungan agregat, dan pengelompokan menurut periode atau golongan kendaraan. Data insiden dan inspeksi memerlukan hubungan antartabel untuk menentukan status atau merangkum item rusak. Konfigurasi SPM/SLA menyediakan batas dan syarat untuk menilai suatu laporan, merangkum hasil dalam satu periode, dan membandingkan dua periode.

Di T1, agen diminta untuk menghitung rata-rata durasi transaksi dari data durasi di dalam laporan. Di T1-C1, jumlah data durasi pada setiap laporan berbeda dan terdapat data durasi bernilai null. Rata-rata keseluruhan dihitung dengan membagi total durasi dari seluruh laporan dengan jumlah data durasi non-null. Di T1-C2, data *booth* dan *longbooth* sama-sama digunakan dalam perhitungan rata-rata durasi transaksi.

Di T2, agen diminta menghitung volume kendaraan dan LHR dalam periode yang tertulis di dalam prompt. LHR dihitung dengan membagi total volume kendaraan dengan jumlah hari kalender dalam periode tersebut, termasuk hari yang tidak memiliki laporan. Di T3, agen diminta menampilkan tren volume dan LHR bulanan berdasarkan golongan kendaraan. Perhitungan LHR menggunakan jumlah hari pada masing-masing bulan.

Pada T4, agen menentukan status insiden dari data tindakan penanganan yang ada. Insiden dinyatakan selesai jika memiliki minimal satu data tindakan dan nilai stage pada seluruh data tindakannya adalah 100. Nilai 50 dan null diperlakukan sebagai tindakan yang belum selesai.

T4-C1 mencakup empat insiden, dengan salah satunya tidak memiliki data tindakan. Tiga insiden lainnya masing-masing memiliki satu data tindakan bernilai 50, dua data tindakan bernilai 100, dan dua data tindakan dengan nilai 100 dan null.

Di T5, suatu kecelakaan dapat memiliki beberapa penyebab, dan penyebab yang sama dapat muncul lebih dari sekali. Agen perlu menghitung berapa kali setiap penyebab tersebut muncul.

Di T6, agen perlu menghubungkan data hasil inspeksi dengan data aset. Di T6-C1, item inspeksi yang memiliki kategori kerusakan tetap dihitung sebagai item rusak meskipun prioritas perbaikannya kosong.

Di T7, agen perlu menentukan status SPM/SLA dengan membandingkan rata-rata durasi setiap gardu dengan batas indikator dan memeriksa apakah SLA berlaku untuk setiap indikator di ruas yang dianalisis. Di T7-C1, terdapat rata-rata durasi yang tepat pada batas indikator dan yang sedikit melebihi batas. Jika rata-rata durasi dibulatkan sebelum dibandingkan dengan batas, nilai yang sedikit melebihi batas dapat terlihat sama dengan batasnya. Di T7-C2, SLA hanya berlaku pada indikator ketiga, sedangkan di T7-C3 tidak ada SLA yang berlaku.

Di T8, agen perlu memeriksa status pemenuhan setiap indikator SPM/SLA pada seluruh laporan untuk menentukan statusnya selama periode yang diminta pada prompt. Di T8-C1, ada indikator yang terpenuhi pada satu laporan dan tidak terpenuhi pada laporan lain. Di T9, agen diminta membandingkan status pemenuhan setiap indikator SPM/SLA pada dua periode, lalu menentukan apakah statusnya tetap, membaik, atau memburuk. Tabel 3.3 menyajikan kondisi setiap kasus dan kemampuan analisis yang diuji.

**Tabel 3.3 Daftar Lima Belas Kasus Uji**

| Kasus | Analisis | Kondisi utama | Kemampuan analisis yang diuji |
| ----- | ----- | ----- | ----- |
| T1-C1 | Rata-rata durasi transaksi | Tiga laporan dengan jumlah data durasi yang berbeda, termasuk data durasi bernilai null | Menggabungkan informasi dari beberapa laporan dengan memperhitungkan perbedaan jumlah data yang dapat digunakan pada setiap laporan. |
| T1-C2 | Rata-rata durasi transaksi | Data durasi *booth* dan *longbooth* | Menentukan informasi yang relevan dari berbagai jenis data dan menggunakannya dalam analisis. |
| T2-C1 | Volume dan LHR | Hari tanpa laporan dan golongan dengan volume nol | Memperhitungkan seluruh hari dalam periode yang diminta dan tetap menyertakan kelompok dengan nilai nol. |
| T3-C1 | Tren lalu lintas | Empat bulan dengan jumlah hari berbeda dan golongan kendaraan dengan volume nol | Mengelompokkan data berdasarkan periode waktu dan menghasilkan ringkasan yang dapat dibandingkan antar periode. |
| T4-C1 | Status insiden | Tidak ada tindakan, satu tindakan dengan stage 50, dua tindakan dengan stage 100, atau dua tindakan dengan stage 100 dan null | Mempertimbangkan tindakan yang berkaitan dengan suatu insiden dan menerapkan syarat untuk menentukan statusnya. |
| T5-C1 | Penyebab kecelakaan | Lebih dari satu penyebab dan penyebab yang berulang | Mempertimbangkan beberapa faktor yang berkaitan dengan suatu kejadian dan menghitung seberapa sering setiap faktor muncul. |
| T6-C1 | Kerusakan pada item inspeksi | Kategori kerusakan di luar R1–R3, item tanpa prioritas, serta item inspeksi yang terhubung dengan data aset melalui beberapa tabel | Menghubungkan data yang saling berkaitan dan tetap menyertakan temuan yang relevan ketika sebagian informasi tidak tersedia. |
| T7-C1 | SPM/SLA per laporan | Rata-rata durasi tepat pada batas dan sedikit melebihi batas, yang dibandingkan sebelum pembulatan | Membandingkan angka dengan batas yang ditetapkan, termasuk saat selisihnya kecil. |
| T7-C2 | SPM/SLA per laporan | SLA hanya berlaku pada indikator ketiga | Mempertimbangkan syarat yang berlaku pada setiap item sebelum menilainya. |
| T7-C3 | SPM/SLA per laporan | Tidak ada SLA yang berlaku | Mengenali kapan suatu syarat tidak berlaku dan mempertimbangkannya saat menarik kesimpulan. |
| T7-C4 | SPM/SLA per laporan | Beberapa laporan pemantauan dengan informasi yang serupa | Memilih informasi yang relevan dengan prompt dari beberapa laporan yang serupa. |
| T8-C1 | SPM/SLA periode | Indikator yang terpenuhi pada satu laporan dan tidak terpenuhi pada laporan lain | Mempertimbangkan hasil dari beberapa laporan untuk menarik kesimpulan mengenai keseluruhan periode. |
| T8-C2 | SPM/SLA periode | Perhitungan menggunakan data durasi *booth*, tanpa menghitung data durasi *longbooth* | Memilih data yang relevan sebelum menarik kesimpulan mengenai suatu periode. |
| T9-C1 | Perbandingan periode | Status tetap dan membaik | Membandingkan dua periode untuk menentukan hasil yang tidak berubah dan hasil yang membaik. |
| T9-C2 | Perbandingan periode | Dua laporan per periode dengan status memburuk | Menggabungkan informasi dalam setiap periode, lalu membandingkan hasil kedua periode. |

### 3.2.3. Penyusunan Expected Result

*Expected result* untuk setiap kasus dihitung dari data yang sesuai dengan prompt berdasarkan aturan bisnis HKA TROM. Hasilnya ditulis dalam format JSON. *Expected result* yang sama digunakan pada semua pengulangan dan tidak dapat diakses oleh agen.

Aturan bisnis untuk menghitung expected result dirangkum pada Tabel 3.4.

Laporan dipilih berdasarkan tanggal operasional dalam rentang tanggal pada test case, termasuk tanggal awal dan akhir. Untuk evaluasi SPM/SLA per laporan, laporan juga harus sesuai dengan ruas, gerbang, dan jadwal *shift* dalam prompt. Gardu diidentifikasi dari nomor gardu dan laporan pemantauannya.

**Tabel 3.4 Aturan Bisnis yang Digunakan dalam Pengujian**

| Analisis | Aturan bisnis | Jenis tugas |
| ----- | ----- | ----- |
| Durasi transaksi | Total durasi dari data *booth* dan *longbooth* yang memiliki durasi non-null dibagi dengan jumlah data tersebut. | T1 |
| Volume dan LHR | LHR dihitung dengan membagi total volume kendaraan dengan jumlah hari kalender, termasuk tanggal awal, tanggal akhir, dan hari tanpa laporan. | T2–T3 |
| Status insiden | Insiden dinyatakan selesai jika memiliki setidaknya satu tindakan penanganan dan nilai stage pada seluruh tindakan tersebut adalah 100. | T4 |
| Penyebab kecelakaan | Setiap penyebab dihitung sesuai jumlah kemunculannya dalam data kecelakaan. | T5 |
| Kondisi inspeksi | Item inspeksi dengan kategori kerusakan non-null tetap dihitung meskipun prioritasnya kosong. | T6 |
| Kecepatan transaksi | Rata-rata durasi (detik) dihitung hanya dari data durasi *booth* untuk setiap gardu dalam satu laporan. Nilai sebelum pembulatan dibandingkan dengan batas kelima indikator SPM serta batas SLA jika berlaku. Batas dan operator pembanding mengikuti konfigurasi ruas dan indikator saat pengujian. Konfigurasi tersebut menentukan kapan SLA berlaku dan digunakan untuk semua periode. Jika ada gardu yang gagal memenuhi suatu indikator dalam salah satu laporan pada periode yang dianalisis, indikator tersebut dinyatakan gagal untuk periode itu. | T7–T9 |

Sebagai contoh, T1-C2 meminta rata-rata durasi transaksi di Ruas BINSTA selama 25–30 Januari 2030. Perhitungan menggunakan laporan transaksi dari ruas tersebut dengan tanggal operasional 27 Januari 2030. Laporan ini memiliki enam data durasi booth masing-masing 10 detik dan satu data durasi longbooth sebesar 2 detik. Tabel 3.5 menunjukkan jumlah data dan total durasinya.

**Tabel 3.5 Perhitungan Rata-Rata Durasi pada T1-C2**

| Jenis data | Jumlah data | Total durasi (detik) |
| ----- | ----- | ----- |
| *booth* | 6 | 60 |
| *longbooth* | 1 | 2 |
| Total | 7 | 62 |

Pada T1-C2, total durasi *D* dihitung dari enam data durasi *booth* dan satu data durasi *longbooth* pada Tabel 3.5.

$$
D = (6 \times 10) + 2 = 62\ \text{detik}
$$

Seluruh data durasi bernilai non-null, sehingga jumlah data yang digunakan adalah *n = 7*. Rata-rata durasi *d̄* dihitung dengan membagi total durasi tersebut dengan jumlah data.

$$
\bar{d} = \frac{D}{n} = \frac{62}{7}\ \text{detik} \approx 8{,}86\ \text{detik}
$$

Rata-rata tersebut dibulatkan menjadi dua angka desimal, yaitu 8,86 detik, dan disimpan pada atribut average_transaction_duration bersama identitas ruas, periode, dan satuan. Lampiran 1 berisi ringkasan *expected result* seluruh kasus serta *prompt* dan *expected result* lengkap untuk T1-C2.

## 3.3. Penyusunan Prompt dan Konteks Bisnis

Kedua model menggunakan system prompt yang sama pada pengujian dengan dan tanpa konteks bisnis. System prompt ini menetapkan ALASKA sebagai asisten HKA TROM dan mengatur cara agen menjawab ketika informasi yang dibutuhkan tidak tersedia atau bertentangan.

| You're ALASKA, a personal assistant within HKA TROM. If required data, tools, scope, configuration, or business definitions are unavailable or conflict, state the specific gap. Do not invent values. Do not request a connection or use another endpoint. |
| :---- |

Prompt berisi pertanyaan analisis dan ketentuan jawaban. Pada pengujian dengan konteks bisnis, agen juga memiliki akses ke dokumen yang dijelaskan pada Bagian 3.3.2.

### 3.3.1. Pertanyaan dan Format Jawaban

Setiap kasus menggunakan satu prompt yang berisi pertanyaan analisis dan ketentuan jawaban, tanpa menyertakan nama tabel, rumus, atau langkah penyelesaian. Blok output_schema berisi JSON Schema yang menentukan atribut, tipe data, dan nilai status yang diperbolehkan dalam jawaban. Instruksi pada blok ini juga mengatur penulisan nama sesuai data sumber, pembulatan angka, dan urutan array.

Sebagai contoh, Tabel 3.6 menyajikan *prompt* T2-C1 yang digunakan dalam pengujian. Prompt ini tidak menjelaskan jumlah hari yang digunakan untuk menghitung LHR ataupun cara memperhitungkan hari tanpa laporan.

**Tabel 3.6 *Prompt* T2-C1**

| Bagian | Isi prompt |
| ----- | ----- |
| Pertanyaan | Berikan ringkasan lalu lintas Ruas PEKBANG untuk 1–7 Maret 2030: total volume, LHR, dan volume per golongan kendaraan. |
| Instruksi output | `<output_schema>` Kembalikan tepat satu objek JSON yang sesuai dengan skema berikut, tanpa teks tambahan atau blok kode. Gunakan ejaan nama sesuai data sumber. Tampilkan LHR sebagai integer; bulatkan ke bilangan terdekat dengan nilai tengah menjauh dari nol. Urutkan by_vehicle_class berdasarkan vehicle_class_id menaik. |
| JSON Schema | {   "$schema": "https://json-schema.org/draft/2020-12/schema",   "title": "T2 Traffic summary",   "type": "object",   "properties": {     "section_id": {       "type": "integer"     },     "section_name": {       "type": "string"     },     "period": {       "type": "object",       "properties": {         "start": {           "type": "string",           "format": "date"         },         "end": {           "type": "string",           "format": "date"         }       },       "required": [         "start",         "end"       ],       "additionalProperties": false     },     "total_volume": {       "type": "integer",       "minimum": 0     },     "lhr": {       "type": "integer",       "minimum": 0     },     "by_vehicle_class": {       "type": "array",       "items": {         "type": "object",         "properties": {           "vehicle_class_id": {             "type": "integer"           },           "vehicle_class_name": {             "type": "string"           },           "volume": {             "type": "integer",             "minimum": 0           }         },         "required": [           "vehicle_class_id",           "vehicle_class_name",           "volume"         ],         "additionalProperties": false       }     }   },   "required": [     "section_id",     "section_name",     "period",     "total_volume",     "lhr",     "by_vehicle_class"   ],   "additionalProperties": false } `</output_schema>` |

### 3.3.2. Konteks Bisnis

Konteks bisnis dibuat berdasarkan pemahaman tentang sistem dan aturan bisnis yang didapat selama pengembangan HKA TROM. Isinya menjelaskan data dan aturan untuk analisis transaksi, lalu lintas, insiden, inspeksi, serta SPM/SLA yang diuji.

Konteks bisnis diberikan dalam bentuk skill hka-trom-business-context, yang terdiri atas SKILL.md dan enam dokumen referensi dalam folder references. Tabel 3.7 merangkum isi setiap dokumen dan fungsinya bagi agen.

**Tabel 3.7 Susunan dan Fungsi Dokumen Konteks Bisnis**

| Dokumen | Isi utama | Fungsi bagi agen |
| :---- | :---- | :---- |
| SKILL.md | Ruang lingkup sistem, instruksi umum, dan panduan memilih referensi. | Mengarahkan agen ke referensi yang sesuai dengan prompt. |
| terminology.md | Istilah operasional, identitas ruas, gerbang, gardu, dan shift, serta tanggal operasional dan relasi tabel. | Memahami istilah dalam prompt dan memilih data yang sesuai. |
| transactions.md | Penjelasan laporan pemantauan transaksi dan data durasinya, termasuk satuan dan perhitungan rata-rata. | Memilih data durasi yang sesuai untuk menghitung rata-rata durasi transaksi. |
| traffic.md | Volume kendaraan, golongan kendaraan, rentang tanggal, perhitungan LHR, dan ringkasan bulanan. | Menghitung volume kendaraan dan mengelompokkan hasil berdasarkan periode yang ditanyakan. LHR dihitung menggunakan jumlah hari kalender pada periode tersebut. |
| incidents.md | Data insiden dan tindakan penanganannya, cara menentukan status insiden, serta penyebab kecelakaan. | Menentukan status insiden dengan memeriksa semua tindakan penanganannya serta menghitung frekuensi setiap penyebab kecelakaan. |
| inspections.md | Struktur data inspeksi, kriteria dan kategori kerusakan, prioritas perbaikan, serta relasi tabel yang menghubungkan inspeksi dengan aset. | Menghitung item inspeksi yang memiliki kategori kerusakan, lalu mengelompokkan hasilnya berdasarkan kategori, prioritas perbaikan, dan aset. |
| spm-sla.md | Indikator, konfigurasi, perhitungan durasi per gardu, syarat untuk memenuhi SPM/SLA, dan cara menentukan status per periode. | Menilai apakah setiap gardu memenuhi SPM/SLA, lalu menentukan status per periode dan membandingkan hasil antar periode. |

Untuk prompt yang mencakup beberapa topik analisis, SKILL.md memberi petunjuk berikut:

| Read the reference for each domain involved in the request. For a request spanning domains, use each relevant reference. |
| :---- |

Sebagai contoh, SKILL.md mengarahkan agen membaca transactions.md dan spm-sla.md untuk mengevaluasi durasi transaksi menurut aturan SPM/SLA. Konteks bisnis yang digunakan dalam pengujian ini dilampirkan pada Lampiran 3.

## 3.4. Generasi Jawaban oleh LLM

### 3.4.1. Model dan Lingkungan Pengujian

Muse Spark 1.3 dan DeepSeek v4 Flash (DeepSeek-V4.1-Flash-1017) dijalankan melalui OpenCode pada Cloudflare OS (Cloudflare, 2026). Ada atau tidaknya konteks bisnis dalam pengujian diatur melalui Cloudflare OS sebagai lingkungan agen.

Pengaturan pada Tabel 3.8 dipertahankan selama pengujian dengan dan tanpa konteks bisnis. Parameter *sampling* mengikuti nilai *default* dari *provider* masing-masing model.

**Tabel 3.8 Pengaturan Model pada Pengujian**

| Pengaturan pengujian | Muse Spark 1.3 | DeepSeek v4 Flash |
| ----- | :---: | :---: |
| *Reasoning* | High | High |
| *Context window* (token) | 1.048.576 | 1.048.576 |
| Batas *output* (token) | 131.072 | 384.000 |
| *Temperature* | 1,0 | 1,0 |
| top_p | 1,0 | 1,0 |

Sumber: konfigurasi pengujian, DeepSeek (2026b), serta dokumentasi API dan konfigurasi OpenCode dari Meta (2026d, 2026e).

Gambar 3.2 menunjukkan alur pelaksanaan pengujian pada setiap model dan kondisi konteks bisnis, termasuk tiga pengulangan untuk setiap kasus.

*Gambar 3.2 Alur Pelaksanaan Pengujian*

### 3.4.2. Akses Data

Akses ke data HKA TROM menggunakan MCP seperti yang dijelaskan pada Bagian 2.4.1. Agen memilih *tool* dan parameter *input*, kemudian MCP server menjalankan permintaan dan mengembalikan hasilnya. Tiga *tool* disediakan agar agen dapat menemukan sumber data, melihat skema, dan membaca data yang diperlukan.

list_entities menampilkan tabel dan *view* yang dapat dibaca tanpa memerlukan parameter *input*. Untuk melihat skema sumber data yang dipilih, describe_entity menerima nama entitas dan mengembalikan informasi kolom, *primary key*, *foreign key*, serta filter yang tersedia.

read_records mengambil satu halaman data berdasarkan entitas, kolom, filter, urutan, limit, dan cursor. Agen dapat melanjutkan pembacaan melalui cursor, lalu menggabungkan data dan menghitung jawaban dari hasil yang diperoleh. Tabel 3.9 merangkum *input* dan kegunaan ketiga *tool* akses data.

**Tabel 3.9 Tool Akses Data HKA TROM**

| *Tool* | Input utama | Kegunaan |
| ----- | ----- | ----- |
| list_entities | Tanpa parameter | Menampilkan tabel dan view yang dapat dibaca |
| describe_entity | Nama entitas | Mengembalikan informasi kolom, primary key, foreign key, dan filter yang tersedia |
| read_records | Entitas, kolom, filter, urutan, limit, cursor | Mengembalikan satu halaman data sesuai kolom, filter, dan urutan yang diminta |

Rincian parameter, filter, dan pagination disajikan pada Lampiran 2.

### 3.4.3. Prosedur Generasi Jawaban

Pada evaluasi utama τ-bench, setiap tugas dijalankan sedikitnya tiga kali (Yao dkk., 2025). Data Interpreter melaporkan rata-rata hasil dari tiga eksekusi pada evaluasi tugas *open-ended* (Hong dkk., 2025).

Setiap kasus dalam penelitian ini dijalankan tiga kali pada masing-masing model, baik dengan ataupun tanpa konteks bisnis, untuk memeriksa konsistensi keberhasilan agen. Pada setiap pengulangan, agen menerima *prompt* dalam percakapan baru, kemudian membaca data melalui *tool* dan menghitung jawaban sesuai permintaan. Ketiga jawaban akhir dibandingkan dengan *expected result* yang sama untuk kasus tersebut.

## 3.5. Evaluasi Hasil Generasi

Setiap jawaban akhir agen dibandingkan dengan *expected result* untuk menentukan status PASS atau FAIL. Cara penilaian per pertanyaan ini juga digunakan dalam InfiAgent-DABench (Hu dkk., 2024).

### 3.5.1. Perbandingan Respons dan *Expected Result*

Jawaban dinilai PASS jika merupakan JSON yang valid dan seluruh struktur serta nilainya sesuai dengan *expected result*. Perbandingan mencakup seluruh atribut, nilai, dan urutan elemen array. Urutan properti dalam JSON tidak memengaruhi penilaian.

Angka dibandingkan berdasarkan nilainya tanpa toleransi tambahan. Misalnya, nilai 10 dan 10.0 dinilai sama.

Tabel 3.10 menunjukkan contoh penilaian PASS dan FAIL pada dua jawaban agen untuk kasus T5-C1 tentang distribusi penyebab kecelakaan di Ruas PEKBANG selama April 2030.

**Tabel 3.10 Contoh Evaluasi PASS dan FAIL pada T5-C1**

| Bagian | Isi JSON |
| ----- | ----- |
| *Expected result* | {   "section_id": 1,   "section_name": "PEKANBARU -  BANGKINANG (PEKBANG)",   "period": {     "start": "2030-04-01",     "end": "2030-04-30"   },   "total_cause_assignments": 5,   "causes": [     {       "cause_id": 49,       "cause_name": "Mengantuk",       "assignment_count": 4     },     {       "cause_id": 50,       "cause_name": "Kelalaian Pengemudi",       "assignment_count": 1     }   ] } |
| Jawaban A (PASS) | {   "section_id": 1,   "section_name": "PEKANBARU -  BANGKINANG (PEKBANG)",   "period": {     "start": "2030-04-01",     "end": "2030-04-30"   },   "total_cause_assignments": 5,   "causes": [     {       "cause_id": 49,       "cause_name": "Mengantuk",       "assignment_count": 4     },     {       "cause_id": 50,       "cause_name": "Kelalaian Pengemudi",       "assignment_count": 1     }   ] } |
| Jawaban B (FAIL) | {   "section_id": 1,   "section_name": "PEKANBARU -  BANGKINANG (PEKBANG)",   "period": {     "start": "2030-04-01",     "end": "2030-04-30"   },   "total_cause_assignments": 7,   "causes": [     {       "cause_id": 49,       "cause_name": "Mengantuk",       "assignment_count": 4     },     {       "cause_id": 50,       "cause_name": "Kelalaian Pengemudi",       "assignment_count": 2     },     {       "cause_id": 51,       "cause_name": "Kondisi Jalan",       "assignment_count": 1     }   ] } |

Jawaban A dinilai PASS karena seluruh atribut dan nilainya sesuai dengan *expected result*. Pada Jawaban B, assignment_count untuk cause_id 50 bernilai 2, sedangkan nilai yang diharapkan adalah 1. Jawaban ini juga menambahkan objek dengan cause_id 51 pada array causes. Nilai total_cause_assignments pada Jawaban B adalah 7, sedangkan pada *expected result* nilainya 5. Perbedaan tersebut menyebabkan Jawaban B dinilai FAIL.

### 3.5.2. Perhitungan Tingkat Keberhasilan

Tingkat keberhasilan dinyatakan sebagai persentase jawaban PASS dari seluruh jawaban yang dinilai, dengan perhitungan berikut.

$$
\text{Tingkat keberhasilan} = \frac{\text{Jumlah jawaban PASS}}{\text{Jumlah jawaban yang dinilai}} \times 100\%
$$

Setiap model menghasilkan 45 jawaban pada setiap kondisi konteks bisnis, dari 15 kasus yang masing-masing dijalankan tiga kali. Persentase pada setiap tabel dihitung dari jumlah jawaban untuk kasus, model, dan kondisi konteks bisnis yang ditampilkan.

Untuk setiap kasus pada model dan kondisi konteks bisnis yang sama, jumlah PASS disajikan sebagai 0/3 hingga 3/3.

### 3.5.3. Analisis Perbandingan Hasil

Analisis dilakukan secara deskriptif. Hasil pengujian dikelompokkan berdasarkan model dan ada atau tidaknya konteks bisnis. Tingkat keberhasilan setiap kelompok disajikan, kemudian hasil kedua model dibandingkan pada kondisi konteks bisnis yang sama. Untuk setiap model, hasil dengan konteks bisnis juga dibandingkan dengan hasil tanpa konteks bisnis.

Pembahasan dibagi menjadi enam kelompok analisis: durasi transaksi (T1), volume lalu lintas dan LHR (T2–T3), insiden dan penyebab kecelakaan (T4–T5), inspeksi dan identitas aset (T6), SPM/SLA per laporan (T7), serta SPM/SLA periode dan antar periode (T8–T9). Jawaban yang dinilai FAIL diperiksa untuk melihat bagian yang tidak sesuai dengan *expected result*. Status PASS/FAIL pada tiga pengulangan dibandingkan untuk memeriksa konsistensi keberhasilan pada kasus, model, dan kondisi konteks bisnis yang sama.

# BAB IV — HASIL DAN PEMBAHASAN

Bab ini membahas hasil evaluasi *Agentic Business Intelligence* pada enam kelompok kebutuhan operasional HKA TROM. Pembahasan dimulai dengan lingkungan pengujian dan data penelitian, kemudian dilanjutkan dengan hasil setiap kelompok berdasarkan konteks bisnis, model, dan kombinasi keduanya. Bab ini diakhiri dengan interpretasi hasil pengujian.

## 4.1. Lingkungan Pengujian

Pengujian dilakukan pada Cloudflare OS dengan model Muse Spark 1.3 dan DeepSeek v4 Flash melalui *provider* OpenCode. Agen menggunakan *tool* melalui MCP untuk melihat daftar tabel dan *view*, melihat struktur tabel, dan membaca data HKA TROM. Lingkungan pengujian dirangkum pada Tabel 4.1.

**Tabel 4.1 Lingkungan Pengujian**

| Aspek | Keterangan |
| ----- | ----- |
| Lingkungan agen | Cloudflare OS |
| Model | Muse Spark 1.3 dan DeepSeek v4 Flash, melalui *provider* OpenCode |
| *Tool* akses data | list_entities, describe_entity, dan read_records |

## 4.2. Data Penelitian

Pengujian menggunakan 237 baris data sintetis. Data tersebut digunakan pada 15 kasus dari sembilan jenis tugas, T1 sampai T9, yang dibagi menjadi enam kelompok analisis.

Setiap kasus dijalankan tiga kali pada Muse Spark 1.3 dan DeepSeek v4 Flash, masing-masing dengan dan tanpa konteks bisnis. Keempat kombinasi tersebut menghasilkan 45 jawaban per kombinasi dan 180 jawaban secara keseluruhan. Tabel 4.2 menyajikan pembagian kasus dan jumlah jawaban untuk setiap kelompok analisis.

**Tabel 4.2 Distribusi Kasus dan Jawaban menurut Kelompok Analisis**

| Kelompok analisis | Jenis tugas | Kasus | Jawaban per kombinasi | Total jawaban |
| ----- | ----- | :---: | :---: | :---: |
| Durasi transaksi | T1 | 2 | 6 | 24 |
| Volume lalu lintas dan LHR | T2, T3 | 2 | 6 | 24 |
| Insiden dan penyebab kecelakaan | T4, T5 | 2 | 6 | 24 |
| Inspeksi dan identitas aset | T6 | 1 | 3 | 12 |
| SPM/SLA per laporan | T7 | 4 | 12 | 48 |
| SPM/SLA periode dan antar periode | T8, T9 | 4 | 12 | 48 |
| Total | Sembilan jenis tugas | 15 | 45 | 180 |

## 4.3. Analisis Hasil pada Durasi Transaksi

### 4.3.1. Berdasarkan Ketersediaan Konteks Bisnis

Pengujian durasi transaksi mencakup T1-C1 dan T1-C2. Hasil pengujian dengan dan tanpa konteks bisnis disajikan pada Tabel 4.3. Setiap kondisi mencakup 12 jawaban dari kedua model.

**Tabel 4.3 Hasil Durasi Transaksi menurut Konteks Bisnis**

| Konteks bisnis | PASS/Total jawaban | Tingkat keberhasilan |
| ----- | :---: | :---: |
| Dengan konteks bisnis | 12/12 | 100,00% |
| Tanpa konteks bisnis | 12/12 | 100,00% |

Kedua kondisi memperoleh 12/12 PASS atau 100,00%. Pada T1-C1, nilai rata-rata yang dihasilkan sesuai dengan *expected result* meskipun setiap laporan memiliki jumlah data durasi yang berbeda. Jawaban T1-C2 juga sesuai dengan *expected result* yang dihitung dari data *booth* dan *longbooth*.

### 4.3.2. Berdasarkan Model

Perbandingan kedua model menggunakan hasil T1-C1 dan T1-C2 pada pengujian dengan dan tanpa konteks bisnis. Tabel 4.4 merangkum 12 jawaban dari masing-masing model.

**Tabel 4.4 Hasil Durasi Transaksi menurut Model**

| Model | PASS/Total jawaban | Tingkat keberhasilan |
| ----- | :---: | :---: |
| Muse Spark 1.3 | 12/12 | 100,00% |
| DeepSeek v4 Flash | 12/12 | 100,00% |

Muse Spark 1.3 dan DeepSeek v4 Flash sama-sama memperoleh 12/12 PASS. Nilai rata-rata yang dihasilkan adalah 23,09 detik pada T1-C1 dan 8,86 detik pada T1-C2, sesuai dengan *expected result*.

### 4.3.3. Berdasarkan Kombinasi Model dan Konteks Bisnis

Pada setiap kombinasi model dan konteks bisnis, T1-C1 dan T1-C2 diuji sebanyak tiga kali. Tabel 4.5 menunjukkan hasil enam jawaban pada masing-masing kombinasi.

**Tabel 4.5 Hasil Durasi Transaksi menurut Kombinasi Model dan Konteks Bisnis**

| Model | Konteks bisnis | PASS/Total jawaban | Tingkat keberhasilan |
| ----- | ----- | :---: | :---: |
| Muse Spark 1.3 | Dengan konteks bisnis | 6/6 | 100,00% |
| Muse Spark 1.3 | Tanpa konteks bisnis | 6/6 | 100,00% |
| DeepSeek v4 Flash | Dengan konteks bisnis | 6/6 | 100,00% |
| DeepSeek v4 Flash | Tanpa konteks bisnis | 6/6 | 100,00% |

Keempat kombinasi memperoleh 6/6 PASS atau 100,00%. Pada masing-masing kombinasi, T1-C1 dan T1-C2 memperoleh 3/3 PASS.

## 4.4. Analisis Hasil pada Volume Lalu Lintas dan LHR

### 4.4.1. Berdasarkan Ketersediaan Konteks Bisnis

Kelompok volume lalu lintas dan LHR mencakup T2-C1 untuk ringkasan mingguan dan T3-C1 untuk tren bulanan. Hasil kedua kasus dibandingkan pada kondisi dengan dan tanpa konteks bisnis. Setiap kondisi mencakup 12 jawaban dari kedua model, seperti ditampilkan pada Tabel 4.6.

**Tabel 4.6 Hasil Volume Lalu Lintas dan LHR menurut Konteks Bisnis**

| Konteks bisnis | PASS/Total jawaban | Tingkat keberhasilan |
| ----- | :---: | :---: |
| Dengan konteks bisnis | 12/12 | 100,00% |
| Tanpa konteks bisnis | 8/12 | 66,67% |

Dengan konteks bisnis, seluruh 12 jawaban memperoleh PASS. Tanpa konteks bisnis, delapan dari 12 jawaban memperoleh PASS atau 66,67%. Keempat jawaban yang gagal berasal dari T3-C1 dan tidak mencantumkan seluruh golongan kendaraan yang diminta dalam *prompt*. Pada T2-C1, total volume, LHR, dan rincian golongan pada seluruh jawaban sesuai dengan *expected result*.

### 4.4.2. Berdasarkan Model

Perbandingan Muse Spark 1.3 dan DeepSeek v4 Flash pada Tabel 4.7 mencakup hasil T2-C1 dan T3-C1. Setiap model menghasilkan 12 jawaban, terdiri atas enam jawaban dengan konteks bisnis dan enam jawaban tanpa konteks bisnis.

**Tabel 4.7 Hasil Volume Lalu Lintas dan LHR menurut Model**

| Model | PASS/Total jawaban | Tingkat keberhasilan |
| ----- | :---: | :---: |
| Muse Spark 1.3 | 11/12 | 91,67% |
| DeepSeek v4 Flash | 9/12 | 75,00% |

Muse Spark 1.3 memperoleh 11/12 PASS atau 91,67%, sedangkan DeepSeek v4 Flash memperoleh 9/12 PASS atau 75,00%. Kedua model memperoleh hasil yang sama ketika konteks bisnis tersedia. Perbedaan hasil muncul pada T3-C1 tanpa konteks bisnis, ketika sebagian jawaban tidak mencantumkan seluruh golongan kendaraan.

### 4.4.3. Berdasarkan Kombinasi Model dan Konteks Bisnis

Tabel 4.8 menunjukkan hasil empat kombinasi model dan konteks bisnis pada T2-C1 dan T3-C1. Setiap kombinasi menghasilkan enam jawaban dari tiga pengulangan pada kedua kasus.

**Tabel 4.8 Hasil Volume Lalu Lintas dan LHR menurut Kombinasi Model dan Konteks Bisnis**

| Model | Konteks bisnis | PASS/Total jawaban | Tingkat keberhasilan |
| ----- | ----- | :---: | :---: |
| Muse Spark 1.3 | Dengan konteks bisnis | 6/6 | 100,00% |
| Muse Spark 1.3 | Tanpa konteks bisnis | 5/6 | 83,33% |
| DeepSeek v4 Flash | Dengan konteks bisnis | 6/6 | 100,00% |
| DeepSeek v4 Flash | Tanpa konteks bisnis | 3/6 | 50,00% |

Dengan konteks bisnis, Muse Spark 1.3 dan DeepSeek v4 Flash masing-masing memperoleh 6/6 PASS. Tanpa konteks bisnis, Muse Spark 1.3 memperoleh 5/6 PASS dan DeepSeek v4 Flash memperoleh 3/6 PASS. Seluruh jawaban T2-C1 memperoleh PASS pada keempat kombinasi.

Pada T3-C1, *expected result* berisi Gol. 5 untuk Januari dan Februari dengan volume 0 dan LHR 0. Tanpa konteks bisnis, Gol. 5 untuk kedua bulan itu tidak ada dalam jawaban Muse Spark 1.3 pada pengulangan kedua ataupun DeepSeek v4 Flash pada ketiga pengulangan. Keempat jawaban dinilai FAIL karena ringkasan golongan kendaraan tidak lengkap, meskipun nilai yang dicantumkan sudah sesuai dengan *expected result*.

Pada ketiga pengulangan DeepSeek v4 Flash tanpa konteks bisnis, agen membuat daftar golongan kendaraan berdasarkan data volume yang ada pada setiap bulan. Gol. 5 tidak ada dalam data volume untuk Januari dan Februari, sehingga tidak dicantumkan dalam ringkasan. Sebagai pembanding, pada pengulangan pertama dengan konteks bisnis, DeepSeek v4 Flash menggunakan seluruh golongan kendaraan dari data master. Jika tidak ada data volume untuk suatu golongan, agen mencantumkan volume 0 dan LHR 0, sehingga Gol. 5 tetap dicantumkan untuk kedua bulan itu.

## 4.5. Analisis Hasil pada Insiden dan Penyebab Kecelakaan

### 4.5.1. Berdasarkan Ketersediaan Konteks Bisnis

Pengujian pada kelompok ini mencakup penentuan status insiden pada T4-C1 dan distribusi penyebab kecelakaan pada T5-C1. Tabel 4.9 merangkum hasil dengan dan tanpa konteks bisnis, dengan 12 jawaban pada setiap kondisi.

**Tabel 4.9 Hasil Insiden dan Penyebab Kecelakaan menurut Konteks Bisnis**

| Konteks bisnis | PASS/Total jawaban | Tingkat keberhasilan |
| ----- | :---: | :---: |
| Dengan konteks bisnis | 12/12 | 100,00% |
| Tanpa konteks bisnis | 10/12 | 83,33% |

Dengan konteks bisnis, seluruh 12 jawaban memperoleh PASS. Tanpa konteks bisnis, 10 dari 12 jawaban memperoleh PASS atau 83,33%. Kedua jawaban yang gagal berasal dari T5-C1. Pada T4-C1, jumlah dan status insiden pada seluruh jawaban sesuai dengan *expected result*, yaitu empat insiden dengan tiga masih ditangani dan satu selesai.

### 4.5.2. Berdasarkan Model

Hasil pengujian T4-C1 dan T5-C1 berdasarkan model ditampilkan pada Tabel 4.10. Setiap model menghasilkan 12 jawaban dari pengujian dengan dan tanpa konteks bisnis.

**Tabel 4.10 Hasil Insiden dan Penyebab Kecelakaan menurut Model**

| Model | PASS/Total jawaban | Tingkat keberhasilan |
| ----- | :---: | :---: |
| Muse Spark 1.3 | 10/12 | 83,33% |
| DeepSeek v4 Flash | 12/12 | 100,00% |

Muse Spark 1.3 memperoleh 10/12 PASS atau 83,33%, sedangkan DeepSeek v4 Flash memperoleh 12/12 PASS atau 100,00%. Seluruh kegagalan Muse Spark 1.3 berasal dari T5-C1 tanpa konteks bisnis. Dengan konteks bisnis, hasil kedua model sama-sama sesuai dengan *expected result* pada kedua kasus.

### 4.5.3. Berdasarkan Kombinasi Model dan Konteks Bisnis

Perbandingan empat kombinasi model dan konteks bisnis pada Tabel 4.11 mencakup T4-C1 dan T5-C1. Setiap kombinasi menghasilkan enam jawaban dari tiga pengulangan pada kedua kasus.

**Tabel 4.11 Hasil Insiden dan Penyebab Kecelakaan menurut Kombinasi Model dan Konteks Bisnis**

| Model | Konteks bisnis | PASS/Total jawaban | Tingkat keberhasilan |
| ----- | ----- | :---: | :---: |
| Muse Spark 1.3 | Dengan konteks bisnis | 6/6 | 100,00% |
| Muse Spark 1.3 | Tanpa konteks bisnis | 4/6 | 66,67% |
| DeepSeek v4 Flash | Dengan konteks bisnis | 6/6 | 100,00% |
| DeepSeek v4 Flash | Tanpa konteks bisnis | 6/6 | 100,00% |

Muse Spark 1.3 memperoleh 6/6 PASS dengan konteks bisnis dan 4/6 PASS tanpa konteks bisnis. DeepSeek v4 Flash memperoleh 6/6 PASS pada kedua kondisi. Dua jawaban yang gagal berasal dari T5-C1 pada pengulangan pertama dan ketiga Muse Spark 1.3 tanpa konteks bisnis.

Pada T5-C1, perhitungan penyebab kecelakaan hanya menggunakan data insiden dengan is_accident = true. Nilai total_cause_assignments pada kedua jawaban yang gagal adalah 7, sedangkan nilainya pada *expected result* adalah 5. Tabel 4.12 menunjukkan rincian perbedaannya.

**Tabel 4.12 Perbedaan Jawaban pada T5-C1**

| Komponen output | *Expected result* | Muse Spark 1.3 tanpa konteks bisnis, pengulangan 1 dan 3 |
| ----- | ----- | :---: |
| assignment_count untuk Mengantuk | 4 | 4 |
| assignment_count untuk Kelalaian Pengemudi | 1 | 2 |
| assignment_count untuk Kondisi Jalan | Tidak ada dalam *expected result* | 1 |
| total_cause_assignments | 5 | 7 |

Pada pengulangan pertama dan ketiga tanpa konteks bisnis, Muse Spark 1.3 membaca data dari empat insiden yang sesuai dengan ruas dan tanggal dalam *prompt*. Salah satu insiden memiliki is_accident = false. Laporan kecelakaannya berisi Kelalaian Pengemudi dan Kondisi Jalan masing-masing satu kali.

Pada pengulangan ketiga dengan konteks bisnis, Muse Spark 1.3 membaca aturan bahwa hanya data insiden dengan is_accident = true yang digunakan untuk menghitung penyebab kecelakaan. Agen menggunakan laporan dari tiga insiden yang memenuhi syarat ini. Nilai total_cause_assignments pada jawabannya adalah 5, sesuai dengan *expected result*.

## 4.6. Analisis Hasil pada Inspeksi dan Identitas Aset

### 4.6.1. Berdasarkan Ketersediaan Konteks Bisnis

Pada T6-C1, hasil ringkasan kerusakan dibandingkan antara kondisi dengan dan tanpa konteks bisnis. Setiap kondisi mencakup enam jawaban dari kedua model. Tabel 4.13 menyajikan hasil perbandingan tersebut.

**Tabel 4.13 Hasil Inspeksi dan Identitas Aset menurut Konteks Bisnis**

| Konteks bisnis | PASS/Total jawaban | Tingkat keberhasilan |
| ----- | :---: | :---: |
| Dengan konteks bisnis | 6/6 | 100,00% |
| Tanpa konteks bisnis | 6/6 | 100,00% |

Kedua kondisi memperoleh 6/6 PASS. Seluruh jawaban mencakup empat item rusak, termasuk satu item yang tidak mempunyai prioritas. Jumlah item dengan prioritas P1 atau P2 adalah tiga, sedangkan jumlah item rusak tetap empat karena item tanpa prioritas juga dihitung.

### 4.6.2. Berdasarkan Model

Perbandingan Muse Spark 1.3 dan DeepSeek v4 Flash mencakup hasil T6-C1 pada kondisi dengan dan tanpa konteks bisnis. Setiap model menghasilkan enam jawaban, dengan hasil seperti pada Tabel 4.14.

**Tabel 4.14 Hasil Inspeksi dan Identitas Aset menurut Model**

| Model | PASS/Total jawaban | Tingkat keberhasilan |
| ----- | :---: | :---: |
| Muse Spark 1.3 | 6/6 | 100,00% |
| DeepSeek v4 Flash | 6/6 | 100,00% |

Muse Spark 1.3 dan DeepSeek v4 Flash sama-sama memperoleh 6/6 PASS. Rincian kategori, prioritas, dan identitas aset pada jawaban kedua model sesuai dengan *expected result*. Pada rincian aset, tiga item tercatat pada Bahu dan satu item pada Lajur 1.

### 4.6.3. Berdasarkan Kombinasi Model dan Konteks Bisnis

Tabel 4.15 memperlihatkan hasil setiap kombinasi model dan konteks bisnis pada tiga pengulangan T6-C1.

**Tabel 4.15 Hasil Inspeksi dan Identitas Aset menurut Kombinasi Model dan Konteks Bisnis**

| Model | Konteks bisnis | PASS/Total jawaban | Tingkat keberhasilan |
| ----- | ----- | :---: | :---: |
| Muse Spark 1.3 | Dengan konteks bisnis | 3/3 | 100,00% |
| Muse Spark 1.3 | Tanpa konteks bisnis | 3/3 | 100,00% |
| DeepSeek v4 Flash | Dengan konteks bisnis | 3/3 | 100,00% |
| DeepSeek v4 Flash | Tanpa konteks bisnis | 3/3 | 100,00% |

Keempat kombinasi memperoleh 3/3 PASS, sehingga jawaban T6-C1 sesuai dengan *expected result* pada seluruh pengulangan.

## 4.7. Analisis Hasil pada SPM dan SLA per Laporan

### 4.7.1. Berdasarkan Ketersediaan Konteks Bisnis

Perbandingan konteks bisnis pada evaluasi SPM/SLA per laporan mencakup T7-C1 hingga T7-C4. Setiap kondisi memiliki 24 jawaban dari kedua model. Hasil pengujian dirangkum pada Tabel 4.16.

**Tabel 4.16 Hasil SPM/SLA per Laporan menurut Konteks Bisnis**

| Konteks bisnis | PASS/Total jawaban | Tingkat keberhasilan |
| ----- | :---: | :---: |
| Dengan konteks bisnis | 24/24 | 100,00% |
| Tanpa konteks bisnis | 20/24 | 83,33% |

Dengan konteks bisnis, seluruh 24 jawaban memperoleh PASS. Tanpa konteks bisnis, 20 dari 24 jawaban memperoleh PASS atau 83,33%. Keempat jawaban yang gagal berasal dari T7-C1 dan T7-C2. Terdapat tiga jawaban dengan status SPM/SLA salah dan satu jawaban yang tidak mencantumkan seluruh hasil evaluasi yang diminta.

### 4.7.2. Berdasarkan Model

Tabel 4.17 menyajikan hasil Muse Spark 1.3 dan DeepSeek v4 Flash pada kelompok SPM/SLA per laporan. Setiap model memiliki 24 jawaban yang mencakup pengujian dengan dan tanpa konteks bisnis.

**Tabel 4.17 Hasil SPM/SLA per Laporan menurut Model**

| Model | PASS/Total jawaban | Tingkat keberhasilan |
| ----- | :---: | :---: |
| Muse Spark 1.3 | 23/24 | 95,83% |
| DeepSeek v4 Flash | 21/24 | 87,50% |

Muse Spark 1.3 memperoleh 23/24 PASS atau 95,83%, sedangkan DeepSeek v4 Flash memperoleh 21/24 PASS atau 87,50%. Perbedaan hasil kedua model muncul pada pengujian tanpa konteks bisnis. Ketika konteks bisnis tersedia, seluruh jawaban kedua model sesuai dengan *expected result*.

### 4.7.3. Berdasarkan Kombinasi Model dan Konteks Bisnis

Hasil setiap kombinasi model dan konteks bisnis disajikan pada Tabel 4.18. Setiap kombinasi mencakup 12 jawaban dari tiga pengulangan pada keempat kasus.

**Tabel 4.18 Hasil SPM/SLA per Laporan menurut Kombinasi Model dan Konteks Bisnis**

| Model | Konteks bisnis | PASS/Total jawaban | Tingkat keberhasilan |
| ----- | ----- | :---: | :---: |
| Muse Spark 1.3 | Dengan konteks bisnis | 12/12 | 100,00% |
| Muse Spark 1.3 | Tanpa konteks bisnis | 11/12 | 91,67% |
| DeepSeek v4 Flash | Dengan konteks bisnis | 12/12 | 100,00% |
| DeepSeek v4 Flash | Tanpa konteks bisnis | 9/12 | 75,00% |

Dengan konteks bisnis, Muse Spark 1.3 dan DeepSeek v4 Flash masing-masing memperoleh 12/12 PASS. Tanpa konteks bisnis, Muse Spark 1.3 memperoleh 11/12 PASS dan DeepSeek v4 Flash memperoleh 9/12 PASS. T7-C3 dan T7-C4 memperoleh 3/3 PASS pada seluruh kombinasi. Keempat jawaban yang gagal berasal dari T7-C1 dan T7-C2, dengan rincian pada Tabel 4.19.

**Tabel 4.19 Ketidaksesuaian Jawaban SPM/SLA per Laporan tanpa Konteks Bisnis**

| Kasus | Model dan pengulangan | Bagian jawaban | *Expected result* | Jawaban agen |
| ----- | ----- | ----- | :---: | ----- |
| T7-C1 | DeepSeek v4 Flash, ke-2 | Gardu 3, indikator 1: spm_passed dan sla_passed | false, false | true, true |
| T7-C2 | Muse Spark 1.3, ke-2 | Gardu 4, indikator 3: spm_passed dan sla_passed | false, false | true, true |
| T7-C2 | DeepSeek v4 Flash, ke-1 | Gardu 4, indikator 3: spm_passed dan sla_passed | false, false | true, true |
| T7-C2 | DeepSeek v4 Flash, ke-3 | Jumlah evaluasi | 20 | 4, seluruhnya indikator 3 |

Terdapat tiga jawaban dengan status SPM/SLA salah untuk gardu dengan rata-rata durasi yang selisih sedikit di atas batas. Status SPM/SLA ditentukan dengan membandingkan rata-rata durasi sebelum pembulatan dengan batas indikator. Pada T7-C1, rata-rata durasi gardu 3 adalah 6,004 detik, yang melebihi batas 6 detik pada indikator pertama. Pada pengulangan kedua tanpa konteks bisnis, DeepSeek v4 Flash membulatkan rata-rata durasi ini menjadi 6,00 detik sebelum membandingkannya dengan batas 6 detik, sehingga spm_passed dan sla_passed bernilai true. Pada pengulangan kedua dengan konteks bisnis, agen membandingkan nilai 6,004 detik dengan batas 6 detik, sehingga kedua status bernilai false sesuai dengan *expected result*.

Pada T7-C2, rata-rata durasi gardu 4 adalah 9,004 detik, yang ditampilkan sebagai 9 detik setelah pembulatan. Nilai sebelum pembulatan melebihi batas 9 detik pada indikator ketiga, sehingga spm_passed dan sla_passed pada *expected result* bernilai false. Tanpa konteks bisnis, DeepSeek v4 Flash pada pengulangan pertama membandingkan nilai 9,00 detik setelah pembulatan dengan batas 9 detik, sehingga kedua status bernilai true. Kedua status juga bernilai true dalam jawaban Muse Spark 1.3 pada pengulangan kedua tanpa konteks bisnis.

Satu jawaban lain pada T7-C2 dinilai FAIL karena tidak berisi seluruh hasil evaluasi yang diminta. *Expected result* berisi 20 hasil evaluasi dari lima indikator pada empat gardu. Pada pengulangan ketiga tanpa konteks bisnis, DeepSeek v4 Flash membaca konfigurasi kelima indikator, lalu menggunakan indikator ketiga saja untuk menilai setiap gardu. Jawabannya berisi empat hasil evaluasi yang sesuai dengan *expected result*, sedangkan 16 hasil evaluasi lainnya tidak dicantumkan. Pada pengulangan ketiga dengan konteks bisnis, agen menilai setiap gardu menggunakan kelima indikator, sehingga jawabannya berisi 20 hasil evaluasi yang sesuai dengan *expected result*.

## 4.8. Analisis Hasil pada SPM/SLA Periode dan Antar Periode

### 4.8.1. Berdasarkan Ketersediaan Konteks Bisnis

Pada T8-C1 dan T8-C2, agen diminta menilai SPM/SLA selama satu periode. Pada T9-C1 dan T9-C2, agen diminta membandingkan status pemenuhan setiap indikator SPM/SLA pada dua periode. Hasil kedua jenis analisis pada kondisi dengan dan tanpa konteks bisnis disajikan pada Tabel 4.20.

**Tabel 4.20 Hasil SPM/SLA Periode dan Antar Periode menurut Konteks Bisnis**

| Konteks bisnis | PASS/Total jawaban | Tingkat keberhasilan |
| ----- | :---: | :---: |
| Dengan konteks bisnis | 24/24 | 100,00% |
| Tanpa konteks bisnis | 24/24 | 100,00% |

Kondisi dengan dan tanpa konteks bisnis masing-masing memperoleh 24/24 PASS. Status indikator pada satu periode dan perubahan status antar periode sesuai dengan *expected result* pada kedua kondisi.

### 4.8.2. Berdasarkan Model

Hasil Muse Spark 1.3 dan DeepSeek v4 Flash pada empat kasus periode dan antar periode disajikan pada Tabel 4.21. Setiap model menghasilkan 24 jawaban dari pengujian dengan dan tanpa konteks bisnis.

**Tabel 4.21 Hasil SPM/SLA Periode dan Antar Periode menurut Model**

| Model | PASS/Total jawaban | Tingkat keberhasilan |
| ----- | :---: | :---: |
| Muse Spark 1.3 | 24/24 | 100,00% |
| DeepSeek v4 Flash | 24/24 | 100,00% |

Kedua model memperoleh 24/24 PASS. Status, jumlah evaluasi, dan jumlah kegagalan yang dicantumkan pada jawaban sesuai dengan *expected result*. Pada evaluasi periode, SLA yang tidak berlaku untuk suatu indikator pada ruas yang dianalisis juga ditandai dengan not_applicable.

### 4.8.3. Berdasarkan Kombinasi Model dan Konteks Bisnis

Tabel 4.22 menyajikan hasil empat kombinasi pada T8-C1, T8-C2, T9-C1, dan T9-C2. Setiap kombinasi mencakup 12 jawaban dari tiga pengulangan pada keempat kasus.

**Tabel 4.22 Hasil SPM/SLA Periode dan Antar Periode menurut Kombinasi Model dan Konteks Bisnis**

| Model | Konteks bisnis | PASS/Total jawaban | Tingkat keberhasilan |
| ----- | ----- | :---: | :---: |
| Muse Spark 1.3 | Dengan konteks bisnis | 12/12 | 100,00% |
| Muse Spark 1.3 | Tanpa konteks bisnis | 12/12 | 100,00% |
| DeepSeek v4 Flash | Dengan konteks bisnis | 12/12 | 100,00% |
| DeepSeek v4 Flash | Tanpa konteks bisnis | 12/12 | 100,00% |

Keempat kombinasi memperoleh 12/12 PASS, dengan 3/3 PASS pada masing-masing kasus.

Pada T9-C2, jawaban pada seluruh kombinasi mencatat empat evaluasi yang gagal untuk indikator keempat pada periode A dan delapan pada periode B. Setiap periode memiliki delapan evaluasi untuk indikator tersebut. Status indikator tetap gagal pada kedua periode karena ada gardu yang gagal memenuhi indikator itu dalam salah satu laporan. Perubahan jumlah kegagalan tetap terlihat pada jawaban meskipun statusnya sama.

## 4.9. Interpretasi Hasil

Hasil pengujian pada enam kelompok analisis menunjukkan bahwa 170 dari 180 jawaban memperoleh PASS. Sepuluh jawaban yang dinilai FAIL berasal dari kondisi tanpa konteks bisnis.

Dengan konteks bisnis, Muse Spark 1.3 dan DeepSeek v4 Flash masing-masing memperoleh 45/45 PASS atau 100,00%. Tanpa konteks bisnis, Muse Spark 1.3 memperoleh 41/45 PASS atau 91,11%, sedangkan DeepSeek v4 Flash memperoleh 39/45 PASS atau 86,67%. Pada kasus yang diuji, kedua model memperoleh lebih banyak PASS ketika diberi konteks bisnis.

Tanpa konteks bisnis, Muse Spark 1.3 memperoleh lebih banyak PASS dibandingkan DeepSeek v4 Flash pada volume lalu lintas dan LHR serta SPM/SLA per laporan. DeepSeek v4 Flash memperoleh lebih banyak PASS pada insiden dan penyebab kecelakaan. Pada durasi transaksi, inspeksi aset, serta SPM/SLA periode dan antar periode, seluruh jawaban memperoleh PASS pada keempat kombinasi.

Kelengkapan jawaban ikut menentukan hasil evaluasi. Nilai yang dicantumkan dalam jawaban T3-C1 yang gagal dan satu jawaban T7-C2 sesuai dengan *expected result*. Jawaban tersebut dinilai FAIL karena rincian golongan kendaraan pada T3-C1 dan evaluasi indikator pada T7-C2 tidak lengkap.

Pada contoh T5-C1, agen memasukkan insiden dengan is_accident = false ke dalam perhitungan penyebab kecelakaan, padahal insiden tersebut seharusnya dikecualikan. Akibatnya, nilai total_cause_assignments pada jawaban menjadi 7, sedangkan nilai pada *expected result* adalah 5. Pada contoh T7-C1, agen membandingkan rata-rata durasi yang sudah dibulatkan dengan batas indikator, sehingga gardu dengan rata-rata durasi di atas batas dinyatakan memenuhi SPM/SLA.

Dengan konteks bisnis, kedua model memperoleh 15/15 PASS pada setiap pengulangan. Tanpa konteks bisnis, Muse Spark 1.3 memperoleh 14/15, 13/15, dan 14/15 PASS, sedangkan DeepSeek v4 Flash memperoleh 13/15 PASS pada masing-masing pengulangan.

Pada DeepSeek v4 Flash tanpa konteks bisnis, kasus yang gagal berubah antarpengulangan meskipun jumlah PASS tetap sama. T3-C1 memperoleh FAIL pada ketiga pengulangan. T7-C2 memperoleh FAIL pada pengulangan pertama dan ketiga, sedangkan T7-C1 memperoleh FAIL pada pengulangan kedua. Rekap hasil per kasus dan pengulangan disajikan pada Tabel L1.2 dan Tabel L1.3 dalam Lampiran 1.

Pengujian dilakukan pada 15 kasus dengan tiga pengulangan pada setiap kombinasi. Karena seluruh dokumen konteks bisnis diberikan bersama, pengaruh masing-masing dokumen terhadap ketepatan jawaban belum dapat diketahui. PASS menunjukkan kesesuaian jawaban dengan *expected result*, sedangkan manfaat jawaban bagi pengambilan keputusan operasional belum dinilai.

# BAB V — PENUTUP

Bab ini berisi kesimpulan dari evaluasi kemampuan *Agentic Business Intelligence* dengan HKA TROM sebagai studi kasus. Pembahasan mencakup ketepatan jawaban Muse Spark 1.3 dan DeepSeek v4 Flash pada pengujian dengan dan tanpa konteks bisnis, serta saran untuk penelitian selanjutnya.

## 5.1. Kesimpulan

Pada pengujian dengan konteks bisnis, Muse Spark 1.3 dan DeepSeek v4 Flash masing-masing memperoleh 45/45 PASS atau 100,00% dalam menjawab kasus analisis operasional HKA TROM. Tanpa konteks bisnis, Muse Spark 1.3 memperoleh 41/45 PASS atau 91,11%, sedangkan DeepSeek v4 Flash memperoleh 39/45 PASS atau 86,67%. Tingkat keberhasilan pada pengujian dengan konteks bisnis lebih tinggi sebesar 8,89 poin persentase untuk Muse Spark 1.3 dan 13,33 poin persentase untuk DeepSeek v4 Flash.

Dalam pengujian tanpa konteks bisnis, Muse Spark 1.3 memperoleh dua PASS lebih banyak daripada DeepSeek v4 Flash. Muse Spark 1.3 menghasilkan lebih banyak PASS pada volume lalu lintas dan LHR serta SPM/SLA per laporan, sementara DeepSeek v4 Flash menghasilkan lebih banyak PASS pada insiden dan penyebab kecelakaan. Untuk durasi transaksi, inspeksi aset, serta SPM/SLA periode dan antar periode, seluruh jawaban memperoleh PASS pada kedua model, baik dengan ataupun tanpa konteks bisnis.

Sepuluh jawaban FAIL seluruhnya berasal dari pengujian tanpa konteks bisnis. Pada T3-C1, empat jawaban tidak mencantumkan Gol. 5. Pada dua jawaban T5-C1, frekuensi Kelalaian Pengemudi terlalu besar dan terdapat kategori Kondisi Jalan yang tidak ada dalam *expected result*, sedangkan frekuensi Mengantuk tetap sesuai. Ketidaksesuaian pada T7-C1 dan T7-C2 mencakup tiga jawaban dengan status SPM/SLA yang salah, serta satu jawaban T7-C2 yang hanya berisi empat dari 20 hasil evaluasi yang diminta.

Seluruh 15 kasus memperoleh 3/3 PASS pada kedua model ketika konteks bisnis tersedia. Tanpa konteks bisnis, masing-masing model memperoleh 3/3 PASS pada 12 kasus, dengan kasus gagal yang berbeda antara kedua model.

Penilaian dilakukan terhadap struktur dan nilai jawaban akhir berdasarkan *expected result*. Kesimpulan ini terbatas pada 15 kasus yang masing-masing dijalankan tiga kali untuk setiap model dan kondisi pengujian.

## 5.2. Saran

Pengujian *Agentic Business Intelligence* selanjutnya sebaiknya mencakup data dari bidang bisnis lain dan tugas analisis yang lebih beragam. Evaluasi dapat mencakup ketepatan pemilihan data, kelengkapan jawaban, serta penerapan aturan bisnis. Pengaruh isi konteks bisnis dapat diperiksa dengan membandingkan konteks lengkap dan beberapa variasi yang masing-masing tidak menyertakan satu dokumen atau menggunakan tingkat detail berbeda untuk masing-masing aturan. Jumlah pengulangan dapat ditambah untuk mengamati konsistensi hasil PASS dan FAIL pada setiap kasus. Evaluasi juga dapat melibatkan analis dan pengguna bisnis untuk menilai kegunaan jawaban agen dalam pekerjaan mereka. Pertanyaan pengujian dapat disusun dari kebutuhan analisis pengguna, dengan rubrik yang mencakup ketepatan hasil, kejelasan penjelasan, dan kegunaan jawaban.

# DAFTAR PUSTAKA

Adyen. (n.d.). About Adyen. https://www.adyen.com/about

Agent Skills. (n.d.). Agent Skills overview. https://agentskills.io/home

Alpar, P., & Schulz, M. (2016). Self-service business intelligence. Business & Information Systems Engineering, 58(2), 151–155. https://doi.org/10.1007/s12599-016-0424-6

Anthropic. (2025, 11 September). Writing effective tools for agents — with agents. https://www.anthropic.com/research/writing-tools-for-agents

Brown, T. B., Mann, B., Ryder, N., Subbiah, M., Kaplan, J., Dhariwal, P., dkk. (2020). Language models are few-shot learners. Dalam Advances in Neural Information Processing Systems, 33 (hlm. 1877–1901). https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html

Chaudhuri, S., Dayal, U., & Narasayya, V. (2011). An overview of business intelligence technology. Communications of the ACM, 54(8), 88–98. https://doi.org/10.1145/1978542.1978562

Chen, H., Chiang, R. H. L., & Storey, V. C. (2012). Business intelligence and analytics: From big data to big impact. MIS Quarterly, 36(4), 1165–1188. https://doi.org/10.2307/41703503

Cloudflare. (2026). Cloudflare OS: An AI productivity environment. GitHub. https://github.com/cloudflare/cloudflare-os

DeepSeek. (2026a, 17 Oktober). DeepSeek-V4.1-Flash-1017 release. DeepSeek API Docs. https://api-docs.deepseek.com/news/news261017/

DeepSeek. (2026b). Messages. DeepSeek API Docs. Diakses 14 November 2026, dari https://api-docs.deepseek.com/api/create-message/

DeepSeek-AI. (2026). DeepSeek-V4.1-Flash-1017: config.json [Berkas konfigurasi model]. Hugging Face. Diakses 14 November 2026, dari https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017/blob/main/config.json

Egg, A., Iglesias Goyanes, M., Kingma, F., Mora, A., von Werra, L., & Wolf, T. (2025). DABstep: Data Agent Benchmark for Multi-step Reasoning. arXiv. https://doi.org/10.48550/arXiv.2506.23719

Gruber, T. R. (1993). A translation approach to portable ontology specifications. Knowledge Acquisition, 5(2), 199–220. https://tomgruber.org/writing/ontolingua-kaj-1993/

Hong, S., Lin, Y., Liu, B., Liu, B., Wu, B., Zhang, C., Li, D., Chen, J., Zhang, J., Wang, J., Zhang, L., Zhang, L., Yang, M., Zhuge, M., Guo, T., Zhou, T., Tao, W., Tang, R., Lu, X., … Wu, C. (2025). Data Interpreter: An LLM Agent for Data Science. Dalam Findings of the Association for Computational Linguistics: ACL 2025 (hlm. 19796–19821). Association for Computational Linguistics. https://doi.org/10.18653/v1/2025.findings-acl.1016

Hu, X., Zhao, Z., Wei, S., Chai, Z., Ma, Q., Wang, G., Wang, X., Su, J., Xu, J., Zhu, M., Cheng, Y., Yuan, J., Li, J., Kuang, K., Yang, Y., Yang, H., & Wu, F. (2024). InfiAgent-DABench: Evaluating Agents on Data Analysis Tasks. Dalam Proceedings of the 41st International Conference on Machine Learning (Proceedings of Machine Learning Research, 235, hlm. 19544–19572). https://proceedings.mlr.press/v235/hu24s.html

Lei, F., Chen, J., Ye, Y., Cao, R., Shin, D., Su, H., Suo, Z., Gao, H., Hu, W., Yin, P., Zhong, V., Xiong, C., Sun, R., Liu, Q., Wang, S., & Yu, T. (2025). Spider 2.0: Evaluating language models on real-world enterprise Text-to-SQL workflows. Dalam International Conference on Learning Representations. https://proceedings.iclr.cc/paper_files/paper/2025/hash/46c10f6c8ea5aa6f267bcdabcb123f97-Abstract-Conference.html

Li, H., Chen, X., Xu, Z., Li, D., Hu, N., Teng, F., Li, Y., Qiu, L., Zhang, C. J., Li, Q., & Chen, L. (2025). Exposing numeracy gaps: A benchmark to evaluate fundamental numerical abilities in large language models. Dalam Findings of the Association for Computational Linguistics: ACL 2025 (hlm. 20004–20026). Association for Computational Linguistics. https://doi.org/10.18653/v1/2025.findings-acl.1026

Li, J., Hui, B., Qu, G., Yang, J., Li, B., Li, B., Wang, B., Qin, B., Geng, R., Huo, N., Zhou, X., Ma, C., Li, G., Chang, K., Huang, F., Cheng, R., & Li, Y. (2023). Can LLM already serve as a database interface? A BIg bench for large-scale database grounded Text-to-SQLs. Dalam Advances in Neural Information Processing Systems, 36 (Datasets and Benchmarks Track). https://proceedings.neurips.cc/paper_files/paper/2023/hash/83fc8fab1710363050bbd1d4b8cc0021-Abstract-Datasets_and_Benchmarks.html

Li, Y., Zhang, Z., Ma, T., Wang, Z., Murugesan, K., Zhang, C., & Ye, Y. (2026). LongDA: Benchmarking LLM Agents for Long-Document Data Analysis. Dalam The Proceedings of Workshop on Document Intelligence and Understanding (hlm. 112–137). Association for Computational Linguistics. https://aclanthology.org/2026.docinsights-1.9/

Liu, N. F., Lin, K., Hewitt, J., Paranjape, A., Bevilacqua, M., Petroni, F., & Liang, P. (2024). Lost in the middle: How language models use long contexts. Transactions of the Association for Computational Linguistics, 12, 157–173. https://doi.org/10.1162/tacl_a_00638

Liu, X., Yu, H., Zhang, H., Xu, Y., Lei, X., Lai, H., Gu, Y., Ding, H., Men, K., Yang, K., Zhang, S., Deng, X., Zeng, A., Du, Z., Zhang, C., Shen, S., Zhang, T., Su, Y., Sun, H., … Tang, J. (2024). AgentBench: Evaluating LLMs as Agents. Dalam International Conference on Learning Representations. https://proceedings.iclr.cc/paper_files/paper/2024/file/e9df36b21ff4ee211a8b71ee8b7e9f57-Paper-Conference.pdf

Meta. (2026a). Introducing Muse Spark 1.3. Meta AI Research. https://research.meta.ai/blog/introducing-muse-spark-1-3

Meta. (2026b). Muse Spark 1.3. Meta for Developers. Diakses 3 November 2026, dari https://dev.meta.ai/models/muse-spark

Meta. (2026c). Models. Meta Model API. Diakses 5 November 2026, dari https://dev.meta.ai/docs/models

Meta. (2026d). Responses API. Meta Model API. Diakses 14 November 2026, dari https://dev.meta.ai/docs/protocols/responses

Meta. (2026e). Quickstart. Meta Model API. Diakses 14 November 2026, dari https://dev.meta.ai/docs/quickstart

Mialon, G., Fourrier, C., Wolf, T., LeCun, Y., & Scialom, T. (2024). GAIA: A benchmark for General AI Assistants. Dalam International Conference on Learning Representations. https://proceedings.iclr.cc/paper_files/paper/2024/hash/25ae35b5b1738d80f1f03a8713e405ec-Abstract-Conference.html

Model Context Protocol. (2026). Architecture. https://modelcontextprotocol.io/specification/2026-07-28/architecture/

Noy, N. F., & McGuinness, D. L. (2001). Ontology development 101: A guide to creating your first ontology (Technical Report KSL-01-05). Stanford Knowledge Systems Laboratory. https://protege.stanford.edu/publications/ontology_development/ontology101-noy-mcguinness.html

Osés Grijalba, J., Ureña-López, L. A., Martínez Cámara, E., & Camacho-Collados, J. (2024). Question Answering over Tabular Data with DataBench: A Large-Scale Empirical Evaluation of LLMs. Dalam Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024) (hlm. 13471–13488). ELRA and ICCL. https://aclanthology.org/2024.lrec-main.1179/

Quamar, A., Özcan, F., Miller, D., Moore, R. J., Niehus, R., & Kreulen, J. (2020). Conversational BI: An Ontology-Driven Conversation System for Business Intelligence Applications. Proceedings of the VLDB Endowment, 13(12), 3369–3381. https://doi.org/10.14778/3415478.3415557

Rumiantsau, M., & Fokeev, I. (2026). Semantic layers for reliable LLM-powered data analytics: A paired benchmark of accuracy and hallucination across three frontier models. arXiv. https://arxiv.org/abs/2604.25149

Sahu, G., Puri, A., Rodriguez, J. A., Abaskohi, A., Chegini, M., Drouin, A., Taslakian, P., Zantedeschi, V., Lacoste, A., Vazquez, D., Chapados, N., Pal, C., Rajeswar, S., & Laradji, I. (2025). InsightBench: Evaluating business analytics agents through multi-step insight generation. Dalam International Conference on Learning Representations. https://proceedings.iclr.cc/paper_files/paper/2025/hash/0dfe31d6e703e138d46a7d2fced38b7c-Abstract-Conference.html

Sawant, P., & Sonawane, K. (2024). NLP-based smart decision making for business and academics. Natural Language Processing Journal, 8, 100090. https://doi.org/10.1016/j.nlp.2024.100090

Shi, F., Chen, X., Misra, K., Scales, N., Dohan, D., Chi, E. H., Schärli, N., & Zhou, D. (2023). Large language models can be easily distracted by irrelevant context. Dalam Proceedings of the 40th International Conference on Machine Learning (Proceedings of Machine Learning Research, 202, hlm. 31210–31227). https://proceedings.mlr.press/v202/shi23a.html

Vishwakarma, H., Agarwal, A., Patil, O., Devaguptapu, C., & Chandran, M. (2025). Can LLMs help you at work? A sandbox for evaluating LLM agents in enterprise environments. Dalam Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (hlm. 9167–9201). Association for Computational Linguistics. https://doi.org/10.18653/v1/2025.emnlp-main.466

Wang, L., Ma, C., Feng, X., Zhang, Z., Yang, H., Zhang, J., Chen, Z., Tang, J., Chen, X., Lin, Y., Zhao, W. X., Wei, Z., & Wen, J. (2024). A survey on large language model based autonomous agents. Frontiers of Computer Science, 18(6), 186345. https://doi.org/10.1007/s11704-024-40231-1

Wu, X., Yang, J., Chai, L., Zhang, G., Liu, J., Du, X., Liang, D., Shu, D., Cheng, X., Sun, T., Li, T., Li, Z., & Niu, G. (2025). TableBench: A Comprehensive and Complex Benchmark for Table Question Answering. Proceedings of the AAAI Conference on Artificial Intelligence, 39(24), 25497–25506. https://doi.org/10.1609/aaai.v39i24.34739

Yao, S., Shinn, N., Razavi, P., & Narasimhan, K. R. (2025). τ-bench: A benchmark for tool-agent-user interaction in real-world domains. Dalam International Conference on Learning Representations. https://proceedings.iclr.cc/paper_files/paper/2025/file/1b126cc38b8638e07bef37e7b2bb72bf-Paper-Conference.pdf
