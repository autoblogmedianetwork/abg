# Prompt: Scout

## Input

- **Topik yang dicari:** [tema umum]
- **Jumlah ide:** maksimal 10

## Template

```
Cari ide konten Threads tentang: {TOPIK}.

Untuk setiap ide, tulis:
- Judul satu kalimat
- Dua kalimat kenapa ide ini relevan sekarang
- Satu tautan sumber yang nyata

Aturan:
- Maksimal 10 ide
- Kalau tidak yakin sumbernya ada, jangan tulis tautannya
- Jangan mengarang statistik atau tren
- Lewati topik yang sudah pernah dipakai (cek drafts/ dan content/)

Format jawaban: markdown, satu blok per ide, dipisah garis.
```

## Setelahnya
Simpan hasil ke `drafts/YYYY-MM-DD-ide-scout.md` dengan `agen: scout`, `status: draft`.
