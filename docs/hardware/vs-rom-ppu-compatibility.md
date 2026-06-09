# VS. UniSystem ROM and PPU Compatibility Notes

This cabinet is being documented as a Nintendo VS. UniSystem upright, not as a DualSystem restoration and not as an NES-console compatibility project.

The current working configuration is:

- Cabinet: original orange Nintendo cabinet, likely Donkey Kong Jr. origin.
- Current platform: Nintendo VS. UniSystem conversion.
- Current game state: VS. Super Mario Bros. ROM kit installed.
- Current PPU: `RP2C04-0004`.
- CPU/APU: `RP2A03` / `2A03`. This is not the PPU.

The edge connector and harness show evidence of prior conversion work, including cut or missing wires. That condition should be documented as part of the cabinet's conversion history. It is not currently being treated as a reason to pursue DualSystem restoration.

## Practical restoration scope

The near-term electrical goal is a clean, reliable UniSystem path:

- board cage and VS mainboard inspection
- harness cleanup and continuity verification
- power, audio, monitor, and control validation
- current VS. Super Mario Bros. configuration validation
- future title-specific wiring only where needed, such as light gun support for VS. Duck Hunt

ROM work should stay documentation-only in this repository. Do not commit ROM images or commercial game binaries.

## Current PPU: RP2C04-0004

The installed `RP2C04-0004` matches the current VS. Super Mario Bros. configuration.

Potential compatible ROM targets for this PPU group include:

| Title | Notes |
| --- | --- |
| VS. Super Mario Bros. | Current installed target. |
| VS. Ice Climber | Same PPU group. |
| VS. Ice Climber Dual | Same PPU group, but dual-game behavior should not drive this UniSystem restoration. |
| VS. Clu Clu Land | Same PPU group. |
| VS. Excitebike, Japan variant | Same PPU group. |
| VS. R.B.I. Baseball | Same PPU group. |

These are the most practical low-friction EPROM candidates because they align with the PPU already installed. Board population, ROM socket layout, daughterboards, controls, and DIP settings still need to be verified per title.

## Future target: VS. Duck Hunt

VS. Duck Hunt should be tracked as a future hardware expansion target, not as a simple ROM swap.

Expected acquisition and validation checklist:

- VS. Duck Hunt ROM set for private preservation and EPROM programming
- `RC2C03B` or compatible 2C03-family VS RGB PPU
- VS light gun
- gun input wiring verification or restoration
- CRT timing, brightness, and gun response validation
- DIP switch verification

The current `RP2C04-0004` Super Mario Bros. setup is not the expected Duck Hunt PPU path.

## Future target: VS. Dr. Mario

VS. Dr. Mario should also be tracked as a hardware expansion target.

Expected acquisition and validation checklist:

- VS. Dr. Mario ROM set for private preservation and EPROM programming
- `RP2C04-0003` PPU
- Nintendo `MDS-VS1-01` daughterboard, if required by the specific board and ROM configuration
- UniSystem control wiring verification
- DIP switch verification

Dr. Mario is not part of the current `RP2C04-0004` Super Mario Bros. group.

## PPU sourcing priorities

The useful acquisition order for this cabinet is:

| Priority | Part | Why it matters |
| --- | --- | --- |
| 1 | `RC2C03B` or compatible 2C03-family VS RGB PPU | Enables the Duck Hunt path when paired with the correct ROM set and gun wiring. |
| 2 | `RP2C04-0003` | Enables the Dr. Mario PPU path. |
| 3 | `MDS-VS1-01` daughterboard | Likely needed for Dr. Mario depending on the board setup. |
| 4 | `RP2C04-0002` | Useful for reconstructing the likely earlier VS. Golf / Stroke & Match Golf era. |
| 5 | Other `RP2C04` variants | Opens additional VS title groups, but should not distract from the Duck Hunt and Dr. Mario targets. |

EPROM programming is expected to be easier than sourcing correct PPUs and any required title-specific hardware.

## Compatibility boundary

Do not treat this cabinet as:

- a general NES ROM host
- a DualSystem restoration project
- a software-selectable multicart platform
- a JAMMA conversion target

Treat it as:

- a Nintendo VS. UniSystem cabinet
- currently configured for VS. Super Mario Bros.
- historically modified and worth documenting as found
- expandable by sourcing correct VS PPUs and title-specific hardware

## Reference links

- NESdev VS. System notes: https://www.nesdev.org/wiki/Vs._System
- VS / PlayChoice chipset list: https://playchoice.riemen.net/vs_chips.html
- John's Arcade Nintendo VS PPU info: https://www.johnsarcade.com/nintendo_vs_ppu_info.php
