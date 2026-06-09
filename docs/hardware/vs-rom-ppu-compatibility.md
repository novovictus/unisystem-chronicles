# VS. UniSystem ROM and PPU Compatibility Notes

This cabinet is being documented as a Nintendo VS. UniSystem upright, not as a DualSystem restoration and not as an NES-console compatibility project.

This file contains cabinet-specific working notes. It is not a mirror of any external compatibility table.

The current working configuration is:

- Cabinet: original orange Nintendo cabinet, likely Donkey Kong Jr. origin.
- Current platform: Nintendo VS. UniSystem conversion.
- Current game state: VS. Super Mario Bros. ROM kit installed.
- Current PPU: `RP2C04-0004`.
- CPU/APU: `RP2A03` / `2A03`. This is not the PPU.

The edge connector and harness show evidence of prior conversion work, including cut or missing wires. That condition should be documented as part of the cabinet's conversion history. It is not currently being treated as a reason to pursue DualSystem restoration.

## Title priority tiers

These priorities describe restoration and acquisition intent for this cabinet. They are not a general VS. System ranking.

| Tier | Titles | Project posture |
| --- | --- | --- |
| Acquired / first-choice target | VS. Super Mario Bros. | Main reason the cabinet was acquired. Current installed game path. |
| Primary future targets | VS. Dr. Mario; VS. Duck Hunt | Main expansion goals. Worth sourcing specific PPUs, daughterboards, gun hardware, and related board parts. |
| Secondary target | VS. Tetris | Worth tracking as a future title, but not ahead of Dr. Mario or Duck Hunt. Requires compatibility verification before buying hardware. |
| Tertiary targets | VS. Ice Climber; VS. Castlevania | Interesting future candidates, but acquisition should remain opportunistic. |
| Last-tier targets | VS. Excitebike; VS. Mahjong | Low-priority interest only. Do not drive sourcing decisions unless parts appear cheaply or as part of a larger lot. |

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

Potential cabinet-relevant targets for this PPU group include:

| Title | Notes |
| --- | --- |
| VS. Super Mario Bros. | Current installed target and first-choice reason for acquiring the cabinet. |
| VS. Ice Climber | Same PPU group; tertiary target. |
| VS. Ice Climber Dual | Same PPU group, but dual-game behavior should not drive this UniSystem restoration. |
| VS. Clu Clu Land | Same PPU group; not currently a priority target. |
| VS. Excitebike, Japan variant | Same PPU group; last-tier target. |
| VS. R.B.I. Baseball | Same PPU group; not currently a priority target. |

These are the most practical low-friction EPROM candidates because they align with the PPU already installed. Board population, ROM socket layout, daughterboards, controls, and DIP settings still need to be verified per title.

## Future primary target: VS. Duck Hunt

VS. Duck Hunt should be tracked as a primary future hardware expansion target, not as a simple ROM swap.

Expected acquisition and validation checklist:

- VS. Duck Hunt ROM set for private preservation and EPROM programming
- `RC2C03B` or compatible 2C03-family VS RGB PPU
- VS light gun
- gun input wiring verification or restoration
- CRT timing, brightness, and gun response validation
- DIP switch verification

The current `RP2C04-0004` Super Mario Bros. setup is not the expected Duck Hunt PPU path.

## Future primary target: VS. Dr. Mario

VS. Dr. Mario should also be tracked as a primary future hardware expansion target.

Expected acquisition and validation checklist:

- VS. Dr. Mario ROM set for private preservation and EPROM programming
- `RP2C04-0003` PPU
- Nintendo `MDS-VS1-01` daughterboard, if required by the specific board and ROM configuration
- UniSystem control wiring verification
- DIP switch verification

Dr. Mario is not part of the current `RP2C04-0004` Super Mario Bros. group.

## Secondary target: VS. Tetris

VS. Tetris is a secondary future target. It should be tracked, but it should not pull sourcing effort away from Dr. Mario or Duck Hunt.

Before buying hardware specifically for Tetris, verify the exact VS title variant, required PPU, board population, and whether the available hardware is original, repro, modified, or part of another conversion path.

## Tertiary and low-priority targets

VS. Ice Climber and VS. Castlevania are tertiary targets. They are worth documenting and may be worth pursuing if compatible parts appear cheaply or as part of a useful board lot.

VS. Excitebike and VS. Mahjong are last-tier targets. They should not drive acquisition unless the parts overlap with higher-priority goals or appear opportunistically.

## Reference-only target: VS. Platoon

VS. Platoon is not a current restoration target. It is tracked only because modern Dr. Mario / Platoon combination daughtercards exist, and those boards may be useful to study as contemporary repro or compatibility hardware.

Do not infer that Dr. Mario and Platoon share a clean original PPU path without hardware verification. If a combination daughtercard is acquired, document the installed PPU, ROM contents privately, daughtercard logic, color output, and any palette compromise.

## PPU sourcing priorities

The useful acquisition order for this cabinet is:

| Priority | Part | Why it matters |
| --- | --- | --- |
| 1 | `RC2C03B` or compatible 2C03-family VS RGB PPU | Enables the Duck Hunt path when paired with the correct ROM set and gun wiring. |
| 2 | `RP2C04-0003` | Enables the Dr. Mario PPU path. |
| 3 | `MDS-VS1-01` daughterboard | Likely needed for Dr. Mario depending on the board setup. |
| 4 | Tetris-specific PPU / board requirements | Secondary target; verify exact requirements before sourcing. |
| 5 | `RP2C04-0002` | Useful for reconstructing the likely earlier VS. Golf / Stroke Match Golf era. |
| 6 | Other `RP2C04` variants | Opens additional VS title groups, but should not distract from the primary targets. |

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

External sources should be consulted at their original URLs. Do not mirror or redistribute external compatibility tables.

- Source boundary notes: [External Source Notes](source-notes.md)
- PAR / Riemen Nintendo VS. System Chips: https://playchoice.riemen.net/vs_chips.html
- NESdev VS. System notes: https://www.nesdev.org/wiki/Vs._System
- John's Arcade Nintendo VS PPU info: https://www.johnsarcade.com/nintendo_vs_ppu_info.php
