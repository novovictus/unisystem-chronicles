# VS. Super Mario Bros. ROM Preservation

This document records the installed VS. Super Mario Bros. ROM kit, its observed physical EPROM population, and the procedure for dumping and verifying the original chips with a GQ-4X programmer.

## Installed kit

```text
Game:        VS. Super Mario Bros.
Kit family:  MDS-SM4
Board:       Nintendo MDS-01-CPU
PPU:         RP2C04-0004
PPU marks:   4L3 21
Provenance:  Nintendo of America envelope, shipped January 2000
```

The January 2000 date is from the Nintendo of America shipping envelope. Treat it as service-stock or replacement-kit provenance, not as the original game release date.

## ROM labels and filenames

The six UV EPROMs are labeled with operator-facing dual socket locations. Preserve the printed capitalization and spacing when recording physical labels.

```text
MDS-SM4 1Aor6A
MDS-SM4 1Bor6B
MDS-SM4 1Cor6C
MDS-SM4 1Dor6D
MDS-SM4 2Aor8A
MDS-SM4 2Bor8B
```

Suggested dump filenames preserve label capitalization while replacing spaces with underscores:

```text
MDS-SM4_1Aor6A.bin
MDS-SM4_1Bor6B.bin
MDS-SM4_1Cor6C.bin
MDS-SM4_1Dor6D.bin
MDS-SM4_2Aor8A.bin
MDS-SM4_2Bor8B.bin
```

Expected size for each dump:

```text
8192 bytes / 0x2000
```

## Observed EPROM population

The Nintendo sticker family is consistent, but the six sockets contain mixed manufacturers and part markings. Preserve that mixed population as physical kit provenance.

```text
MDS-SM4 1Aor6A
Manufacturer: Intel
Part:         D2764A
Body marks:   U4120008S; PGM@12.5V; (c)INTEL '83

MDS-SM4 1Bor6B
Manufacturer: Intel
Part:         D2764A-3
Body marks:   U40522725; PGM@12.5V; (c)INTEL '83

MDS-SM4 1Cor6C
Manufacturer: Intel
Part:         D2764A-3
Body marks:   U4052269S; PGM@12.5V; (c)INTEL '83

MDS-SM4 1Dor6D
Manufacturer: Intel
Part:         D2764A-3
Body marks:   U3491199S; PGM@12.5V; (c)INTEL '83

MDS-SM4 2Aor8A
Manufacturer: Mitsubishi
Part:         M5L2764K
Body marks:   8413AM; JAPAN

MDS-SM4 2Bor8B
Manufacturer: Mitsubishi
Part:         M5L2764K
Body marks:   8414A1; JAPAN
```

The first four ROMs are Intel `D2764A` / `D2764A-3` devices. The two `2Aor8A` and `2Bor8B` ROMs are Mitsubishi `M5L2764K` devices. All observed parts are 2764-class 8 KiB UV EPROMs.

Do not erase, blank-check, write, or relabel the original parts before dumping and verifying their contents.

## Equipment and local workspace

- GQ-4X programmer
- GQUSBprg software
- Good USB cable
- ESD-safe work surface
- IC puller or small chip puller
- Masking tape or opaque labels for EPROM windows
- Camera for before/after reference photos
- Local working directory for ROM binaries

Example local working directory:

```text
unisystem-private-dumps/
  raw-read-1/
  raw-read-2/
  manifests/
```

Keep the working ROM files outside the repository or in a path that is explicitly ignored and never committed.

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
6. Mark each chip orientation in the notes. Pin 1 orientation matters.
7. Remove only one ROM at a time unless every socket has already been photographed and mapped.

## GQUSBprg device selection

Use the closest exact manufacturer/device profile available for each physical chip:

```text
MDS-SM4 1Aor6A -> Intel D2764A, or compatible 2764 / 27C64
MDS-SM4 1Bor6B -> Intel D2764A-3, or compatible 2764 / 27C64
MDS-SM4 1Cor6C -> Intel D2764A-3, or compatible 2764 / 27C64
MDS-SM4 1Dor6D -> Intel D2764A-3, or compatible 2764 / 27C64
MDS-SM4 2Aor8A -> Mitsubishi M5L2764K, or compatible 2764 / 27C64
MDS-SM4 2Bor8B -> Mitsubishi M5L2764K, or compatible 2764 / 27C64
```

Expected profile class:

```text
EPROM 2764 / 27C64
8 KiB
DIP-28
```

If the exact manufacturer profile is unavailable, use a compatible 2764 / 27C64 read-only profile and record the exact profile used. Do not use a 27128, 27256, or larger profile for the observed chips; a larger profile can produce extra data that does not match the expected MAME dump shape.

