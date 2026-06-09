# UniSystem Chronicles

Nintendo VS. UniSystem restoration and technical documentation from an original orange Donkey Kong Jr. cabinet conversion.

This repository documents the cabinet as found, its likely conversion history, hardware inventory, restoration work, high-resolution documentation scans, and technical notes around Nintendo VS. System board/PPU/ROM relationships.

## Current cabinet state

Working hypothesis based on the initial inspection:

```text
Original Donkey Kong Jr. orange Nintendo cabinet
-> converted to Nintendo VS. UniSystem
-> previously ran VS. Golf / Stroke & Match Golf
-> currently has a VS. Super Mario Bros. ROM kit installed
```

Known current details:

- Cabinet: original orange Nintendo cabinet, likely Donkey Kong Jr. origin.
- Current platform: Nintendo VS. UniSystem conversion.
- Current game state: VS. Super Mario Bros. ROM kit installed.
- Current PPU: `RP2C04-0004`.
- CPU/APU note: `RP2A03` / `2A03` is the CPU/APU, not the PPU.
- Known issue at acquisition: strong speaker hum.
- Monitor: initially reported solid.
- Harness state: edge connector and harness show prior conversion work, including cut or missing wires.
- Restoration posture: preserve original boards and harnesses where practical, clean/test/repair, avoid irreversible JAMMA-style conversion.

## PPU / ROM notes

Nintendo VS. System game sets are effectively tied to specific PPU variants because the RP2C04 PPUs use different RGB palette mappings. A mismatched PPU may allow a game to run, but it will usually produce incorrect colors or fail title-specific expectations.

The current VS. Super Mario Bros. kit is installed with `RP2C04-0004`, which is consistent with the expected PPU family for VS. Super Mario Bros.

Current `RP2C04-0004` expansion candidates include:

- VS. Super Mario Bros.
- VS. Ice Climber
- VS. Ice Climber Dual
- VS. Clu Clu Land
- VS. Excitebike, Japan variant
- VS. R.B.I. Baseball

Future target hardware to source:

- VS. Duck Hunt: `RC2C03B` or compatible 2C03-family VS RGB PPU, plus light gun and gun wiring validation.
- VS. Dr. Mario: `RP2C04-0003`, and likely Nintendo `MDS-VS1-01` daughterboard depending on board setup.
- Prior VS. Golf / Stroke & Match Golf reconstruction: likely `RP2C04-0002`, pending confirmation.

The `RP2A03` / `2A03` remains the CPU/APU. It is not the PPU.

Detailed notes: [VS. UniSystem ROM and PPU Compatibility Notes](docs/hardware/vs-rom-ppu-compatibility.md)

## Project goals

- Chronicle the build from acquisition through repair and validation.
- Preserve technical observations that are easy to lose in forum/chat history.
- Document cabinet provenance and conversion evidence.
- Inventory boards, cage, harnessing, power, audio, monitor, controls, and documentation.
- High-resolution scan all paper documentation and organize it with stable filenames.
- Capture photo evidence as the work progresses.
- Keep ROM and copyrighted game binary material out of the repository.

## Repository layout

```text
docs/
  restoration/          Work logs, restoration plan, issue notes
  hardware/             Board, PPU, harness, PSU, audio, monitor notes
  documentation/        Indexes and notes for scanned manuals/cards/schematics
  photos/               Photo inventory indexes and caption notes
scans/                  Placeholder for scan manifests only; avoid raw copyrighted scans unless rights are clear
notes/                  Chat-derived notes and open questions
```

## Initial photo set

Initial acquisition photos were taken after the cabinet came off the truck and the cabinet was opened for first inspection.

External album:

- https://photos.app.goo.gl/nQhC1So1yUntDKtJA

Suggested handling:

- Keep original full-resolution photos outside Git history if large.
- Add selected compressed documentation photos later if useful.
- Maintain a photo manifest in `docs/photos/photo-log.md`.
- Record observations from each photo rather than relying on image filenames alone.

## Legal / preservation boundary

This repository is for restoration documentation, hardware notes, scan manifests, provenance notes, and repair logs.

Do not commit:

- ROM images
- decrypted game binaries
- commercial artwork scans intended for reproduction unless rights/status are clear
- copyrighted manuals/schematics unless redistribution is known to be allowed

Use manifests, filenames, hashes, and notes to document private preservation scans without redistributing restricted material.

## Status

Initial scaffold. Hardware notes are based on early inspection and conversation-derived working assumptions. Update once the cabinet is hands-on and board markings/photos are verified.
