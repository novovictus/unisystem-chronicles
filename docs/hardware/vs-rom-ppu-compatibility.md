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

## Current EPROM test batch, 2026-06-10

This batch records ROM sets available for private EPROM programming and hardware validation with the currently installed `RP2C04-0004` PPU. ROM binaries are not stored in this repository.

| ZIP / set | Title/path | Current `RP2C04-0004` posture | Test priority | Bench expectation |
| --- | --- | --- | --- | --- |
| `iceclimb.zip` / `iceclimb` | VS. Ice Climber | Direct `RP2C04-0004` match | Burn/test first | Expected clean color path if ROM placement, EPROM type, and DIP settings are correct. |
| `excitebkj.zip` / `excitebkj` | VS. Excitebike, Japan variant | Direct `RP2C04-0004` match | Burn/test first | Expected clean color path for the Japan variant. Do not generalize this to every Excitebike set. |
| `vstetris.zip` / `vstetris` | VS. Tetris | Compatibility-test candidate, not a clean one-PPU assumption | Burn/test after the direct matches | External notes indicate Tetris can work across more than one PPU path with DIP/color behavior. Validate actual color output on hardware. |
| `vsmahjng.zip` / `vsmahjng` | VS. Mahjong | Not a normal `RP2C04-0004` UniSystem target | Document only unless intentionally testing edge cases | Expected PPU/color mismatch and possible DualSystem/control assumptions. Keep out of the first clean test pass. |

Batch conclusion: the active burn/test batch is `iceclimb`, `excitebkj`, and `vstetris`. `vsmahjng` is retained as a documented reference/edge-case candidate, not as a clean current-cabinet recommendation.

## Validated `RP2C04-0004` candidates for the current cabinet

This section records only claims validated strongly enough to act on for the current `RP2C04-0004` cabinet path. It intentionally does not reproduce an unverified broad compatibility table.

| Game/path | MAME set name | PPU status for current cabinet | UniSystem posture | Notes | Priority |
|---|---|---|---|---|---|
| VS. Ice Climber | `iceclimb` | Direct `RP2C04-0004` match | Good single-game UniSystem burn-and-test candidate | MAME associates `iceclimb` with `PALETTE_2C04_0004`; standard VS ROM/EPROM workflow still needs exact set verification before burning. | High, friction-first |
| VS. Excitebike, Japan variant | `excitebkj` | Direct `RP2C04-0004` family candidate | Good candidate after exact set verification | MAME's PPU-family notes list Excitebike Japan under `RP2C04-0004`. Treat non-Japan Excitebike variants separately because Excitebike also appears in other PPU contexts. | High, variant-sensitive |
| VS. Tetris | `vstetris` | Compatibility-test candidate with `RP2C04-0004`; not treated as a clean fixed-PPU match | Burn-and-test candidate after direct matches | MAME's PPU-family notes list Tetris under `RP2C04-0001` with a caveat that starred games can work with multiple PPU types when DIP settings match the installed PPU. John's Arcade and PAR/Riemen notes also support multi-PPU behavior for some titles. Validate actual color output on this cabinet. | Medium, test batch |
| VS. Mahjong | `vsmahjng` / Mahjong path | Not a `RP2C04-0004` color match | Low-priority verification candidate only | MAME's PPU-family notes place Mahjong in the `RC2C03B` / `RP2C03B` group. Wrong colors are expected with the current `RP2C04-0004`; single-player and controller-input behavior are explicitly to be verified before being treated as operational guidance. | Low, reference only |

Validated practical conclusion: with the current installed `RP2C04-0004`, the clean immediate alternate paths are VS. Ice Climber and the Japan `RP2C04-0004` Excitebike variant. VS. Tetris is now part of the test batch because external notes support multi-PPU/DIP behavior, but it remains a hardware-output validation item rather than a native 0004 claim. Mahjong remains a documented edge case until exact PPU, controls, board behavior, and single-side behavior are verified.

## Platform caveats from external references

These notes are project-specific conclusions from external references. Do not mirror the source tables.

- A UniSystem is expected to run one game path at a time. Do not pursue DualSystem behavior unless later cabinet evidence requires it.
- Games using 8 or 12 ROMs should be treated as possible DualSystem-only candidates until verified otherwise.
- `RP2C04` PPUs can be physically/functionally interchangeable in some cases, but palette output changes and may be wrong.
- The VS RGB PPU family matters. `2C03`, `2C04`, and `2C05` paths are not interchangeable assumptions.
- Some titles, especially Tetris and Duck Hunt, have looser PPU behavior than a simple one-title/one-PPU rule suggests, so exact board photos, chip markings, DIP settings, and output validation matter.

## Title priority tiers

