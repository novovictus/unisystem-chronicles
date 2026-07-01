# EPROM Programming Notes

This file records cabinet-specific EPROM handling notes for the Nintendo VS. UniSystem restoration. ROM binaries are not stored in this repository.

## Current EPROM stock, 2026-06-10

A batch of pulled Texas Instruments 27C256-family UV EPROMs and 28-pin machined-pin DIP sockets arrived for the current burn/test workflow.

Observed markings on the EPROMs include variations of:

- `TMS27C256JL`
- `TMS JL 27C256`
- `27C256`
- manufacturing/date/lot codes such as `8745`, `8935`, `9145`, and similar codes
- factory/location markings such as `SINGAPORE`

The parts show visible package/window/marking differences, but the markings are consistent with TI TMS27C256JL-family UV EPROMs. Treat these as the current standard EPROM stock for 27256/27C256-compatible VS ROM socket work unless a chip fails blank check, programming, or verify.

## Practical compatibility posture

For this cabinet workflow, the relevant working assumption is:

```text
TMS27C256JL / 27C256
-> UV-erasable EPROM
-> 32K x 8
-> DIP-28
-> suitable for sockets expecting 27256 / 27C256 devices
```

Use the programmer's TI TMS27C256 profile when available. A generic 27C256 / 27256 profile is the fallback if the programmer does not provide a TI-specific profile.

## UV eraser setup and safety, 2026-06-25

The current UV eraser is a low-cost AY / Patriot-style EPROM eraser being reused for the VS. UniSystem EPROM workflow. Prior use suggests that a nominal 20-minute cycle may not always fully erase older UV EPROMs, so erase time should be treated as an empirical bench variable rather than a guaranteed setting.

Current operating posture:

- Remove all stickers and adhesive residue from the quartz window before erasing.
- Place EPROMs window-up and centered under the UV tube.
- Use a thin makeup compact mirror in the drawer as a non-conductive riser/reflector if it clears the bulb and tray movement.
- Start with a 20-minute erase cycle, then run a programmer blank check.
- If the chip is not blank, repeat in 10-minute increments and blank-check again.
- Avoid unattended long-duration erasing; do not treat hours of UV exposure as a normal troubleshooting step.
- Treat erase success as verified only when the programmer reports a clean blank check.

Peephole/shutter safety posture:

- Do not use the front peephole as an open viewing port.
- Use an opaque metal laptop camera shutter on the outside of the tray door as the primary UV block.
- If used, layered Kapton tape belongs on the inside of the tray door as secondary containment only.
- Do not treat Kapton tape as the primary eye-safety control.
- Treat this as a practical improvement to hobby bench gear, not as a certified UV safety enclosure.

## Socket notes

The received sockets are 28-pin machined-pin DIP sockets. They are appropriate for repeated installation/removal compared with inexpensive leaf sockets, though they are not as convenient as ZIF sockets.

Use sockets as a serviceability improvement where soldering a socket is appropriate and where board originality/preservation concerns have been considered. Avoid unnecessary rework of stable original board areas.

## Burn/test checklist

For each EPROM used in the test batch:

1. Inspect pins and package condition.
2. UV erase if the chip is not known blank.
3. Run a blank check in the programmer.
4. Program using a TMS27C256 or generic 27C256 / 27256 profile.
5. Run a full verify after programming.
6. Apply an opaque label over the quartz window.
7. Label the chip with game/set, socket position, date, and programmer profile if useful.
8. Install only with confirmed notch orientation and correct socket position.
9. On first power-up, watch for immediate abnormal heat, smell, blank raster behavior, or supply distress.

## Documentation boundary

This repository may document EPROM type, socket placement, labels, private file hashes, test results, DIP settings, and cabinet behavior.

Do not commit ROM images, decrypted binaries, or commercial game data.
