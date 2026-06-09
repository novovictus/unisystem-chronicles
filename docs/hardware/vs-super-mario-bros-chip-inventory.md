# VS. Super Mario Bros. EPROM Chip Inventory

This inventory records both the Nintendo sticker text and the physical EPROM body markings observed on the six UV EPROMs in the `MDS-SM4` VS. Super Mario Bros. kit.

No ROM binaries are stored in this repository.

## Board context

```text
Game:        VS. Super Mario Bros.
Kit family:  MDS-SM4
Board:       Nintendo MDS-01-CPU
PPU:         RP2C04-0004
PPU marks:   4L3 21
Provenance:  Nintendo of America envelope, shipped January 2000
```

## Observed EPROM inventory

| Manufacturer | Nintendo sticker | Chip text line 1 | Chip text line 2 | Chip text line 3 | Chip text line 4 | Notes |
|---|---|---|---|---|---|---|
| Intel | `MDS-SM4 1Aor6A` | `D2764A` | `U4120008S` | `PGM@12.5V` | `(c)INTEL '83` | 2764-class UV EPROM |
| Intel | `MDS-SM4 1Bor6B` | `D2764A-3` | `U40522725` | `PGM@12.5V` | `(c)INTEL '83` | 2764-class UV EPROM |
| Intel | `MDS-SM4 1Cor6C` | `D2764A-3` | `U4052269S` | `PGM@12.5V` | `(c)INTEL '83` | 2764-class UV EPROM |
| Intel | `MDS-SM4 1Dor6D` | `D2764A-3` | `U3491199S` | `PGM@12.5V` | `(c)INTEL '83` | 2764-class UV EPROM |
| Mitsubishi | `MDS-SM4 2Aor8A` | `M5L2764K` | `8413AM` | `JAPAN` | `N/A` | 2764-class UV EPROM |
| Mitsubishi | `MDS-SM4 2Bor8B` | `M5L2764K` | `8414A1` | `JAPAN` | `N/A` | 2764-class UV EPROM |

## Programmer profile implication

The observed chip markings are all consistent with 2764-class 8 KiB EPROMs:

```text
Intel D2764A / D2764A-3
Mitsubishi M5L2764K
```

For the GQ-4X workflow, use the closest exact manufacturer/device profile available in GQUSBprg for each chip. If an exact profile is not available, use a compatible 2764 / 27C64 read profile and record the exact profile used in the dump manifest.

Expected dump size for each chip remains:

```text
8192 bytes / 0x2000
```

## Dump filename convention

Preserve the sticker capitalization in filenames while replacing spaces with underscores:

```text
MDS-SM4_1Aor6A.bin
MDS-SM4_1Bor6B.bin
MDS-SM4_1Cor6C.bin
MDS-SM4_1Dor6D.bin
MDS-SM4_2Aor8A.bin
MDS-SM4_2Bor8B.bin
```

## Notes

- The first four ROMs are Intel `D2764A` / `D2764A-3` devices.
- The two `2Aor8A` and `2Bor8B` ROMs are Mitsubishi `M5L2764K` devices.
- The mixed manufacturer population should be preserved in notes because it is part of the physical kit provenance.
- Do not erase, blank-check, write, or relabel these parts before dumping and verifying the ROM contents.