## Read procedure

For each ROM:

1. Open GQUSBprg.
2. Select the GQ-4X programmer.
3. Select the device profile matching that specific physical EPROM.
4. Record the exact profile used.
5. Confirm that the software shows an 8 KiB / `0x2000` device size.
6. Insert the EPROM in the ZIF socket with the correct pin 1 orientation.
7. Lock the ZIF socket.
8. Use `Read` to load the device contents into the buffer.
9. Save the buffer as a binary file using the label-preserving filename.
10. Remove the chip and return it to its original socket or a labeled antistatic-safe location.
11. Repeat for the remaining ROMs.

First-pass output:

```text
raw-read-1/MDS-SM4_1Aor6A.bin
raw-read-1/MDS-SM4_1Bor6B.bin
raw-read-1/MDS-SM4_1Cor6C.bin
raw-read-1/MDS-SM4_1Dor6D.bin
raw-read-1/MDS-SM4_2Aor8A.bin
raw-read-1/MDS-SM4_2Bor8B.bin
```

Perform a second independent read of every chip into `raw-read-2/` using the same filenames and the same per-chip device profile recorded during the first pass.

## Repeated-read verification

Compare each first-pass file byte-for-byte with its second-pass counterpart before comparing against known hashes.

Linux, macOS, or Git Bash examples:

```bash
cmp raw-read-1/MDS-SM4_1Aor6A.bin raw-read-2/MDS-SM4_1Aor6A.bin
cmp raw-read-1/MDS-SM4_1Bor6B.bin raw-read-2/MDS-SM4_1Bor6B.bin
cmp raw-read-1/MDS-SM4_1Cor6C.bin raw-read-2/MDS-SM4_1Cor6C.bin
cmp raw-read-1/MDS-SM4_1Dor6D.bin raw-read-2/MDS-SM4_1Dor6D.bin
cmp raw-read-1/MDS-SM4_2Aor8A.bin raw-read-2/MDS-SM4_2Aor8A.bin
cmp raw-read-1/MDS-SM4_2Bor8B.bin raw-read-2/MDS-SM4_2Bor8B.bin
```

Windows PowerShell or Command Prompt examples:

```powershell
fc /b raw-read-1\MDS-SM4_1Aor6A.bin raw-read-2\MDS-SM4_1Aor6A.bin
fc /b raw-read-1\MDS-SM4_1Bor6B.bin raw-read-2\MDS-SM4_1Bor6B.bin
fc /b raw-read-1\MDS-SM4_1Cor6C.bin raw-read-2\MDS-SM4_1Cor6C.bin
fc /b raw-read-1\MDS-SM4_1Dor6D.bin raw-read-2\MDS-SM4_1Dor6D.bin
fc /b raw-read-1\MDS-SM4_2Aor8A.bin raw-read-2\MDS-SM4_2Aor8A.bin
fc /b raw-read-1\MDS-SM4_2Bor8B.bin raw-read-2\MDS-SM4_2Bor8B.bin
```

No differences means the repeated reads are stable. If any pair differs, clean and reseat the chip, confirm the per-chip device selection, and perform another read before drawing conclusions.

## MAME-style hashes

Generate CRC32 and SHA1 values for each individual 8 KiB dump. Do not combine the six ROMs into one file for initial matching.

Expected output shape:

```text
MDS-SM4_1Aor6A.bin  8192  CRC(1abf053c)  SHA1(f17db88ce0c9bf1ed88dc16b9650f11d10835cec)
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

The known alternate/harder set substitutes only `1Cor6C`:

```text
CRC32: 0011fc5a
SHA1:  5c2c49938a12affc03e64e5bdab307998be20020
```

Identification criteria:

- All six standard hashes match: known MAME `suprmrio` Set E Rev 4.
- Only `1Cor6C` matches the alternate hash: known alternate/harder set.
- Any other mismatch: repeat the dump and verify the read before investigating it as a possible variant.

## Preservation notes

- Keep the first raw reads untouched.
- Perform at least two independent reads per chip.
- Compare repeated reads byte-for-byte before drawing conclusions.
- Keep UV windows covered whenever the chips are not actively being inspected or read.
- Do not peel original labels merely to identify the silicon unless there is a technical reason.
- Use read-only operations on the original EPROMs.
- Return each ROM to the same socket and orientation from which it was removed.
- If the board currently works, make no corrective changes until dump verification and photo documentation are complete.
- Commit only notes, labels, appropriate photos, and MAME-style hash manifests.

## Dump results

Record the completed dump date, GQUSBprg version, exact per-chip device profiles, repeated-read hashes, MAME comparison, and any anomalies here after the physical preservation pass.
