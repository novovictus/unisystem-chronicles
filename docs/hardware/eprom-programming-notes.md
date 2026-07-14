# EPROM Programming Notes

This file records cabinet-specific EPROM handling notes for the Nintendo VS. UniSystem restoration. ROM binaries are not stored in this repository.

## Current EPROM stock, 2026-06-10

A batch of pulled Texas Instruments 27C256-family UV EPROMs and 28-pin machined-pin DIP sockets for the current erase/burn/test workflow.

Observed markings on the EPROMs include variations of:

- `TMS27C256JL`
- `TMS JL 27C256`
- `27C256`
- manufacturing/date/lot codes such as `8745`, `8935`, `9145`, and similar codes
- factory/location markings such as `SINGAPORE`

The parts show visible package/window/marking differences, but the markings are consistent with TI TMS27C256JL-family UV EPROMs. These are the current standard EPROM stock for 27256/27C256-compatible VS ROM socket work unless a chip fails blank check, programming, or verify.

## Practical compatibility posture

The relevant working assumption is:

```text
TMS27C256JL / 27C256
-> UV-erasable EPROM
-> 32K x 8
-> DIP-28
-> suitable for sockets expecting 27256 / 27C256 devices
```

Use the programmer's TI TMS27C256 profile, generic 27C256 profile is the fallback if the programmer does not provide a TI-specific profile.

## UV eraser setup and safety, 2026-06-25 / 2026-07-03

The current UV eraser is a low-cost AY / Patriot-style EPROM eraser being reused for the workflow. Prior use suggests that a nominal 20-minute cycle may not always fully erase older UV EPROMs, so erase time should be treated as an empirical bench variable rather than a guaranteed setting.

The tool has been refurbished and modified for safer, more repeatable bench use. This is a practical hobby-bench improvement, not a certified UV safety enclosure.

### Operating baseline

- Remove all stickers and adhesive residue from the quartz window before erasing.
- Start with a 20-minute erase cycle, then run a programmer blank check.
- Treat erase success as verified only when the programmer reports a clean blank check.

### Tray and reflector experiment sequence

The lower-tray work is being retained as an experiment sequence.

1. Compact-mirror proof of concept: a small makeup/compact mirror was first used as a removable, non-conductive riser and visible-reflection test surface. This validated the value of raising and cleaning up the chip-contact area without placing EPROM legs directly on conductive foil.
2. Cut lower mirror: a second-hand mirror was then cut into a rectangle matching the drawer footprint and installed as a fitted non-conductive tray insert/riser. This provided a clean, flat drawer surface and preserved electrical isolation at the chip-contact layer. It may contribute some secondary reflection, but household mirror construction is not assumed to be optimized for 254 nm UV-C reflection.
3. Aluminum cavity reflector: 3M 3340 aluminum HVAC foil tape was added to recover more of the tube lamp output that would otherwise be absorbed by the plastic shell. The tape lettering was stripped with automotive parts cleaner before installation to leave a cleaner reflective surface. Strips were cut to match the inner drawer side-wall height, and a full piece was used to line the top lid area.
4. Fused-quartz lower tray iteration: Alpha Nanotech fused quartz plates were selected for the lower tray. The order expected two plates but arrived as two four-packs, providing additional sacrificial stock. Rather than cutting one 50 x 50 x 1 mm pane down to fit the remaining tray width, the working approach is to let the panes overlap/step and use approximately 1 mm aluminum spacer rails to level and support the elevated pane.
5. Destructive quartz cutting test: a sacrificial 1 mm fused-quartz pane was tested with a diamond blade on a handheld angle grinder. Attempt 1 used water, sacrificial wood, and clamping; the cut area visibly overheated almost immediately and the pane fractured within seconds. Attempt 2 used shorter cut cycles, repeated water spray, and a sandwich of thin fiberboard with a flexible buffer layer on both sides. This produced a mildly clean cut roughly three quarters through the pane before final fracture. Conclusion: handheld angle-grinder cutting is not part of the working process for these panes. Heat concentration, blade speed, vibration, pressure control, and end-of-cut fragility make destruction likely without precision diamond/lapidary tooling and continuous coolant.
6. Bottom foil liner and spacer-rail salvage: the bottom tray was pre-emptively lined with foil, using the glass pane as a cutting template. Salvaged aluminum cable strands measuring just over 1 mm thick are used as the spacer/support material. Sn60/Pb40 solder was rejected for this application because ordinary electronics solder does not reliably wet aluminum and solder blobs or cooked foil-tape adhesive would create uneven supports and contamination risk.
7. Three-piece aluminum raft: the final mechanical support is a loose three-piece raft made from the salvaged aluminum strands. One straight edge locks in the bottom quartz pane. Two W-shaped pieces, each with short end legs, support the raised pane, prevent shifting, and add rigidity without overbuilding the tray. The raft is intended to provide distributed line support and anti-shift geometry.
8. External safety labeling: supplemental UV warning labels were made from stock-photo source material, printed on inkjet vinyl sticker paper, cut to size, and applied externally to improve bench visibility of the hazard.

