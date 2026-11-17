# BAB I — PENDAHULUAN

Bab ini menjelaskan kerangka dasar dari penelitian yang terdiri dari latar belakang, rumusan masalah, tujuan penelitian, manfaat penelitian, batasan penelitian, dan sistematika penulisan. Seluruh bagian tersebut disusun untuk memberikan gambaran umum mengenai arah, fokus, serta ruang lingkup penelitian secara menyeluruh.

## 1.1. Latar Belakang

Evaluasi merupakan bagian krusial dalam proses pembelajaran karena memungkinkan dosen dan mahasiswa menilai sejauh mana capaian pembelajaran telah tercapai. Salah satu bentuk evaluasi yang paling bernilai adalah pemberian *feedback*, yang tidak hanya menunjukkan kekurangan dalam jawaban mahasiswa, tetapi juga memberikan arahan untuk perbaikan dan penguatan pemahaman. *Feedback* yang efektif telah terbukti dapat meningkatkan kualitas belajar mandiri, memperkuat refleksi akademik, dan meningkatkan hasil belajar secara keseluruhan (Williams, 2024).

Namun, dalam praktiknya, pemberian *feedback* secara manual oleh dosen seringkali menemui berbagai kendala. Di lingkungan pendidikan tinggi, terutama pada kelas dengan jumlah mahasiswa besar, dosen menghadapi keterbatasan waktu dan beban kerja tinggi yang dapat berdampak pada keterlambatan, ketidakkonsistenan, atau bahkan penghilangan proses pemberian *feedback* secara menyeluruh (M. Zhang dkk., 2025) Hal ini menimbulkan kebutuhan akan solusi yang dapat membantu proses evaluasi tanpa mengorbankan kualitas instruksionalnya.

Untuk menjawab tantangan tersebut, berkembanglah pendekatan *automatic feedback generation*, yakni pemanfaatan teknologi untuk menghasilkan umpan balik secara otomatis terhadap jawaban mahasiswa. Salah satu teknologi terdepan dalam bidang ini adalah penggunaan *Large Language Models* (LLM), yaitu model bahasa besar yang dilatih untuk memahami dan menghasilkan teks secara kontekstual. Model seperti GPT dari OpenAI dan LLaMA dari Meta AI telah menunjukkan kemampuan dalam berbagai tugas pemrosesan bahasa alami, termasuk *feedback generation* berbasis *prompt* (Tanwar dkk., 2024; M. Zhang dkk., 2025).

Meski menjanjikan efisiensi, masih terdapat celah antara *automatic feedback* dan *human feedback* dari sisi relevansi, kejelasan instruksi, dan konteks akademik. Penelitian menunjukkan bahwa kualitas *output* LLM sangat bergantung pada desain *prompt* yang diberikan. Strategi *prompting* seperti Zero-Shot, One-Shot, Few-Shot, dan Chain-of-Thought dapat menghasilkan gaya dan kedalaman *feedback* yang berbeda-beda (Wei et al., 2022). Selain itu, penggunaan *persona prompting*, seperti menyisipkan identitas model sebagai “Dosen” atau “Ahli”, turut memengaruhi gaya bahasa dan sudut pandang *feedback* yang dihasilkan (Stahl dkk., 2024).

Beberapa pendekatan telah dikembangkan untuk memanfaatkan LLM dalam *feedback generation*, di antaranya adalah *fine-tuning* model, *retrieval-augmented generation*, dan *prompt engineering*. *Fine-tuning* memungkinkan adaptasi model terhadap domain tertentu, namun membutuhkan data dalam jumlah besar dan sumber daya komputasi tinggi. *Retrieval-based* cenderung mengandalkan basis data eksternal dan sistem pencocokan, tetapi kurang fleksibel dalam memproduksi respons kontekstual. Sementara itu, *prompt engineering* menawarkan pendekatan yang ringan dan fleksibel, cukup dengan mengubah instruksi masukan tanpa perlu melatih ulang model (Mazzullo & Bulut, 2024).

Oleh karena itu, dalam penelitian ini dipilih pendekatan *prompt engineering*, karena pendekatan ini memungkinkan eksplorasi berbagai strategi instruksi (*prompting*) dan persona tanpa perlu *fine-tuning* model atau integrasi sistem tambahan. Hal ini sangat sesuai dengan keterbatasan data dan infrastruktur yang tersedia, serta memungkinkan evaluasi langsung terhadap pengaruh desain *prompt* terhadap kualitas *feedback* yang dihasilkan oleh LLM.

Penelitian ini dirancang untuk mengevaluasi kualitas *feedback* yang dihasilkan oleh LLM terhadap jawaban mahasiswa dari dua mata kuliah berbeda, yaitu Sistem Cerdas dan Metodologi Penelitian dan Penulisan Ilmiah (MPI). Kedua mata kuliah tersebut dipilih karena mewakili dua karakteristik tugas akademik yang berbeda: Sistem Cerdas lebih banyak berisi jawaban teknis dan konseptual yang bersifat spesifik dalam bidang ilmu komputer, sedangkan MPI menuntut penulisan jawaban naratif dan argumentatif yang lebih panjang serta terstruktur. Perbedaan karakteristik ini penting untuk menguji sejauh mana LLM mampu menghasilkan *feedback* yang fleksibel dan relevan dalam konteks disiplin ilmu yang berbeda, baik yang bersifat teknis maupun yang bersifat penulisan ilmiah.

Penelitian dilakukan dengan menerapkan empat strategi *prompting*, tiga konfigurasi persona, dan dua model LLM (GPT-4o mini dan LLaMA 3.1). Evaluasi kualitas dilakukan menggunakan empat metrik otomatis: BLEU, ROUGE-L, METEOR, dan BERTScore, yang mencakup pendekatan leksikal dan semantik. Penelitian ini diharapkan dapat memberikan kontribusi baik secara praktis dalam membantu dosen menghasilkan *feedback* berkualitas, maupun secara teoretis dalam pengembangan riset NLP di bidang pendidikan tinggi.

## 1.2. Rumusan Masalah

Penelitian ini dilatarbelakangi oleh kebutuhan akan mekanisme pemberian umpan balik yang efisien, relevan, dan berkualitas dalam konteks pendidikan tinggi, khususnya terhadap jawaban mahasiswa yang bersifat terbuka atau naratif. Dengan berkembangnya teknologi *Large Language Model* (LLM), proses *feedback generation* dapat diotomatisasi melalui pendekatan *prompt engineering*. Namun, kualitas *feedback* yang dihasilkan model sangat dipengaruhi oleh strategi *prompting* yang digunakan serta peran atau persona yang dimasukkan dalam *prompt*.

Berdasarkan latar belakang tersebut, rumusan masalah dalam penelitian ini adalah bagaimana kualitas *feedback* yang dihasilkan oleh LLM terhadap jawaban mahasiswa, jika dianalisis berdasarkan strategi *prompting*, jenis persona, model LLM, dan kombinasi strategi *prompting* yang digunakan, serta dievaluasi menggunakan metrik otomatis BLEU, ROUGE-L, METEOR, dan BERTScore dalam konteks pendidikan tinggi.

## 1.3. Tujuan Penelitian

Tujuan dari penelitian ini adalah untuk mengevaluasi kualitas *feedback* yang dihasilkan oleh *Large Language Model* (LLM) terhadap jawaban mahasiswa dengan menganalisis pengaruh strategi *prompting*, jenis persona, dan model yang digunakan.

Penelitian ini bertujuan untuk menilai efektivitas berbagai strategi *prompting*, yaitu Zero-Shot, One-Shot, Few-Shot, dan Chain-of-Thought, serta menganalisis bagaimana penggunaan persona seperti Base, Dosen, dan Ahli dapat memengaruhi kualitas respons model. Selain itu, penelitian ini juga membandingkan performa dua model LLM, yaitu GPT-4o mini dan LLaMA 3.1, dalam menghasilkan *feedback* akademik yang relevan. Seluruh hasil evaluasi dianalisis menggunakan metrik otomatis BLEU, ROUGE-L, METEOR, dan BERTScore, untuk mengukur sejauh mana *feedback* yang dihasilkan mendekati *feedback* referensi yang telah disusun sebelumnya, baik dalam konteks mata kuliah Sistem Cerdas maupun Metodologi Penelitian dan Penulisan Ilmiah.

## 1.4. Manfaat Penelitian

Penelitian ini diharapkan dapat memberikan manfaat baik secara teoritis maupun praktis. Secara teoritis, penelitian ini memperkaya kajian di bidang *Natural Language Processing* (NLP) dan penerapan *Large Language Models* (LLM) dalam konteks pendidikan tinggi, khususnya dalam tugas evaluasi otomatis berbasis teks. Dengan mengeksplorasi pengaruh strategi *prompting*, persona, dan jenis model terhadap kualitas *feedback* yang dihasilkan, penelitian ini dapat memberikan kontribusi terhadap pengembangan metode evaluasi berbasis *prompt engineering* dan pemodelan konteks pada sistem kecerdasan buatan.

Secara praktis, hasil dari penelitian ini dapat dimanfaatkan oleh pendidik, institusi pendidikan, maupun pengembang teknologi edukasi dalam mengimplementasikan LLM sebagai alat bantu pemberian umpan balik terhadap tugas mahasiswa. Temuan mengenai kombinasi strategi dan persona yang paling efektif dapat menjadi acuan dalam mendesain sistem *feedback generator* yang lebih adaptif, efisien, dan relevan dengan konteks pembelajaran di kelas. Selain itu, penelitian ini juga dapat membantu institusi dalam mempertimbangkan integrasi LLM sebagai bagian dari solusi pembelajaran berbasis AI, terutama pada mata kuliah yang menuntut analisis naratif atau konseptual.

## 1.5. Batasan Penelitian

Penelitian ini memiliki beberapa keterbatasan yang perlu diperhatikan untuk memperjelas ruang lingkup dan interpretasi hasil, antara lain:

1. **Terbatas pada dua mata kuliah.** Penelitian hanya dilakukan pada dua mata kuliah, yaitu Sistem Cerdas dan Metodologi Penelitian dan Penulisan Ilmiah (MPI). Oleh karena itu, temuan yang diperoleh belum tentu dapat digeneralisasikan ke bidang lain yang memiliki jenis tugas atau bentuk jawaban yang berbeda.

2. **Evaluasi sepenuhnya otomatis.** Penelitian ini menggunakan empat metrik berbasis teks tanpa penilaian manual dari manusia (dosen, ahli, atau mahasiswa). Akibatnya, interpretasi hasil hanya merefleksikan kesamaan leksikal dan semantik dengan *feedback* referensi, bukan nilai pedagogis atau dampak pembelajaran.

3. **Terbatas pada dua model LLM dan konfigurasi default.** Model yang digunakan terbatas pada GPT-4o mini (API) dan LLaMA 3.1 (lokal via Ollama), sehingga belum mencakup variasi arsitektur model lain atau versi dengan *tuning* berbeda. Selain itu, penelitian hanya menguji empat strategi *prompting* (Zero-Shot, One-Shot, Few-Shot, Chain-of-Thought) dan tiga jenis persona (Base, Dosen, Ahli), tanpa mengeksplorasi elemen seperti panjang *prompt*, gaya bahasa, atau pengaturan temperatur model secara sistematis.

4. **Tidak membahas perbandingan antar tipe One-Shot.** Penelitian ini menggunakan One-Shot *prompting* dengan tipe yang berdasarkan variasi nilai jawaban mahasiswa (rendah, sedang, tinggi) tetapi belum melakukan analisis terpisah terhadap jenis One-Shot *prompting* berdasarkan variasi nilai jawaban mahasiswa, sehingga belum dapat menyimpulkan apakah efektivitas One-Shot dipengaruhi oleh kualitas jawaban yang dijadikan contoh dalam *prompt*.

5. **Tidak mengevaluasi dampak nyata terhadap pembelajaran.** Penelitian ini tidak mengukur secara langsung bagaimana *feedback* yang dihasilkan memengaruhi proses belajar atau kualitas revisi mahasiswa. Fokus utama hanya pada kesesuaian *output* dengan *feedback* referensi, bukan pada validitas fungsional atau penerimaan pengguna akhir.

## 1.6. Sistematika Penulisan

Sistematika penulisan skripsi ini disusun untuk memberikan gambaran yang terstruktur mengenai isi penelitian. Skripsi terdiri dari lima bab utama, yang masing-masing membahas aspek berbeda dari penelitian ini.

**BAB I PENDAHULUAN**

Bab ini memuat latar belakang penelitian, perumusan masalah, tujuan dan manfaat penelitian, batasan ruang lingkup, serta sistematika penulisan. Bab ini bertujuan untuk mengenalkan konteks dan arah penelitian.

**BAB II TINJAUAN PUSTAKA**

Bab ini menguraikan teori, konsep, dan hasil penelitian terdahulu yang relevan dengan topik penelitian. Di dalamnya dibahas mengenai *Large Language Models* (LLM), konsep *feedback* dalam pendidikan, strategi *prompting* (Zero-Shot, One-Shot, Few-Shot, dan Chain-of-Thought), persona dalam *prompting*, serta metrik evaluasi otomatis seperti BLEU, ROUGE-L, METEOR, dan BERTScore.

**BAB III METODE PENELITIAN**

Bab ini menjelaskan secara rinci rancangan penelitian yang digunakan, termasuk pendekatan penelitian, sumber dan jumlah data, prosedur penyusunan *prompt*, proses generasi *feedback* menggunakan dua model LLM (GPT-4o dan LLaMA), serta teknik evaluasi menggunakan empat metrik otomatis. Selain itu, dijelaskan pula metode analisis data serta perangkat lunak yang digunakan dalam eksperimen.

**BAB IV HASIL DAN PEMBAHASAN**

Bab ini menyajikan hasil eksperimen berupa analisis skor evaluasi dari strategi *prompting*, persona dalam *prompt*, model LLM, dan setiap kombinasi model terhadap jawaban mahasiswa pada hasil keluaran model berdasarkan mata kuliah Sistem Cerdas dan Metodologi Penelitian dan Penulisan Ilmiah. Analisis dilakukan terhadap performa masing-masing strategi, persona, model, dan kombinasi baik dari segi rata-rata maupun sebaran skor.

**BAB V PENUTUP**

Bab terakhir ini memuat kesimpulan dari temuan utama yang diperoleh dari penelitian, serta memberikan saran untuk penelitian lanjutan atau pengembangan sistem *feedback* otomatis berbasis LLM di masa depan. Peneliti juga merefleksikan keterbatasan penelitian sebagai dasar pertimbangan pengembangan lebih lanjut.

# BAB II — TINJAUAN PUSTAKA

Bab ini membahas landasan teori yang meliputi konsep *Artificial Intelligence*, *Natural Language Processing*, *feedback* dalam pendidikan, serta *feedback generation* otomatis menggunakan *Large Language Models* (LLM). Selain itu, dijelaskan pula strategi *prompting*, penggunaan persona, metrik evaluasi otomatis, dan penelitian terdahulu yang relevan sebagai dasar analisis dalam penelitian ini.

## 2.1. State-of-the-Art

Penelitian terdahulu mengenai *Large Language Model* (LLM) untuk *feedback* pada pendidikan mencakup domain, metode, strategi *prompt*, metrik evaluasi, dan temuan dapat dilihat pada Tabel 2.1.

**Tabel 2.1. Rincian Penelitian Sebelumnya**

| No. | Penelitian (Tahun) | Domain & Tugas | Model/Metode LLM | Strategi Prompting | Metrik | Temuan |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | Prihar dkk. (2023) | Matematika (penjelasan langkah) | GPT-3 (175B) | *few-shot* vs. ringkasan *tutoring* | Survei guru (skala kualitas) | GPT-3 tidak sebanding kualitasnya dengan buatan guru, hanya 10% penjelasan dari *few-shot* yang benar secara matematika, sehingga GPT-3 dinilai belum mampu menghasilkan penjelasan matematika berkualitas tinggi. |
| 2 | Stahl dkk. (2024) | *Essay scoring* & *feedback* | Mistral-7B-Instruct | *Feedback-only*, *scoring-only*, CoT, persona, *few-shot* | Quadratic Weighted Kappa (QWK) | *Chain-of-Thought prompting* sendiri tidak selalu efektif, tetapi kombinasi CoT dengan rubrik mampu meningkatkan akurasi penilaian. Evaluasi otomatis oleh Mistral cukup selaras dengan penilaian manusia (r=0,61), sedangkan LLaMA-2 tidak. |
| 3 | Meyer dkk. (2024) | EFL *essay writing* (revisi) | GPT-3.5-turbo (OpenAI) | Zero-shot | *Automated Essay Scoring* (skor peningkatan) | *Feedback* LLM terbukti meningkatkan kualitas revisi esai (d=0,19) serta menaikkan motivasi (d=0,36) dan emosi positif siswa. Umpan balik otomatis efektif sebagai intervensi di kelas besar, siswa yang menerima saran GPT melakukan lebih banyak perbaikan dibanding yang tidak mendapat *feedback*. |
| 4 | McNichols dkk. (2024) | *Feedback Intelligent Tutoring Systems* (ITS) matematika (aljabar) | Llama-2, Mistral 7B (*fine-tune*), & GPT-3.5 | *Fine-tuning* vs. *prompting* | BLEU / Text Similarity (dengan *feedback* ITS asli) | GPT-3.5 mampu meniru *feedback* yang sudah dilatih, namun kesulitan menangani kesalahan matematika baru, dan justru menurun performanya saat ditambah label kesalahan. |
| 5 | Haider dkk. (2024) | *Code review* | Code Llama 7B (QLoRA *fine-tune*) & GPT-3.5 | *Few-shot* dengan konteks (graf fungsi, dsb.) | BLEU-4 (*dataset* CodeReviewer) | *Few-shot* GPT-3.5 melampaui *baseline* BLEU-4 hingga 90%, sementara Gemini-1.0 Pro, QLoRA *fine-tuned* Code Llama, dan Llama 3.1 juga menunjukkan peningkatan kompetitif. |
| 6 | Lee dkk. (2024) | Sains (skoring jawaban uraian) | GPT-3.5 vs GPT-4 (API) | Zero vs. Few-shot, Chain-of-Thought, Rubrik | Akurasi klasifikasi benar/salah | *Few-shot* lebih akurat dari *zero-shot* (67% vs 60%), CoT tanpa konteks tidak efektif, tapi CoT + rubrik meningkatkan akurasi (+13%). GPT-4 unggul 8,6% atas GPT-3.5, dengan *prompt* terbaik: *single-call greedy* + contoh & rubrik. |
| 7 | Tian dkk. (2024) | *chatbot eval* | GPT-4 | *zero-shot* vs *few-shot*; dengan vs tanpa rubrik | Weighted κ, ρ (korelasi vs pakar) | GPT-4 menunjukkan kesesuaian tinggi dengan penilaian manusia pada aspek *greet intent* dan *fallback intent* (QWK ~0.7–0.8), namun hanya kesesuaian sedang hingga rendah pada aspek *training phrases*, *follow-up intents*, dan *responses*. Strategi *few-shot-rubric* paling unggul dalam menilai *fallback intent*, *follow-up intents*, dan *training phrases*, sedangkan *few-shot-basic* lebih efektif untuk *greet intent* dan *responses*. |

Tabel 2.1 menyajikan ringkasan beberapa penelitian terdahulu yang relevan dengan penggunaan *Large Language Model* (LLM) dalam konteks pemberian *feedback* di bidang pendidikan. Penelitian-penelitian tersebut mencakup beragam domain, mulai dari matematika dan penulisan esai hingga pemrograman dan evaluasi *chatbot*, dengan pendekatan model, strategi *prompting*, serta metrik evaluasi yang bervariasi.

Prihar dkk. (2023) menggunakan GPT-3 untuk menjelaskan langkah-langkah dalam tugas matematika dan membandingkan strategi *few-shot prompting* dengan pendekatan berbasis ringkasan tutor. Meskipun hasilnya menunjukkan bahwa GPT-3 belum mampu menggantikan guru dalam memberikan penjelasan matematika yang mendalam, model ini dianggap membantu mempercepat proses pemberian *feedback*. Stahl dkk. (2024) meneliti kombinasi strategi *prompting* seperti persona, *few-shot*, dan *chain-of-thought* (CoT) dalam tugas *essay scoring* dan *feedback generation*. Hasilnya menunjukkan bahwa *prompt* yang menggabungkan *feedback* dan penilaian dengan persona “peneliti pendidikan” memberikan hasil paling efektif.

Penelitian oleh Meyer dkk. (2024) menegaskan manfaat praktis dari *feedback* otomatis menggunakan GPT-3.5-turbo dalam konteks revisi esai untuk pembelajar bahasa Inggris (EFL). Hasilnya menunjukkan peningkatan signifikan dalam kualitas revisi, motivasi tugas, dan emosi positif siswa. Sementara itu, McNichols dkk. (2024) mengeksplorasi kemampuan LLM dalam meniru *feedback Intelligent Tutoring Systems* (ITS) untuk aljabar. LLM seperti LLaMA dan Mistral menunjukkan performa baik saat di-*fine-tune* dengan data ITS, namun mengalami kesulitan saat menghadapi kesalahan siswa yang belum pernah dilihat sebelumnya.

Haider dkk. (2024) menerapkan LLM dalam domain *code review*, menggunakan kombinasi *few-shot prompting* dengan informasi semantik tambahan seperti grafik fungsi. Mereka menemukan bahwa augmentasi semantik dan penggunaan GPT-3.5 dapat menghasilkan skor BLEU-4 yang tinggi dan relevansi komentar yang baik menurut pengembang. Penelitian Lee dkk. (2024) menyoroti pentingnya *prompt structure* dan rubrik dalam tugas penilaian jawaban uraian sains. Mereka menemukan bahwa kombinasi *few-shot* dengan rubrik dan contoh menghasilkan akurasi tertinggi, dengan GPT-4 mengungguli GPT-3.5.

Tian dkk. (2024) mengevaluasi LLM dalam tugas penilaian *chatbot*. Mereka menunjukkan bahwa *few-shot prompting* dan penggunaan rubrik eksplisit menghasilkan hasil yang paling konsisten dengan penilaian pakar. Meskipun demikian, model cenderung hanya meniru rubrik tanpa memberi penjelasan mendalam, sehingga strategi seperti CoT direkomendasikan untuk memperdalam kualitas *reasoning* dalam *output* LLM.

Secara keseluruhan, penelitian-penelitian tersebut menegaskan bahwa performa LLM dalam tugas *feedback generation* sangat dipengaruhi oleh desain strategi *prompt*, keberadaan contoh, peran persona, dan jenis rubrik yang digunakan. Hal ini menguatkan pentingnya pendekatan *prompt engineering* yang sistematis untuk mengarahkan LLM menghasilkan *feedback* yang akurat, kontekstual, dan relevan secara pedagogis.

