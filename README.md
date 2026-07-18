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

- [VS. Super Mario Bros. ROM Preservation](docs/hardware/vs-super-mario-bros-rom-preservation.md)
- [VS. UniSystem ROM and PPU Compatibility Notes](docs/hardware/vs-rom-ppu-compatibility.md)
- [EPROM Programming Notes](docs/hardware/eprom-programming-notes.md)
- [Restoration Work Log](docs/work-log.md)

## Project goals

- Document the cabinet's physical state and conversion history.
- Record repair, validation, and restoration work.
- Preserve original EPROM contents and hardware provenance.
- Produce high-resolution scans and photo documentation where useful.
- Publish technical observations that may help other Nintendo VS. System restorations.

## Prior Nintendo machines

This project is the first Nintendo arcade restoration I am documenting as a preservation-oriented workflow. The earlier machines below were owned, repaired, restored, or maintained before I kept formal preservation notes, so their details are reconstructed from memory and surviving machine context.

Those machines shaped the approach used here: verify power before startup, respect rare Nintendo-specific components, preserve original ROM contents, avoid unnecessary mechanical strain, and document the work while it is happening.

### Nintendo Red Tent

I previously owned a Nintendo Red Tent cocktail cabinet. The machine had a blown power supply. From memory, it was likely not configured correctly for 100-120V input, which resulted in PSU failure.

I do not have a complete troubleshooting log from that repair. What I do remember is performing a wiring overhaul afterward to ensure the correct voltage rails were routed properly across the boards.

The main lesson carried forward from that machine is simple: Nintendo arcade hardware should not be powered casually until input configuration, PSU behavior, harness condition, grounding, and board voltages are verified.

### Nintendo PlayChoice-10

I also previously owned a Nintendo PlayChoice-10. That machine did not require a full overhaul.

Most of the work was physical and contact-related: button issues, contact cleaning, and restoration of high-use connection points. Its condition was consistent with a machine that had spent time in a high-humidity environment.

The PlayChoice-10 sits in the same broader Nintendo arcade lineage as the VS. UniSystem, but the restoration needs were much lighter than the current cabinet.

### Super Mario Bros. pinball

I also maintain a Super Mario Bros. pinball machine that I acquired over a decade ago. It was restored before I kept formal project logs, so the details are reconstructed from memory and current machine state.

Known restoration work included:

- Cold solder joint repair
- Power supply troubleshooting
- DMD cutout repair
- Dead diode and transistor replacement
- Full LED conversion
- Full solenoid and flipper rebuilds
- Playfield cleaning, wax, and polish
- New silicone flippers and rubbers throughout

The machine remains in regular playable condition and is often played by shop visitors. Unlike a static collectible, it is part of the working shop environment.

These earlier machines explain the conservative workflow used on the current UniSystem cabinet. The goal is not just to make the cabinet turn on. The goal is to preserve original ROM contents, avoid unnecessary mechanical stress on rare parts such as the PPU, validate power and grounding before startup, and record the process while the work is still happening.

## Repository layout

```text
docs/
  work-log.md             Chronological restoration and bench work
  hardware/               EPROM, ROM, PPU, and compatibility references
```

## Photos

Initial acquisition and inspection photos:

https://photos.app.goo.gl/nQhC1So1yUntDKtJA
