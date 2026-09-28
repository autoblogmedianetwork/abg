# AGENTS.md — Perusahaan AI

> Konstitusi repo ini. Dipakai Codex, Copilot, Cursor, Gemini CLI, Jules, dan tool lain.
> Batas keras: 150 baris. Kalau nambah bagian, pangkas yang lain.

## Perintah

```bash
git status                                  # cek perubahan
git diff                                    # baca isi perubahan sebelum commit
python tools/cek_konten.py drafts/          # validasi draft konten, WAJIB sebelum commit
python tools/cek_konten.py drafts/ --fix    # perbaiki jumlah karakter di frontmatter
```

> Di laptop Windows Pak Slem, `python` tidak bisa dipakai karena mengarah ke stub Microsoft Store.
> Gunakan `py -3 tools/cek_konten.py drafts/` sebagai gantinya.

## Struktur folder

| Folder | Isi | Siapa yang tulis |
|---|---|---|
| `docs/` | dokumen perusahaan: kartu agen, SOP, keputusan, roadmap | semua agent, manusia review |
| `drafts/` | draft konten, format `YYYY-MM-DD-nama.md` | Writer |
| `content/` | arsip konten yang sudah tayang | Publisher |
| `prompts/` | template prompt tiap agen | Writer, manusia |
| `tools/` | script kecil, Python standar saja tanpa dependensi | semua agent |

File baru hanya boleh masuk ke folder di atas. Jangan bikin folder lain tanpa humans yang menyetujui.

## Aturan konten

- Batas karakter Threads: **500**. Hitung pakai `tools/cek_konten.py`, jangan dikira-kira
- Satu file draft = satu konten. Nama file = tanggal + slug
- Setiap draft wajib punya frontmatter berikut

```yaml
---
tanggal: 2026-09-28
agen: writer            # scout | writer | publisher | analyst
platform: threads
status: draft           # draft | disetujui | tayang | gagal
karakter: 0             # diisi tools/cek_konten.py
---
```

- Bahasa Indonesia santai, langsung ke inti, tanpa pembuka basa-basi
- Dilarang memakai klaim angka atau hasil yang belum diverifikasi

## Batas keselamatan

- **Jangan pernah** commit `.env`, token, `user_id`, atau berkas `*.secret.json`. `.gitignore` sudah menutupnya
- **Jangan pernah** menayangkan ke Threads tanpa `status: disetujui` yang humans-given
- **Jangan pernah** melakukan auto-like, auto-follow, atau reply massal. Ini penyebab nomor diblokir
- **Jangan pernah** melewati `tools/cek_konten.py` demi buru-buru commit
- Kuota Threads: 250 post dan 1000 reply per 24 jam per akun. Jangan sampai kehabisan di tengah siklus
- Kalau tidak yakin, catat di `docs/DECISIONS.md` lalu tanya manusia. Jangan menebak lalu commit

## Git workflow

- Branch: `nama-agt/deskripsi-singkat`, contoh `writer/alur-approval`
- Commit: Conventional Commits, yaitu `feat:`, `fix:`, `docs:`, `chore:`, `content:`
- Satu commit satu tujuan. Jangan campur `content:` dengan `fix:`
- PR wajib mengisi `.github/PULL_REQUEST_TEMPLATE.md` dengan hasil `tools/cek_konten.py` yang bersih

## Standar laporan

Setiap tugas selesai harus menyebutkan tiga hal: file yang diubah, perintah verifikasi yang dijalankan, dan hasilnya. Kalau gagal, sebutkan alasannya. Jangan diamkan.
