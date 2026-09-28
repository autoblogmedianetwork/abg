# Struktur Perusahaan

```
                    Pak Slem (CEO & manusia)
                     │  satu keputusan: boleh tayang atau tidak
                     ▼
        ┌────────────────────────────┐
        │  Pipeline Konten          │
        │                            │
        │  Scout → Writer → [APPROVAL] → Publisher → Analyst
        │                 │                        │
        │                 │                        └──► umpan balik ke Scout
        │                 └── humans
        └────────────────────────────┘
```

## Pembagian peran

| Peran | Siapa | Batas keputusan |
|---|---|---|
| Ide & riset | Scout | bebas, selama dari sumber nyata |
| Naskah | Writer | bebas, selama lolos validasi |
| Tayang | Publisher | **tidak boleh** tanpa approval manusia |
| Ukur & evaluasi | Analyst | bebas, cuma laporan |

## Prinsip yang dipegang

1. **Manusia di atas mesin** untuk keputusan yang affects publik
2. **Satu sumber kebenaran** — semua aturan di `AGENTS.md`
3. **Gagal dicatat** — setiap kegagalan ditulis di `docs/DECISIONS.md`, bukan dihapus
4. **Hemat sumber daya** — laptop 8 GB, jangan jalankan semua agent bersamaan

Kembali ke [README](../README.md)
