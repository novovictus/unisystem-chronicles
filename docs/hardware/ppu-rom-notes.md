# PPU and ROM Notes

## Key clarification

`2A03` is not the PPU.

`RP2A03` / `2A03` is the Ricoh CPU/APU used in NTSC NES-derived hardware. It contains the 6502-derived CPU core and audio functionality. Video output is handled by a separate PPU.

For Nintendo VS. System hardware, the PPU is typically a separate 40-pin Ricoh chip marked with names such as:

- `RP2C04-0001`
- `RP2C04-0002`
- `RP2C04-0003`
- `RP2C04-0004`
- `RP2C03B`
- `RP2C05-xx`

## Current observed PPU

Current PPU reported in this cabinet:

```text
RP2C04-0004
```

This is consistent with a VS. Super Mario Bros. installation.

## Why PPU matching matters

On Nintendo VS. System, the game ROM set and PPU are effectively paired.

The `RP2C04` PPUs use different RGB palette mappings. A game may boot with the wrong PPU, but colors will usually be wrong because the palette mapping does not match the ROM set's expectations.

Practical rule:

- Correct PPU: game displays with intended colors.
- Wrong PPU: game may run but colors are scrambled/incorrect.
- Some games also use other board/security expectations, so PPU is not always the only variable.

## Current working hypothesis

The cabinet appears to have followed this path:

```text
Donkey Kong Jr. orange Nintendo cabinet
-> VS. UniSystem conversion
-> VS. Golf / Stroke & Match Golf at some point
-> VS. Super Mario Bros. ROM kit with RP2C04-0004
```

VS. Golf / Stroke & Match Golf is commonly associated with a different `RP2C04` variant than VS. Super Mario Bros. If this cabinet truly ran VS. Golf before Mario, the PPU was likely swapped when the Mario kit was installed.

## Documentation rule

Do not commit ROM images. For private preservation, document labels, board positions, checksums, and dump metadata only.
