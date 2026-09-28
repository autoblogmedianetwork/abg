# Prompt: Writer

Salin isi bagian "Template" ke dalam sesi agent, lalu isi kolomnya.

## Input

- **Ide dari Scout:** [salin dari drafts/]
- **Format:** [post Threads / balasan / utas]
- **Batas karakter:** 500

## Template

```
Tulis satu konten Threads untuk topik: {TOPIK}.

Aturan:
- Maksimal 500 karakter, hitung dengan tools/cek_konten.py
- Bahasa Indonesia santai, langsung ke inti, tanpa "Halo gaes"
- Satu ide saja
- Akhiri dengan pertanyaan atau ajakan membalas, bukan permintaan like+follow
- Jangan mengarang angka, statistik, atau pengalaman orang lain

Balas hanya dengan teks kontennya, tanpa penjelasan.
```

## Setelah ditulis
1. Simpan ke `drafts/YYYY-MM-DD-nama.md`
2. Isi frontmatter: `tanggal`, `agen: writer`, `platform: threads`, `status: draft`, `karakter: 0`
3. Jalankan `python tools/cek_konten.py drafts/ --fix`
