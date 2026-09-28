# Log Keputusan

> Setiap keputusan penting ditulis di sini: tanggal, isi, alasan.
> Format: entri terbaru di paling atas.

## 2026-09-28 — Repo ini memakai `AGENTS.md` sebagai sumber tunggal

**Keputusan:** semua instruksi agent diletakkan di `AGENTS.md`; `CLAUDE.md` dan `GEMINI.md` cuma mengimpor.

**Alasan:** `AGENTS.md` dibaca 20+ tool sekaligus, sementara Claude Code tidak membacanya secara native.
Manfaat format ini lebih besar daripada beban file tambahan yang kecil.

## 2026-09-28 — Orkestrator belum dipilih

**Keputusan:** postpone. Repo ini berdiri sendiri dulu, tanpa mengikat ke Claw-Empire, Nano-Workforce, atau Potato-Claw.

**Alasan:** ketiganya menambah proses yang harus dijalankan, sedangkan laptop hanya 8 GB.
Pilih nanti kalau pipeline sudah terbukti jalan manual, dan pilih yang paling sedikit biaya RAM-nya.
Kriteria penilaiannya: berapa proses yang harus hidup bersamaan, dukungan Windows, dan biaya lisensi.

## 2026-09-28 — Konten tidak boleh tayang tanpa approval manusia

**Keputusan:** `status` tidak boleh naik dari `disetujui` ke `tayang` tanpa review manusia.

**Alasan:** kalau salah tayang, akun bisa kena sanction dan seluruh aset ikut hilang. Ini satu-satunya keputusan yang perlu dikunci rapat-rapat.