## 2.2. Feedback dalam Pendidikan

Carless dan Boud (2018) menyatakan bahwa *feedback* merupakan komponen penting dalam proses pembelajaran karena dapat membantu mahasiswa mengenali kesalahan, memperbaiki pemahaman, dan meningkatkan kualitas hasil belajarnya. Dalam konteks pendidikan tinggi, *feedback* yang konstruktif dan relevan mendorong keterlibatan mahasiswa secara aktif serta membentuk pemikiran reflektif terhadap tugas akademik. Umpan balik yang diberikan secara tepat waktu dan jelas terbukti memiliki pengaruh positif terhadap perkembangan kompetensi mahasiswa, terutama dalam penugasan terbuka seperti esai dan laporan analitis (Carless & Boud, 2018).

Namun demikian, tantangan utama dalam pemberian *feedback* di lingkungan perkuliahan adalah keterbatasan waktu dan tenaga pengajar, khususnya ketika harus menilai tugas dalam jumlah besar. Kondisi ini sering menyebabkan *feedback* menjadi terbatas, bersifat umum, atau bahkan tertunda. Oleh karena itu, integrasi teknologi berbasis kecerdasan buatan mulai dilirik sebagai solusi potensial dalam memberikan *feedback* otomatis yang lebih cepat dan konsisten, sekaligus tetap memperhatikan kualitas isi yang bersifat personal dan sesuai konteks (Carless & Boud, 2018).

## 2.3. Feedback Generation Otomatis

*Feedback generation* otomatis merujuk pada proses pemberian umpan balik kepada mahasiswa secara otomatis menggunakan teknologi kecerdasan buatan, khususnya *Large Language Models* (LLM). Teknologi ini memungkinkan penyediaan umpan balik yang cepat, konsisten, dan personal terhadap tugas-tugas terbuka seperti esai atau pemrograman. Studi oleh Mazzullo & Bulut (2024) menunjukkan bahwa model GPT-3.5-turbo yang telah disesuaikan mampu menghasilkan umpan balik berkualitas tinggi pada pertanyaan terbuka, dengan tingkat kepuasan pengguna mencapai 84,8%. Hal ini menunjukkan potensi LLM dalam meningkatkan efisiensi dan efektivitas proses pembelajaran.

Namun, tantangan dalam penerapan *feedback* otomatis tetap ada, terutama terkait dengan keakuratan dan relevansi umpan balik yang dihasilkan. Penelitian oleh M. Zhang dkk. (2025) memperkenalkan kerangka kerja *Synthetic Educational Feedback Loops* (SEFL) yang menggunakan dua LLM untuk mensimulasikan interaksi antara guru dan siswa, menghasilkan pasangan data sintetik untuk melatih model yang lebih kecil dan efisien. Pendekatan ini menunjukkan peningkatan kualitas umpan balik dalam hal kejelasan dan ketepatan waktu. Meskipun demikian, evaluasi lebih lanjut diperlukan untuk memastikan bahwa umpan balik yang dihasilkan benar-benar mendukung tujuan pembelajaran dan tidak menimbulkan kesalahpahaman.

## 2.4. Artificial Intelligence

*Artificial Intelligence* (AI) adalah cabang ilmu komputer yang berfokus pada pengembangan sistem yang mampu meniru dan menjalankan fungsi kognitif manusia secara otomatis, seperti pengenalan pola, pemrosesan bahasa alami, pengambilan keputusan, serta pembelajaran dari data (Russell & Norvig, 2022). Seiring dengan kemajuan teknologi, terutama dalam bidang *machine learning* dan pemrosesan bahasa alami, AI telah berevolusi dari sistem berbasis aturan sederhana menjadi sistem cerdas yang dapat beradaptasi terhadap konteks, serta menghasilkan keluaran yang kompleks dan dinamis.

Dalam konteks pendidikan, penerapan AI mengalami perkembangan signifikan, terutama dalam mendukung pembelajaran adaptif dan otomatisasi penilaian. Salah satu implementasi penting adalah penggunaan AI untuk memberikan *feedback* otomatis kepada mahasiswa, yang memungkinkan dosen menyampaikan umpan balik secara cepat, konsisten, dan relevan tanpa harus meninjau seluruh jawaban secara manual. Selain itu, AI juga dimanfaatkan untuk membantu pengajar meningkatkan efektivitas proses pembelajaran melalui analisis bahasa yang digunakan di kelas serta penyediaan umpan balik berbasis teks terhadap performa mengajar (Demszky, 2023). Hal ini menunjukkan bahwa AI berperan penting dalam mendorong efisiensi, personalisasi, dan kualitas proses pembelajaran di era digital.

## 2.5. Natural Language Processing

*Natural Language Processing* (NLP) merupakan cabang dari kecerdasan buatan yang berfokus pada interaksi antara komputer dan bahasa manusia (Jurafsky & Martin, 2021). Dalam konteks pendidikan, NLP memungkinkan pengembangan sistem yang dapat memahami, menganalisis, dan menghasilkan teks secara otomatis, sehingga mendukung berbagai aplikasi seperti penilaian otomatis, pemberian umpan balik, dan personalisasi pembelajaran. Teknologi ini memungkinkan analisis teks dalam skala besar, memungkinkan pendidik untuk memperoleh wawasan mendalam tentang pemahaman dan kebutuhan belajar siswa (Gao dkk., 2023).

Penerapan NLP dalam pendidikan telah menunjukkan dampak positif dalam meningkatkan efisiensi dan efektivitas proses pembelajaran. Misalnya, sistem evaluasi tulisan otomatis seperti Grammarly dan Pigai memanfaatkan NLP untuk memberikan umpan balik korektif kepada siswa, membantu mereka dalam meningkatkan kualitas tulisan. Selain itu, NLP juga digunakan dalam pengembangan sistem pembelajaran adaptif yang dapat menyesuaikan materi dan metode pengajaran sesuai dengan kebutuhan individu siswa, sehingga mendukung pendekatan pembelajaran yang lebih personal dan efektif (Gao dkk., 2023).

## 2.6. Prompt Engineering

*Prompt engineering* merupakan proses menyusun instruksi atau masukan (*prompt*) secara sistematis untuk mengarahkan *output* dari *Large Language Models* (LLM) (Madotto dkk., 2021; Wei dkk., 2023). Dalam konteks pendidikan, *prompt engineering* digunakan untuk menghasilkan *feedback* otomatis yang sesuai dengan gaya akademik, tujuan pembelajaran, dan konteks jawaban mahasiswa. Kualitas *prompt* memiliki pengaruh signifikan terhadap hasil keluaran LLM, terutama dalam tugas-tugas yang memerlukan penalaran, evaluasi, atau gaya bahasa tertentu. Jacobsen dkk. (2025) menunjukkan bahwa variasi desain *prompt* dapat menghasilkan perbedaan *output* yang substansial dalam hal akurasi, relevansi, dan kejelasan *feedback*.

Penelitian ini menggunakan empat strategi *prompting* utama yang banyak digunakan dalam eksperimen NLP dan evaluasi pembelajaran otomatis, yaitu Zero-Shot Prompting, One-Shot Prompting, Few-Shot Prompting, dan Chain-of-Thought Prompting. Keempat strategi ini diterapkan untuk mengevaluasi efektivitas masing-masing strategi dalam mengarahkan model menghasilkan *feedback* otomatis berkualitas tinggi terhadap jawaban mahasiswa.

### 2.6.1. Strategi Prompting

#### 2.6.1.1. Zero-Shot Prompting

*Zero-shot prompting* adalah teknik di mana model diberikan instruksi secara langsung tanpa contoh kontekstual, mengandalkan sepenuhnya pada pemahaman instruksi yang dirancang dalam *prompt* serta kemampuan bawaan model untuk menafsirkan maksud pengguna (Brown dkk., 2020). Dalam praktiknya, pendekatan ini cocok digunakan untuk tugas sederhana yang memiliki struktur pertanyaan yang eksplisit. Gao dkk. (2023) mencatat bahwa *zero-shot prompting* bekerja cukup efektif untuk tugas seperti klasifikasi dasar dan pengenalan entitas, tetapi performanya menurun pada tugas dengan dimensi analitis atau naratif yang tinggi.

Dalam konteks pendidikan, *zero-shot prompting* digunakan sebagai *baseline* karena tidak melibatkan pengetahuan tambahan dari contoh sebelumnya. Strategi ini berguna untuk mengevaluasi kemampuan murni LLM dalam menghasilkan *feedback* tanpa bantuan pola atau konteks sebelumnya. Namun, beberapa studi melaporkan bahwa *feedback* yang dihasilkan sering kali terlalu umum, tidak spesifik terhadap konten jawaban mahasiswa, dan kurang memperhatikan nuansa akademik (Gao dkk., 2023). Contoh penggunaan *prompting* dengan strategi Zero-Shot dapat dilihat pada Gambar 1.1.

**Gambar 1.1. Contoh Zero-Shot Prompting**

#### 2.6.1.2. One-Shot Prompting

Berbeda dari *zero-shot*, *one-shot prompting* memberikan satu contoh *input-output* (misalnya: jawaban dan *feedback*) sebagai konteks sebelum model diminta menghasilkan *feedback* baru. Strategi ini memperkenalkan struktur dan gaya yang diinginkan kepada model, namun dengan tetap menjaga singkatnya *prompt*. Madotto dkk. (2021) menemukan bahwa *one-shot prompting* secara signifikan meningkatkan kohesi gaya bahasa dan struktur dibandingkan *zero-shot*, terutama dalam konteks interaksi akademik dan pembelajaran.

Dalam implementasi pendidikan, *one-shot prompting* membantu LLM memahami harapan pengguna, seperti bentuk kalimat, nada bahasa, dan kedalaman evaluasi yang diinginkan. Model menjadi lebih terarah dalam menyusun tanggapan yang menyerupai format referensi. Meski begitu, keberhasilan strategi ini sangat tergantung pada kualitas contoh yang diberikan; jika contoh tidak representatif, respons model dapat menjadi bias atau menyimpang dari tujuan evaluatif. Contoh penggunaan *prompting* dengan strategi One-Shot dapat dilihat pada Gambar 1.2.

**Gambar 1.2. Contoh One-Shot Prompting**

#### 2.6.1.3. Few-Shot Prompting

*Few-shot prompting* menyediakan dua hingga lima contoh *input-output* untuk memberi konteks yang lebih luas kepada model. Strategi ini memungkinkan model mengenali pola dari contoh-contoh yang disediakan, sehingga mampu menghasilkan *output* yang lebih konsisten dan kontekstual. Madotto dkk. (2021) menunjukkan bahwa *few-shot prompting* dapat memperbaiki performa model pada tugas generatif yang kompleks seperti *summarization* dan *argument-based evaluation*.

Dalam penelitian ini, *few-shot prompting* digunakan untuk membekali model dengan berbagai gaya dan isi *feedback* dari beberapa jenis jawaban mahasiswa. Hasil dari pendekatan ini menunjukkan bahwa *output* yang dihasilkan cenderung lebih terstruktur dan sesuai dengan konteks akademik yang diharapkan. Namun, tantangan utama dari strategi ini adalah keterbatasan panjang *prompt* dan potensi terjadinya *overfitting* terhadap contoh. Contoh penggunaan *prompting* dengan strategi Few-Shot dapat dilihat pada Gambar 1.3.

**Gambar 1.3. Contoh Few-Shot Prompting**

#### 2.6.1.4. Chain-of-Thought Prompting

*Chain-of-Thought* (CoT) *prompting* adalah strategi yang meminta model untuk menjelaskan proses berpikir secara eksplisit sebelum memberikan kesimpulan atau *feedback* akhir. Teknik ini diperkenalkan untuk meningkatkan kemampuan penalaran logis model, terutama dalam tugas yang memerlukan deduksi, pengurutan argumen, atau penjelasan bertahap. Wei dkk. (2023) membuktikan bahwa CoT *prompting* meningkatkan akurasi respons model dalam tugas-tugas penalaran multi-langkah.

Dalam konteks *feedback* pendidikan, CoT digunakan untuk menghasilkan umpan balik yang tidak hanya menilai isi secara langsung, tetapi juga menunjukkan mengapa dan bagaimana jawaban mahasiswa bisa diperbaiki. Pendekatan ini dianggap paling mendekati cara kerja dosen manusia, yang biasanya menjelaskan alasan di balik penilaian mereka. Meskipun CoT menghasilkan *feedback* yang lebih reflektif, waktu proses dan panjang *output* menjadi lebih tinggi dibanding strategi lainnya. Contoh *prompting* dengan strategi Chain-of-Thought dapat dilihat pada Gambar 1.4.

**Gambar 1.4. Contoh Chain-of-Thought Prompting**

### 2.6.2. Persona dalam Prompting

Dalam konteks *prompt engineering*, persona merujuk pada identitas atau peran tertentu yang ditugaskan kepada model selama proses generasi teks. Dengan menambahkan persona seperti “seorang dosen”, “pakar NLP”, atau “pengulas akademik”, pengguna dapat mengarahkan gaya bahasa, sudut pandang, serta kedalaman respons yang dihasilkan oleh *Large Language Models* (LLM). Penelitian oleh Stahl dkk. (2024) menunjukkan bahwa penyesuaian persona dalam *prompt* secara signifikan memengaruhi gaya komunikasi model, tingkat keformalan bahasa, dan fokus isi *output*, menjadikannya lebih selaras dengan kebutuhan pengguna dalam domain tertentu.

Dalam penelitian ini, digunakan tiga jenis persona: Base (tanpa persona eksplisit), Dosen (dengan peran sebagai pengajar), dan Ahli (sebagai pakar di bidang tertentu). Persona Base bertindak netral dan menghasilkan respons umum tanpa kejelasan identitas, sementara persona Dosen diharapkan memberikan *feedback* dengan nuansa pembelajaran, seperti mengarahkan dan membimbing mahasiswa. Sebaliknya, persona Ahli digunakan untuk menampilkan kedalaman pengetahuan teknis dan keakuratan evaluatif dalam bidang spesifik. Temuan Stahl dkk. (2024) juga memperlihatkan bahwa penggunaan persona akademik secara eksplisit membantu model menghasilkan *feedback* yang lebih relevan secara kontekstual, serta lebih dihargai oleh pengguna akhir dalam sistem pembelajaran otomatis. Contoh penggunaan *prompting* menggunakan persona dapat dilihat pada Gambar 1.5.

**Gambar 1.5. Contoh Penggunaan Persona dalam Prompt**

## 2.7. Large Language Models

*Large Language Models* (LLM) merupakan model pembelajaran mesin berskala besar yang dirancang untuk memahami dan menghasilkan bahasa alami berdasarkan data dalam jumlah besar (Brown dkk., 2020). Dalam konteks pendidikan, LLM digunakan untuk memberikan umpan balik otomatis terhadap tugas mahasiswa, karena mampu meniru gaya evaluatif guru dan menghasilkan tanggapan yang sesuai dengan konteks akademik (Prihar dkk., 2023; Stahl dkk., 2024).

Penelitian ini menggunakan dua model *Large Language Model* (LLM) yang berbeda, yaitu GPT-4o mini dan LLaMA 3.1, yang masing-masing memiliki karakteristik dan keunggulan tersendiri. GPT-4o mini merupakan model LLM yang dikembangkan oleh OpenAI, dan dirancang agar dapat menghasilkan teks yang koheren dengan kualitas semantik tinggi (OpenAI, 2024). Meskipun ukuran parameter pasti dari GPT-4o mini tidak dipublikasikan secara resmi, model ini merupakan versi yang lebih ringan dibanding GPT-4 penuh, sehingga lebih efisien dari segi biaya penggunaan (OpenAI, 2024). Kelemahan utama GPT-4o mini adalah ketergantungannya pada koneksi internet dan kebijakan biaya API, sehingga memerlukan biaya tambahan setiap kali proses generasi dilakukan (Brown et al., 2020; OpenAI, 2024).

Sebaliknya, LLaMA 3.1 8B merupakan model LLM yang dikembangkan oleh Meta AI dan bersifat *open-source*. Model ini memiliki ukuran sekitar 8 miliar parameter dan dapat dijalankan secara lokal menggunakan *backend* seperti Ollama, sehingga tidak memerlukan koneksi internet selama proses inferensi (Touvron dkk., 2023). LLaMA unggul dalam hal fleksibilitas, biaya rendah, serta memungkinkan peneliti memiliki kontrol penuh atas lingkungan eksperimen. Namun, dibandingkan GPT-4o mini, LLaMA 3.1 cenderung sedikit lebih terbatas dalam menghasilkan teks yang kompleks secara semantik atau konteks panjang, meskipun performanya sangat baik dalam tugas-tugas berbasis pola dan instruksi sederhana (Touvron dkk., 2023; M. Zhang dkk., 2025).

Pemilihan kedua model dalam penelitian ini bertujuan untuk membandingkan performa LLM dalam menghasilkan kualitas *feedback*, khususnya dalam konteks pembuatan *feedback* otomatis di bidang pendidikan. Tabel perbandingan kedua model dapat dilihat pada Tabel 2.2.

**Tabel 2.2. Perbandingan Model GPT4o-mini dan LLama**

| No | Aspek | GPT4o-mini | LLama3.1 |
| ---: | --- | --- | --- |
| 1 | Pengembang | OpenAI | Meta AI |
| 2 | Ukuran | Tidak dipublikasikan pasti (lebih ringan dari GPT-4 penuh) | 8 miliar parameter |
| 3 | Kelebihan | Kualitas semantik tinggi dan pemahaman konteks sangat baik | Open-source, fleksibel, dan biaya rendah |
| 4 | Kekurangan | Bergantung koneksi internet, biaya pada setiap penggunaan | Performa sedikit lebih terbatas pada konteks panjang dibanding GPT-4o mini |
| 5 | Biaya | Berbayar per token API | Gratis |

### 2.7.1. GPT4o-mini

Model ini dibangun dengan arsitektur *transformer* dan dirancang untuk mendukung berbagai tugas berbasis teks seperti penerjemahan, ringkasan, dan generasi umpan balik. Meskipun tidak sekuat GPT-4 penuh, GPT-4o mini tetap mempertahankan kemampuan untuk memahami konteks kompleks dan menghasilkan teks dengan kohesi semantik yang tinggi (M. Zhang dkk., 2025).

**Gambar 1.6. Ilustrasi Model**

Gambar 1.6 menggambarkan model bahasa semi-kausal berfungsi sebagai antarmuka serbaguna dan mendukung interaksi dengan berbagai model dasar. Untuk memahami lebih lanjut mengenai bagaimana *transformer* digunakan secara efektif dalam tugas-tugas pemrosesan bahasa dan visi, Hao dkk. (2022) menjelaskan pendekatan semi-kausal dalam model bahasa yang dapat meningkatkan kemampuan *in-context learning* dan generalisasi *zero-shot*. Pendekatan ini menggabungkan manfaat dari *encoder* non-kausal dan *decoder* kausal untuk menciptakan antarmuka umum yang mampu mengintegrasikan berbagai modalitas. Arsitektur ini secara signifikan meningkatkan efisiensi inferensi dan kemampuan GPT-4o Mini (Hao dkk., 2022).

**Gambar 1.7. Ilustrasi Vision Transformer (ViT)**

Pada Gambar 1.7 Dosovitskiy dkk. (2021) menggarisbawahi penerapan *transformer* pada domain visual dalam model *Vision Transformer* (ViT), yang dapat dihubungkan dengan pendekatan multimodal dalam GPT-4o Mini. ViT memperlihatkan bahwa model berbasis *transformer* mampu mencapai hasil yang setara atau bahkan lebih baik dibandingkan jaringan konvolusional tradisional dalam berbagai tugas klasifikasi citra, yang menunjukkan potensi kuat dari pendekatan *transformer* dalam aplikasi multimodal seperti pada GPT-4o Mini (Dosovitskiy dkk., 2021).

Secara keseluruhan, GPT-4o mini menawarkan kombinasi efisiensi, konsistensi, dan kepraktisan yang sangat relevan untuk tugas *feedback generation* dalam pendidikan tinggi. Model ini menjadi representasi dari LLM komersial berbasis API yang dapat digunakan secara langsung oleh institusi pendidikan maupun peneliti individu untuk mendukung otomatisasi evaluasi akademik.

### 2.7.2. LLaMa

LLaMA (*Large Language Model Meta AI*) merupakan serangkaian model bahasa besar yang dikembangkan oleh Meta (sebelumnya Facebook AI Research) dengan tujuan menghadirkan model generatif berkualitas tinggi yang dapat diakses secara terbuka. LLaMA telah menjadi salah satu model yang banyak digunakan dalam penelitian karena ketersediaan kode dan fleksibilitas penggunaan. Model ini tersedia dalam beberapa skala parameter, memungkinkan peneliti menyesuaikannya dengan kebutuhan komputasi dan ruang lingkup penelitian (Touvron dkk., 2023).

**Gambar 1.8. Model Arsitektur**

Gambar 1.7 menunjukkan keseluruhan arsitektur model Llama 3.1. Llama 3 menggunakan arsitektur Transformer standar dan padat (Sucholutsky dkk., 2019). Dalam hal arsitektur model, model ini tidak jauh berbeda dari Llama dan Llama 2 (Touvron et al., 2023); Meta mengklaim bahwa peningkatan kinerjanya terutama didorong oleh peningkatan kualitas dan keragaman data serta peningkatan skala pelatihan.

Salah satu keunggulan utama LLaMA dibandingkan model komersial adalah kemampuannya dijalankan secara lokal tanpa konektivitas internet. Hal ini memungkinkan penelitian dilakukan dengan kontrol penuh terhadap lingkungan eksperimen, privasi data, dan efisiensi biaya. Dalam penelitian ini LLaMA digunakan melalui platform Ollama, yaitu sistem integrasi LLM lokal yang memungkinkan *prompt* dijalankan secara *real-time* di perangkat peneliti tanpa melalui *server* eksternal.

Dari sisi performa, LLaMA menunjukkan hasil yang kompetitif dalam tugas-tugas berbasis teks, terutama dalam strategi Zero-Shot dan One-Shot *Prompting*. Model ini mampu memahami instruksi dasar dan menghasilkan umpan balik yang bersifat umum, koheren, dan gramatikal. Namun, dalam strategi yang membutuhkan penalaran berlapis seperti *Chain-of-Thought Prompting*, LLaMA versi dasar yang digunakan cenderung menghasilkan respons yang lebih pendek, kurang elaboratif, dan kadang tidak kontekstual. Hal ini sesuai dengan temuan Touvron dkk. (2023), yang menyebutkan bahwa kapasitas *reasoning* LLaMA meningkat seiring dengan ukuran dan *fine-tuning* tambahan.

