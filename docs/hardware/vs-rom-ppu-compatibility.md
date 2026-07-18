# VS. UniSystem ROM and PPU Compatibility Notes

The current working configuration is:

- Cabinet: original orange Nintendo cabinet, likely Donkey Kong Jr. origin.
- Current platform: Nintendo VS. UniSystem conversion.
- Current game state: VS. Super Mario Bros. ROM kit installed.
- Current PPU: `RP2C04-0004`.
- CPU/APU: `RP2A03` / `2A03`. This is not the PPU.

The edge connector and harness show evidence of prior conversion work, including cut or missing wires. That condition should be documented as part of the cabinet's conversion history. It is not currently being treated as a reason to pursue DualSystem restoration.

# PPU Notes

`RP2A03` / `2A03` is the Ricoh CPU/APU used in NTSC NES-derived hardware. It contains the 6502-derived CPU core and audio functionality. Video output is handled by a separate PPU.

For Nintendo VS. System hardware, the PPU is typically a separate 40-pin Ricoh chip marked with names such as:

- `RP2C04-0001`
- `RP2C04-0002`
- `RP2C04-0003`
- `RP2C04-0004`
- `RP2C03B`
- `RP2C05-xx`

## Current EPROM test batch, 2026-06-10

This batch records ROM sets available for private EPROM programming and hardware validation with the currently installed `RP2C04-0004` PPU. ROM binaries are not stored in this repository.

| ZIP / set | Title/path | Current `RP2C04-0004` posture | Test priority | Bench expectation |
| --- | --- | --- | --- | --- |
| `iceclimb.zip` / `iceclimb` | VS. Ice Climber | Direct `RP2C04-0004` match | Burn/test first | Expected clean color path if ROM placement, EPROM type, and DIP settings are correct. |
| `excitebkj.zip` / `excitebkj` | VS. Excitebike, Japan variant | Direct `RP2C04-0004` match | Burn/test first | Expected clean color path for the Japan variant. Do not generalize this to every Excitebike set. |
| `vstetris.zip` / `vstetris` | VS. Tetris | Compatibility-test candidate, not a clean one-PPU assumption | Burn/test after the direct matches | External notes indicate Tetris can work across more than one PPU path with DIP/color behavior. Validate actual color output on hardware. |
| `vsmahjng.zip` / `vsmahjng` | VS. Mahjong | Not a normal `RP2C04-0004` UniSystem target | Document only unless intentionally testing edge cases | Expected PPU/color mismatch and possible DualSystem/control assumptions. Keep out of the first clean test pass. |

Batch conclusion: the active burn/test batch is `iceclimb`, `excitebkj`, and `vstetris`. `vsmahjng` is retained as a documented reference/edge-case candidate, not as a clean current-cabinet recommendation.

## DIP test:

| Set | DIP test | Notes |
| --- | --- | --- |
| `iceclimb` | Use ordinary gameplay/coinage defaults first. MAME records SW1:1-3 as coinage, SW1:4-5 as lives, SW1:6 as difficulty, SW1:7 as bear timer, and SW1:8 as unused. | No PPU-select DIP is expected. |
| `excitebkj` | Use ordinary gameplay/coinage defaults first. MAME records the Excitebike DIP block as coinage, bonus bike, qualifying-time difficulty, and one unknown/unused bit. | No PPU-select DIP is expected. |
| `vstetris` | Set the PPU selection bits for `RP2C04-0004` before judging color correctness. MAME records VS. Tetris `PPU Type` on SW1:6, SW1:7, and SW1:8, with `RP2C04-0004` represented by the `0xc0` value. | In MAME's active-low DIP notation this appears as SW1:6 ON, SW1:7 ON, SW1:8 OFF for `RP2C04-0004`. Verify against the physical board's ON arrow and document the actual switch positions used. |
| `vsmahjng` | Do not include in the first test. | Expected PPU/color mismatch and possible DualSystem/control assumptions. |

Tetris note: interpretation for `RP2C04-0004` is SW1:6 ON, SW1:7 ON, SW1:8 OFF, must be verified against the DIP bank orientation.

## `RP2C04-0004` candidates for the current cabinet

| Game/path | MAME set name | PPU status for current cabinet | UniSystem posture | Notes | Priority |
|---|---|---|---|---|---|
| VS. Ice Climber | `iceclimb` | Direct `RP2C04-0004` match | Good single-game UniSystem burn-and-test candidate | MAME associates `iceclimb` with `PALETTE_2C04_0004`; standard VS ROM/EPROM workflow still needs exact set verification before burning. | High, friction-first |
| VS. Excitebike, Japan variant | `excitebkj` | Direct `RP2C04-0004` family candidate | Good candidate after exact set verification | MAME's PPU-family notes list Excitebike Japan under `RP2C04-0004`. Treat non-Japan Excitebike variants separately because Excitebike also appears in other PPU contexts. | High, variant-sensitive |
| VS. Tetris | `vstetris` | Compatibility-test candidate with `RP2C04-0004`; not treated as a clean fixed-PPU match | Burn-and-test candidate after direct matches | MAME's PPU-family notes list Tetris under `RP2C04-0001` with a caveat that starred games can work with multiple PPU types when DIP settings match the installed PPU. John's Arcade and PAR/Riemen notes also support multi-PPU behavior for some titles. Validate actual color output on this cabinet. | Medium, test batch |
| VS. Mahjong | `vsmahjng` / Mahjong path | Not a `RP2C04-0004` color match | Low-priority verification candidate only | MAME's PPU-family notes place Mahjong in the `RC2C03B` / `RP2C03B` group. Wrong colors are expected with the current `RP2C04-0004`; single-player and controller-input behavior are explicitly to be verified before being treated as operational guidance. | Low, reference only |

Alternate paths are VS. Ice Climber and the Japan `RP2C04-0004` Excitebike variant. VS. Tetris external notes support multi-PPU/DIP behavior, but it remains a hardware-output validation item rather than a native 0004 claim. Mahjong remains a documented edge case until exact PPU, controls, board behavior, and single-side behavior are verified.

## Platform caveats from external references

- A UniSystem is expected to run one game path at a time.
- Games using 8 or 12 ROMs should be treated as possible DualSystem-only candidates until verified otherwise.
- `RP2C04` PPUs can be physically/functionally interchangeable in some cases, but palette output changes and may be wrong.
- The VS RGB PPU family matters. `2C03`, `2C04`, and `2C05` paths are not interchangeable assumptions.
- Some titles, especially Tetris and Duck Hunt, have looser PPU behavior than a simple one-title/one-PPU rule suggests, so exact board photos, chip markings, DIP settings, and output validation matter.
