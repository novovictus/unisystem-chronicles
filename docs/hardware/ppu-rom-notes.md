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