Kelebihan lain dari LLaMA adalah sifat *open-source*-nya yang memungkinkan modifikasi lanjutan, termasuk *fine-tuning*, *instruction tuning*, atau *alignment* untuk domain pendidikan tertentu. Meski dalam penelitian ini model digunakan dalam konfigurasi *default* (tanpa pelatihan ulang), potensi eksplorasi lanjutan tetap terbuka bagi studi di masa depan. Model ini juga sangat cocok untuk eksperimen skala lokal, terutama di lingkungan penelitian yang memerlukan independensi teknologi atau pembatasan akses *cloud*.

Dengan mempertimbangkan semua faktor di atas, LLaMA berperan sebagai representasi dari model LLM sumber terbuka yang memberikan fleksibilitas tinggi dalam pengujian *feedback generation*. Perbandingannya dengan GPT-4o mini dalam penelitian ini bertujuan untuk mengidentifikasi sejauh mana model lokal dapat mendekati kualitas *feedback* yang dihasilkan oleh model komersial berbasis *cloud*.

## 2.8. Evaluasi Kualitas Feedback

Evaluasi kualitas *feedback* yang dihasilkan oleh model bahasa besar (LLM) merupakan langkah penting untuk mengukur seberapa baik *output* model mencerminkan umpan balik manusia yang ideal. Dalam penelitian ini, digunakan pendekatan evaluasi berbasis teks otomatis dengan mengukur tingkat kesamaan antara *feedback* yang dihasilkan oleh model dan *feedback* referensi yang telah disusun sebelumnya. Metrik evaluasi ini digunakan karena bersifat objektif, dapat diotomatisasi, dan umum digunakan dalam tugas evaluasi teks seperti *machine translation*, *text summarization*, dan *text generation* (T. Zhang dkk., 2020).

Empat metrik utama digunakan dalam penelitian ini, yaitu BLEU, ROUGE-L, METEOR, dan BERTScore. Masing-masing metrik mewakili pendekatan berbeda dalam mengevaluasi kesamaan antara dua teks. BLEU dan ROUGE-L berfokus pada kesamaan leksikal seperti n-gram dan subsekuensi, sedangkan METEOR memperhitungkan sinonim dan *stemming*. Sementara itu, BERTScore menawarkan pendekatan berbasis *embedding* semantik yang mampu menangkap kesamaan makna meskipun struktur kalimat berbeda. Kombinasi keempat metrik ini bertujuan untuk memberikan penilaian yang lebih komprehensif terhadap kualitas *feedback* otomatis dari berbagai sudut pandang.

### 2.8.1. BLEU

BLEU (*Bilingual Evaluation Understudy*) adalah salah satu metrik evaluasi teks generatif yang paling awal dan banyak digunakan dalam penelitian pemrosesan bahasa alami. Metrik ini mengukur kesamaan antara teks yang dihasilkan (*output* sistem) dengan teks referensi (*ground truth*) berdasarkan tingkat kecocokan n-gram (urutan kata) dalam dua kalimat. Skor BLEU berkisar antara 0 hingga 1 (atau 0–100 jika dikalikan), di mana nilai yang lebih tinggi menunjukkan tingkat kesamaan yang lebih besar. BLEU bekerja dengan menghitung presisi n-gram (biasanya hingga 4-gram) dan menerapkan penalti terhadap kalimat yang terlalu pendek melalui *brevity penalty* (Papineni dkk., 2002).

Secara matematis, definisi BLEU dapat dilihat pada Persamaan 2.1:

\[
\mathrm{BLEU} = \mathrm{BP}\cdot\exp\left(\sum_{n=1}^{N} w_n\cdot\log p_n\right) \tag{2.1}
\]

Keterangan:

- \(w_n\): *Modified precision* dari n-gram ke-n antara *output* dan referensi.
- \(p_n\): Bobot dari masing-masing n-gram.
- \(\mathrm{BP}\): *Brevity penalty*.

Rumus *Brevity Penalty* dapat dilihat pada Persamaan 2.2:

\[
\mathrm{BP}=\begin{cases}1, & \text{jika }c>r \\ e^{1-r/c}, & \text{jika }c\le r\end{cases} \tag{2.2}
\]

Keterangan:

- \(c\): Panjang *output* (*candidate*).
- \(r\): Panjang referensi.

Dalam konteks *feedback generation*, BLEU digunakan untuk menilai seberapa besar kemiripan leksikal antara *feedback* otomatis yang dihasilkan oleh model LLM dan *feedback* referensi yang telah disusun oleh dosen atau pakar. Sebagai contoh, jika referensi dosen menyatakan, “Jawaban sudah tepat, tetapi perlu ditambahkan contoh”, maka *feedback* model yang menyatakan “Sudah benar, namun akan lebih baik jika diberi contoh” akan memperoleh skor BLEU sedang hingga tinggi karena terdapat kemiripan n-gram. Namun, BLEU memiliki keterbatasan, yaitu tidak mampu menangkap kesamaan semantik jika struktur kalimat berubah meskipun maknanya tetap sama. Oleh karena itu, dalam penelitian ini, BLEU digunakan sebagai salah satu metrik pelengkap dalam rangka evaluasi komprehensif.

### 2.8.2. ROUGE-L

ROUGE (*Recall-Oriented Understudy for Gisting Evaluation*) adalah metrik evaluasi yang awalnya dikembangkan untuk menilai kualitas ringkasan otomatis dengan membandingkan keluaran sistem terhadap satu atau lebih referensi manusia. ROUGE-L, salah satu variannya, mengukur kemiripan berdasarkan *Longest Common Subsequence* (LCS), yaitu urutan kata terpanjang yang muncul secara berurutan dalam kedua kalimat (Lin, 2004). Tidak seperti BLEU yang mengutamakan presisi, ROUGE-L lebih menekankan aspek *recall*, sehingga lebih toleran terhadap variasi struktur kalimat selama urutan penting tetap terjaga.

Dalam konteks penelitian ini, ROUGE-L digunakan untuk mengevaluasi seberapa besar bagian dari *feedback* referensi yang berhasil direproduksi oleh model LLM, meskipun urutannya tidak selalu identik secara leksikal. Sebagai contoh, apabila *feedback* referensi berbunyi, “Jawaban Anda sudah mengarah ke konsep yang benar, namun masih perlu elaborasi lebih lanjut”, maka *feedback* otomatis seperti “Konsep Anda sudah tepat, tapi kurang penjelasan mendalam” akan tetap memperoleh nilai ROUGE-L yang baik. Metrik ini dianggap relevan dalam evaluasi *feedback generation* karena mampu menangkap kesamaan dalam struktur naratif yang umum digunakan oleh pengajar, meskipun terdapat perbedaan minor dalam pilihan kata.

Secara matematis, ROUGE-L dihitung berdasarkan *precision* dan *recall* terhadap panjang *Longest Common Subsequence* (LCS) antara kalimat kandidat dan referensi. Rumus ROUGE-L dapat dilihat pada Persamaan 2.3:

\[
\mathrm{ROUGE}\text{-}L=\frac{(1+\beta^2)\cdot R_{\mathrm{LCS}}\cdot P_{\mathrm{LCS}}}{R_{\mathrm{LCS}}+\beta^2\cdot P_{\mathrm{LCS}}} \tag{2.3}
\]

Keterangan:

- \(R_{\mathrm{LCS}}\): *Recall* dari LCS.
- \(P_{\mathrm{LCS}}\): *Precision* dari LCS.
- \(\beta\): Faktor penimbang antara *recall* dan *precision*.
- \(\mathrm{LCS}(c,r)\): Panjang *Longest Common Subsequence* antara kalimat.

Komponen *Recall* ROUGE-L dan *Precision* ROUGE-L dihitung dari panjang LCS dibagi dengan panjang referensi atau kandidat, masing-masing dapat dilihat *Recall* ROUGE-L pada Persamaan 2.4 dan *Precision* ROUGE-L pada Persamaan 2.5:

\[
R_{\mathrm{LCS}}=\frac{\mathrm{LCS}(c,r)}{\mathrm{length}(r)} \tag{2.4}
\]

\[
P_{\mathrm{LCS}}=\frac{\mathrm{LCS}(c,r)}{\mathrm{length}(c)} \tag{2.5}
\]

Keterangan:

- \(c\): *candidate*.
- \(r\): referensi.
- \(\mathrm{LCS}(c,r)\): Panjang *Longest Common Subsequence* antara kalimat.

### 2.8.3. METEOR

METEOR (*Metric for Evaluation of Translation with Explicit ORdering*) adalah metrik evaluasi teks yang dikembangkan untuk memperbaiki kelemahan BLEU dalam menangkap kesamaan semantik dan fleksibilitas bahasa. Tidak seperti BLEU yang hanya menghitung kecocokan n-gram, METEOR memperhitungkan beberapa faktor seperti *stemming* (bentuk dasar kata), sinonim, dan pengurutan kata. METEOR bekerja dengan menyelaraskan (*aligning*) kata-kata dari hasil sistem dan referensi, lalu menghitung skor berdasarkan presisi dan *recall* yang digabungkan dalam rumus F1-score (Banerjee & Lavie, 2005). Karena mempertimbangkan struktur linguistik dan variasi bahasa, METEOR dianggap lebih sensitif terhadap kesamaan makna daripada metrik leksikal lainnya.

Dalam konteks *feedback generation*, METEOR sangat bermanfaat untuk mengevaluasi kualitas *output* model yang menggunakan sinonim atau parafrase berbeda dari referensi. Sebagai contoh, apabila *feedback* referensi menyatakan, “Berikan contoh konkret agar argumen lebih kuat”, dan model menghasilkan, “Tambahkan ilustrasi nyata untuk memperjelas argumen”, maka METEOR tetap memberikan skor tinggi karena mendeteksi makna serupa walaupun pilihan katanya berbeda. Kelebihan ini menjadikan METEOR metrik yang ideal untuk mengukur variasi bahasa dalam umpan balik otomatis yang tetap mempertahankan kesamaan pesan inti.

Secara matematis, skor METEOR dihitung dengan menggabungkan *precision* dan *recall* dalam bentuk *harmonic mean*, serta mengurangi skor tersebut dengan penalti berdasarkan jumlah *chunk* (urutan kata cocok yang terpisah). Rumus meteor dapat dilihat pada Persamaan 2.6:

\[
\mathrm{METEOR}=F_{\mathrm{mean}}\cdot(1-\mathrm{Penalty}) \tag{2.6}
\]

Keterangan:

- \(F_{\mathrm{mean}}\): *Harmonic Mean*.
- \(\mathrm{Penalty}\): Penalti.

Skor METEOR diperoleh dengan mengalikan nilai \(F_{\mathrm{mean}}\) dan penalti. Nilai penalti mengurangi skor akhir jika susunan kata yang cocok tersebar tidak berurutan dalam kalimat. Rumus *Harmonic Mean* (F-mean) dapat dilihat pada Persamaan 2.7:

\[
F_{\mathrm{mean}}=\frac{10\cdot\mathrm{Precision}\cdot\mathrm{Recall}}{\mathrm{Recall}+9\cdot\mathrm{Precision}} \tag{2.7}
\]

Rumus *Penalty* dapat dilihat pada Persamaan 2.8:

\[
\mathrm{Penalty}=\gamma\left(\frac{ch}{m}\right)^\theta \tag{2.8}
\]

Keterangan:

- \(m\): Jumlah kata yang cocok (*unigram match*).
- \(ch\): Jumlah *chunk* (urutan token yang cocok namun tidak kontigu).
- \(\gamma,\theta\): Parameter penalti, secara umum \(\gamma=0.5\) dan \(\theta=3\).

### 2.8.4. BERTScore

BERTScore adalah metrik evaluasi berbasis pembelajaran representasi semantik yang memanfaatkan *pre-trained language models* seperti BERT untuk menghitung kesamaan makna antara dua kalimat (T. Zhang dkk., 2020). Berbeda dengan BLEU, ROUGE, dan METEOR yang bergantung pada pencocokan kata secara leksikal, BERTScore menghitung kemiripan vektor antar kata dari hasil sistem dan referensi menggunakan teknik *embedding contextualized*. Metrik ini mengukur kesamaan berdasarkan *cosine similarity* dan memberikan skor pada tingkat *token*, lalu dirata-ratakan menjadi skor F1 (T. Zhang dkk., 2020). Karena berfokus pada kesamaan semantik, BERTScore dianggap lebih selaras dengan penilaian manusia, khususnya dalam tugas generatif kompleks. Rumus BERTScore dapat dilihat pada Persamaan 2.8.

\[
F_{\mathrm{BERT}}=2\times\frac{P_{\mathrm{BERT}}\times R_{\mathrm{BERT}}}{P_{\mathrm{BERT}}+R_{\mathrm{BERT}}} \tag{2.8}
\]

Keterangan:

- \(P_{\mathrm{BERT}}\): *Precision*.
- \(R_{\mathrm{BERT}}\): *Recall*.

Rumus *Precision* BERT dapat dilihat pada Persamaan 2.9:

\[
P_{\mathrm{BERT}}=\frac{1}{|X|}\sum_{x\in X}\max_{y\in Y}\cos(E(x),E(y)) \tag{2.9}
\]

Rumus *Recall* BERT dapat dilihat pada Persamaan 2.10:

\[
R_{\mathrm{BERT}}=\frac{1}{|Y|}\sum_{y\in Y}\max_{x\in X}\cos(E(y),E(x)) \tag{2.10}
\]

Keterangan:

- \(|X|\): Jumlah *token* pada *candidate*.
- \(|Y|\): Jumlah *token* pada *reference*.
- \(X\): *Token* pada *candidate*.
- \(Y\): *Token* pada *reference*.
- \(E()\): *Embedding* BERT.
- \(\cos()\): Nilai *cosine similarity* antara *token* x (*candidate*) dan *token* y (*reference*).

Dalam konteks penelitian ini, BERTScore digunakan untuk mengevaluasi seberapa bermakna *feedback* yang dihasilkan oleh model dibandingkan dengan *feedback* referensi, tanpa bergantung pada kesamaan struktur kalimat. Sebagai contoh, jika *feedback* referensi menyatakan, “Perlu ada penjelasan lebih dalam mengenai argumen Anda”, dan model menghasilkan, “Argumen Anda butuh elaborasi yang lebih menyeluruh”, maka meskipun susunan katanya berbeda, BERTScore tetap menghasilkan nilai tinggi karena makna kedua kalimat tersebut dianggap serupa dalam ruang semantik. Metrik ini sangat relevan untuk mengevaluasi kualitas *feedback* otomatis yang dihasilkan oleh LLM, terutama saat model menggunakan sinonim, reformulasi, atau variasi sintaks yang tidak memengaruhi substansi.

# BAB III — METODOLOGI PENELITIAN

Bab ini menjelaskan secara rinci pendekatan, data dan prosedur yang digunakan dalam penelitian untuk mengevaluasi kualitas *feedback* yang dihasilkan oleh *Large Language Models* (LLM) terhadap jawaban mahasiswa. Penjelasan mencakup pengolahan *prompt* menggunakan empat strategi *prompting* (Zero-Shot, One-Shot, Few-Shot, dan Chain-of-Thought) dan tiga jenis persona (Base, Dosen, dan Ahli). Selain itu, bab ini menjelaskan dua model LLM yang digunakan, yaitu GPT-4o mini dan LLaMA 3.1 beserta format struktur *prompt* yang diterapkan. Evaluasi dilakukan dengan empat metrik otomatis (BLEU, ROUGE-L, METEOR, dan BERTScore) menggunakan *pipeline* Python berbasis pustaka NLP.

## 3.1. Gambaran Umum Penelitian

Penelitian ini menggunakan pendekatan kuantitatif deskriptif, dengan tujuan mengevaluasi kualitas *feedback* yang dihasilkan oleh *Large Language Model* (LLM) terhadap jawaban mahasiswa pada dua mata kuliah: Sistem Cerdas dan Metodologi Penelitian dan Penulisan Ilmiah. Fokus utama penelitian ini adalah menguji efektivitas strategi *prompting* dan konfigurasi persona dalam meningkatkan kesesuaian *feedback* LLM dengan *feedback* referensi yang telah disusun sebelumnya oleh dosen atau ahli. Pendekatan ini dipilih karena memungkinkan analisis terstruktur atas keluaran model berbasis data numerik dari metrik evaluasi otomatis.

Secara umum, proses penelitian terdiri dari lima tahap utama: (1) Pengumpulan Data, (2) Penyusunan Prompt, (3) Generasi Feedback, (4) Evaluasi Otomatis, dan (5) Analisis Hasil. Tahap persiapan data mencakup pengumpulan jawaban mahasiswa dari dua mata kuliah serta *feedback* referensi untuk masing-masing jawaban. Data ini kemudian dikelompokkan dan disiapkan sebagai pasangan *input-output* yang akan digunakan dalam proses *prompting* dan evaluasi. Bagan alur rancangan penelitian dapat dilihat pada Gambar 3.1.

**Gambar 3.1. Bagan Alur Gambaran Umum Penelitian**

Pada tahap kedua, yaitu penyusunan *prompt*, dilakukan perancangan instruksi atau *template* yang akan dikirimkan ke model LLM. Empat strategi *prompting* digunakan: Zero-Shot (tanpa contoh), One-Shot (satu contoh), Few-Shot (beberapa contoh), dan Chain-of-Thought (berpikir bertahap). Setiap strategi dikombinasikan dengan tiga jenis persona: Base (netral), Dosen (gaya instruksional), dan Ahli (berbasis keilmuan). Penyusunan *prompt* dilakukan secara otomatis berdasarkan parameter yang ditentukan, sehingga menghasilkan variasi kombinasi sebanyak 21 konfigurasi untuk satu model.

Tahap ketiga adalah proses generasi *feedback*, yaitu mengirimkan *prompt* yang telah dirancang ke dua model LLM yang digunakan: GPT-4o mini (diakses melalui GPT API) dan LLaMA 3.1 (dijalankan secara lokal melalui Ollama). Setiap kombinasi strategi dan persona dijalankan pada seluruh jawaban mahasiswa, menghasilkan total 42 kombinasi (21 × 2 model) untuk setiap jawaban. Dengan jumlah 153 jawaban mahasiswa, proses ini menghasilkan 6.426 entri *feedback* yang kemudian menjadi objek evaluasi.

Tahap keempat adalah evaluasi otomatis terhadap *feedback* yang dihasilkan. Evaluasi dilakukan dengan empat metrik: BLEU untuk kesamaan n-gram, ROUGE-L untuk kesamaan urutan token, METEOR untuk kemiripan semantik dengan mempertimbangkan sinonim dan morfologi kata, serta BERTScore yang mengukur kedekatan representasi semantik berbasis model *transformer*. Nilai evaluasi disimpan dalam format terstruktur untuk keperluan analisis.

Tahap terakhir adalah analisis hasil, yaitu membandingkan performa dari setiap kombinasi strategi, persona, dan model berdasarkan nilai keempat metrik tersebut. Analisis dilakukan secara deskriptif kuantitatif menggunakan visualisasi berupa *box plot*, *bar chart*, dan tabel rata-rata untuk mengidentifikasi konfigurasi terbaik. Dengan pendekatan ini, penelitian tidak hanya menghasilkan informasi tentang model mana yang paling efektif, tetapi juga memberikan wawasan tentang pengaruh strategi *prompting* dan gaya persona terhadap kualitas *feedback* LLM dalam konteks pendidikan tinggi.

## 3.2. Pengumpulan Data

Data utama yang digunakan terdiri atas dua komponen, yaitu jawaban mahasiswa dan *feedback* referensi. Jawaban mahasiswa diperoleh dari tugas berbentuk pertanyaan terbuka yang diberikan dalam dua mata kuliah, yaitu Sistem Cerdas dan Metodologi Penelitian dan Penulisan Ilmiah (MPI) dengan masing-masing mata kuliah satu soal. Topik yang dibahas pada mata kuliah Sistem Cerdas berkaitan dengan konsep *iterative search*, sedangkan pada mata kuliah MPI lebih menekankan pada hubungan antar struktur penulisan ilmiah, seperti latar belakang, rumusan masalah, dan tujuan penelitian.

Jumlah total jawaban mahasiswa yang dianalisis dalam penelitian ini adalah 154 entri, yang terdiri dari 62 jawaban untuk mata kuliah Sistem Cerdas dan 91 jawaban untuk mata kuliah Metodologi Penelitian dan Penulisan Ilmiah (MPI). Contoh data pada mata kuliah Sistem Cerdas dapat dilihat pada Tabel 3.1.

**Tabel 3.1. Contoh Data pada Mata Kuliah Sistem Cerdas**

| Pertanyaan | Jawaban Mahasiswa | Feedback Referensi | Nilai |
| --- | --- | --- | ---: |
| Jelaskan perbedaan antara iterative searching dan non iterative searching? | Iterative search adalah sebuah jenis search yang akan terus menghitung kemungkinan sampai ditemukannya goal state. Dalam iterative search, solusi tidak selalu berupa path karena dapat mencoba untuk mencari benefit terbanyak atau cost terendah.<br><br>Non-iterative search adalah search yang tidak diulang-ulang hingga menemukan solusi terbaik, sehingga tidak melalui trial and error. Pada non-iterative search, dicarikan path untuk mencapai goal state. | Jawaban kamu hampir benar. Kamu telah menjelaskan perbedaan penggunaan serta kondisi akhir dari proses pencarian iterative search dan non-iterative search, namun kamu belum menyimpulkan kedua hal tersebut sebagai dua poin pembeda diantara kedua teknik search. | 10 |
| | iterative menggunakan hitungan dari awal sampe akhir, sedangkan non iterative tidak. | Jawaban kamu salah. Kamu tidak menjelaskan perbedaan iterative searching dan non iterative searching dari segi penggunaan dan kondisi akhir serta jawaban kamu tidak sesuai | 7 |
| | Perbedaan antara iterative seraching dan non iterative searching | Jawaban kamu salah karena tidak menjelaskan mengenai perbedaan konsep penggunaan dan kondisi akhir dari iterative searching serta non iterative searching | 1 |

*Feedback* referensi merupakan umpan balik yang telah disusun sebelumnya terhadap setiap jawaban mahasiswa. *Feedback* ini mencakup evaluasi terhadap isi jawaban, kekuatan dan kelemahan argumen yang disampaikan, serta saran konkret untuk perbaikan. Setiap jawaban mahasiswa memiliki satu *feedback* referensi yang digunakan sebagai acuan dalam mengevaluasi kualitas *feedback* yang dihasilkan oleh model LLM. Contoh data pada mata kuliah Metodologi Penelitian dan Penulisan Ilmiah dapat dilihat pada Tabel 3.2.

