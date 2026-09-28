# Template: Kartu Agen

> Salin file ini menjadi `docs/AGENT-<nama>.md` saat menambah agen baru.

```markdown
# Kartu Agen: <Nama>

> Sumber aturan: [`AGENTS.md`](../AGENTS.md)

## Identitas
- **Peran:** <satu kalimat>
- **Input:** <asal data>
- **Output:** <bentuk file, bukan bebas>
- **Tool:** <yang boleh dipakai>
- **Batas keputusan:** <bebas, atau wajib ada manusia>

## Tugas
1. <urutan kerja>

## Dilarang
- <batas keras>

## Kalau gagal
<apa yang harus ditulis, bukan dihapus>
```

Setelah file dibuat, tambahkan barisnya ke tabel agent di `docs/ORG.md`, lalu jalankan
`python tools/cek_konten.py drafts/` untuk memastikan semuanya masih bersih.
