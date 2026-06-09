# VS. Super Mario Bros. ROM Kit State

This note records the current known state of the VS. Super Mario Bros. kit installed in the UniSystem board. It is based on direct board inspection, photo review, and the per-chip EPROM inventory captured from the kit. No ROM binaries are stored in this repository.

## Current identification

```text
Game:        VS. Super Mario Bros.
Kit family:  MDS-SM4
Board:       Nintendo MDS-01-CPU
PPU:         RP2C04-0004
PPU marks:   4L3 21
Provenance:  Nintendo of America envelope, shipped January 2000
```

The January 2000 date is from the Nintendo of America shipping envelope. Treat it as service-stock or replacement-kit provenance, not as the original game release date.

## ROM labels

The six UV EPROMs are labeled with operator-facing dual socket locations. Preserve the printed capitalization and spacing when recording physical labels.

```text
MDS-SM4 1Aor6A
MDS-SM4 1Bor6B
MDS-SM4 1Cor6C
MDS-SM4 1Dor6D
MDS-SM4 2Aor8A
MDS-SM4 2Bor8B
```

Suggested dump filenames, preserving the label capitalization while avoiding spaces:

```text
MDS-SM4_1Aor6A.bin
MDS-SM4_1Bor6B.bin
MDS-SM4_1Cor6C.bin
MDS-SM4_1Dor6D.bin
MDS-SM4_2Aor8A.bin
MDS-SM4_2Bor8B.bin
```

## Physical EPROM population

The kit is not populated with six identical EPROM devices. The current observed population is:

| Sticker | Manufacturer | Chip body marking |
|---|---|---|
| `MDS-SM4 1Aor6A` | Intel | `D2764A`, `U4120008S`, `PGM@12.5V`, `(c)INTEL '83` |
| `MDS-SM4 1Bor6B` | Intel | `D2764A-3`, `U40522725`, `PGM@12.5V`, `(c)INTEL '83` |
| `MDS-SM4 1Cor6C` | Intel | `D2764A-3`, `U4052269S`, `PGM@12.5V`, `(c)INTEL '83` |
| `MDS-SM4 1Dor6D` | Intel | `D2764A-3`, `U3491199S`, `PGM@12.5V`, `(c)INTEL '83` |
| `MDS-SM4 2Aor8A` | Mitsubishi | `M5L2764K`, `8413AM`, `JAPAN` |
| `MDS-SM4 2Bor8B` | Mitsubishi | `M5L2764K`, `8414A1`, `JAPAN` |

See [`vs-super-mario-bros-chip-inventory.md`](vs-super-mario-bros-chip-inventory.md) for the dedicated per-chip inventory.

## Expected MAME-style hashes

Use MAME convention for comparison: CRC32 and SHA1 per ROM chip dump. Do not hash a combined set file for initial matching.

Expected dump size for each chip:

```text
8192 bytes / 0x2000
```

Known `suprmrio` / VS. Super Mario Bros. Set E Rev 4 hashes:

| Label | Size | CRC32 | SHA1 |
|---|---:|---|---|
| `MDS-SM4 1Dor6D` | 8192 | `be4d5436` | `08162a7c987f1939d09bebdb676f596c86abf465` |
| `MDS-SM4 1Cor6C` | 8192 | `5e3fb550` | `de4494e4dd52f7f7b04cf1d9019fd89fb90eaca9` |
| `MDS-SM4 1Bor6B` | 8192 | `b1b87893` | `8563ceaca664cf4495ef1020c07179ca7e4af9f3` |
| `MDS-SM4 1Aor6A` | 8192 | `1abf053c` | `f17db88ce0c9bf1ed88dc16b9650f11d10835cec` |
| `MDS-SM4 2Bor8B` | 8192 | `42418d40` | `22ab61589742cfa4cc6856f7205d7b4b8310bc4d` |
| `MDS-SM4 2Aor8A` | 8192 | `15506b86` | `69ecf7a3cc8bf719c1581ec7c0d68798817d416f` |

Known alternate/harder-set difference:

| Label | Size | CRC32 | SHA1 |
|---|---:|---|---|
| alternate `MDS-SM4 1Cor6C` | 8192 | `0011fc5a` | `5c2c49938a12affc03e64e5bdab307998be20020` |

Matching rule:

```text
All six match the main table
  -> standard known MAME suprmrio set

Only 1Cor6C differs and matches CRC32 0011fc5a / SHA1 5c2c49938a12affc03e64e5bdab307998be20020
  -> known alternate/harder set

Any other mismatch
  -> redump first, then investigate
```

## Dumping notes

- Keep the first raw reads untouched.
- Perform at least two independent reads per chip.
- Compare repeated reads byte-for-byte before drawing conclusions.
- Keep ROM windows covered except when required by the programmer workflow.
- Do not commit ROM images or reconstructed game binaries to this repository.
- Commit only notes, labels, photos where appropriate, and MAME-style hash manifests.