**Tabel 3.2. Contoh Data pada Mata Kuliah Metodologi Penelitian dan Penulisan Ilmiah**

| Pertanyaan | Jawaban Mahasiswa | Feedback Referensi | Nilai |
| --- | --- | --- | ---: |
| Jelaskan selengkap mungkin yang anda ketahui mengenai research question (rumusan masalah) dan research objective (tujuan penelitian), serta bagaimana hubungan di antara keduanya? | Baik itu Research Question (RQ) maupun Research Objective (RO), mereka berdua adalah hasil dari sebuah Research Problem (RP). RQ sendiri adalah pertanyaan-pertanyaan yang muncul setelah kita mendefinisikan RP. Jadi RQ itu sendiri adalah pertanyaan-pertanyaan tentang bagaimana kita menyelesaikan RP yang ada. Sedangkan RO adalah tujuan/goal yang harus kita capai untuk menyelesaikan RP. Hubungan di antara keduanya adalah Research Objective bertujuan untuk mendapat jawaban dan kesimpulan untuk Research Question. | Jawaban kamu sangat benar. Kamu memberikan penjelasan tentang Research Question (Rumusan Masalah) dan Research Objective (Tujuan Masalah) dengan tepat. | 10 |
| | Research question adalah rumusan masalah yang melandasi dilakukannya penelitian ilmiah secara objektif dan nantinya dapat dibuktikan secara valid dan logis, sedangkan research objective adalah tujuan dari diadakannya penelitian ilmiah. Hubungan keduanya adalah dari rumusan masalah akan dijadikan tujuan penelitian yang ingin dicapai. | Jawaban kamu salah. Penjelasan mengenai Research Question (Rumusan Masalah) dan Research Objective (Tujuan Penelitian) masih belum tepat, terutama dalam menjelaskan hubungan antara keduanya. | 7 |
| | RESEARCH QUESTION (RUMUSAN MASALAH) adalah bagaimana meningkatkan efisiensi proses training dan kinerja dari analisa sentimen berdasarkan Convolutional Neural Network dengan penerapan Bayesian optimization. RESEARCH OBJECTIVE (TUJUAN PENELITIAN) adalah bagaimana menerapkan Bayesian optimization untuk proses hyperparameter tuning pada sentiment analysis berdasarkan Convolutional Neural Network. | Jawaban kamu sangat salah. Kamu tidak memberikan penjelasan mengenai Research Question (Rumusan Masalah) dan Research Objective (Tujuan Penelitian) dengan benar, serta kamu tidak memberikan penjelasan mengenai hubungan antara keduanya. | 1 |

Selain jawaban dan *feedback* referensi, terdapat nilai atau skor dari masing-masing jawaban mahasiswa. Nilai ini digunakan secara khusus dalam strategi One-Shot *prompting* sebagai dasar pemilihan contoh jawaban yang akan disisipkan dalam *prompt*. Contoh tersebut dipilih dari jawaban mahasiswa yang memiliki kualitas tinggi (nilai tertinggi) untuk dijadikan representasi *one-shot* tinggi. Dengan demikian nilai tidak hanya berfungsi sebagai indikator performa, tetapi juga sebagai elemen desain *prompt* yang dapat memengaruhi kualitas *feedback generation* pada strategi One-Shot.

## 3.3. Penyusunan Prompt

Strategi *prompting* merupakan pendekatan kunci dalam penelitian ini untuk mengarahkan model *Large Language Model* (LLM) dalam menghasilkan umpan balik yang sesuai terhadap jawaban mahasiswa. Empat jenis strategi digunakan: Zero-Shot, One-Shot, Few-Shot, dan Chain-of-Thought, yang masing-masing menawarkan mekanisme berbeda dalam menyajikan konteks kepada model.

Tahap pertama dalam eksperimen adalah penyusunan *prompt*, yaitu instruksi dalam Bahasa Indonesia yang digunakan untuk mengarahkan model LLM dalam menghasilkan *feedback* atas jawaban mahasiswa. Untuk masing-masing model (GPT-4o mini dan LLaMA), dirancang sebanyak 21 kombinasi strategi *prompting* dan persona, yang mencakup empat pendekatan *prompting* (Zero-Shot, One-Shot, Few-Shot, dan Chain-of-Thought) serta tiga jenis persona (Base, Dosen, dan Ahli).

Untuk strategi One-Shot dan Few-Shot, *prompt* menyertakan contoh jawaban mahasiswa dan *feedback* referensi sebagai konteks pembelajaran. Sedangkan untuk strategi Chain-of-Thought, *prompt* dimodifikasi dengan arahan tambahan berupa kalimat “pikirkan langkah demi langkah” agar model dapat mengekspresikan penalarannya secara eksplisit.

### 3.3.1. Strategi Zero-Shot

Strategi Zero-Shot mengandalkan instruksi langsung tanpa memberikan contoh sebelumnya. Dalam pendekatan ini, model diminta memberikan *feedback* berdasarkan perintah eksplisit seperti mengevaluasi ketepatan konsep, mengidentifikasi kesalahan, dan memberikan saran perbaikan. Strategi ini menguji kemampuan dasar model dalam memahami dan merespons tugas tanpa pembelajaran dari konteks tambahan. Penyusunan *prompt* menggunakan strategi Zero-Shot pada mata kuliah Sistem Cerdas dapat dilihat pada Tabel 3.3 dan Metodologi Penelitian dan Penulisan Ilmiah dapat dilihat pada Tabel 3.4.

**Tabel 3.3. Penyusunan Prompt Strategi Zero-Shot pada Mata Kuliah Sistem Cerdas**

| Komponen Prompt | Prompt |
| --- | --- |
| Persona | **Base:** “Anda adalah asisten AI yang memberikan feedback singkat dan objektif. Tugas Anda adalah mengevaluasi jawaban mahasiswa dalam mata kuliah Sistem Cerdas. Feedback harus jelas, berbasis konsep kecerdasan buatan, dan memberikan saran konkret untuk perbaikan.”<br><br>**Dosen:** “Anda adalah seorang dosen yang mengajar mata kuliah Sistem Cerdas. Feedback Anda harus bersifat pedagogis, membimbing mahasiswa untuk memahami konsep kecerdasan buatan (AI), pencarian heuristik, pembelajaran mesin, dan sistem berbasis pengetahuan. Berikan saran yang membantu mahasiswa mengembangkan pemahamannya terhadap konsep yang diajarkan.”<br><br>**Ahli:** “Anda adalah seorang ahli dalam bidang Sistem Cerdas dengan pengalaman dalam kecerdasan buatan (AI), machine learning, pencarian heuristik, dan sistem berbasis pengetahuan. Tugas Anda adalah mengevaluasi jawaban mahasiswa dengan standar akademik tinggi, memastikan pemahaman mendalam terhadap algoritma pencarian, representasi pengetahuan, serta penerapan AI dalam berbagai domain. Feedback harus mendalam, memberikan kritik konstruktif, serta menyarankan literatur atau pendekatan yang lebih tepat.” |
| Ruang Lingkup | “Evaluasi jawaban mahasiswa dalam mata kuliah Sistem Cerdas” |
| Pertanyaan | “Pertanyaan: Jelaskan perbedaan antara iterative searching dan non iterative searching?” |
| Jawaban Mahasiswa | “Jawaban: {jawaban mahasiswa}” |
| Instruksi | “Berikan feedback yang:<br>1) Mengevaluasi ketepatan konsep.<br>2) Menyebutkan kesalahan atau kekurangan pemahaman jika ada.<br>3) Memberikan saran akademik atau perbaikan agar lebih baik.” |

**Tabel 3.4. Penyusunan Prompt Strategi Zero-Shot pada Mata Kuliah Metodologi Penelitian dan Penulisan Ilmiah**

| Komponen Prompt | Prompt |
| --- | --- |
| Persona | **Base:** “Anda adalah asisten AI yang memberikan feedback singkat, objektif, dan berbasis prinsip penelitian ilmiah. Tugas Anda adalah mengevaluasi jawaban mahasiswa dalam mata kuliah Metodologi Penelitian dan Penulisan Ilmiah. Feedback harus jelas, ringkas, dan memberikan saran spesifik untuk perbaikan jawaban”<br><br>**Dosen:** “Anda adalah seorang dosen yang mengajar mata kuliah Metodologi Penelitian dan Penulisan Ilmiah. Feedback Anda harus bersifat pedagogis, membantu mahasiswa memahami konsep dasar penelitian ilmiah, seperti perumusan masalah, metode penelitian, validitas data, dan struktur penulisan ilmiah.”<br><br>**Ahli:** “Anda adalah seorang ahli dalam bidang Metodologi Penelitian dan Penulisan Ilmiah dengan pengalaman mendalam dalam desain eksperimen, analisis data, dan publikasi akademik. Tugas Anda adalah mengevaluasi jawaban mahasiswa dengan standar akademik yang tinggi, mencakup keakuratan metodologi, kesesuaian pendekatan penelitian, serta kepatuhan terhadap kaidah penulisan ilmiah. Feedback harus mendalam, memberikan kritik konstruktif, serta menyarankan referensi atau pendekatan yang lebih tepat untuk meningkatkan kualitas penelitian mahasiswa. Berikan saran yang membimbing mahasiswa untuk menyusun penelitian yang lebih sistematis dan akademik.” |
| Ruang Lingkup | “Evaluasi jawaban mahasiswa dalam mata kuliah Metodologi Penelitian dan Penulisan Ilmiah.” |
| Pertanyaan | “Pertanyaan: Jelaskan selengkap mungkin yang anda ketahui mengenai research question (rumusan masalah) dan research objective (tujuan penelitian), serta bagaimana hubungan di antara keduanya?” |
| Jawaban Mahasiswa | “Jawaban: {jawaban mahasiswa}” |
| Instruksi | “Berikan feedback yang:<br>1) Mengevaluasi ketepatan konsep.<br>2) Menyebutkan kesalahan atau kekurangan pemahaman jika ada.<br>3) Memberikan saran akademik atau perbaikan agar lebih baik.” |

### 3.3.2. Strategi One-Shot

Strategi One-Shot memberikan satu contoh *feedback* untuk satu pertanyaan dan jawaban mahasiswa yang berbeda sebelum model diminta mengevaluasi jawaban baru. Contoh tersebut diambil dari data *feedback* referensi yang memiliki nilai tinggi (8–10), sedang (5–7), dan rendah (0–5), dan *feedback* dari jawaban itu dengan asumsi bahwa model akan belajar dari respons dari setiap contoh *feedback* yang diberikan. Dengan cara ini, model memiliki referensi gaya dan substansi umpan balik sebelum memproses *input* baru. Penyusunan *prompt* menggunakan strategi One-Shot pada mata kuliah Sistem Cerdas dapat dilihat pada Tabel 3.5 dan Metodologi Penelitian dan Penulisan Ilmiah dapat dilihat pada Tabel 3.6.

**Tabel 3.5. Penyusunan Prompt Strategi One-Shot pada Mata Kuliah Sistem Cerdas**

| Komponen Prompt | Prompt |
| --- | --- |
| Persona | **Base:** “Anda adalah asisten AI yang memberikan feedback singkat dan objektif. Tugas Anda adalah mengevaluasi jawaban mahasiswa dalam mata kuliah Sistem Cerdas. Feedback harus jelas, berbasis konsep kecerdasan buatan, dan memberikan saran konkret untuk perbaikan.”<br><br>**Dosen:** “Anda adalah seorang dosen yang mengajar mata kuliah Sistem Cerdas. Feedback Anda harus bersifat pedagogis, membimbing mahasiswa untuk memahami konsep kecerdasan buatan (AI), pencarian heuristik, pembelajaran mesin, dan sistem berbasis pengetahuan. Berikan saran yang membantu mahasiswa mengembangkan pemahamannya terhadap konsep yang diajarkan.”<br><br>**Ahli:** “Anda adalah seorang ahli dalam bidang Sistem Cerdas dengan pengalaman dalam kecerdasan buatan (AI), machine learning, pencarian heuristik, dan sistem berbasis pengetahuan. Tugas Anda adalah mengevaluasi jawaban mahasiswa dengan standar akademik tinggi, memastikan pemahaman mendalam terhadap algoritma pencarian, representasi pengetahuan, serta penerapan AI dalam berbagai domain. Feedback harus mendalam, memberikan kritik konstruktif, serta menyarankan literatur atau pendekatan yang lebih tepat.” |
| Ruang Lingkup | “Evaluasi jawaban mahasiswa dalam mata kuliah Sistem Cerdas” |
| Contoh Feedback | **Tinggi:** “Berikut adalah contoh feedback untuk jawaban mahasiswa:<br><br>Pertanyaan: Jelaskan perbedaan antara iterative searching dan non iterative searching?<br><br>Jawaban Mahasiswa: Iterative search adalah sebuah jenis search yang akan terus menghitung kemungkinan sampai ditemukannya goal state. Dalam iterative search, solusi tidak selalu berupa path karena dapat mencoba untuk mencari benefit terbanyak atau cost terendah.<br>Non-iterative search adalah search yang tidak diulang-ulang hingga menemukan solusi terbaik, sehingga tidak melalui trial and error. Pada non-iterative search, dicarikan path untuk mencapai goal state.<br><br>Feedback: Jawaban kamu hampir benar. Kamu telah menjelaskan perbedaan penggunaan serta kondisi akhir dari proses pencarian iterative search dan non-iterative search, namun kamu belum menyimpulkan kedua hal tersebut sebagai dua poin pembeda diantara kedua teknik search.”<br><br>**Sedang:** “Berikut adalah contoh feedback untuk jawaban mahasiswa:<br><br>Pertanyaan: Jelaskan perbedaan antara iterative searching dan non iterative searching?<br><br>Jawaban Mahasiswa: iterative menggunakan hitungan dari awal sampe akhir, sedangkan non iterative tidak.<br><br>Feedback: Jawaban kamu salah. Kamu tidak menjelaskan perbedaan iterative searching dan non iterative searching dari segi penggunaan dan kondisi akhir serta jawaban kamu tidak sesuai”<br><br>**Rendah:** “Berikut adalah contoh feedback untuk jawaban mahasiswa:<br><br>Pertanyaan: Jelaskan perbedaan antara iterative searching dan non iterative searching?<br><br>Jawaban Mahasiswa: Perbedaan antara iterative seraching dan non iterative searching<br><br>Feedback: Jawaban kamu salah karena tidak menjelaskan mengenai perbedaan konsep penggunaan dan kondisi akhir dari iterative searching serta non iterative searching”<br><br>**Feedback Asli:** “{feedback referensi}” |
| Instruksi (Pertanyaan dan Jawaban Mahasiswa) | “Sekarang, berikan feedback untuk jawaban berikut:<br><br>Pertanyaan: Jelaskan perbedaan antara iterative searching dan non iterative searching?<br><br>Jawaban Mahasiswa: {jawaban mahasiswa}<br><br>Feedback:” |

**Tabel 3.6. Penyusunan Prompt Strategi One-Shot pada Mata Kuliah Metodologi Penelitian dan Penulisan Ilmiah**

| Komponen Prompt | Prompt |
| --- | --- |
| Persona | **Base:** “Anda adalah asisten AI yang memberikan feedback singkat, objektif, dan berbasis prinsip penelitian ilmiah. Tugas Anda adalah mengevaluasi jawaban mahasiswa dalam mata kuliah Metodologi Penelitian dan Penulisan Ilmiah. Feedback harus jelas, ringkas, dan memberikan saran spesifik untuk perbaikan jawaban”<br><br>**Dosen:** “Anda adalah seorang dosen yang mengajar mata kuliah Metodologi Penelitian dan Penulisan Ilmiah. Feedback Anda harus bersifat pedagogis, membantu mahasiswa memahami konsep dasar penelitian ilmiah, seperti perumusan masalah, metode penelitian, validitas data, dan struktur penulisan ilmiah.”<br><br>**Ahli:** “Anda adalah seorang ahli dalam bidang Metodologi Penelitian dan Penulisan Ilmiah dengan pengalaman mendalam dalam desain eksperimen, analisis data, dan publikasi akademik. Tugas Anda adalah mengevaluasi jawaban mahasiswa dengan standar akademik yang tinggi, mencakup keakuratan metodologi, kesesuaian pendekatan penelitian, serta kepatuhan terhadap kaidah penulisan ilmiah. Feedback harus mendalam, memberikan kritik konstruktif, serta menyarankan referensi atau pendekatan yang lebih tepat untuk meningkatkan kualitas penelitian mahasiswa. Berikan saran yang membimbing mahasiswa untuk menyusun penelitian yang lebih sistematis dan akademik.” |
| Ruang Lingkup | “Evaluasi jawaban mahasiswa dalam mata kuliah Metodologi Penelitian dan Penulisan Ilmiah.” |
| Contoh Feedback | **Tinggi:** “Berikut adalah contoh feedback untuk jawaban mahasiswa:<br><br>Pertanyaan: Jelaskan selengkap mungkin yang anda ketahui mengenai research question (rumusan masalah) dan research objective (tujuan penelitian), serta bagaimana hubungan di antara keduanya?<br><br>Jawaban Mahasiswa: Baik itu Research Question (RQ) maupun Research Objective (RO), mereka berdua adalah hasil dari sebuah Research Problem (RP). RQ sendiri adalah pertanyaan-pertanyaan yang muncul setelah kita mendefinisikan RP. Jadi RQ itu sendiri adalah pertanyaan-pertanyaan tentang bagaimana kita menyelesaikan RP yang ada. Sedangkan RO adalah tujuan/goal yang harus kita capai untuk menyelesaikan RP. Hubungan di antara keduanya adalah Research Objective bertujuan untuk mendapat jawaban dan kesimpulan untuk Research Question.<br><br>Feedback: Jawaban kamu sangat benar. Kamu memberikan penjelasan tentang Research Question (Rumusan Masalah) dan Research Objective (Tujuan Masalah) dengan tepat.”<br><br>**Sedang:** “Berikut adalah contoh feedback untuk jawaban mahasiswa:<br><br>Pertanyaan: Jelaskan selengkap mungkin yang anda ketahui mengenai research question (rumusan masalah) dan research objective (tujuan penelitian), serta bagaimana hubungan di antara keduanya?<br><br>Jawaban Mahasiswa: Research question adalah rumusan masalah yang melandasi dilakukannya penelitian ilmiah secara objektif dan nantinya dapat dibuktikan secara valid dan logis, sedangkan research objective adalah tujuan dari diadakannya penelitian ilmiah. Hubungan keduanya adalah dari rumusan masalah akan dijadikan tujuan penelitian yang ingin dicapai.<br><br>Feedback: Jawaban kamu salah. Penjelasan mengenai Research Question (Rumusan Masalah) dan Research Objective (Tujuan Penelitian) masih belum tepat, terutama dalam menjelaskan hubungan antara keduanya.”<br><br>**Rendah:** “Berikut adalah contoh feedback untuk jawaban mahasiswa:<br><br>Pertanyaan: Jelaskan selengkap mungkin yang anda ketahui mengenai research question (rumusan masalah) dan research objective (tujuan penelitian), serta bagaimana hubungan di antara keduanya?<br><br>Jawaban Mahasiswa: RESEARCH QUESTION (RUMUSAN MASALAH) adalah bagaimana meningkatkan efisiensi proses training dan kinerja dari analisa sentimen berdasarkan Convolutional Neural Network dengan penerapan Bayesian optimization. RESEARCH OBJECTIVE (TUJUAN PENELITIAN) adalah bagaimana menerapkan Bayesian optimization untuk proses hyperparameter tuning pada sentiment analysis berdasarkan Convolutional Neural Network.<br><br>Feedback: Jawaban kamu sangat salah. Kamu tidak memberikan penjelasan mengenai Research Question (Rumusan Masalah) dan Research Objective (Tujuan Penelitian) dengan benar, serta kamu tidak memberikan penjelasan mengenai hubungan antara keduanya.”<br><br>**Feedback Asli:** “{feedback referensi}” |
| Instruksi (Pertanyaan dan Jawaban Mahasiswa) | “Sekarang, berikan feedback untuk jawaban berikut:<br><br>Pertanyaan: Jelaskan selengkap mungkin yang anda ketahui mengenai research question (rumusan masalah) dan research objective (tujuan penelitian), serta bagaimana hubungan di antara keduanya?<br><br>Jawaban Mahasiswa: {student_answer}<br><br>Feedback:” |

### 3.3.3. Strategi Few-Shot

Strategi Few-Shot memberikan beberapa contoh lengkap (pertanyaan, jawaban, dan *feedback*) dalam *prompt*. Strategi ini memberi model konteks yang lebih luas mengenai pola evaluasi yang diharapkan. Contoh-contoh tersebut disusun agar mencerminkan keberagaman respon dan gaya evaluasi akademik, dengan harapan meningkatkan ketepatan dan konsistensi *feedback* model. Penyusunan *prompt* menggunakan strategi Few-Shot pada mata kuliah Sistem Cerdas dapat dilihat pada Tabel 3.7 dan Metodologi Penelitian dan Penulisan Ilmiah dapat dilihat pada Tabel 3.8.

**Tabel 3.7. Penyusunan Prompt Strategi Few-Shot pada Mata Kuliah Sistem Cerdas**

