# Scan Manifest

This manifest tracks paper documentation and preservation status.

The repository should keep metadata, provenance notes, filenames, checksums, and public archive links. Full manual preservation should happen through Internet Archive items when appropriate rather than by committing large scan files directly to Git.

## Internet Archive placeholders

| Item | Local master filename | Local derivative filename | SHA256 | Internet Archive item URL | Internet Archive file URL | Rights/status notes | Repository link target | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TBD manual/document | TBD | TBD | TBD | `https://archive.org/details/TBD` | `https://archive.org/download/TBD/TBD.pdf` | Preservation/reference; verify rights/status before upload | Link from README/docs once published | Placeholder |

## Local scan tracking

| Date scanned | Item | Source/location | Master filename | Working filename | SHA256 | Preservation status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| TBD | TBD | TBD | TBD | TBD | TBD | Pending IA upload | TBD |

## Suggested Internet Archive metadata

Use consistent metadata so the archive item is discoverable and defensible as preservation/reference material:

- Title: `Nintendo VS. UniSystem / Donkey Kong Jr. Cabinet Documentation - <item name>`
- Creator: `Nintendo` or the actual document creator when known.
- Date: document date if printed; otherwise use `unknown` or acquisition/scan year in notes.
- Collection: choose an appropriate public collection at upload time.
- Description: include cabinet context, scan source, physical condition, and whether the document came with the cabinet.
- Subject tags: `Nintendo`, `VS. UniSystem`, `Donkey Kong Jr.`, `arcade`, `operator manual`, `schematics`, `preservation`.
- Rights: document the known/unknown status plainly. Do not overclaim ownership.

## Repository policy

Once an item is uploaded to Internet Archive:

1. Add the IA item URL here.
2. Add direct file URLs for PDF and/or image derivatives when stable.
3. Record SHA256 checksums for local masters and uploaded derivatives when available.
4. Link the IA item from the relevant hardware/restoration/documentation page.
5. Do not commit ROMs, game binaries, or unnecessary large scan masters to Git.
