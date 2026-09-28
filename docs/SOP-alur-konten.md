# SOP: Alur Konten

> Sumber aturan: [`AGENTS.md`](../AGENTS.md)

## Alur normal

```
1. Scout    -> ide mentah, max 10, wajib ada sumbernya
2. Writer   -> naskah di drafts/, di bawah 500 karakter
3. Validasi -> python tools/cek_konten.py drafts/
4. Approval -> humans baca dan ubah status jadi disetujui
5. Publisher-> tayang, pindahkan ke content/
6. Analyst  -> ukur, beri umpan balik ke Scout
```

## Kapan alur berhenti

Alur berhenti dan perlu humans kalau salah satu ini muncul:

- Gagal dua kali berturut-turut di tahap yang sama
- Butuh keputusan yang mengubah aturan di `AGENTS.md`
- Butuh biaya, API, atau hosting baru
- Butuh publish di luar jadwal yang sudah disepakati

Tulis alasannya di `docs/DECISIONS.md`, lalu berhenti. Jangan mencoba bypass.

## Jadwal harian

- Pagi: Scout + Writer (2 draft)
- Siang: humans review
- Sore: Publisher menayangkan yang disetujui
- Akhir pekan: Analyst menulis laporan

## Kalau ada ide bagus tapi belum ripe
Simpan di `docs/ROADMAP.md` bagian Backlog. Jangan dipaksakan jadi konten.
