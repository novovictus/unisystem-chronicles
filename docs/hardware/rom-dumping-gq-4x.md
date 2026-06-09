# ROM Dumping Instructions: GQ-4X

This procedure is for dumping the six UV EPROMs from the VS. Super Mario Bros. `MDS-SM4` kit using a GQ-4X programmer. It is written for preservation and verification only. Do not commit ROM images or reconstructed game binaries to this repository.

## Target ROM set

Current known board state:

```text
Game:        VS. Super Mario Bros.
Kit family:  MDS-SM4
Board:       Nintendo MDS-01-CPU
PPU:         RP2C04-0004
PPU marks:   4L3 21
```

ROM labels to preserve exactly in notes:

```text
MDS-SM4 1Aor6A
MDS-SM4 1Bor6B
MDS-SM4 1Cor6C
MDS-SM4 1Dor6D
MDS-SM4 2Aor8A
MDS-SM4 2Bor8B
```

Suggested local dump filenames:

```text
MDS-SM4_1Aor6A.bin
MDS-SM4_1Bor6B.bin
MDS-SM4_1Cor6C.bin
MDS-SM4_1Dor6D.bin
MDS-SM4_2Aor8A.bin
MDS-SM4_2Bor8B.bin
```

Expected size per dump:

```text
8192 bytes / 0x2000
```

## Equipment

- GQ-4X programmer
- GQUSBprg software
- Good USB cable
- ESD-safe work surface
- IC puller or small chip puller
- Masking tape or opaque labels for EPROM windows
- Camera for before/after reference photos
- Local working directory outside the repository for ROM binaries

Example local working directory:

```text
unisystem-private-dumps/
  raw-read-1/
  raw-read-2/
  manifests/
```

Do not place this directory inside the Git repository unless it is explicitly ignored and never committed.

## Before removing chips

1. Power the cabinet down and unplug it.
2. Photograph the board before touching the ROMs.
3. Photograph the ROM labels close-up.
4. Record the PPU text:

```text
RP2C04
0004
4L3 21
```

5. Confirm the EPROM windows are covered.
6. Mark each chip orientation in your notes. Pin 1 orientation matters.
7. Remove only one ROM at a time unless you have already photographed and mapped every socket.

## Observed per-chip EPROM inventory

Each socket position may contain a different manufacturer or EPROM device even when the Nintendo sticker family is consistent. Record both the Nintendo sticker text and the actual chip body marking for every ROM before choosing the GQUSBprg device profile.

Current observed devices:

| Socket label | Sticker text | Manufacturer | Chip body part number | Additional body marks | Expected GQUSBprg profile class | Notes |
|---|---|---|---|---|---|---|
| 1A or 6A | `MDS-SM4 1Aor6A` | Intel | `D2764A` | `U4120008S`; `PGM@12.5V`; `(c)INTEL '83` | Intel `D2764A` or compatible `2764` / `27C64` | 8 KiB UV EPROM |
| 1B or 6B | `MDS-SM4 1Bor6B` | Intel | `D2764A-3` | `U40522725`; `PGM@12.5V`; `(c)INTEL '83` | Intel `D2764A-3` or compatible `2764` / `27C64` | 8 KiB UV EPROM |
| 1C or 6C | `MDS-SM4 1Cor6C` | Intel | `D2764A-3` | `U4052269S`; `PGM@12.5V`; `(c)INTEL '83` | Intel `D2764A-3` or compatible `2764` / `27C64` | 8 KiB UV EPROM |
| 1D or 6D | `MDS-SM4 1Dor6D` | Intel | `D2764A-3` | `U3491199S`; `PGM@12.5V`; `(c)INTEL '83` | Intel `D2764A-3` or compatible `2764` / `27C64` | 8 KiB UV EPROM |
| 2A or 8A | `MDS-SM4 2Aor8A` | Mitsubishi | `M5L2764K` | `8413AM`; `JAPAN` | Mitsubishi `M5L2764K` or compatible `2764` / `27C64` | 8 KiB UV EPROM |
| 2B or 8B | `MDS-SM4 2Bor8B` | Mitsubishi | `M5L2764K` | `8414A1`; `JAPAN` | Mitsubishi `M5L2764K` or compatible `2764` / `27C64` | 8 KiB UV EPROM |

Do not assume all six chips are the same silicon. Use the chip body part number when selecting the programmer profile. If the exact manufacturer profile is not available in GQUSBprg, use a compatible 2764 / 27C64 read-only profile and record the exact profile used.

## Device selection

The observed chips are all 2764-class 8 KiB UV EPROMs:

```text
Intel D2764A
Intel D2764A-3
Mitsubishi M5L2764K
```

Use the closest exact manufacturer/device profile available in GQUSBprg for each chip:

```text
MDS-SM4 1Aor6A -> Intel D2764A, or compatible 2764 / 27C64
MDS-SM4 1Bor6B -> Intel D2764A-3, or compatible 2764 / 27C64
MDS-SM4 1Cor6C -> Intel D2764A-3, or compatible 2764 / 27C64
MDS-SM4 1Dor6D -> Intel D2764A-3, or compatible 2764 / 27C64
MDS-SM4 2Aor8A -> Mitsubishi M5L2764K, or compatible 2764 / 27C64
MDS-SM4 2Bor8B -> Mitsubishi M5L2764K, or compatible 2764 / 27C64
```