These priorities describe restoration and acquisition intent for this cabinet. They are not a general VS. System ranking.

| Tier | Titles | Project posture |
| --- | --- | --- |
| Acquired / first-choice target | VS. Super Mario Bros. | Main reason the cabinet was acquired. Current installed game path. |
| Primary future targets | VS. Dr. Mario; VS. Duck Hunt | Main expansion goals. Worth sourcing specific PPUs, daughterboards, gun hardware, and related board parts. |
| Secondary target | VS. Tetris | Worth tracking and now part of the current test batch, but not ahead of Dr. Mario or Duck Hunt for sourcing. Has PPU/DIP nuance; verify color output on hardware. |
| Tertiary targets | VS. Ice Climber; VS. Castlevania | Ice Climber is in the current test batch because it is a clean `RP2C04-0004` path. Castlevania remains opportunistic. |
| Last-tier targets | VS. Excitebike; VS. Mahjong | Excitebike Japan is in the current test batch because it aligns with `RP2C04-0004`. Mahjong remains low-priority/reference unless testing edge cases. |

## Current low-friction paths

This list is friction-first, not priority-first. It assumes the cabinet currently has only one available PPU, `RP2C04-0004`, and that no daughterboard-required, DualSystem-only, or light-gun-dependent paths are in scope for immediate testing.

Excluded from this immediate list:

- VS. Super Mario Bros.: already installed.
- VS. Duck Hunt: requires a 2C03-family PPU, light gun, and gun wiring path; stretch goal for now.
- VS. Dr. Mario: requires `RP2C04-0003` and daughterboard support.
- VS. Castlevania: requires different PPU and likely Konami daughterboard support.
- VS. Ice Climber Dual: DualSystem-style behavior is outside current scope.
- VS. Clu Clu Land and VS. R.B.I. Baseball: not current target titles.
- VS. Mahjong: retained as a reference/edge-case candidate, not a clean first-pass test.

Immediate friction-first candidates:

| Friction rank | Title/path | Current blocker | Notes |
| ---: | --- | --- | --- |
| 1 | VS. Ice Climber | Correct VS ROM set and EPROM burn | Best next burn-and-test candidate using the current `RP2C04-0004` path. Good validation of dump/burn/install workflow after preserving the current Super Mario Bros. ROMs. |
| 2 | VS. Excitebike, Japan variant | Exact variant verification | Aligns with the current `RP2C04-0004` path when using the Japan-compatible set. Do not generalize this to all Excitebike variants. |
| 3 | VS. Tetris | DIP/color behavior verification | In the current test batch. Burn/test after the direct 0004 matches and document actual color output, DIP settings, and any mismatch. |
| 4 | VS. Mahjong | PPU mismatch and controls verification | Low-priority curiosity only. Expected to have incorrect colors on the current `RP2C04-0004` path; single-player mode and joystick/button control mapping remain to be verified. |

Working conclusion: VS. Ice Climber is the cleanest next EPROM workflow test once the current Super Mario Bros. ROMs are dumped, labeled, and preserved. The Japan `RP2C04-0004` Excitebike path is the next-best low-friction candidate. VS. Tetris is also worth burning in this batch, but its result should be recorded as hardware compatibility evidence, especially color/DIP behavior.

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
| VS. Ice Climber | Same PPU group; tertiary target and current lowest-friction alternate title. |
| VS. Ice Climber Dual | Same PPU group, but dual-game behavior should not drive this UniSystem restoration. |
| VS. Clu Clu Land | Same PPU group; not currently a priority target. |
| VS. Excitebike, Japan variant | Same PPU group; last-tier target and variant-sensitive low-friction candidate. |
| VS. R.B.I. Baseball | Same PPU group; not currently a priority target. |
| VS. Tetris | Not listed here as a native 0004 title, but included in the current test batch because multiple references indicate broader PPU/DIP compatibility behavior. |

These are the most practical low-friction EPROM candidates because they either align with the PPU already installed or have enough external compatibility evidence to justify a controlled test. Board population, ROM socket layout, daughterboards, controls, DIP settings, and actual color output still need to be verified per title.

## Future primary target: VS. Duck Hunt

VS. Duck Hunt should be tracked as a primary future hardware expansion target, not as a simple ROM swap.

Expected acquisition and validation checklist:

- VS. Duck Hunt ROM set for private preservation and EPROM programming
- `RC2C03B`, `RP2C03B`, `RC2C03C`, or another verified compatible 2C03-family VS RGB PPU
- VS light gun
- gun input wiring verification or restoration
- CRT timing, brightness, and gun response validation
- DIP switch verification

Additional caveats:

- Duck Hunt requires a gun path; it may alarm or fail operationally if no gun is present.
- External references indicate Duck Hunt existed with multiple 2C03-family PPU variants, so do not reject a Duck Hunt board solely because the PPU is not `RC2C03B` if the rest of the evidence is consistent.
- The current `RP2C04-0004` Super Mario Bros. setup is not the expected Duck Hunt PPU path.

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

VS. Tetris is a secondary future title and is also part of the current EPROM test batch. It should be tracked, but it should not pull sourcing effort away from Dr. Mario or Duck Hunt.

Working notes:

- Treat Tetris as a title requiring PPU and DIP-switch verification rather than assuming a single fixed PPU path.
- External references indicate Tetris can work with more than one PPU path and may include DIP color-setting behavior.
- Capture the suggested DIP setting for later hardware testing with `RP2C04-0004`: DIP 5 = ON, DIP 6 = OFF, DIP 7 = ON, DIP 8 = test/verify. This is a test note, not a validated cabinet setting.
- Burn/test is reasonable after the direct 0004 matches because the ROM set is available and the experiment is low-friction.
- Before buying hardware specifically for Tetris, verify the exact VS title variant, required PPU, board population, DIP expectations, and whether the available hardware is original, repro, modified, or part of another conversion path.

## Mahjong verification notes

VS. Mahjong is a low-priority verification item only.

Working notes to verify before treating Mahjong as operationally documented:

- Whether the available Mahjong ROM path can run usefully in single-player on one side of a UniSystem-style setup.
- Whether the CPU-opponent assumption is correct for the specific ROM path being tested.
- Whether joystick plus button input is sufficient for tile selection, discard, and command selection.
- Whether Up/Down command navigation for actions such as Pon, Chi, or related prompts is correct.
- Expected color mismatch when using the current `RP2C04-0004`, since the referenced Mahjong path is associated with the `RC2C03B` / `RP2C03B` group.

Do not describe Mahjong as a clean current-cabinet recommendation until single-player mode, controls, DIP behavior, and color output are verified on hardware or a stronger source.

## Tertiary target: VS. Castlevania

VS. Castlevania is a tertiary target.

Working notes:

- Track `RP2C04-0002` as the likely PPU path for Castlevania.
- Track Konami daughterboard requirements before buying a loose ROM set.
- A Top Gun donor path may be relevant only as a comparative or conversion note; verify before sourcing because Top Gun itself is a different PPU/security path.

## Other tertiary and low-priority targets

VS. Ice Climber is a tertiary target and remains interesting because it is in the current `RP2C04-0004` group.

VS. Excitebike and VS. Mahjong are last-tier targets. Excitebike Japan is included in the current test batch because it overlaps the installed PPU. Mahjong should not drive acquisition unless the parts overlap with higher-priority goals or appear opportunistically.

Working notes:

- Excitebike appears in more than one VS context. Track exact variant and PPU before sourcing.
- Mahjong appears in external references near the 2C03-family grouping. Treat it as a low-priority verification item, not a purchase driver.

## Reference-only target: VS. Platoon

VS. Platoon is not a current restoration target. It is tracked only because modern Dr. Mario / Platoon combination daughtercards exist, and those boards may be useful to study as contemporary repro or compatibility hardware.

Do not infer that Dr. Mario and Platoon share a clean original PPU path without hardware verification. If a combination daughtercard is acquired, document the installed PPU, ROM contents privately, daughtercard logic, color output, and any palette compromise.

## PPU sourcing priorities

The useful acquisition order for this cabinet is:

| Priority | Part | Why it matters |
| --- | --- | --- |
| 1 | Verified 2C03-family VS RGB PPU for Duck Hunt | Enables the Duck Hunt path when paired with the correct ROM set and gun wiring. |
| 2 | `RP2C04-0003` | Enables the Dr. Mario PPU path. |
| 3 | `MDS-VS1-01` daughterboard | Likely needed for Dr. Mario depending on the board setup. |
| 4 | Tetris-specific PPU / board requirements | Secondary target; verify exact requirements before sourcing. |
| 5 | `RP2C04-0002` | Useful for Castlevania and reconstructing the likely earlier VS. Golf / Stroke Match Golf era. |
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

- MAME `vsnes.cpp` source, used only as a validation reference for PPU-family notes: https://github.com/mamedev/mame/blob/master/src/mame/nintendo/vsnes.cpp
- Source boundary notes: [External Source Notes](source-notes.md)
- PAR / Riemen Nintendo VS. System Chips: https://playchoice.riemen.net/vs_chips.html
- NESdev VS. System notes: https://www.nesdev.org/wiki/Vs._System
- John's Arcade Nintendo VS PPU info: https://www.johnsarcade.com/nintendo_vs_ppu_info.php
