---
applyTo: "drafts/**"
description: Aturan saat membuat atau mengubah konten
---

# Aturan Konten

- Batas **500 karakter** untuk Threads. Ukur dengan `python tools/cek_konten.py`, jangan dikira-kira
- Frontmatter wajib: `tanggal`, `agen`, `platform`, `status`, `karakter`
- `status` hanya boleh naik: `draft` → `disetujui` → `tayang` atau `gagal`
- Mengubah `status` dari `disetujui` ke `tayang` butuh review manusia
- Bahasa Indonesia santai. Satu ide per file
- Dilarang klaim angka, hasil, atau testimoni yang belum bisa diverifikasi
