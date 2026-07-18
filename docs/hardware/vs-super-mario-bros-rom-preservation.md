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
