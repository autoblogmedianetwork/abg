# Kontribusi

Semua aturan agent ada di [`AGENTS.md`](AGENTS.md). Dokumen ini melengkapi untuk manusia.

## Sebelum commit

```bash
python tools/cek_konten.py drafts/
git diff
```

Kalau validasi gagal, **jangan** bypass. Perbaiki dulu.

## Commit

Conventional Commits:

| Prefix | Kapan dipakai |
|---|---|
| `feat:` | fitur atau capability baru |
| `fix:` | perbaikan bug |
| `docs:` | dokumen saja |
| `content:` | nambah atau ubah konten |
| `chore:` | tooling, config, dependency |

Contoh: `content: tambah draft 5 ide threads 28 sep`

## Branch

`nama-agt/deskripsi-singkat` — contoh `writer/fix-hitung-karakter`

## Pull request

Isi template di `.github/PULL_REQUEST_TEMPLATE.md`. Wajib nyantumin hasil running `tools/cek_konten.py`.