Expected read profile class:

```text
EPROM 2764 / 27C64
8 KiB
DIP-28
```

Do not use a 27128, 27256, or larger profile for these observed chips. A larger profile can produce extra data that is not the expected MAME dump shape.

## GQUSBprg read procedure

For each ROM:

1. Open GQUSBprg.
2. Select the GQ-4X programmer.
3. Select the device profile matching that specific physical EPROM, using the observed inventory above.
4. Record the exact device profile used in the per-chip inventory.
5. Confirm the software shows an 8 KiB / `0x2000` device size.
6. Insert the EPROM in the ZIF socket with correct pin 1 orientation.
7. Lock the ZIF socket.
8. Use `Read` to read the device into the buffer.
9. Save the buffer as a binary file using the label-preserving filename.
10. Remove the chip and return it to its original socket or a labeled antistatic-safe location.
11. Repeat for the remaining ROMs.

First pass output:

```text
raw-read-1/MDS-SM4_1Aor6A.bin
raw-read-1/MDS-SM4_1Bor6B.bin
raw-read-1/MDS-SM4_1Cor6C.bin
raw-read-1/MDS-SM4_1Dor6D.bin
raw-read-1/MDS-SM4_2Aor8A.bin
raw-read-1/MDS-SM4_2Bor8B.bin
```

Then perform a second independent read of every chip into `raw-read-2/` using the same filenames and the same per-chip device profile recorded during the first pass.

## Verification workflow

After two complete read passes, compare each first-pass file to the corresponding second-pass file.

Linux/macOS/Git Bash example:

```bash
cmp raw-read-1/MDS-SM4_1Aor6A.bin raw-read-2/MDS-SM4_1Aor6A.bin
cmp raw-read-1/MDS-SM4_1Bor6B.bin raw-read-2/MDS-SM4_1Bor6B.bin
cmp raw-read-1/MDS-SM4_1Cor6C.bin raw-read-2/MDS-SM4_1Cor6C.bin
cmp raw-read-1/MDS-SM4_1Dor6D.bin raw-read-2/MDS-SM4_1Dor6D.bin
cmp raw-read-1/MDS-SM4_2Aor8A.bin raw-read-2/MDS-SM4_2Aor8A.bin
cmp raw-read-1/MDS-SM4_2Bor8B.bin raw-read-2/MDS-SM4_2Bor8B.bin
```

Windows PowerShell example:

```powershell
fc /b raw-read-1\MDS-SM4_1Aor6A.bin raw-read-2\MDS-SM4_1Aor6A.bin
fc /b raw-read-1\MDS-SM4_1Bor6B.bin raw-read-2\MDS-SM4_1Bor6B.bin
fc /b raw-read-1\MDS-SM4_1Cor6C.bin raw-read-2\MDS-SM4_1Cor6C.bin
fc /b raw-read-1\MDS-SM4_1Dor6D.bin raw-read-2\MDS-SM4_1Dor6D.bin
fc /b raw-read-1\MDS-SM4_2Aor8A.bin raw-read-2\MDS-SM4_2Aor8A.bin
fc /b raw-read-1\MDS-SM4_2Bor8B.bin raw-read-2\MDS-SM4_2Bor8B.bin
```

No differences means the repeated reads are stable. If any file differs between reads, clean and reseat the chip, confirm the per-chip device selection, and perform another read before comparing against MAME hashes.

## MAME-style hash generation

Use the repository helper:

```bash
python tools/hash_mame_roms.py /path/to/unisystem-private-dumps/raw-read-1/
```

Expected output shape:

```text
MDS-SM4_1Aor6A.bin          8192 CRC(1abf053c) SHA1(f17db88ce0c9bf1ed88dc16b9650f11d10835cec)
```

MAME convention uses CRC32 and SHA1 per ROM chip dump. Do not combine the six ROMs into a single file for initial matching.

## Expected hashes

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

## Preservation manifest

Commit only a manifest, not ROM files. Suggested manifest path after dumping:

```text
docs/hardware/vs-super-mario-bros-dump-manifest.md
```

Suggested manifest fields:

```text
Dump date:
Programmer: GQ-4X
Software: GQUSBprg, version unknown unless recorded
Board: Nintendo MDS-01-CPU
PPU: RP2C04-0004, marking 4L3 21
ROM label:
Socket label:
Sticker text:
Chip body manufacturer:
Chip body part number:
Chip body speed/date/lot marks:
Device profile used:
Filename:
Read pass 1 CRC32:
Read pass 1 SHA1:
Read pass 2 CRC32:
Read pass 2 SHA1:
MAME match:
Notes:
```

## Handling notes

- Keep UV windows covered whenever the chips are not actively being inspected.
- Do not peel original labels just to identify the silicon unless there is a technical reason.
- Do not write, blank-check, erase, or program these EPROMs.
- Use read-only operations only.
- Return each ROM to the same socket orientation it came from.
- If the board currently works, make no corrective changes until after dump verification and photo documentation are complete.
