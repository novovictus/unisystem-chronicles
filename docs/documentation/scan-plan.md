# Documentation Scan Plan

## Goal

Fully preserve paper documentation associated with the cabinet using high-resolution local scans and public Internet Archive uploads where appropriate.

The GitHub repository should document provenance, scan process, checksums, captions, and stable archive links. Internet Archive should hold the preserved manual/document files when redistribution is appropriate or accepted for public preservation.

## Suggested scan settings

- Master archival scans: 600 dpi, TIFF or PNG, color.
- Working copies: PDF and/or compressed JPEG/PNG as needed.
- Include front and back of loose sheets, cards, labels, and envelopes.
- Capture scale/reference when useful.
- Do not crop away edge wear, stamps, handwritten notes, operator markings, staple holes, stains, folds, or marginalia from archival masters.
- Keep a clean derivative PDF for reading, but preserve raw/uncropped masters separately.

## Suggested naming convention

```text
YYYYMMDD_source_short-description_side_or_page.ext
```

Examples:

```text
20260608_cabinet_operator-card_front.tif
20260608_cabinet_operator-card_back.tif
20260608_vs-smb_instruction-card_front.tif
20260608_vs-golf_note_page-01.tif
```

## Internet Archive workflow

1. Scan archival masters locally.
2. Generate a readable PDF derivative.
3. Compute SHA256 checksums for the master files and derivative PDF.
4. Upload the preserved document package to Internet Archive.
5. Record the IA item URL and direct file URLs in `scan-manifest.md`.
6. Link the IA item from any relevant repo page.
7. Keep local masters backed up outside Git.

## Repository policy

Use this repository for:

- scan manifests
- Internet Archive item links
- descriptions
- physical condition notes
- filenames
- hashes
- rights/status notes
- scan workflow notes

Avoid committing raw scan masters directly to Git. Use Internet Archive for full public preservation of manuals and documents when appropriate.

Never commit ROM images or copyrighted game binaries.