| Komponen Prompt | Prompt |
| --- | --- |
| Persona | **Base:** “Anda adalah asisten AI yang memberikan feedback singkat dan objektif. Tugas Anda adalah mengevaluasi jawaban mahasiswa dalam mata kuliah Sistem Cerdas. Feedback harus jelas, berbasis konsep kecerdasan buatan, dan memberikan saran konkret untuk perbaikan.”<br><br>**Dosen:** “Anda adalah seorang dosen yang mengajar mata kuliah Sistem Cerdas. Feedback Anda harus bersifat pedagogis, membimbing mahasiswa untuk memahami konsep kecerdasan buatan (AI), pencarian heuristik, pembelajaran mesin, dan sistem berbasis pengetahuan. Berikan saran yang membantu mahasiswa mengembangkan pemahamannya terhadap konsep yang diajarkan.”<br><br>**Ahli:** “Anda adalah seorang ahli dalam bidang Sistem Cerdas dengan pengalaman dalam kecerdasan buatan (AI), machine learning, pencarian heuristik, dan sistem berbasis pengetahuan. Tugas Anda adalah mengevaluasi jawaban mahasiswa dengan standar akademik tinggi, memastikan pemahaman mendalam terhadap algoritma pencarian, representasi pengetahuan, serta penerapan AI dalam berbagai domain. Feedback harus mendalam, memberikan kritik konstruktif, serta menyarankan literatur atau pendekatan yang lebih tepat.” |
| Ruang Lingkup | “Evaluasi jawaban mahasiswa dalam mata kuliah Sistem Cerdas” |
| Contoh Feedback | “Berikut adalah contoh feedback untuk jawaban mahasiswa:<br><br>Pertanyaan: Jelaskan perbedaan antara iterative searching dan non iterative searching?<br><br>Jawaban Mahasiswa: Iterative search adalah sebuah jenis search yang akan terus menghitung kemungkinan sampai ditemukannya goal state. Dalam iterative search, solusi tidak selalu berupa path karena dapat mencoba untuk mencari benefit terbanyak atau cost terendah.<br>Non-iterative search adalah search yang tidak diulang-ulang hingga menemukan solusi terbaik, sehingga tidak melalui trial and error. Pada non-iterative search, dicarikan path untuk mencapai goal state.<br><br>Feedback: Jawaban kamu hampir benar. Kamu telah menjelaskan perbedaan penggunaan serta kondisi akhir dari proses pencarian iterative search dan non-iterative search, namun kamu belum menyimpulkan kedua hal tersebut sebagai dua poin pembeda diantara kedua teknik search.”<br><br>“Berikut adalah contoh feedback untuk jawaban mahasiswa:<br><br>Pertanyaan: Jelaskan perbedaan antara iterative searching dan non iterative searching?<br><br>Jawaban Mahasiswa: iterative menggunakan hitungan dari awal sampe akhir, sedangkan non iterative tidak.<br><br>Feedback: Jawaban kamu salah. Kamu tidak menjelaskan perbedaan iterative searching dan non iterative searching dari segi penggunaan dan kondisi akhir serta jawaban kamu tidak sesuai”<br><br>“Berikut adalah contoh feedback untuk jawaban mahasiswa:<br><br>Pertanyaan: Jelaskan perbedaan antara iterative searching dan non iterative searching?<br><br>Jawaban Mahasiswa: Perbedaan antara iterative seraching dan non iterative searching<br><br>Feedback: Jawaban kamu salah karena tidak menjelaskan mengenai perbedaan konsep penggunaan dan kondisi akhir dari iterative searching serta non iterative searching” |
| Instruksi (Pertanyaan dan Jawaban Mahasiswa) | “Sekarang, berikan feedback untuk jawaban berikut:<br><br>Pertanyaan: Jelaskan perbedaan antara iterative searching dan non iterative searching?<br><br>Jawaban Mahasiswa: {jawaban mahasiswa}<br><br>Feedback:” |

**Tabel 3.8. Penyusunan Prompt Strategi Few-Shot pada Mata Kuliah Sistem Cerdas**

| Komponen Prompt | Prompt |
| --- | --- |
| Persona | **Base:** “Anda adalah asisten AI yang memberikan feedback singkat, objektif, dan berbasis prinsip penelitian ilmiah. Tugas Anda adalah mengevaluasi jawaban mahasiswa dalam mata kuliah Metodologi Penelitian dan Penulisan Ilmiah. Feedback harus jelas, ringkas, dan memberikan saran spesifik untuk perbaikan jawaban”<br><br>**Dosen:** “Anda adalah seorang dosen yang mengajar mata kuliah Metodologi Penelitian dan Penulisan Ilmiah. Feedback Anda harus bersifat pedagogis, membantu mahasiswa memahami konsep dasar penelitian ilmiah, seperti perumusan masalah, metode penelitian, validitas data, dan struktur penulisan ilmiah.”<br><br>**Ahli:** “Anda adalah seorang ahli dalam bidang Metodologi Penelitian dan Penulisan Ilmiah dengan pengalaman mendalam dalam desain eksperimen, analisis data, dan publikasi akademik. Tugas Anda adalah mengevaluasi jawaban mahasiswa dengan standar akademik yang tinggi, mencakup keakuratan metodologi, kesesuaian pendekatan penelitian, serta kepatuhan terhadap kaidah penulisan ilmiah. Feedback harus mendalam, memberikan kritik konstruktif, serta menyarankan referensi atau pendekatan yang lebih tepat untuk meningkatkan kualitas penelitian mahasiswa. Berikan saran yang membimbing mahasiswa untuk menyusun penelitian yang lebih sistematis dan akademik.” |
| Ruang Lingkup | “Evaluasi jawaban mahasiswa dalam mata kuliah Metodologi Penelitian dan Penulisan Ilmiah.” |
| Contoh Feedback 1 | Berikut adalah contoh feedback untuk jawaban mahasiswa:<br><br>**Pertanyaan:** Jelaskan selengkap mungkin yang anda ketahui mengenai research question (rumusan masalah) dan research objective (tujuan penelitian), serta bagaimana hubungan di antara keduanya?<br><br>**Jawaban Mahasiswa:** Baik itu Research Question (RQ) maupun Research Objective (RO), mereka berdua adalah hasil dari sebuah Research Problem (RP). RQ sendiri adalah pertanyaan-pertanyaan yang muncul setelah kita mendefinisikan RP. Jadi RQ itu sendiri adalah pertanyaan-pertanyaan tentang bagaimana kita menyelesaikan RP yang ada. Sedangkan RO adalah tujuan/goal yang harus kita capai untuk menyelesaikan RP. Hubungan di antara keduanya adalah Research Objective bertujuan untuk mendapat jawaban dan kesimpulan untuk Research Question.<br><br>**Feedback:** Jawaban kamu sangat benar. Kamu memberikan penjelasan tentang Research Question (Rumusan Masalah) dan Research Objective (Tujuan Penelitian) dengan tepat. |
| Contoh Feedback 2 | Berikut adalah contoh feedback untuk jawaban mahasiswa:<br><br>**Pertanyaan:** Jelaskan selengkap mungkin yang anda ketahui mengenai research question (rumusan masalah) dan research objective (tujuan penelitian), serta bagaimana hubungan di antara keduanya?<br><br>**Jawaban Mahasiswa:** Research question adalah rumusan masalah yang melandasi dilakukannya penelitian ilmiah secara objektif dan nantinya dapat dibuktikan secara valid dan logis, sedangkan research objective adalah tujuan dari diadakannya penelitian ilmiah. Hubungan keduanya adalah dari rumusan masalah akan dijadikan tujuan penelitian yang ingin dicapai.<br><br>**Feedback:** Jawaban kamu salah. Penjelasan mengenai Research Question (Rumusan Masalah) dan Research Objective (Tujuan Penelitian) masih belum tepat, terutama dalam menjelaskan hubungan antara keduanya. |
| Contoh Feedback 3 | Berikut adalah contoh feedback untuk jawaban mahasiswa:<br><br>**Pertanyaan:** Jelaskan selengkap mungkin yang anda ketahui mengenai research question (rumusan masalah) dan research objective (tujuan penelitian), serta bagaimana hubungan di antara keduanya?<br><br>**Jawaban Mahasiswa:** RESEARCH QUESTION (RUMUSAN MASALAH) adalah bagaimana meningkatkan efisiensi proses training dan kinerja dari analisa sentimen berdasarkan Convolutional Neural Network dengan penerapan Bayesian optimization. RESEARCH OBJECTIVE (TUJUAN PENELITIAN) adalah bagaimana menerapkan Bayesian optimization untuk proses hyperparameter tuning pada sentiment analysis berdasarkan Convolutional Neural Network.<br><br>**Feedback:** Jawaban kamu sangat salah. Kamu tidak memberikan penjelasan mengenai Research Question (Rumusan Masalah) dan Research Objective (Tujuan Penelitian) dengan benar, serta kamu tidak memberikan penjelasan mengenai hubungan antara keduanya. |
| Instruksi (Pertanyaan dan Jawaban Mahasiswa) | “Sekarang, berikan feedback untuk jawaban berikut:<br><br>Pertanyaan: Jelaskan selengkap mungkin yang anda ketahui mengenai research question (rumusan masalah) dan research objective (tujuan penelitian), serta bagaimana hubungan di antara keduanya?<br><br>Jawaban Mahasiswa: {student_answer}<br><br>Feedback:” |

### 3.3.4. Strategi Chain-of-Thought

Strategi *Chain-of-Thought* menambahkan elemen berpikir bertahap dalam menyusun *feedback*. Dalam *prompt*, model diarahkan untuk mengevaluasi jawaban secara sistematis, mulai dari analisis konsep, identifikasi kesalahan, pemberian saran, hingga kaitan dengan penerapan dunia nyata atau teori terkait. Pendekatan ini bertujuan meningkatkan kualitas *reasoning* model dan relevansi *feedback*. Penyusunan *prompt* menggunakan strategi *Chain-of-Thought* pada mata kuliah Sistem Cerdas dapat dilihat pada Tabel 3.9 dan Metodologi penelitian dan Penulisan Ilmiah dapat dilihat pada Tabel 3.10.

**Tabel 3.9. Penyusunan Prompt Strategi Chain-of-Thought pada Sistem Cerdas**

| Komponen Prompt | Prompt |
| --- | --- |
| Persona | **Base:** “Anda adalah asisten AI yang memberikan feedback singkat dan objektif. Tugas Anda adalah mengevaluasi jawaban mahasiswa dalam mata kuliah Sistem Cerdas. Feedback harus jelas, berbasis konsep kecerdasan buatan, dan memberikan saran konkret untuk perbaikan.”<br><br>**Dosen:** “Anda adalah seorang dosen yang mengajar mata kuliah Sistem Cerdas. Feedback Anda harus bersifat pedagogis, membimbing mahasiswa untuk memahami konsep kecerdasan buatan (AI), pencarian heuristik, pembelajaran mesin, dan sistem berbasis pengetahuan. Berikan saran yang membantu mahasiswa mengembangkan pemahamannya terhadap konsep yang diajarkan.”<br><br>**Ahli:** “Anda adalah seorang ahli dalam bidang Sistem Cerdas dengan pengalaman dalam kecerdasan buatan (AI), machine learning, pencarian heuristik, dan sistem berbasis pengetahuan. Tugas Anda adalah mengevaluasi jawaban mahasiswa dengan standar akademik tinggi, memastikan pemahaman mendalam terhadap algoritma pencarian, representasi pengetahuan, serta penerapan AI dalam berbagai domain. Feedback harus mendalam, memberikan kritik konstruktif, serta menyarankan literatur atau pendekatan yang lebih tepat.” |
| Instruksi Chain-of-Thought | “Gunakan pendekatan berpikir bertahap (Chain-of-Thought) untuk memberikan feedback:<br>1) Evaluasi ketepatan konsep.<br>2) Identifikasi kesalahan atau kekurangan dalam jawaban mahasiswa.<br>3) Berikan saran konkret dan akademik untuk memperbaiki jawaban.<br>4) Kaitkan dengan penerapan dunia nyata atau referensi teori jika relevan.” |
| Ruang Lingkup | “Evaluasi jawaban mahasiswa dalam mata kuliah Sistem Cerdas” |
| Pertanyaan | “Pertanyaan: Jelaskan perbedaan antara iterative searching dan non iterative searching? |
| Jawaban Mahasiswa | “Jawaban: {jawaban mahasiswa}” |

**Tabel 3.10. Penyusunan Prompt Strategi Chain-of-Thought pada Mata Kuliah Metodologi dan Penelitian Ilmiah**

| Komponen Prompt | Prompt |
| --- | --- |
| Persona | **Base:** “Anda adalah asisten AI yang memberikan feedback singkat, objektif, dan berbasis prinsip penelitian ilmiah. Tugas Anda adalah mengevaluasi jawaban mahasiswa dalam mata kuliah Metodologi Penelitian dan Penulisan Ilmiah. Feedback harus jelas, ringkas, dan memberikan saran spesifik untuk perbaikan jawaban”<br><br>**Dosen:** “Anda adalah seorang dosen yang mengajar mata kuliah Metodologi Penelitian dan Penulisan Ilmiah. Feedback Anda harus bersifat pedagogis, membantu mahasiswa memahami konsep dasar penelitian ilmiah, seperti perumusan masalah, metode penelitian, validitas data, dan struktur penulisan ilmiah.”<br><br>**Ahli:** “Anda adalah seorang ahli dalam bidang Metodologi Penelitian dan Penulisan Ilmiah dengan pengalaman mendalam dalam desain eksperimen, analisis data, dan publikasi akademik. Tugas Anda adalah mengevaluasi jawaban mahasiswa dengan standar akademik yang tinggi, mencakup keakuratan metodologi, kesesuaian pendekatan penelitian, serta kepatuhan terhadap kaidah penulisan ilmiah. Feedback harus mendalam, memberikan kritik konstruktif, serta menyarankan referensi atau pendekatan yang lebih tepat untuk meningkatkan kualitas penelitian mahasiswa. Berikan saran yang membimbing mahasiswa untuk menyusun penelitian yang lebih sistematis dan akademik.” |
| Instruksi Chain-of-Thought | “Gunakan pendekatan berpikir bertahap (Chain-of-Thought) untuk memberikan feedback:<br>1) Evaluasi ketepatan konsep.<br>2) Identifikasi kesalahan atau kekurangan dalam jawaban mahasiswa.<br>3) Berikan saran konkret dan akademik untuk memperbaiki jawaban.<br>4) Kaitkan dengan penerapan dunia nyata atau referensi teori jika relevan.” |
| Ruang Lingkup | “Evaluasi jawaban mahasiswa dalam mata kuliah Metodologi Penelitian dan Penulisan Ilmiah.” |
| Pertanyaan | “Pertanyaan: Jelaskan selengkap mungkin yang anda ketahui mengenai research question (rumusan masalah) dan research objective (tujuan penelitian), serta bagaimana hubungan di antara keduanya?” |
| Jawaban Mahasiswa | “Jawaban: {jawaban mahasiswa}” |

## 3.4. Generasi Feedback oleh LLM

Proses generasi *feedback* dalam penelitian ini dilakukan dengan menerapkan kombinasi strategi *prompting* dan persona pada dua model LLM, yaitu GPT-4o mini yang dijalankan melalui antarmuka API GPT, serta LLaMA lokal yang dijalankan menggunakan platform Ollama secara *offline*. Setiap model dipasangkan dengan 21 kombinasi eksperimen, sehingga total terdapat 42 kombinasi feedback yang dihasilkan untuk setiap jawaban mahasiswa. Dengan jumlah total 153 jawaban yang terdiri dari 62 jawaban pada mata kuliah Sistem Cerdas dan 91 pada mata kuliah Metodologi Penelitian dan Penulisan Ilmiah, proses ini menghasilkan sebanyak 6,426 output feedback yang siap dievaluasi.

Untuk setiap kombinasi eksperimen, model diberikan sebuah *prompt* yang telah disusun sebelumnya berdasarkan empat strategi utama, yaitu *Zero-Shot*, *One-Shot*, *Few-Shot*, dan *Chain-of-Thought*, serta tiga persona, yaitu Base, Dosen, dan Ahli. Prompt disusun dalam Bahasa Indonesia agar konsisten dengan bahasa jawaban mahasiswa. Strategi *One-Shot* dan *Few-Shot* menyertakan contoh konteks sebelumnya sebagai bagian dari isi *prompt*, sementara strategi *Zero-Shot* dan *Chain-of-Thought* menggunakan instruksi langsung tanpa konteks, atau dengan penekanan pada proses penalaran bertahap. *Prompt* ini dikombinasikan dengan setiap jawaban mahasiswa untuk menghasilkan *feedback* otomatis dari LLM.

Seluruh hasil *output* disimpan dalam format CSV dengan struktur yang terstandarisasi agar mudah diolah secara terotomatisasi. Setiap entri data mencakup kolom-kolom sebagai berikut: "Strategy", "OneShotType", "Persona", "Question", "Jawaban", "GeneratedFeedback", "Prompt", "BLEU", "ROUGE_L", "METEOR", dan "BERTScore_F1". Kolom "Strategy" berisi jenis strategi prompting yang digunakan, sedangkan "OneShotType" diisi dengan "N/A" apabila strategi yang digunakan bukan *One-Shot* atau *Few-Shot*. Kolom "Persona" menunjukkan peran yang diasumsikan oleh model dalam *prompt*. Kolom "Question" dan "Jawaban" menyimpan soal yang dijawab dan isi jawaban mahasiswa, sedangkan "Prompt" menyimpan isi lengkap perintah yang diberikan ke model. Hasil *feedback* yang dihasilkan model disimpan dalam "GeneratedFeedback", dan skor evaluasi terhadap *feedback* tersebut tercatat dalam kolom BLEU, ROUGE_L, METEOR, dan BERTScore_F1.

## 3.5. Evaluasi Hasil Generasi

Evaluasi hasil generasi *feedback* dalam penelitian ini dilakukan untuk menilai seberapa baik *output* model LLM mendekati atau menyerupai *feedback* referensi (*gold standard*). Proses evaluasi ini menggunakan pendekatan evaluasi otomatis berbasis kemiripan teks yang telah umum digunakan dalam *Natural Language Generation* (NLG), khususnya pada tugas-tugas seperti *summarization*, *translation*, dan *feedback generation*.

Subbab berikut akan ditampilkan contoh perhitungan keempat metrik evaluasi, yaitu BLEU, ROUGE-L, METEOR, dan BERTScore, menggunakan pasangan kalimat *feedback* referensi dan *feedback* hasil LLM sebagai data uji. Setiap hasil *feedback* yang dihasilkan oleh model akan dievaluasi terhadap *feedback* referensi menggunakan keempat metrik tersebut. Setiap langkah perhitungan dijelaskan secara rinci agar pembaca memahami proses evaluasi yang diterapkan, termasuk bagaimana nilai *precision*, *recall*, dan skor akhir dihitung untuk setiap metrik. *Feedback* referensi yang akan digunakan dapat dilihat pada Tabel 3.11.

**Tabel 3.11. Data Feedback Referensi Contoh Perhitungan Setiap Metrik**

| Jenis | Data |
| --- | --- |
| Kalimat | Jawaban kamu salah. Penjelasan mengenai Research Question (Rumusan Masalah) dan Research Objective (Tujuan Masalah) salah dan penjelasan mengenai hubungan Research Question (Rumusan Masalah) dan Research Objective (Tujuan Masalah) masih salah. |
| Token | `["Jawaban", "kamu", "salah.", "Penjelasan", "mengenai", "Research", "Question", "(Rumusan", "Masalah)", "dan", "Research", "Objective", "(Tujuan", "Masalah)", "salah", "dan", "penjelasan", "mengenai", "hubungan", "Research", "Question", "(Rumusan", "Masalah)", "dan", "Research", "Objective", "(Tujuan", "Masalah)", "masih", "salah."]` |

Terdapat juga *feedback* yang merupakan hasil *generate* dari LLM yang merupakan kandidat (*candidate*). Data *feedback* LLM dapat dilihat pada Tabel 3.12.

**Tabel 3.12. Data Feedback Referensi Contoh Perhitungan Setiap Metrik**

| Jenis | Data |
| --- | --- |
| Kalimat | Jawaban kamu kurang tepat. Penjelasan tentang Research Question (Rumusan Masalah) dan Research Objective (Tujuan Masalah) tidak benar, serta hubungan antara Research Question dan Research Objective juga keliru. |
| Token | `["Jawaban", "kamu", "kurang", "tepat.", "Penjelasan", "tentang", "Research", "Question", "(Rumusan", "Masalah)", "dan", "Research", "Objective", "(Tujuan", "Masalah)", "tidak", "benar,", "serta", "hubungan", "antara", "Research", "Question", "dan", "Research", "Objective", "juga", "keliru."]` |

### 3.5.1. Perhitungan Metrik Evaluasi BLEU

Pada penelitian ini, salah satu metrik yang digunakan untuk mengevaluasi kualitas *feedback* yang dihasilkan oleh LLM adalah BLEU (*Bilingual Evaluation Understudy*). BLEU menghitung sejauh mana kesamaan leksikal antara kalimat yang dihasilkan model (*candidate*) dengan kalimat acuan yang telah disusun sebelumnya (*reference*). Skor BLEU berada pada rentang 0 hingga 1, di mana nilai yang lebih tinggi menunjukkan tingkat kemiripan yang lebih besar.

Langkah pertama dalam menghitung BLEU adalah melakukan tokenisasi pada kedua kalimat, yaitu memecah kalimat menjadi kata-kata. Dari proses tokenisasi diperoleh panjang kalimat referensi sebanyak 30 token, sedangkan panjang kalimat *candidate* adalah 26 token.

Selanjutnya, dilakukan perhitungan BLEU-1, yaitu kesesuaian pada tingkat unigram. Dari total 26 token pada kalimat *candidate*, terdapat 18 token yang cocok dengan kalimat referensi, seperti kata Jawaban, kamu, Research, Question, dan Objective. Perhitungan token yang cocok dapat dilihat pada Tabel 3.13.

**Tabel 3.13. Perhitungan Token BLEU-1**

| Token | Kecocokan |
| --- | --- |
| Jawaban | Cocok |
| kamu | Cocok |
| kurang | Tidak Cocok |
| tepat | Tidak Cocok |
| Penjelasan | Cocok |
| tentang | Tidak Cocok |
| Research | Cocok |
| Question | Cocok |
| (Rumusan | Cocok |
| Masalah) | Cocok |
| dan | Cocok |
| Research | Cocok |
| Objective | Cocok |
| (Tujuan | Cocok |
| Masalah) | Cocok |
| tidak | Tidak Cocok |
| benar | Tidak Cocok |
| serta | Tidak Cocok |
| hubungan | Cocok |
| antara | Tidak Cocok |
| Research | Cocok |
| Question | Cocok |
| dan | Cocok |
| Research | Cocok |
| Objective | Cocok |
| juga | Tidak Cocok |
| keliru | Tidak Cocok |

Sehingga *precision* BLEU-1 dihitung sebagai berikut:

\[
P_1=\frac{\text{Unigram cocok}}{\text{Panjang candidate}}=\frac{18}{26}\approx0.692
\]

Selain unigram, dihitung pula BLEU-2, yang memperhitungkan kesamaan urutan dua kata (*bigram*). Dari perhitungan, ditemukan 8 bigram yang cocok, seperti Jawaban kamu, Research Question, dan dan Research. Perhitungan bigram yang cocok dapat dilihat pada Tabel 3.14.

**Tabel 3.14. Perhitungan Bigram yang Cocok**

