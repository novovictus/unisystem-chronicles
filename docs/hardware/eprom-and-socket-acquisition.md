# EPROM and Socket Acquisition Notes

This file tracks ordered consumables for Nintendo VS. UniSystem ROM preservation, EPROM programming, and repeated ROM handling.

ROM images and commercial game binaries must not be committed to this repository. This file documents physical parts, handling workflow, and validation notes only.

Scope: this note is limited to the current VS. UniSystem board-side DIP-28 workflow.

## Ordered parts

### 27C256 EPROM test stock

Ordered item:

```text
Major Brands GB233 27C256 EPROM Grab Bag
32K x 8 DIP-28
Quantity: 10 pieces
Condition: used pulls / mixed manufacturers
Preparation required: clean and UV erase before use
Amazon listing price at order review: about $15.64 per 10-pack
ASIN: B0CWJ2HQMD
```

Relevant listing details captured from the order review:

- Device family: `27C256` EPROM.
- Organization: `32K x 8`, equal to 256 Kbit.
- Package: `DIP-28`.
- Quantity: 10 pieces.
- Condition note: grab bag from various manufacturers, described as pulls that need cleaning and erasing.
- Use posture: cheap test/programming stock, not trusted archival stock until individually validated.

Risk notes:

- Mixed manufacturers and mixed access speeds are possible.
- Some chips may arrive programmed, dirty, stickered, bent, solder-contaminated, or dead.
- Review evidence on the listing was mixed, ranging from mostly usable batches to completely failed batches.
- Treat every chip as unknown until it passes read, erase, blank-check, program, verify, and post-rest verification.

### 28-pin wide DIP sockets

Ordered item:

```text
uxcell 10pcs DIP IC Chip Socket Adaptor
Pitch: 2.54 mm / 0.1 inch
Row spacing: 15.24 mm / 0.6 inch
Pins: 28
Pin style: round pin listing, through-hole solder type
Quantity: 10 pieces
Amazon listing price at order review: about $9.99 per 10-pack
ASIN: B07H3SHH6K
```

Relevant listing details captured from the order review:

- Board-side ROM socket target: 28-pin wide DIP footprint.
- Pitch: 2.54 mm / 0.1 inch.
- Row-to-row spacing: 15.24 mm / 0.6 inch.
- Package content: 10 sockets.
- Intended use: solder socket to PCB, then insert/remove ICs without repeatedly soldering the chip itself.

Use posture:

- Suitable candidate for board-side socket replacement where repeated ROM removal is expected.
- Preferred over ZIF sockets for the installed arcade PCB because it is lower profile and mechanically less intrusive.
- ZIF sockets remain bench-jig tooling, not a preferred installed-board modification.

## Handling workflow

For every acquired 27C256 EPROM:

```text
1. Photograph top markings before cleaning.
2. Record manufacturer, speed marking, visible condition, and any label/window state.
3. Remove stickers or opaque labels from the quartz window.
4. Clean package and pins with appropriate electronics-safe process.
5. Inspect and straighten pins before insertion into programmer or board socket.
6. Read current contents if possible and record whether read succeeds.
7. UV erase for 20 to 30 minutes.
8. Blank-check in programmer.
9. If not blank, repeat UV erase and blank-check.
10. Program only after a clean blank-check.
11. Verify immediately after programming.
12. Let the programmed EPROM sit overnight if practical.
13. Verify again before installing in the VS. UniSystem board.
14. Label the programmed EPROM clearly with title, ROM position, checksum, date, and source set notes.
```

## Cabinet-specific policy

- Preserve and dump the current VS. Super Mario Bros. ROM set before swapping parts.
- Do not use original Nintendo mask ROMs or known-good historical EPROMs as repeated test consumables.
- Use the ordered 27C256 parts as expendable burn/test stock.
- Keep failed, marginal, slow, or inconsistent EPROMs physically separated from validated parts.
- Keep final game kits labeled as sets by title, socket position, PPU requirement, and board configuration.
- Do not commit ROM binary data to this repository.

## Validation fields to record later

Create a chip inventory table once the parts arrive:

| ID | Manufacturer | Marking | Speed | Initial read | Erase result | Program result | Verify result | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EPROM-001 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| EPROM-002 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| EPROM-003 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| EPROM-004 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| EPROM-005 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| EPROM-006 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| EPROM-007 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| EPROM-008 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| EPROM-009 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| EPROM-010 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |

Socket inventory to record later:

| ID | Package | Pin count | Pitch | Row spacing | Installed location | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| SOCKET-001 | DIP wide | 28 | 2.54 mm | 15.24 mm | TBD | TBD |
| SOCKET-002 | DIP wide | 28 | 2.54 mm | 15.24 mm | TBD | TBD |
| SOCKET-003 | DIP wide | 28 | 2.54 mm | 15.24 mm | TBD | TBD |
| SOCKET-004 | DIP wide | 28 | 2.54 mm | 15.24 mm | TBD | TBD |
| SOCKET-005 | DIP wide | 28 | 2.54 mm | 15.24 mm | TBD | TBD |
| SOCKET-006 | DIP wide | 28 | 2.54 mm | 15.24 mm | TBD | TBD |
| SOCKET-007 | DIP wide | 28 | 2.54 mm | 15.24 mm | TBD | TBD |
| SOCKET-008 | DIP wide | 28 | 2.54 mm | 15.24 mm | TBD | TBD |
| SOCKET-009 | DIP wide | 28 | 2.54 mm | 15.24 mm | TBD | TBD |
| SOCKET-010 | DIP wide | 28 | 2.54 mm | 15.24 mm | TBD | TBD |
