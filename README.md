Tujuan Mengecek gambar dikirim pengguna apakah ia mie ayam atau tidak dengan bantuan AI
Alur Kerja Bot:
Penerimaan → Bot discord menerima gambar dari pengguna (format JPG/PNG).
Pra-pemrosesan → Backend (Flask/FastAPI) mengubah ukuran gambar menjadi 224×224 piksel, lalu mengonversinya menjadi array numerik dan menormalisasi nilainya ke rentang 0–1.
Inferensi → Array gambar dikirim ke model terlatih (format .h5/.onnx). Model menghitung probabilitas tiap kelas menggunakan Softmax—misal [0.95, 0.05] berarti Mie ayam dengan keyakinan 95%.
Hasil → Prediksi (label dengan probabilitas tertinggi) dan skor keyakinan dikirim balik ke pengguna melalui pesan discord, lengkap dengan nama makanan, persentase keyakinan, dan fitur tambahan (kalimat memuji).
<img width="720" height="1600" alt="WhatsApp Image 2026-08-23 at 11 25 30" src="https://github.com/user-attachments/assets/54f93fdf-49c1-4a72-989d-da60a7db16ca" />