Material/spec notes recorded from product listings at time of selection:

3M 3340 aluminum foil tape: selected as a high-temperature HVAC foil tape intended for ductwork sealing, with listing/spec language indicating UL 181A-P / UL 181B-FX style use and a service temperature range of -40 F to 300 F (-40 C to 149 C). In this eraser it is being used as a reflective aluminum surface, not as a structural safety component or certified UV enclosure material.
Alpha Nanotech fused quartz plates: selected as 50 x 50 x 1 mm double-side-polished fused quartz plates. Listing spec  for the plates claimed heat resistance up to 1450 C, resistance to acid/base/organic solvents, and dimensional variation within 0.10 mm for industrial grade and 0.05 mm for laboratory UV-Vis grade with claimed optical suitability over 190-2500 nm with transmission above 83%.
These vendor-stated material specifications are not independent measurements with the assumption that fused quartz is a better lower-tray insulator than ordinary mirror glass because the useful EPROM-erasing wavelength is in the shortwave UV-C region around 254 nm.

The quartz/aluminum lower tray replaces the cut household mirror as the active chip-contact surface but does not invalidate the earlier mirror experiments. The compact mirror and cut mirror established the mechanical requirements: fitted tray support, EPROM-leg isolation, cleanable surface, and repeatable placement. The quartz iteration attempts to preserve those mechanical benefits while reducing the UV-C absorption penalty expected from ordinary mirror glass.

Current quartz-fit: do not cut the fused quartz. The accepted bench approach is overlap/step geometry with a loose aluminum raft supporting the raised pane.

The reflector work is intended to improve the UV-C cavity geometry. A tube lamp emits in multiple directions, while the stock housing wastes much of the upward and sideward output into the shell. Side-wall foil, top-lid foil, and a lower aluminum reflector under fused quartz should redirect some of the otherwise wasted light toward the EPROM tray. Expected improvement is a meaningful gain.

### Peephole/shutter safety posture

The stock peephole is treated as a raw UV-C viewing path. The design problem is spectral separation of the hazardous  erasing energy, which is shortwave UV-C, while the operator only needs a visible lamp-on indication.

Kapton tape is installed on the inside of the tray door as a filter containment layer. The metal laptop camera slider on the outside of the tray door is the primary opaque shutter. For a brief status check, the shutter can be opened allowing a muted visible lamp-on glow without relying on a direct raw UV-C sightline.

The value of the Kapton layer is not simply that it is an electrical insulator, it is being used as a thin, thermally tolerant, translucent filter layer that attenuates the UV-C sightline while still passing enough longer-wavelength visible glow to act as a status indicator.

### Cord and strain-relief refurbishment

- The original cheap power cord was desoldered and original grommet removed.
- The cord entry hole was drilled to fit a new 3/8-inch grommet, a donor cord from the bench stash was soldered in, and wiring was rerouted and secured with Kapton tape.

Photo reference:

- External Google Photos album: https://photos.app.goo.gl/2X9sLU1n8wPv37jN6
