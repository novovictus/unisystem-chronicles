# UniSystem Chronicles

Documentation of an original orange Nintendo cabinet converted from Donkey Kong Jr. to VS. UniSystem operation.

The repository records the cabinet as found, conversion evidence, hardware state, restoration work, ROM and PPU relationships, and preservation material produced during the project.

## Cabinet state

```text
Original Donkey Kong Jr. orange Nintendo cabinet
-> converted to Nintendo VS. UniSystem
-> previously ran VS. Golf / Stroke & Match Golf
-> currently fitted with a VS. Super Mario Bros. MDS-SM4 ROM kit
```

Current board configuration:

```text
Board: Nintendo MDS-01-CPU
PPU:   RP2C04-0004
Game:  VS. Super Mario Bros.
```

The installed ROM kit was supplied in a Nintendo of America envelope shipped in January 2000. That date reflects service-stock or replacement-kit provenance, not the original game release.

## Preservation approach

The original EPROMs will be removed, read repeatedly, and verified before any runtime testing. Verified copies will be written to replacement EPROMs so the originals can be preserved and stored.

The `RP2C04-0004` PPU will remain installed. No reliable expendable drop-in replacement has been identified, and removing it would add mechanical risk without a preservation benefit.

## Documentation

- [VS. Super Mario Bros. ROM Kit State](docs/hardware/vs-super-mario-bros-rom-kit.md)
- [VS. UniSystem ROM and PPU Compatibility Notes](docs/hardware/vs-rom-ppu-compatibility.md)
- [EPROM Programming Notes](docs/hardware/eprom-programming-notes.md)
- [Prior Nintendo Machines](notes/prior-nintendo-machines.md)

## Project goals

- Document the cabinet's physical state and conversion history.
- Record repair, validation, and restoration work.
- Preserve original EPROM contents and hardware provenance.
- Produce high-resolution scans and photo documentation where useful.
- Publish technical observations that may help other Nintendo VS. System restorations.

## Repository layout

```text
docs/
  restoration/          Repair logs, restoration plans, and issue notes
  hardware/             Board, PPU, harness, PSU, audio, monitor, and EPROM notes
  documentation/        Indexes and notes for manuals, cards, and schematics
  photos/               Photo inventories and captions
scans/                  Scan manifests and archival notes
notes/                  Historical context and open questions
```

## Photos

Initial acquisition and inspection photos:

https://photos.app.goo.gl/nQhC1So1yUntDKtJA
