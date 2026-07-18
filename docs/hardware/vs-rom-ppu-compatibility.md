# VS. UniSystem ROM and PPU Compatibility Notes

The current working configuration is:

- Cabinet: original orange Nintendo cabinet, likely Donkey Kong Jr. origin.
- Current platform: Nintendo VS. UniSystem conversion.
- Current game state: VS. Super Mario Bros. ROM kit installed.
- Current PPU: `RP2C04-0004`.

The edge connector and harness show evidence of prior conversion work, including cut or missing wires. That condition should be documented as part of the cabinet's conversion history. It is not currently being treated as a reason to pursue DualSystem restoration.

## PPU notes

`RP2A03` / `2A03` is the Ricoh CPU/APU used in NTSC NES-derived hardware. It contains the 6502-derived CPU core and audio functionality. Video output is handled by a separate PPU.

For Nintendo VS. System hardware, the PPU is typically a separate 40-pin Ricoh chip marked with names such as:

- `RP2C04-0001`
- `RP2C04-0002`
- `RP2C04-0003`
- `RP2C04-0004`
- `RP2C03B`
- `RP2C05-xx`

## Current EPROM test batch, 2026-06-10

| ZIP / set | Title/path | PPU relationship | DIP requirement | Expected result | Test priority |
| --- | --- | --- | --- | --- | --- |
| `iceclimb.zip` / `iceclimb` | VS. Ice Climber | Direct `RP2C04-0004` match | Use ordinary gameplay and coinage defaults. MAME records SW1:1-3 as coinage, SW1:4-5 as lives, SW1:6 as difficulty, SW1:7 as bear timer, and SW1:8 as unused. | Expected clean color path if ROM placement, EPROM type, and DIP settings are correct. | High, burn/test first |
| `excitebkj.zip` / `excitebkj` | VS. Excitebike, Japan variant | Direct `RP2C04-0004` family candidate | Use ordinary gameplay and coinage defaults. MAME records the DIP block as coinage, bonus bike, qualifying-time difficulty, and one unknown or unused bit. | Expected clean color path for the Japan variant. Do not generalize this to every Excitebike set. | High, burn/test first |
| `vstetris.zip` / `vstetris` | VS. Tetris | Compatibility-test candidate with `RP2C04-0004`, not a clean fixed-PPU match | MAME records PPU selection on SW1:6-8. Current interpretation for `RP2C04-0004` is SW1:6 ON, SW1:7 ON, SW1:8 OFF. Verify against the physical DIP-bank ON arrow. | External notes support multi-PPU behavior when DIP settings match the installed PPU. Validate actual color output on hardware. | Medium, after direct matches |
| `vsmahjng.zip` / `vsmahjng` | VS. Mahjong | Not a `RP2C04-0004` color match; MAME places it in the `RC2C03B` / `RP2C03B` group | Do not include in the first test pass. | Wrong colors are expected. Single-player mode, controller mapping, board behavior, and possible DualSystem assumptions remain unverified. | Low, reference only |

The active burn/test batch is `iceclimb`, `excitebkj`, and `vstetris`. `vsmahjng` remains a documented edge case rather than a current-cabinet recommendation.

## Platform caveats from external references

- A UniSystem is expected to run one game path at a time.
- Games using 8 or 12 ROMs should be treated as possible DualSystem-only candidates until verified otherwise.
- `RP2C04` PPUs can be physically and functionally interchangeable in some cases, but palette output changes and may be wrong.
- The VS RGB PPU family matters. `2C03`, `2C04`, and `2C05` paths are not interchangeable assumptions.
- Some titles, especially Tetris and Duck Hunt, have looser PPU behavior than a simple one-title/one-PPU rule suggests, so exact board photos, chip markings, DIP settings, and output validation matter.
