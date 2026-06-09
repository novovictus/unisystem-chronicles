# External Source Notes

This repository uses external Nintendo VS. System references for restoration research. It does not mirror, repost, or redistribute external compatibility tables.

## Referenced sources

- PAR / Riemen Nintendo VS. System Chips: https://playchoice.riemen.net/vs_chips.html
- NESdev VS. System notes: https://www.nesdev.org/wiki/Vs._System
- John's Arcade Nintendo VS PPU info: https://www.johnsarcade.com/nintendo_vs_ppu_info.php

## Use boundary

External pages are cited for cross-checking PPU, daughterboard, ROM, and cabinet-behavior relationships. Cabinet-specific notes in this repository are limited to:

- hardware present in this restoration
- observed chip markings
- harness and cabinet evidence
- restoration decisions
- narrow target-title compatibility notes
- original measurements, photos, repair notes, and validation results

Do not copy, mirror, scrape, convert, or redistribute external compatibility tables, screenshots, EPROM lists, or wording from third-party pages.

## Cabinet-relevant derived notes

These are narrow working notes for this restoration, not a replacement for the original reference tables.

| Target | Project note |
| --- | --- |
| VS. Super Mario Bros. | Current installed configuration uses `RP2C04-0004`. |
| VS. Duck Hunt | Future target. Requires a 2C03-family VS RGB PPU path and light gun support. |
| VS. Dr. Mario | Future target. Requires `RP2C04-0003` path and daughterboard support. |
| VS. Platoon | Reference-only target because modern Dr. Mario / Platoon combination daughtercards exist. Not a current restoration goal. |
| VS. Golf / Stroke Match Golf | Possible prior cabinet history; verify through board photos, chip markings, harness evidence, and parts provenance. |

## Citation posture

Use direct source links and project-specific conclusions. Avoid copying source wording. Avoid reproducing large row sets or source table structures.

Acceptable:

```md
The cabinet currently contains an `RP2C04-0004` PPU and a VS. Super Mario Bros. ROM kit. External VS. System references are consistent with this being the expected Super Mario Bros. PPU path.
```

Not acceptable:

```md
A full mirrored compatibility table copied from another site.
```

## Preservation boundary

This repository may document private preservation work through filenames, manifests, hashes, photos of owned hardware, repair notes, and observations. It should not publish ROM images, decrypted game binaries, commercial artwork scans, or copyrighted manuals/schematics unless redistribution rights are clear.
