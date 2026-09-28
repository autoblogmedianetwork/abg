# Perusahaan AI

Perusahaan konten yang dijalankan agent AI, dengan manusia sebagai pemilik.

**Status:** awal. Belum ada yang tayang ke publik.

## Premis

Satu pipeline konten: **riset → tulis → approval → tayang → ukur**.
Manusia, yaitu Pak Slem, memegang satu keputusan: **boleh tayang atau tidak**.
Selebihnya boleh diputuskan agent.

## Agent

| Agent | Tugas | Output |
|---|---|---|
| Scout | mencari ide dan bahan mentah | daftar ide |
| Writer | mengubah ide jadi draft | `drafts/*.md` |
| Publisher | menayangkan yang sudah disetujui | `content/*.md` plus log |
| Analyst | mengukur performa, memberi umpan balik ke ide | laporan mingguan |

Kartu lengkap tiap agent ada di `docs/AGENT-*.md`.

## Mulai cepat

Butuh Python 3.11 atau lebih baru. Tidak ada dependensi eksternal.

```bash
git clone <alamat-repo>
cd perusahaan-ai
python tools/cek_konten.py drafts/
```

Di Windows, kalau `python` tidak bisa dipakai, pakai `py -3` sebagai gantinya.

## Kalau mulai bekerja dengan agent

Baca [`AGENTS.md`](AGENTS.md) lebih dulu. Itu konstitusi repo ini dan berlaku untuk semua agent.

## Struktur

```
AGENTS.md      konstitusi agent
docs/          SOP, kartu agen, keputusan, roadmap
drafts/        konten yang menunggu approval
content/       arsip konten yang tayang
prompts/       template prompt
tools/         script validasi
```
