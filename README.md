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

## PPU / ROM notes

Nintendo VS. System game sets are effectively tied to specific PPU variants because the RP2C04 PPUs use different RGB palette mappings. A mismatched PPU may allow a game to run, but it will usually produce incorrect colors or fail title-specific expectations.

The current VS. Super Mario Bros. kit is installed with `RP2C04-0004`.

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

Detailed notes:

- [VS. UniSystem ROM and PPU Compatibility Notes](docs/hardware/vs-rom-ppu-compatibility.md)
- [EPROM Programming Notes](docs/hardware/eprom-programming-notes.md)

## Project goals

- Chronicle the build from acquisition through repair and validation.
- Preserve technical observations.
- Document cabinet provenance and conversion evidence.
- Inventory all components.
- High-resolution scan documentation and publicly archive.
- Capture photo evidence.

## Repository layout

```text
docs/
  restoration/          Work logs, restoration plan, issue notes
  hardware/             Board, PPU, harness, PSU, audio, monitor, EPROM notes
  documentation/        Indexes and notes for scanned manuals/cards/schematics
  photos/               Photo inventory indexes and caption notes
scans/                  Placeholder for scan manifests only; avoid raw copyrighted scans unless rights are clear
notes/                  Chat-derived notes and open questions
```

## Initial photo set

Initial acquisition photos were taken after the cabinet came off the truck and the cabinet was opened for first inspection.

External album:

- https://photos.app.goo.gl/nQhC1So1yUntDKtJA

## Related context

This project is part of a longer personal history with Nintendo arcade hardware and shop machines:

- [Prior Nintendo Machines](notes/prior-nintendo-machines.md)

## Status

Initial scaffold. Hardware notes are based on early inspection and conversation-derived working assumptions. Update once the cabinet is hands-on and board markings/photos are verified.
