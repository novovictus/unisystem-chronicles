# Chat-Derived Notes

These notes preserve early reasoning from the project discussion. Treat as working notes until verified against hardware photos and hands-on inspection.

## 2A03 identification

`2A03` is not the PPU. It is the Ricoh CPU/APU used in NTSC NES-derived hardware.

The VS. System PPU is a separate Ricoh video chip, commonly marked as an `RP2C04`, `RP2C03B`, or `RP2C05` variant depending on game/board context.

## Current PPU

Reported current PPU:

```text
RP2C04-0004
```

This aligns with the current VS. Super Mario Bros. ROM kit.

## ROM kit and PPU relationship

Nintendo VS. System ROM kits generally need the correct PPU variant to display correct colors. Wrong PPU combinations may boot but typically show incorrect/scrambled colors due to palette differences.

## Cabinet history hypothesis

The cabinet is believed to be:

```text
Donkey Kong Jr. cabinet
-> VS. UniSystem conversion
-> VS. Golf at some point
-> VS. Super Mario Bros. currently
```

The current `RP2C04-0004` likely came with or was installed for the VS. Super Mario Bros. kit. If the cabinet previously ran VS. Golf, it likely had a different PPU at that time.

## Restoration philosophy

- Preserve original boards and harnesses where practical.
- Clean, test, recap/repair as needed.
- Avoid irreversible modern/JAMMA conversion.
- Use reproduction materials only where needed and clearly document what is original versus replacement.

## Immediate technical questions

- Which VS. motherboard revision is installed?
- What ROM daughtercards/edge boards are present?
- Is there evidence of the earlier VS. Golf configuration?
- What is the exact source of speaker hum?
- Which PSU and monitor chassis are installed?
- What cabinet labels/stamps confirm original provenance?