| Bigram |
| --- |
| Jawaban kamu |
| Research Question |
| Question (Rumusan |
| (Rumusan Masalah) |
| Research Objective |
| (Tujuan Masalah) |
| Research Question |
| dan Research |

Sehingga akan didapatkan nilai *precision* BLEU-2 adalah:

\[
P_2=\frac{\text{Bigram cocok}}{\text{Panjang candidate}}=\frac{8}{25}\approx0.32
\]

Karena panjang kalimat *candidate* lebih pendek daripada referensi, dikenakan *brevity penalty* (BP) untuk menghindari bias kalimat pendek. Nilai BP dihitung sebagai:

\[
BP=e^{(1-r/c)}=e^{(1-30/26)}\approx0.857
\]

Dengan demikian, skor BLEU-2 akhir dihitung menggunakan rata-rata log *precision* dari unigram dan bigram, kemudian dikalikan BP:

\[
\mathrm{BLEU}\text{-}2=BP\times\exp\left(\frac12\log P_1+\frac12\log P_2\right)
\]

\[
\mathrm{BLEU}\text{-}2=0.857\times\exp\left(\frac{-0.367+(-1.139)}{2}\right)\approx0.404
\]

Sehingga skor BLEU-2 untuk contoh kalimat ini adalah 0.404. Dari hasil perhitungan ini, dapat disimpulkan bahwa meskipun terdapat cukup banyak kata yang sama antara *feedback* model dengan *feedback* referensi, perbedaan urutan kata dan penggunaan kata yang berbeda membuat skor BLEU-2 menjadi tidak terlalu tinggi. Hal ini menunjukkan bahwa BLEU sensitif terhadap kesamaan urutan kata, bukan hanya kemiripan kata-kata secara individual. Oleh karena itu, untuk konteks evaluasi *feedback* dalam pendidikan, BLEU perlu dilengkapi dengan metrik lain yang mampu menangkap kesamaan makna secara lebih mendalam.

### 3.5.2. Perhitungan Metrik Evaluasi ROUGE-L

Penelitian ini menggunakan ROUGE-L (*Recall-Oriented Understudy for Gisting Evaluation – Longest Common Subsequence*) sebagai salah satu metrik evaluasi untuk menilai kesamaan antara *feedback* yang dihasilkan model (*candidate*) dan *feedback* referensi (*reference*). Berbeda dari BLEU yang mengandalkan kecocokan kata secara berurutan (n-gram), ROUGE-L mengukur *Longest Common Subsequence* (LCS), yaitu urutan kata terpanjang yang sama dalam kedua kalimat, meskipun tidak selalu muncul berdampingan.

Selanjutnya, dicari *Longest Common Subsequence* (LCS) antara kedua kalimat. Misalnya, dalam contoh ini, LCS yang ditemukan meliputi token yang dapat dilihat pada Tabel 3.15.

**Tabel 3.15. Perhitungan Token LCS**

| Token |
| --- |
| `["Jawaban", "kamu", "Research", "Question", "(Rumusan", "Masalah)", "dan", "Research", "Objective", "hubungan"]` |

Berdasarkan nilai LCS, dihitung dua komponen utama, yaitu *recall* dan *precision*:

\[
R_{\mathrm{LCS}}=\frac{\mathrm{LCS}(c,r)}{\mathrm{length}(r)}=\frac{10}{30}\approx0.333
\]

\[
P_{\mathrm{LCS}}=\frac{\mathrm{LCS}(c,r)}{\mathrm{length}(c)}=\frac{10}{26}\approx0.3846
\]

Dengan \(\beta=1\) (menyeimbangkan *recall* dan *precision*):

\[
\mathrm{ROUGE}\text{-}L=\frac{(1+\beta^2)\cdot R_{\mathrm{LCS}}\cdot P_{\mathrm{LCS}}}{R_{\mathrm{LCS}}+\beta^2\cdot P_{\mathrm{LCS}}}
\]

\[
\mathrm{ROUGE}\text{-}L=\frac{2\times0.3333\times0.3846}{0.3333+0.3846}=\frac{0.2564}{0.7179}\approx0.3573
\]

Sehingga, skor ROUGE-L untuk contoh kalimat ini adalah sekitar 0.3573. Hasil perhitungan ini menunjukkan bahwa meskipun ada kesamaan beberapa kata penting antara *feedback* model dengan *feedback* referensi, urutan kata yang tidak identik dan banyaknya kata yang berbeda menyebabkan skor ROUGE-L tidak terlalu tinggi. Hal ini menggambarkan kekuatan ROUGE-L dalam mengukur kesamaan urutan kata dalam konteks teks panjang, meskipun bersifat lebih fleksibel dibanding BLEU karena tidak memerlukan kata muncul berurutan.

### 3.5.3. Perhitungan Metrik Evaluasi METEOR

Penelitian ini menggunakan METEOR (*Metric for Evaluation of Translation with Explicit ORdering*) sebagai salah satu metrik evaluasi untuk mengukur kesamaan antara *feedback* yang dihasilkan model (*candidate*) dan *feedback* referensi (*reference*). Berbeda dari BLEU yang hanya mengandalkan kesamaan leksikal, METEOR memperhitungkan sinonim, *stemming*, dan penalti urutan kata, sehingga lebih sensitif dalam menangkap kesamaan makna.

Langkah pertama dalam perhitungan METEOR adalah melakukan tokenisasi pada kedua kalimat. Kalimat referensi memiliki panjang 30 token, sedangkan kalimat *candidate* memiliki panjang 26 token.

Setelah tokenisasi, dicari jumlah *unigram match*, yaitu kata-kata yang sama persis antara *candidate* dan *reference*. Berdasarkan pengecekan kata per kata, terdapat 18 token yang cocok, antara lain kata Jawaban, kamu, Penjelasan, Research, Question, Objective, dan, hubungan, serta beberapa kemunculan ulang kata yang sama di kalimat.

Dari hasil *unigram match* tersebut, dihitung nilai *precision* (P) sebagai berikut:

\[
P=\frac{\text{Unigram cocok}}{\text{Panjang candidate}}=\frac{18}{26}\approx0.692
\]

Sedangkan nilai *recall* (R) dihitung sebagai:

\[
R=\frac{\text{Unigram cocok}}{\text{Panjang reference}}=\frac{18}{30}\approx0.6
\]

Kedua nilai ini kemudian digabungkan melalui *harmonic mean* (Fmean) dengan formula METEOR, di mana *recall* diberikan bobot lebih tinggi (sembilan kali) dibanding *precision*.

\[
F_{\mathrm{mean}}=\frac{10\cdot\mathrm{Precision}\cdot\mathrm{Recall}}{\mathrm{Recall}+9\mathrm{Precision}}=\frac{10\times0.692\times0.6}{0.6+(9\times0.692)}\approx0.608
\]

Selanjutnya, METEOR menghitung *penalty* yang memperhitungkan jumlah *chunk*, yaitu kelompok kata cocok yang muncul tidak berdampingan secara berurutan. Pada contoh ini diasumsikan terdapat 4 *chunk* terpisah. Nilai *penalty* dihitung sebagai berikut:

\[
\mathrm{Penalty}=\gamma\left(\frac{ch}{m}\right)^\theta=0.5\times\left(\frac4{18}\right)^3=0.5\times0.0137\approx0.0068
\]

Akhirnya, skor METEOR dihitung dengan mengalikan Fmean dengan (1 − Penalty):

\[
\mathrm{METEOR}=F_{\mathrm{mean}}\times(1-\mathrm{Penalty})=0.6083\times0.9932\approx0.6043
\]

Sehingga skor METEOR untuk contoh kalimat ini adalah sekitar 0.6043. Hasil perhitungan ini menunjukkan bahwa METEOR memberikan nilai yang lebih tinggi dibanding ROUGE-L dan BLEU, karena mampu menangkap kemiripan makna meskipun terdapat variasi kata yang digunakan. Dalam konteks *feedback generation*, METEOR menjadi metrik yang relevan, sebab gaya bahasa antar dosen atau sistem bisa berbeda, tetapi tetap menyampaikan makna yang sama.

### 3.5.4. Perhitungan Metrik Evaluasi BERTScore

Penelitian ini juga menggunakan BERTScore sebagai salah satu metrik evaluasi untuk mengukur kesamaan antara *feedback* yang dihasilkan model (*candidate*) dan *feedback* referensi (*reference*). BERTScore merupakan metrik berbasis pembelajaran mendalam yang menghitung kesamaan makna antar kalimat dengan memanfaatkan *embedding* vektor dari model bahasa *pre-trained* seperti BERT.

Berbeda dari metrik tradisional yang mengandalkan kesamaan kata secara leksikal, BERTScore mampu mengukur kesamaan semantik antara kalimat meskipun kata-kata yang digunakan berbeda. Metrik ini sangat relevan dalam konteks *feedback generation*, karena memungkinkan sistem mendeteksi bahwa kalimat berbeda kata bisa memiliki makna yang sama.

Langkah pertama dalam perhitungan BERTScore adalah memecah kalimat menjadi token, kemudian menghitung *embedding* vektor setiap token menggunakan model BERT. Misalnya token “Jawaban” dan “kamu” akan diwakili oleh vektor berdimensi 768 (untuk BERT-base) yang menggambarkan makna kata dalam konteks kalimat.

Setelah semua token direpresentasikan sebagai vektor, dilakukan perhitungan *cosine similarity* antara setiap token pada kalimat *candidate* dengan token pada kalimat *reference*. Setiap token *candidate* akan dicocokkan ke token *reference* yang memiliki *cosine similarity* tertinggi.

Misalnya, meskipun kata salah di kalimat referensi berbeda dari kata tidak benar pada *candidate*, BERTScore bisa mendeteksi bahwa kedua kata tersebut memiliki vektor *embedding* yang sangat mirip dalam ruang semantik, sehingga tetap dihitung sebagai kecocokan.

Perhitungan BERTScore menghasilkan tiga nilai utama:

1. Precision (P): rata-rata *cosine similarity* token *candidate* terhadap *reference*.
2. Recall (R): rata-rata *cosine similarity* token *reference* terhadap *candidate*.
3. F1 Score (F1): *harmonic mean* dari *precision* dan *recall*.

Berdasarkan perhitungan menggunakan *library* Python BERTscore, diperoleh nilai estimasi berikut:

\[
P_{\mathrm{BERT}}=\frac1{|X|}\sum_{x\in X}\max_{y\in Y}\cos(E(x),E(y))
\]

\[
R_{\mathrm{BERT}}=\frac1{|Y|}\sum_{y\in Y}\max_{x\in X}\cos(E(y),E(x))
\]

\[
F_{\mathrm{BERT}}=2\times\frac{P_{\mathrm{BERT}}\times R_{\mathrm{BERT}}}{P_{\mathrm{BERT}}+R_{\mathrm{BERT}}}
\]

\[
P\approx0.812,\qquad R\approx0.785,\qquad F1\approx0.798
\]

Sehingga, nilai BERTScore-F1 untuk contoh kalimat ini adalah sekitar 0.798. Hasil perhitungan ini menunjukkan bahwa BERTScore memberikan nilai yang jauh lebih tinggi dibanding BLEU, ROUGE-L, maupun METEOR. Hal ini terjadi karena BERTScore menangkap makna, bukan hanya kesamaan kata literal. Dalam konteks *feedback generation*, hal ini sangat penting karena model dapat menghasilkan kalimat yang berbeda susunan atau kata, tetapi maknanya tetap relevan dengan *feedback* referensi.

# BAB IV — HASIL DAN PEMBAHASAN

Bab ini menyajikan hasil eksperimen dan analisis terhadap *feedback* yang dihasilkan oleh model LLM berdasarkan kombinasi strategi *prompting*, persona, dan model yang digunakan. Pembahasan diawali dengan penjelasan data penelitian, termasuk jumlah, distribusi, dan struktur kombinasi eksperimen. Selanjutnya, hasil evaluasi disajikan berdasarkan empat metrik utama: BLEU, ROUGE-L, METEOR, dan BERTScore. Analisis dilakukan untuk mengidentifikasi efektivitas masing-masing strategi dan model, yaitu GPT-4o mini dan LLaMA 3.1. Selain itu, disertakan pula analisis berdasarkan mata kuliah serta visualisasi hasil dalam bentuk grafik dan diagram. Bab ini ditutup dengan pembahasan temuan utama dan interpretasi terhadap hasil yang diperoleh.

## 4.1. Lingkungan Proses Generating dan Evaluasi

Penelitian ini dilakukan menggunakan Google Colab dengan bahasa pemrograman Python dengan spesifikasi sebagai berikut:

1. CPU: Intel(R) Xeon(R) CPU @ 2.20GHz
2. RAM: 83.5 GB
3. GPU: NVIDIA A100
4. GPU RAM: 40.0 GB
5. DISK: 235.7 GB

## 4.2. Data Penelitian

Data yang digunakan dalam penelitian ini terdiri atas jawaban mahasiswa dari dua mata kuliah, yaitu Sistem Cerdas dan Metodologi Penelitian dan Penulisan Ilmiah (MPI). Jumlah total jawaban yang dianalisis adalah sebanyak 153 entri, yang terdiri dari 62 jawaban untuk mata kuliah Sistem Cerdas dan 91 jawaban untuk mata kuliah MPI. Setiap jawaban dijadikan objek evaluasi untuk menghasilkan *feedback* oleh model LLM, sehingga menjadi dasar dari seluruh proses eksperimen yang dilakukan.

Untuk setiap jawaban mahasiswa, diterapkan kombinasi dari empat strategi *prompting* (Zero-Shot, One-Shot, Few-Shot, dan Chain-of-Thought), tiga jenis persona (Base, Dosen, dan Ahli), dan dua model LLM (GPT-4o mini dan LLaMA 3.1). Gabungan dari ketiga dimensi ini menghasilkan total 42 kombinasi eksperimen unik. Dengan demikian, setiap jawaban mahasiswa diproses sebanyak 42 kali oleh model yang berbeda dalam konfigurasi strategi dan persona, menghasilkan total 6.426 *feedback* (153 jawaban × 42 kombinasi).

Khusus untuk strategi One-Shot, digunakan dua pendekatan sumber contoh *feedback*, yaitu One-Shot Asli dan One-Shot Template. Pada One-Shot Asli, *feedback* referensi yang sesuai dengan jawaban mahasiswa digunakan secara langsung sebagai contoh dalam *prompt*, menyesuaikan isi dan gaya dengan topik yang sama. Sedangkan pada One-Shot Template, contoh *feedback* yang digunakan berasal dari *template* tetap berdasarkan kategori nilai (rendah, sedang, tinggi) dan karakteristik tertentu. Kedua pendekatan ini memungkinkan peneliti untuk menguji apakah strategi One-Shot mempengaruhi hasil dari evaluasi rata-rata dari *output* yang dikeluarkan oleh model. Sehingga total kombinasi dari strategi One-Shot terdapat 4 kombinasi.

Setiap entri *feedback* disimpan dalam format terstruktur yang memuat informasi strategi *prompting*, jenis persona, nama model, pertanyaan, jawaban mahasiswa, *prompt* yang digunakan, hasil *feedback*, serta skor dari masing-masing metrik evaluasi (BLEU, ROUGE-L, METEOR, dan BERTScore). Distribusi data ini memungkinkan analisis performa model secara rinci berdasarkan dimensi strategi, persona, jenis model, serta konteks mata kuliah. Distribusi jumlah jawaban per mata kuliah dan total kombinasi eksperimen dapat dilihat pada Tabel 4.1.

**Tabel 4.1. Distribusi Jumlah Jawaban per Mata Kuliah dan Total Kombinasi Eksperimen**

| Mata Kuliah | Jumlah Jawaban | Total Kombinasi per Jawaban | Total Feedback |
| --- | ---: | ---: | ---: |
| Sistem Cerdas | 62 | 42 | 2.604 |
| Metodologi Penelitian dan Penulisan Ilmiah | 91 | 42 | 3.822 |
| **Total** | **153** | **42** | **6.426** |

## 4.3. Analisis Hasil pada Mata Kuliah Sistem Cerdas

### 4.3.1. Berdasarkan Strategi Prompting

Evaluasi performa strategi *prompting* dalam menghasilkan *feedback* pada mata kuliah Sistem Cerdas dilakukan menggunakan empat metrik otomatis yaitu BLEU, ROUGE-L, METEOR, dan BERTScore_F1. Hasil analisis ditampilkan melalui visualisasi *box-plot* dan rekapitulasi rata-rata skor per strategi.

**Gambar 4.1. Persebaran Nilai BLEU Berdasarkan Strategi Prompting pada Mata Kuliah Sistem Cerdas**

Berdasarkan Gambar 4.1, strategi One-Shot memiliki persebaran nilai BLEU tertinggi dibandingkan strategi lainnya. Nilai median lebih tinggi dari strategi lainnya dan terdapat sejumlah *outlier* yang mencapai lebih dari 0.45, menunjukkan bahwa dalam beberapa kasus, model mampu menghasilkan *feedback* yang sangat mirip secara leksikal dengan *feedback* referensi. Few-Shot juga menunjukkan performa cukup baik dengan persebaran yang cukup lebar, namun sedikit lebih rendah dari One-Shot. Sementara itu, strategi Zero-Shot dan Chain-of-Thought menghasilkan skor BLEU yang sangat rendah, dengan median mendekati nol dan distribusi yang sempit.

**Gambar 4.2. Persebaran Nilai ROUGE-L Berdasarkan Strategi Prompting pada Mata Kuliah Sistem Cerdas**

Berdasarkan Gambar 4.2, strategi Few-Shot dan One-Shot kembali unggul dari segi ROUGE-L, dengan median yang cukup tinggi dan sebaran distribusi yang lebar. Hal ini menunjukkan bahwa *feedback* yang dihasilkan memiliki kemiripan urutan kata dengan *feedback* referensi. Zero-Shot dan CoT memiliki nilai ROUGE-L yang rendah dengan median di bawah 0.1, mengindikasikan bahwa model kurang berhasil mereproduksi struktur kalimat atau subsekuensi penting dalam referensi saat tidak diberikan contoh eksplisit.

**Gambar 4.3. Persebaran Nilai METEOR Berdasarkan Strategi Prompting pada Mata Kuliah Sistem Cerdas**

Berdasarkan Gambar 4.3, strategi Few-Shot dan One-Shot kembali mendominasi dengan nilai METEOR yang cukup tinggi. METEOR yang mengukur kesamaan dengan mempertimbangkan sinonim dan struktur kalimat menunjukkan bahwa strategi berbasis contoh memungkinkan model menghasilkan *feedback* yang fleksibel namun tetap relevan. Strategi Zero-Shot dan CoT kembali menunjukkan performa rendah dengan median yang jauh tertinggal.

**Gambar 4.4. Persebaran Nilai BERTScore-F1 Berdasarkan Strategi Prompting pada Mata Kuliah Sistem Cerdas**

Berdasarkan Gambar 4.4, strategi Few-Shot dan One-Shot memiliki skor BERTScore_F1 yang tinggi, dengan median mendekati 0.6–0.65 dan banyak *outlier* di atas 0.7. Hal ini menunjukkan bahwa model berhasil menghasilkan *feedback* yang memiliki kemiripan semantik tinggi dengan referensi. Zero-Shot dan CoT memiliki skor median yang lebih rendah, dengan distribusi sempit dan nilai minimum yang lebih rendah dari strategi berbasis contoh.

**Tabel 4.2. Rata-Rata Skor Evaluasi Setiap Strategi pada Mata Kuliah Sistem Cerdas**

| Strategi | BLEU | ROUGE-L | METEOR | BERTScore-F1 |
| --- | ---: | ---: | ---: | ---: |
| Zero-Shot | 0.0065 | 0.0933 | 0.1585 | 0.5385 |
| One-Shot | 0.0205 | 0.1510 | 0.2276 | 0.5939 |
| Few-Shot | 0.0194 | 0.1648 | 0.2446 | 0.5989 |
| Chain-of-Thought | 0.0053 | 0.0771 | 0.1391 | 0.5136 |

Berdasarkan tabel di atas, strategi berbasis contoh, terutama Few-Shot dan One-Shot, menunjukkan efektivitas dalam meniru struktur kalimat referensi. Sebaliknya, Zero-Shot dan CoT menghasilkan *feedback* yang kurang serupa, baik secara leksikal maupun semantik dibanding dua strategi lain.

### 4.3.2. Berdasarkan Strategi Persona

Evaluasi terhadap pengaruh penggunaan persona dalam *prompt* dilakukan dengan membandingkan tiga jenis persona: Base (tanpa persona), Dosen, dan Ahli. Analisis ini menggunakan empat metrik otomatis—BLEU, ROUGE-L, METEOR, dan BERTScore_F1—dengan visualisasi berupa *box-plot* serta rekapitulasi skor rata-rata.

**Gambar 4.5. Persebaran Nilai BLEU Berdasarkan Persona pada Mata Kuliah Sistem Cerdas**

Gambar 4.5 menunjukkan bahwa persona Base menghasilkan skor BLEU tertinggi, dengan median yang lebih tinggi dari persona Dosen maupun Ahli. Hal ini menunjukkan bahwa ketika model tidak diarahkan pada gaya atau sudut pandang tertentu, respons yang dihasilkan cenderung lebih dekat secara leksikal dengan referensi. Persona Dosen dan Ahli menghasilkan skor BLEU yang lebih rendah dengan persebaran yang lebih sempit.

**Gambar 4.6. Persebaran Nilai ROUGE-L Berdasarkan Persona pada Mata Kuliah Sistem Cerdas**

Gambar 4.6 memperlihatkan bahwa persona Base kembali mencatat skor ROUGE-L tertinggi, dengan distribusi yang lebar dan median yang lebih tinggi. Persona Dosen dan Ahli memiliki distribusi yang lebih terbatas, dengan median lebih rendah. Hal ini menunjukkan bahwa persona Base cenderung memberikan *output* yang memiliki struktur kalimat lebih mirip dengan referensi, meskipun tanpa sudut pandang pedagogis atau keilmuan yang eksplisit.

**Gambar 4.7. Persebaran Nilai METEOR Berdasarkan Persona pada Mata Kuliah Sistem Cerdas**

Pada Gambar 4.7, skor METEOR menunjukkan pola yang serupa. Persona Base tetap unggul, dengan nilai median yang lebih tinggi dibanding persona lainnya. Hal ini mengindikasikan bahwa persona netral memungkinkan model meniru bentuk dan variasi sinonim yang lebih dekat dengan referensi, sementara persona Dosen dan Ahli sedikit membatasi fleksibilitas gaya bahasa karena gaya komunikasinya lebih formal dan struktural.

**Gambar 4.8. Persebaran Nilai BERTScore-F1 Berdasarkan Strategi Prompting pada Mata Kuliah Sistem Cerdas**

Gambar 4.8 menunjukkan perbandingan dari sisi semantik. Persona Base memiliki median BERTScore_F1 tertinggi, diikuti oleh Dosen dan Ahli. Meskipun perbedaan tidak terlalu ekstrem, hal ini menunjukkan bahwa persona netral menghasilkan *feedback* yang secara semantik paling mendekati referensi. Performa persona Ahli cenderung paling rendah, kemungkinan karena respons yang lebih evaluatif dan abstrak, sehingga cenderung menyimpang dari gaya penulisan referensi dosen yang lebih komunikatif.

**Tabel 4.3. Rata-Rata Skor Evaluasi Setiap Persona pada Mata Kuliah Sistem Cerdas**

| Persona | BLEU | ROUGE-L | METEOR | BERTScore-F1 |
| --- | ---: | ---: | ---: | ---: |
| Base | 0.0239 | 0.1696 | 0.2304 | 0.6000 |
| Dosen | 0.0130 | 0.1240 | 0.2035 | 0.5690 |
| Ahli | 0.0116 | 0.1090 | 0.1886 | 0.5567 |

Berdasarkan Tabel 4.3 dapat disimpulkan bahwa persona Base menghasilkan performa terbaik secara konsisten pada keempat metrik evaluasi. Persona Dosen dan Ahli cenderung memiliki skor yang lebih rendah, yang mengindikasikan bahwa penambahan persona secara eksplisit belum tentu meningkatkan kesesuaian dengan referensi yang bersifat komunikatif dan langsung.

### 4.3.3. Berdasarkan Strategi Model

Evaluasi terhadap model LLM dilakukan dengan membandingkan skor GPT dan LLaMA menggunakan empat metrik evaluasi otomatis: BLEU, ROUGE-L, METEOR, dan BERTScore_F1. Visualisasi hasil ditunjukkan dalam bentuk *box-plot* serta didukung dengan tabel rata-rata skor masing-masing metrik.

**Gambar 4.9. Persebaran Nilai BLEU Berdasarkan Model pada Mata Kuliah Sistem Cerdas**

Gambar 4.9 memperlihatkan bahwa LLaMA menghasilkan skor BLEU yang lebih tinggi dibandingkan GPT, baik dari segi median maupun sebaran. Model LLaMA juga menunjukkan lebih banyak *outlier* dengan nilai BLEU tinggi (>0.1), menunjukkan bahwa dalam beberapa kasus, LLaMA menghasilkan *feedback* yang secara leksikal lebih dekat dengan referensi. GPT memiliki distribusi yang lebih sempit dan median yang lebih rendah.

**Gambar 4.10. Persebaran Nilai ROUGE-L Berdasarkan Model pada Mata Kuliah Sistem Cerdas**

Pada Gambar 4.10, skor ROUGE-L menunjukkan hasil yang cukup berimbang antara kedua model. GPT sedikit unggul dari LLaMA dalam hal median, namun perbedaan yang ditunjukkan tidak terlalu signifikan. Ini menunjukkan bahwa kedua model memiliki kemampuan yang hampir setara dalam menghasilkan urutan kata yang menyerupai referensi, meskipun gaya dan susunannya bisa berbeda.

**Gambar 4.11. Persebaran Nilai METEOR Berdasarkan Model pada Mata Kuliah Sistem Cerdas**

Gambar 4.11 menunjukkan bahwa LLaMA mencatat skor METEOR yang lebih tinggi dibandingkan GPT. METEOR sebagai metrik yang mempertimbangkan sinonim dan *stemming* memberikan indikasi bahwa *feedback* dari LLaMA cenderung lebih fleksibel dan kaya dalam struktur bahasa. Hal ini menguntungkan terutama dalam konteks tugas akademik terbuka yang memungkinkan variasi ekspresi yang luas.

**Gambar 4.12. Persebaran Nilai BERTScore-F1 Berdasarkan Model pada Mata Kuliah Sistem Cerdas**

Berdasarkan Gambar 4.12, GPT memiliki median BERTScore_F1 yang lebih tinggi dibandingkan LLaMA. Metrik ini mengukur kemiripan semantik antar kalimat, dan hasil ini mengindikasikan bahwa meskipun secara leksikal dan struktur LLaMA unggul, GPT lebih baik dalam menangkap makna atau substansi dari *feedback* referensi.

**Tabel 4.4. Rata-Rata Skor Evaluasi Setiap Model pada Mata Kuliah Sistem Cerdas**

| Model | BLEU | ROUGE-L | METEOR | BERTScore-F1 |
| --- | ---: | ---: | ---: | ---: |
| GPT | 0.0125 | 0.1372 | 0.1994 | 0.5811 |
| LLaMA | 0.0199 | 0.1312 | 0.2156 | 0.5694 |

Hasil pada tabel menunjukkan bahwa LLaMA unggul pada BLEU dan METEOR, menandakan kekuatan dalam struktur dan fleksibilitas bahasa. Sebaliknya, GPT unggul dalam ROUGE-L dan BERTScore_F1, yang menandakan kemampuannya dalam menghasilkan *feedback* yang relevan secara semantik dan cenderung lebih komunikatif.

Secara keseluruhan, tidak ada model yang secara absolut lebih baik dalam semua aspek. LLaMA lebih baik dari sisi kemiripan struktur dan variasi kata, sementara GPT menunjukkan keunggulan dari sisi makna dan koherensi semantik. Pemilihan model ideal dapat disesuaikan dengan tujuan utama sistem. Jika fokus pada kesamaan makna, GPT lebih direkomendasikan. Namun, jika ingin menghasilkan *feedback* yang lebih eksplisit dan dekat dengan struktur referensi, LLaMA bisa menjadi pilihan.

### 4.3.4. Berdasarkan Kombinasi Strategi, Persona, dan Model

Analisis kombinasi dilakukan untuk mengevaluasi performa setiap model LLM (GPT dan LLaMA) pada seluruh kombinasi strategi *prompting* (Zero-Shot, One-Shot, Few-Shot, CoT) dan persona (Base, Dosen, Ahli). Tujuan dari analisis ini adalah untuk mengidentifikasi konfigurasi paling optimal dalam menghasilkan *feedback* yang mendekati referensi, berdasarkan keempat metrik evaluasi: BLEU, ROUGE-L, METEOR, dan BERTScore_F1.

**Gambar 4.13. Persebaran Nilai BLEU Berdasarkan Kombinasi Strategi, Persona, dan Model pada Mata Kuliah Sistem Cerdas**

Gambar 4.13 menunjukkan bahwa kombinasi dengan menggunakan model LLaMA, strategi One-Shot, dan persona Base menghasilkan skor BLEU tertinggi di antara kombinasi lainnya, dengan banyak *outlier* yang mencapai nilai di atas 0.4. Hal ini mengindikasikan bahwa menggunakan satu contoh dan persona netral sangat efektif dalam menghasilkan *feedback* yang secara leksikal sangat mirip dengan referensi. Kombinasi dengan model LLaMA, strategi Few-Shot, dan persona Base serta dengan model GPT, strategi Few-Shot, dan persona Base juga menempati posisi atas, sementara konfigurasi berbasis CoT atau persona Ahli menghasilkan skor BLEU yang cenderung rendah.

**Gambar 4.14. Persebaran Nilai ROUGE-L Berdasarkan Kombinasi Strategi, Persona, dan Model pada Mata Kuliah Sistem Cerdas**

Berdasarkan Gambar 4.14, kombinasi dengan strategi Few-Shot dan One-Shot masih mendominasi skor ROUGE-L tertinggi. Secara khusus, model GPT, strategi Few-Shot, persona Base serta model LLaMA, strategi One-Shot, dan persona Base menunjukkan konsistensi tinggi dalam menyusun urutan kata yang serupa dengan referensi. Konfigurasi dengan strategi Zero-Shot atau CoT, terutama saat dikombinasikan dengan persona Ahli, menunjukkan hasil yang lebih lemah dari sisi kesamaan struktur kalimat.

**Gambar 4.15. Persebaran Nilai METEOR Berdasarkan Kombinasi Strategi, Persona, dan Model pada Mata Kuliah Sistem Cerdas**

Gambar 4.15 menunjukkan bahwa model LLaMA, strategi Few-Shot, dan persona Base memiliki skor METEOR tertinggi, disusul oleh model LLaMA, strategi One-Shot, persona Base serta model GPT, strategi Few-Shot, dan persona Base. METEOR yang memperhitungkan sinonim dan kemiripan bentuk kata menunjukkan bahwa kombinasi berbasis contoh (khususnya dengan persona Base) membantu model menghasilkan *feedback* yang kaya dan fleksibel dalam gaya bahasa. Di sisi lain, kombinasi berbasis CoT dan persona Ahli kembali berada di posisi bawah.

**Gambar 4.16. Persebaran Nilai BertScore-F1 Berdasarkan Kombinasi Strategi, Persona, dan Model pada Mata Kuliah Sistem Cerdas**

Pada Gambar 4.16, terlihat bahwa kombinasi model GPT, strategi Few-Shot, persona Base menghasilkan skor BERTScore-F1 tertinggi, menandakan bahwa *feedback* yang dihasilkan secara semantik paling mendekati makna *feedback* referensi. Disusul oleh model, strategi One-Shot, dan persona Base serta model LLaMA, strategi One-Shot, persona Base, tren ini memperkuat temuan bahwa strategi berbasis contoh dengan persona netral merupakan kombinasi terbaik dalam menghasilkan *feedback* akademik yang relevan.

**Tabel 4.5. Rata-Rata Skor Evaluasi Setiap Kombinasi Model, Strategi, dan Persona pada Mata Kuliah Sistem Cerdas**

| No | Strategi | Persona | Model | BLEU | ROUGE-L | METEOR | BERTScore-F1 |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: |
| 1 | zero-shot | base | GPT | 0.0079 | 0.1109 | 0.1771 | 0.5606 |
| 2 | zero-shot | base | LLaMA | 0.0078 | 0.1107 | 0.1752 | 0.5511 |
| 3 | zero-shot | dosen | GPT | 0.0057 | 0.0814 | 0.1522 | 0.5297 |
| 4 | zero-shot | dosen | LLaMA | 0.0067 | 0.0937 | 0.1597 | 0.5397 |
| 5 | zero-shot | ahli | GPT | 0.0045 | 0.0754 | 0.1285 | 0.5215 |
| 6 | zero-shot | ahli | LLaMA | 0.0066 | 0.0879 | 0.1580 | 0.5282 |
| 7 | one-shot | base | GPT | 0.0226 | 0.2080 | 0.2362 | 0.6412 |
| 8 | one-shot | base | LLaMA | 0.0414 | 0.1857 | 0.2744 | 0.6073 |
| 9 | one-shot | dosen | GPT | 0.0122 | 0.1416 | 0.2207 | 0.5932 |
| 10 | one-shot | dosen | LLaMA | 0.0186 | 0.1315 | 0.2218 | 0.5780 |
| 11 | one-shot | ahli | GPT | 0.0101 | 0.1201 | 0.2052 | 0.5719 |
| 12 | one-shot | ahli | LLaMA | 0.0182 | 0.1193 | 0.2071 | 0.5720 |
| 13 | few-shot | base | GPT | 0.0244 | 0.2214 | 0.2565 | 0.6534 |
| 14 | few-shot | base | LLaMA | 0.0270 | 0.1834 | 0.2809 | 0.5998 |
| 15 | few-shot | dosen | GPT | 0.0163 | 0.1700 | 0.2385 | 0.6108 |
| 16 | few-shot | dosen | LLaMA | 0.0203 | 0.1503 | 0.2489 | 0.5781 |
| 17 | few-shot | ahli | GPT | 0.0105 | 0.1263 | 0.2061 | 0.5751 |
| 18 | few-shot | ahli | LLaMA | 0.0180 | 0.1375 | 0.2368 | 0.5764 |
| 19 | cot | base | GPT | 0.0054 | 0.0825 | 0.1374 | 0.5159 |
| 20 | cot | base | LLaMA | 0.0067 | 0.0904 | 0.1558 | 0.5258 |
| 21 | cot | dosen | GPT | 0.0044 | 0.0691 | 0.1267 | 0.5078 |
| 22 | cot | dosen | LLaMA | 0.0058 | 0.0791 | 0.1527 | 0.5156 |
| 23 | cot | ahli | GPT | 0.0039 | 0.0651 | 0.1159 | 0.5038 |
| 24 | cot | ahli | LLaMA | 0.0054 | 0.0763 | 0.1463 | 0.5130 |

Berdasarkan Tabel 4.5 strategi berbasis contoh (One-Shot & Few-Shot) menghasilkan *feedback* yang paling mirip dengan referensi. Persona Base (tanpa peran eksplisit) justru menghasilkan kualitas *feedback* terbaik, kemungkinan karena tidak membatasi gaya atau sudut pandang model. Model LLaMA unggul dalam struktur dan fleksibilitas bahasa (BLEU & METEOR), sedangkan GPT lebih kuat secara semantik (BERTScore_F1). Kombinasi dengan menggunakan model GPT, strategi Few-Shot, dan persona Base merupakan yang paling optimal secara keseluruhan, terutama dalam menghasilkan *feedback* yang semantik, informatif, dan mendekati referensi dosen.

## 4.4. Analisis Hasil pada Mata Kuliah Metodologi Penelitian dan Penulisan Ilmiah

### 4.4.1. Berdasarkan Strategi Prompting

Evaluasi performa strategi *prompting* terhadap kualitas *feedback* pada mata kuliah Metodologi Penelitian dan Penulisan Ilmiah dilakukan menggunakan empat metrik: BLEU, ROUGE-L, METEOR, dan BERTScore-F1. Hasilnya divisualisasikan melalui *box-plot* dan diperkuat dengan tabel skor rata-rata per strategi.

**Gambar 4.17. Persebaran Nilai BLEU Berdasarkan Strategi Prompting pada Mata Kuliah Metodologi Penelitian dan Penulisan Ilmiah**

Gambar 4.17 menunjukkan bahwa strategi Few-Shot memiliki skor BLEU tertinggi dengan persebaran yang lebar dan *outlier* yang mencapai nilai di atas 0.4. Ini menandakan bahwa dengan memberikan beberapa contoh *feedback* sebelumnya, model mampu menghasilkan *feedback* yang sangat mirip secara leksikal dengan *feedback* referensi. Strategi One-Shot menyusul dengan performa yang juga baik, sedangkan Zero-Shot dan CoT memiliki distribusi rendah dan sempit.

**Gambar 4.18. Persebaran Nilai ROUGE-L Berdasarkan Strategi Prompting pada Mata Kuliah Metodologi Penelitian dan Penulisan Ilmiah**

Gambar 4.18 menunjukkan pola yang sama, di mana strategi Few-Shot dan One-Shot memiliki median ROUGE-L lebih tinggi dibanding strategi lainnya. Ini mengindikasikan kemampuan model dalam meniru struktur kalimat referensi lebih baik saat diberikan contoh. Zero-Shot dan CoT kembali menunjukkan keterbatasan karena tidak memiliki panduan eksplisit dalam *prompt*.

**Gambar 4.19. Persebaran Nilai METEOR Berdasarkan Strategi Prompting pada Mata Kuliah Metodologi Penelitian dan Penulisan Ilmiah**

Pada Gambar 4.19, METEOR kembali memperlihatkan dominasi strategi Few-Shot dan One-Shot. Dengan median dan distribusi nilai yang lebih tinggi, kedua strategi ini terbukti memungkinkan model menghasilkan *feedback* dengan variasi bahasa yang tetap bermakna dan relevan. Zero-Shot dan CoT menghasilkan skor METEOR yang lebih rendah, menunjukkan terbatasnya variasi ekspresif dalam *output* model.

**Gambar 4.20. Persebaran Nilai BERTScore-F1 Berdasarkan Strategi Prompting pada Mata Kuliah Metodologi Penelitian dan Penulisan Ilmiah**

Gambar 4.20 menunjukkan bahwa Few-Shot juga unggul secara semantik, disusul oleh One-Shot. Skor median dan sebaran nilai BERTScore_F1 dari strategi Few-Shot dan One-Shot lebih tinggi dibandingkan dua strategi lainnya. Ini mengindikasikan bahwa model tidak hanya meniru bentuk leksikal, tetapi juga memahami makna yang terkandung dalam *feedback* referensi saat diberi contoh.

**Tabel 4.6. Rata-Rata Skor Evaluasi Setiap Strategi pada Mata Kuliah Metodologi Penelitian dan Penulisan Ilmiah**

| Strategi | BLEU | ROUGE-L | METEOR | BERTScore-F1 |
| --- | ---: | ---: | ---: | ---: |
| Zero-Shot | 0.0055 | 0.1112 | 0.1678 | 0.5378 |
| One-Shot | 0.0256 | 0.1515 | 0.2395 | 0.5631 |
| Few-Shot | 0.0458 | 0.1699 | 0.2805 | 0.5746 |
| CoT | 0.0043 | 0.0926 | 0.1567 | 0.5232 |

Dari tabel di atas, dapat disimpulkan bahwa strategi Few-Shot menghasilkan performa tertinggi di semua metrik, menunjukkan bahwa memberikan beberapa contoh dalam *prompt* mampu meningkatkan pemahaman model dalam menyusun *feedback* yang relevan dan bernilai akademik. Strategi One-Shot juga menunjukkan performa yang kompetitif, terutama dalam BLEU dan METEOR. Sementara itu, Zero-Shot dan CoT secara konsisten berada di posisi bawah, baik dalam hal struktur maupun makna.

Strategi *prompting* berbasis contoh, khususnya Few-Shot terbukti paling efektif dalam konteks mata kuliah MPI. Hasil ini menunjukkan bahwa kemampuan model untuk memahami ekspektasi dan struktur *feedback* meningkat secara signifikan ketika diberikan panduan dalam bentuk contoh. Sebaliknya, strategi tanpa contoh (Zero-Shot dan CoT) kurang mampu menghasilkan *output* yang sejajar dengan referensi.

### 4.4.2. Berdasarkan Strategi Persona

Analisis ini mengevaluasi pengaruh persona dalam *prompt* terhadap kualitas *feedback* yang dihasilkan oleh model LLM. Tiga jenis persona dibandingkan: Base (tanpa persona), Dosen, dan Ahli, menggunakan empat metrik evaluasi: BLEU, ROUGE-L, METEOR, dan BERTScore-F1.

**Gambar 4.21. Persebaran Nilai BLEU Berdasarkan Persona pada Mata Kuliah Metodologi Penelitian dan Penulisan Ilmiah**

Gambar 4.21 menunjukkan bahwa persona Base mencatat skor BLEU tertinggi dibanding dua persona lainnya. Median distribusinya lebih tinggi dan memiliki *outlier* hingga di atas 0.4, menunjukkan bahwa tanpa persona eksplisit, model lebih mampu menghasilkan *feedback* yang strukturnya mendekati referensi. Persona Dosen dan Ahli cenderung menghasilkan skor BLEU yang lebih rendah dan sempit dalam variasi.

**Gambar 4.22. Persebaran Nilai ROUGE-L Berdasarkan Persona pada Mata Kuliah Metodologi Penelitian dan Penulisan Ilmiah**

Pada Gambar 4.22, kembali terlihat bahwa persona Base unggul dalam ROUGE-L. Hal ini mengindikasikan bahwa model yang diarahkan secara netral (tanpa persona) lebih konsisten dalam meniru struktur urutan kata atau subsekuensi dari *feedback* referensi. Persona Dosen dan Ahli menunjukkan median yang lebih rendah, yang menunjukkan bahwa penambahan gaya komunikatif akademik belum tentu memperbaiki struktur keluaran dari model.

**Gambar 4.23. Persebaran Nilai METEOR Berdasarkan Persona pada Mata Kuliah Metodologi Penelitian dan Penulisan Ilmiah**

Gambar 4.23 memperkuat temuan sebelumnya, dengan persona Base menghasilkan nilai METEOR tertinggi. METEOR yang mempertimbangkan variasi bentuk kata dan sinonim menunjukkan bahwa persona Base memberikan ruang lebih besar pada model untuk menyesuaikan gaya bahasa sesuai konteks, tanpa dibatasi oleh struktur peran tertentu. Persona Dosen dan Ahli menunjukkan nilai lebih rendah namun tetap stabil.

**Gambar 4.24. Persebaran Nilai BERTScore-F1 Berdasarkan Persona pada Mata Kuliah Metodologi Penelitian dan Penulisan Ilmiah**

Pada Gambar 4.24, persona Base kembali unggul dari sisi semantik, dengan median BERTScore_F1 lebih tinggi dibanding Dosen dan Ahli. Ini berarti *feedback* yang dihasilkan tanpa persona eksplisit lebih sejalan secara makna dengan *feedback* referensi. Persona Ahli menunjukkan skor paling rendah, kemungkinan karena fokus pada bahasa teknis dan evaluatif yang membuat *output* model lebih jauh dari gaya referensi dosen.

**Tabel 4.7. Rata-Rata Skor Evaluasi Setiap Persona pada Mata Kuliah Metodologi Penelitian dan Penulisan Ilmiah**

| Persona | BLEU | ROUGE-L | METEOR | BERTScore-F1 |
| --- | ---: | ---: | ---: | ---: |
| Base | 0.0333 | 0.1802 | 0.2520 | 0.5770 |
| Dosen | 0.0181 | 0.1275 | 0.2121 | 0.5511 |
| Ahli | 0.0163 | 0.1121 | 0.2057 | 0.5382 |

Berdasarkan Tabel 4.7 persona Base terbukti menghasilkan *feedback* dengan kualitas terbaik, baik dari segi leksikal maupun semantik. Hasil ini menunjukkan bahwa menambahkan persona seperti Dosen atau Ahli tidak selalu meningkatkan kualitas *feedback* secara signifikan. Sebaliknya, model tanpa persona eksplisit cenderung menghasilkan respons yang bersifat umum dan instruksional, sesuai gaya referensi yang digunakan.

### 4.4.3. Berdasarkan Strategi Model

Analisis ini mengevaluasi pengaruh model LLM terhadap kualitas *feedback* yang dihasilkan. Kedua model, LLaMA dan GPT, dibandingkan menggunakan empat metrik evaluasi: BLEU, ROUGE-L, METEOR, dan BERTScore_F1.

**Gambar 4.25. Persebaran Nilai BLEU Berdasarkan Model pada Mata Kuliah Metodologi Penelitian dan Penulisan Ilmiah**

Gambar 4.25 menunjukkan bahwa LLaMA mencatat skor BLEU yang lebih tinggi dibanding GPT, baik dari segi median maupun sebaran. LLaMA memiliki lebih banyak *outlier* di atas 0.1, dengan skor maksimum mendekati 0.45, yang menunjukkan bahwa dalam sejumlah kasus, *feedback* yang dihasilkan sangat mirip secara leksikal dengan *feedback* referensi. GPT memiliki distribusi yang lebih sempit dan nilai median yang lebih rendah.

**Gambar 4.26. Persebaran Nilai ROUGE-L Berdasarkan Model pada Mata Kuliah Metodologi Penelitian dan Penulisan Ilmiah**

Pada Gambar 4.26, nilai ROUGE-L dari LLaMA lebih tinggi, mengindikasikan kemampuannya dalam meniru urutan kata dari referensi.

**Gambar 4.27. Persebaran Nilai METEOR Berdasarkan Model pada Mata Kuliah Metodologi Penelitian dan Penulisan Ilmiah**

Pada Gambar 4.27, perbedaan performa semakin mencolok. LLaMA menunjukkan skor METEOR yang lebih tinggi dan lebih stabil. Karena METEOR mempertimbangkan sinonim dan variasi morfologi kata, ini menunjukkan bahwa LLaMA mampu menghasilkan *feedback* yang lebih fleksibel namun tetap relevan secara isi.

**Gambar 4.28. Persebaran Nilai BERTScore-F1 Berdasarkan Model pada Mata Kuliah Metodologi Penelitian dan Penulisan Ilmiah**

Gambar 4.28 menunjukkan bahwa LLaMA masih unggul dibanding GPT dari sisi semantik, walaupun selisih skor BERTScore-F1 tidak sebesar metrik lainnya. Median nilai LLaMA berada sedikit di atas GPT, dengan rentang distribusi yang lebih stabil.

**Tabel 4.8. Rata-Rata Skor Evaluasi Setiap Model pada Mata Kuliah Metodologi Penelitian dan Penulisan Ilmiah**

| Model | BLEU | ROUGE-L | METEOR | BERTScore-F1 |
| --- | ---: | ---: | ---: | ---: |
| LLaMA | 0.0297 | 0.1452 | 0.2395 | 0.5640 |
| GPT | 0.0154 | 0.1347 | 0.2070 | 0.5469 |

Secara keseluruhan, LLaMA unggul di keempat metrik evaluasi otomatis. Model ini menunjukkan kemampuan yang lebih tinggi dalam menghasilkan *feedback* yang dekat secara struktur dan makna dengan *feedback* referensi, baik dari segi kemiripan leksikal (BLEU, ROUGE-L), fleksibilitas ekspresi (METEOR), maupun relevansi semantik (BERTScore). Meskipun GPT masih menghasilkan *output* yang cukup stabil, hasil menunjukkan bahwa dalam konteks mata kuliah MPI, LLaMA lebih optimal untuk tugas *feedback generation*.

### 4.4.4. Berdasarkan Kombinasi Strategi, Persona dan Model

Analisis kombinasi dilakukan untuk mengevaluasi performa setiap model LLM (GPT dan LLaMA) pada seluruh kombinasi strategi *prompting* (Zero-Shot, One-Shot, Few-Shot, CoT) dan persona (Base, Dosen, Ahli). Tujuan dari analisis ini adalah untuk mengidentifikasi konfigurasi paling optimal dalam menghasilkan *feedback* yang mendekati referensi, berdasarkan keempat metrik evaluasi: BLEU, ROUGE-L, METEOR, dan BERTScore-F1.

**Gambar 4.29. Persebaran Nilai BLEU Berdasarkan Kombinasi Strategi, Persona, dan Model pada Mata Kuliah Metode Penelitian dan Penulisan Ilmiah**

Berdasarkan Gambar 4.29 dan tabel, kombinasi dengan menggunakan model GPT, strategi Few-Shot, dan persona Base mencatat skor BLEU tertinggi (0.0795), disusul oleh menggunakan model LLaMA, strategi One-Shot, dan Base (0.0572) serta model LLaMA, strategi Few-Shot, dan persona Base (0.0544). Ini menunjukkan bahwa strategi berbasis contoh, khususnya dengan persona Base, memberikan kontribusi terbesar dalam menghasilkan *feedback* yang leksikalnya sangat mirip dengan referensi. Kombinasi berbasis CoT dan Zero-Shot cenderung menghasilkan skor BLEU terendah.

**Gambar 4.30. Persebaran Nilai ROUGE-L Berdasarkan Kombinasi Strategi, Persona, dan Model pada Mata Kuliah Metode Penelitian dan Penulisan Ilmiah**

Gambar 4.30 menunjukkan bahwa kombinasi menggunakan model GPT, strategi Few-Shot, dan persona kembali mencatat nilai ROUGE-L tertinggi (0.2419), menunjukkan bahwa *feedback* model meniru struktur kalimat referensi secara konsisten. Model LLaMA, strategi One-Shot, dan persona Base serta model LLaMA, strategi Few-Shot, persona Base juga mencatat kombinasi yang memiliki nilai tinggi, menguatkan bahwa kombinasi model kuat dengan strategi berbasis contoh dan persona netral menghasilkan struktur *feedback* yang baik.

**Gambar 4.31. Persebaran Nilai METEOR Berdasarkan Kombinasi Strategi, Persona, dan Model pada Mata Kuliah Metode Penelitian dan Penulisan Ilmiah**

Gambar 4.31, kombinasi menggunakan model GPT, strategi Few-Shot, dan persona serta model LLaMA, strategi Few-Shot, persona Base unggul dengan nilai METEOR di atas 0.32, yang berarti *feedback* yang dihasilkan kaya secara leksikal dan fleksibel secara bentuk. CoT dan Zero-Shot kembali berada di posisi terbawah, terutama dengan persona Ahli.

**Gambar 4.32. Persebaran Nilai BERTSScore-F1 Berdasarkan Kombinasi Strategi, Persona, dan Model pada Mata Kuliah Metode Penelitian dan Penulisan Ilmiah**

Gambar 4.32 menunjukkan bahwa kombinasi menggunakan model GPT, strategi Few-Shot, dan persona mencatat nilai BERTScore-F1 tertinggi (0.6013), menandakan kemiripan semantik yang tinggi antara *feedback* model dan referensi. Kombinasi One-Shot dan Few-Shot lainnya (terutama dengan persona Base dan model LLaMA) juga mencatat skor semantik yang baik. Sementara itu, kombinasi CoT dan persona Ahli menghasilkan skor terendah dalam aspek ini.

**Tabel 4.9. Rata-Rata Skor Evaluasi Setiap Kombinasi Model, Strategi, dan Persona pada Mata Metodologi Penelitian dan Penulisan Ilmiah**

| No | Strategi | Persona | Model | BLEU | ROUGE-L | METEOR | BERTScore-F1 |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: |
| 1 | zero-shot | base | GPT | 0.0061 | 0.1332 | 0.1744 | 0.5553 |
| 2 | zero-shot | base | LLaMA | 0.0070 | 0.1314 | 0.1907 | 0.5504 |
| 3 | zero-shot | dosen | GPT | 0.0034 | 0.0963 | 0.1542 | 0.5259 |
| 4 | zero-shot | dosen | LLaMA | 0.0064 | 0.1115 | 0.1706 | 0.5398 |
| 5 | zero-shot | ahli | GPT | 0.0043 | 0.0965 | 0.1573 | 0.5233 |
| 6 | zero-shot | ahli | LLaMA | 0.0058 | 0.0985 | 0.1598 | 0.5323 |
| 7 | one-shot | base | GPT | 0.0199 | 0.2002 | 0.2484 | 0.5825 |
| 8 | one-shot | base | LLaMA | 0.0572 | 0.2030 | 0.2962 | 0.5967 |
| 9 | one-shot | dosen | GPT | 0.0099 | 0.1221 | 0.2003 | 0.5446 |
| 10 | one-shot | dosen | LLaMA | 0.0291 | 0.1479 | 0.2517 | 0.5699 |
| 11 | one-shot | ahli | GPT | 0.0090 | 0.1075 | 0.2005 | 0.5283 |
| 12 | one-shot | ahli | LLaMA | 0.0284 | 0.1281 | 0.2399 | 0.5568 |
| 13 | few-shot | base | GPT | 0.0795 | 0.2419 | 0.3239 | 0.6013 |
| 14 | few-shot | base | LLaMA | 0.0544 | 0.1961 | 0.3234 | 0.5953 |
| 15 | few-shot | dosen | GPT | 0.0365 | 0.1535 | 0.2458 | 0.5634 |
| 16 | few-shot | dosen | LLaMA | 0.0442 | 0.1675 | 0.2962 | 0.5847 |
| 17 | few-shot | ahli | GPT | 0.0281 | 0.1190 | 0.2326 | 0.5356 |
| 18 | few-shot | ahli | LLaMA | 0.0325 | 0.1416 | 0.2609 | 0.5670 |
| 19 | CoT | base | GPT | 0.0045 | 0.1015 | 0.1640 | 0.5257 |
| 20 | CoT | base | LLaMA | 0.0059 | 0.1058 | 0.1737 | 0.5326 |
| 21 | CoT | dosen | GPT | 0.0032 | 0.0847 | 0.1498 | 0.5176 |
| 22 | CoT | dosen | LLaMA | 0.0043 | 0.0913 | 0.1447 | 0.5264 |
| 23 | CoT | ahli | GPT | 0.0036 | 0.0831 | 0.1494 | 0.5143 |
| 24 | CoT | ahli | LLaMA | 0.0040 | 0.0893 | 0.1586 | 0.5224 |

Strategi Few-Shot dan One-Shot dengan persona Base secara konsisten menghasilkan performa tertinggi di seluruh metrik, baik leksikal maupun semantik. GPT unggul dalam aspek semantik dan struktur global (ROUGE, BERTScore), sedangkan LLaMA memberikan performa kuat dalam variasi kata dan kejelasan bentuk (BLEU, METEOR). Penggunaan persona Dosen dan Ahli cenderung menurunkan performa, terutama ketika dikombinasikan dengan strategi yang tidak berbasis contoh. Kombinasi menggunakan model GPT, strategi Few-Shot, dan persona menjadi konfigurasi paling optimal untuk menghasilkan *feedback* yang akurat, bernuansa, dan mendekati kualitas referensi dosen.

## 4.5. Interpretasi Hasil

Berdasarkan hasil evaluasi terhadap 6.426 entri *feedback* yang dihasilkan oleh dua model LLM (GPT-4o mini dan LLaMA 3.1) dengan kombinasi strategi *prompting* dan persona, dapat diambil beberapa temuan penting yang konsisten di kedua mata kuliah.

Pertama, strategi *prompting* yang berbasis contoh khususnya Few-Shot dan One-Shot secara konsisten menghasilkan *feedback* yang lebih berkualitas dibanding strategi Zero-Shot dan Chain-of-Thought. Ini tercermin dari skor BLEU, ROUGE-L, METEOR, dan BERTScore yang tinggi, baik dalam konteks leksikal maupun semantik. Few-Shot memiliki keunggulan karena menyediakan keragaman referensi yang memungkinkan model menggeneralisasi bentuk dan substansi *feedback* secara lebih baik, sementara One-Shot lebih ringkas namun tetap efektif.

Kedua, penggunaan persona Base (tanpa peran eksplisit) terbukti lebih efektif dibanding persona Dosen maupun Ahli. Tanpa persona, model memiliki fleksibilitas untuk menyesuaikan gaya dan struktur *feedback* dengan lebih baik. Persona yang bersifat instruktif (Dosen) atau teknis (Ahli) cenderung menghasilkan *output* yang terlalu kaku atau tidak selaras dengan gaya bahasa dalam referensi dosen.

Ketiga, dari sisi model, LLaMA 3.1 unggul dalam menghasilkan *feedback* yang lebih baik dari segi struktur dan fleksibilitas bahasa (BLEU dan METEOR), sedangkan GPT-4o mini lebih unggul dalam aspek semantik (BERTScore) dan struktur global kalimat (ROUGE-L). Dengan demikian, pemilihan model ideal dapat disesuaikan dengan tujuan evaluasi, apakah ingin mendekati struktur tekstual atau substansi makna.

Keempat, kombinasi terbaik secara keseluruhan pada kedua mata kuliah adalah menggunakan model GPT, strategi Few-Shot, dan persona, diikuti oleh dengan menggunakan model LLaMA, strategi One-Shot, dan persona Base serta model LLaMA, strategi Few-Shot, dan persona Base. Kombinasi tersebut secara konsisten menempati peringkat tertinggi dalam hampir semua metrik evaluasi. Ini menunjukkan bahwa pendekatan netral tanpa persona, dengan strategi berbasis contoh, memberikan hasil yang paling stabil dan akurat dalam konteks *feedback generation* akademik.

Terakhir, perbandingan hasil antara mata kuliah Sistem Cerdas dan MPI menunjukkan tren yang mirip, tetapi nilai metrik pada mata kuliah MPI cenderung lebih tinggi. Hal ini kemungkinan disebabkan oleh sifat jawaban MPI yang lebih terstruktur dan naratif, sehingga lebih mudah untuk dievaluasi oleh model LLM dibandingkan topik-topik teknis dalam Sistem Cerdas.

# BAB V — PENUTUP

Bab ini berisi rangkuman hasil penelitian yang telah dilakukan, termasuk kesimpulan utama yang diperoleh dari evaluasi kualitas *feedback* yang dihasilkan oleh model LLM berdasarkan strategi *prompting*, persona, dan model yang digunakan serta memberikan saran untuk pengembangan penelitian di masa mendatang agar lebih komprehensif dan aplikatif dalam konteks pendidikan tinggi.

## 5.1. Kesimpulan

Strategi *prompting* dan konfigurasi persona memiliki pengaruh signifikan terhadap kualitas *feedback* yang dihasilkan oleh model *Large Language Model* (LLM) terhadap jawaban mahasiswa. Strategi Few-Shot dan One-Shot terbukti paling efektif dalam menghasilkan *feedback* yang mendekati referensi, baik secara leksikal maupun semantik. Persona Base, yang tidak menyertakan peran khusus, memberikan hasil terbaik dibanding persona Dosen maupun Ahli, menunjukkan bahwa gaya netral lebih sesuai dengan pola umpan balik referensi dosen. Dari sisi performa model, LLaMA 3.1 unggul pada aspek struktural (BLEU dan METEOR), sedangkan GPT-4o mini lebih menonjol pada kesamaan makna (ROUGE-L dan BERTScore). Kombinasi menggunakan model GPT, strategi Few-Shot, dan persona secara konsisten menempati peringkat tertinggi dalam berbagai metrik, menjadikannya konfigurasi paling optimal untuk tugas *feedback generation* dalam konteks akademik. Hasil pada mata kuliah MPI menunjukkan skor evaluasi yang lebih tinggi dibanding Sistem Cerdas, yang kemungkinan besar dipengaruhi oleh bentuk jawaban yang lebih naratif dan terstruktur, serta lebih mudah diproses oleh model. Secara keseluruhan, pendekatan *prompt engineering* berbasis konteks menunjukkan efektivitas dalam memaksimalkan kinerja LLM untuk mendukung pembelajaran berbasis evaluasi otomatis.

## 5.2. Saran

Evaluasi kualitas *feedback* sebaiknya tidak hanya mengandalkan metrik otomatis, tetapi juga melibatkan penilaian manual dari dosen atau ahli bidang terkait guna memastikan relevansi dan akurasi substansi. Kedua, cakupan data dan mata kuliah dapat diperluas untuk mencakup disiplin ilmu yang lebih beragam, sehingga generalisasi hasil menjadi lebih representatif terhadap konteks pendidikan tinggi secara luas. Ketiga, penggunaan persona dalam *prompt* perlu dikembangkan lebih kontekstual, misalnya disesuaikan dengan rubrik penilaian yang nyata atau gaya komunikasi yang digunakan dosen dalam praktik sebenarnya. Keempat, penggunaan model LLM yang telah dilatih ulang (*fine-tuned*) secara khusus untuk domain pendidikan atau instruksi bahasa Indonesia, guna meningkatkan koherensi, kedalaman, dan relevansi *feedback*. Terakhir, integrasi hasil penelitian ke dalam sistem *e-learning* sebagai fitur otomatisasi evaluasi tugas terbuka dapat menjadi kontribusi praktis yang membantu dosen dan mendukung pembelajaran mandiri mahasiswa secara lebih efektif dan konsisten.

# DAFTAR PUSTAKA

Banerjee, S., & Lavie, A. (2005). *METEOR: An Automatic Metric for MT Evaluation with Improved Correlation with Human Judgments.* https://aclanthology.org/W05-0909

Brown, T. B., Mann, B., Ryder, N., Subbiah, M., Kaplan, J., Dhariwal, P., Neelakantan, A., Shyam, P., Sastry, G., Askell, A., Agarwal, S., Herbert-Voss, A., Krueger, G., Henighan, T., Child, R., Ramesh, A., Ziegler, D. M., Wu, J., Winter, C., ... Amodei, D. (2020). *Language Models are Few-Shot Learners.* http://arxiv.org/abs/2005.14165

Carless, D., & Boud, D. (2018). The development of student feedback literacy: enabling uptake of feedback. *Assessment and Evaluation in Higher Education, 43*(8), 1315–1325. https://doi.org/10.1080/02602938.2018.1463354

Dosovitskiy, A., Beyer, L., Kolesnikov, A., Weissenborn, D., Zhai, X., Unterthiner, T., Dehghani, M., Minderer, M., Heigold, G., Gelly, S., Uszkoreit, J., & Houlsby, N. (2021). *An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale.* http://arxiv.org/abs/2010.11929

Gao, R., Merzdorf, H. E., Anwar, S., Hipwell, M. C., & Srinivasa, A. (2023). *Automatic assessment of text-based responses in post-secondary education: A systematic review.* https://doi.org/2308.16151

Haider, Md. A., Mostofa, A. B., Mosaddek, Sk. S. Bin, Iqbal, A., & Ahmed, T. (2024). *Prompting and Fine-tuning Large Language Models for Automated Code Review Comment Generation.* http://arxiv.org/abs/2411.10129

Hao, Y., Song, H., Dong, L., Huang, S., Chi, Z., Wang, W., Ma, S., & Wei, F. (2022). *Language Models are General-Purpose Interfaces.* http://arxiv.org/abs/2206.06336

Jacobsen, L. J., Rohlmann, J., & Weber, K. E. (2025). *AI Feedback in Education: The Impact of Prompt Design and Human Expertise on LLM Performance.* https://doi.org/10.31219/osf.io/fx5qz

Jurafsky, D., & Martin, J. H. (2021). *Speech and Language Processing An Introduction to Natural Language Processing, Computational Linguistics, and Speech Recognition with Language Models Third Edition draft Summary of Contents.*

Lee, G. G., Latif, E., Wu, X., Liu, N., & Zhai, X. (2024). Applying large language models and chain-of-thought for automatic scoring. *Computers and Education: Artificial Intelligence, 6.* https://doi.org/10.1016/j.caeai.2024.100213

Lin, C.-Y. (2004). *ROUGE: A Package for Automatic Evaluation of Summaries.* https://aclanthology.org/W04-1013

Madotto, A., Lin, Z., Winata, G. I., & Fung, P. (2021). *Few-Shot Bot: Prompt-Based Learning for Dialogue Systems.* http://arxiv.org/abs/2110.08118

Mazzullo, E., & Bulut, O. (2024). Automated Feedback Generation for Open-Ended Questions: Insights from Fine-Tuned LLMs. Dalam *Proceedings of Machine Learning Research* (Vol. 1). https://proceedings.mlr.press/v264/mazzullo25a.html

McNichols, H., Lee, J., Fancsali, S., Ritter, S., & Lan, A. (2024). *Can Large Language Models Replicate ITS Feedback on Open-Ended Math Questions?* http://arxiv.org/abs/2405.06414

Meyer, J., Jansen, T., Schiller, R., Liebenow, L. W., Steinbach, M., Horbach, A., & Fleckenstein, J. (2024). Using LLMs to bring evidence-based feedback into the classroom: AI-generated feedback increases secondary students’ text revision, motivation, and positive emotions. *Computers and Education: Artificial Intelligence, 6*, 100199. https://doi.org/10.1016/j.caeai.2023.100199

Papineni, K., Roukos, S., Ward, T., & Zhu, W.-J. (2002). *BLEU: a Method for Automatic Evaluation of Machine Translation.* https://doi.org/10.3115/1073083.1073135

Prihar, E., Lee, M., Hopman, M., Kalai, A. T., Vempala, S., Wang, A., Wickline, G., Murray, A., & Heffernan, N. (2023). *Comparing Different Approaches to Generating Mathematics Explanations Using Large Language Models* (hlm. 290–295). https://doi.org/10.1007/978-3-031-36336-8_45

Russell, S., & Norvig, P. (2022). *Artificial Intelligence A Modern Approach Fourth Edition Global Edition.*

Stahl, M., Biermann, L., Nehring, A., & Wachsmuth, H. (2024). *Exploring LLM Prompting Strategies for Joint Essay Scoring and Feedback Generation.* 283–298. http://arxiv.org/abs/2404.15845

Sucholutsky, I., Narayan, A., Schonlau, M., & Fischmeister, S. (2019). Pay attention and you won’t lose it: A deep learning approach to sequence imputation. *PeerJ Computer Science, 2019*(8). https://doi.org/10.7717/peerj-cs.210

Tanwar, H., Shrivastva, K., Singh, R., & Kumar, D. (2024). *OpineBot: Class Feedback Reimagined Using a Conversational LLM.* http://arxiv.org/abs/2401.15589

Tian, X., Mannekote, A., Solomon, C. E., Song, Y., Wise, C. F., Mcklin, T., Barrett, J., Boyer, K. E., & Israel, M. (2024). *Examining LLM Prompting Strategies for Automatic Evaluation of Learner-Created Computational Artifacts.* https://doi.org/10.5281/zenodo.12729922

Touvron, H., Martin, L., Stone, K., Albert, P., Almahairi, A., Babaei, Y., Bashlykov, N., Batra, S., Bhargava, P., Bhosale, S., Bikel, D., Blecher, L., Ferrer, C. C., Chen, M., Cucurull, G., Esiobu, D., Fernandes, J., Fu, J., Fu, W., ... Scialom, T. (2023). *Llama 2: Open Foundation and Fine-Tuned Chat Models.* http://arxiv.org/abs/2307.09288

Wei, J., Wang, X., Schuurmans, D., Bosma, M., Ichter, B., Xia, F., Chi, E., Le, Q., & Zhou, D. (2023). *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models.* http://arxiv.org/abs/2201.11903

Williams, A. (2024). Delivering Effective Student Feedback in Higher Education: An Evaluation of the Challenges and Best Practice. *International Journal of Research in Education and Science, 10*(2), 473–501. https://doi.org/10.46328/ijres.3404

Zhang, M., Dilling, A. P., Gondelman, L., Lyngdorf, N. E. R., Lindsay, E. D., & Bjerva, J. (2025). *SEFL: Harnessing Large Language Model Agents to Improve Educational Feedback Systems.* http://arxiv.org/abs/2502.12927

Zhang, T., Kishore, V., Wu, F., Weinberger, K. Q., & Artzi, Y. (2020). *BERTScore: Evaluating Text Generation with BERT.* http://arxiv.org/abs/1904.09675
