#!/usr/bin/env python3
"""Validasi draft konten Perusahaan AI.

Cek frontmatter, nilai yang valid, dan batas 500 karakter Threads.
Pakai Python standar saja, tanpa dependensi.

Pemakaian:
    python tools/cek_konten.py drafts/
    python tools/cek_konten.py drafts/ --fix
"""

from __future__ import annotations

import argparse
import pathlib
import sys

BATAS_KARAKTER = 500
WAJIB = ("tanggal", "agen", "platform", "status", "karakter")
STATUS_VALID = {"draft", "disetujui", "tayang", "gagal"}
AGEN_VALID = {"scout", "writer", "publisher", "analyst"}


def pisah_frontmatter(teks: str) -> tuple[str, str]:
    """Kembalikan (frontmatter, isi). Kalau tidak ada frontmatter, kasih string kosong."""
    if not teks.startswith("---"):
        return "", teks
    akhir = teks.find("\n---", 3)
    if akhir == -1:
        return "", teks
    return teks[3:akhir], teks[akhir + 4 :].lstrip("\n")


def parse_frontmatter(blok: str) -> dict[str, str]:
    data: dict[str, str] = {}
    for baris in blok.splitlines():
        bersih = baris.strip()
        if not bersih or bersih.startswith("#") or ":" not in bersih:
            continue
        kunci, nilai = bersih.split(":", 1)
        data[kunci.strip()] = nilai.strip()
    return data


def cek_file(path: pathlib.Path, perbaiki: bool) -> tuple[list[str], int, int]:
    """Balik: (masalah, jumlah_karakter, jumlah_perbaikan)."""
    # utf-8-sig supaya file yang disimpan editor Windows dengan BOM tetap terbaca
    teks = path.read_text(encoding="utf-8-sig")
    blok, isi = pisah_frontmatter(teks)
    fm = parse_frontmatter(blok)
    masalah: list[str] = []
    perbaikan = 0

    for kunci in WAJIB:
        if kunci not in fm:
            masalah.append(f"frontmatter kurang: {kunci}")

    status = fm.get("status", "")
    if status and status not in STATUS_VALID:
        masalah.append(f"status tidak dikenal: {status!r} (pilihan: {', '.join(sorted(STATUS_VALID))})")

    agen = fm.get("agen", "")
    if agen and agen not in AGEN_VALID:
        masalah.append(f"agen tidak dikenal: {agen!r} (pilihan: {', '.join(sorted(AGEN_VALID))})")

    karakter = len(isi.strip())
    if karakter > BATAS_KARAKTER:
        masalah.append(f"{karakter} karakter, batas {BATAS_KARAKTER}")

    tercatat = fm.get("karakter", "")
    if tercatat.isdigit() and int(tercatat) != karakter:
        if perbaiki:
            fm["karakter"] = str(karakter)
            perbaikan += 1
        else:
            masalah.append(f"frontmatter karakter {tercatat}, hasil hitung {karakter} (pakai --fix)")

    if perbaiki and perbaikan and fm != parse_frontmatter(blok):
        header = "\n".join(f"{k}: {v}" for k, v in fm.items())
        path.write_text(f"---\n{header}\n---\n\n{isi.lstrip()}", encoding="utf-8")

    return masalah, karakter, perbaikan


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(description="Validasi draft konten Perusahaan AI")
    parser.add_argument("folder", nargs="?", default="drafts", help="folder yang diperiksa (default: drafts)")
    parser.add_argument("--fix", action="store_true", help="perbaiki jumlah karakter di frontmatter")
    args = parser.parse_args()

    folder = pathlib.Path(args.folder)
    if not folder.is_dir():
        print(f"Folder tidak ada: {folder}", file=sys.stderr)
        return 2

    files = sorted(folder.glob("*.md"))
    if not files:
        print(f"Belum ada file .md di {folder}. Tidak ada yang perlu divalidasi.")
        return 0

    gagal = 0
    for path in files:
        masalah, karakter, perbaikan = cek_file(path, args.fix)
        label = f"{path.name} ({karakter}/{BATAS_KARAKTER} karakter)"
        if masalah:
            gagal += 1
            print(f"GAGAL  {label}")
            for item in masalah:
                print(f"        - {item}")
        else:
            catatan = f"  [diperbaiki: {perbaikan}]" if perbaikan else ""
            print(f"OK     {label}{catatan}")

    print()
    if gagal:
        print(f"{gagal} dari {len(files)} file bermasalah. Jangan commit sebelum bersih.")
        return 1
    print(f"Semua {len(files)} file lolos.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
