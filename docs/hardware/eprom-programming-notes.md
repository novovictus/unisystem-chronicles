# EPROM Programming Notes

This file records cabinet-specific EPROM stock, handling, erasing, programming, and bench-tool notes for the Nintendo VS. UniSystem restoration.

## Current EPROM stock and acquisition, 2026-06-10

A batch of pulled Texas Instruments 27C256-family UV EPROMs and 28-pin machined-pin DIP sockets:

- Device family: `27C256` EPROM.
- Organization: `32K x 8`, equal to 256 Kbit.
- Package: `DIP-28`.
- Quantity: 10 pieces.
- Condition: grab bag from various manufacturers, described as pulls that need cleaning and erasing.

Markings on the EPROMs include variations of:

- `TMS27C256JL`
- `TMS JL 27C256`
- `27C256`
- manufacturing/date/lot codes such as `8745`, `8935`, `9145`, and similar codes
- factory/location markings such as `SINGAPORE`

The parts show visible package, window, and marking differences, but the markings are consistent with TI TMS27C256JL-family UV EPROMs.

## UV eraser setup and mods, 2026-06-25 / 2026-07-03

The current UV eraser is an AY / Patriot-style EPROM eraser. Prior use suggests that a 20-minute cycle may not always fully erase EPROMs.

### Tray and reflector experiment sequence

The lower-tray work is being retained as an experiment sequence.

1. Compact-mirror proof of concept: a small makeup/compact mirror was first used as a removable, non-conductive riser and visible-reflection test surface. This validated the value of raising and cleaning up the chip-contact area without placing EPROM legs directly on conductive foil.
2. Cut lower mirror: a second-hand mirror was then cut into a rectangle matching the drawer footprint and installed as a fitted non-conductive tray insert/riser. This provided a clean, flat drawer surface and preserved electrical isolation at the chip-contact layer. It may contribute some secondary reflection, but household mirror construction is not assumed to be optimized for 254 nm UV-C reflection.
3. Aluminum cavity reflector: 3M 3340 aluminum HVAC foil tape was added to recover more of the tube lamp output that would otherwise be absorbed by the plastic shell. The tape lettering was stripped with automotive parts cleaner before installation. Strips were cut to match the inner drawer side wall and top lid area.
4. Alpha Nanotech fused quartz plates were selected for the lower tray. The order expected two plates but arrived as two four-packs, providing additional sacrificial stock. Rather than cutting one 50 x 50 x 1 mm pane down to fit the remaining tray width, the working approach is to let the panes overlap/step and use approximately 1 mm aluminum spacer rails to level and support the elevated pane.
5. Destructive quartz cutting test: a sacrificial 1 mm fused-quartz pane was tested with a diamond blade on a handheld angle grinder. Attempt 1 used water, sacrificial wood, and clamping; the cut area visibly overheated almost immediately and the pane fractured within seconds. Attempt 2 used shorter cut cycles, repeated water spray, and a sandwich of thin fiberboard with a flexible buffer layer on both sides. This produced a mildly clean cut roughly three quarters through the pane before final fracture. Conclusion: handheld angle-grinder cutting is not viable due to heat, blade speed, vibration, pressure, and end-of-cut fragility, which make destruction likely without precision diamond/lapidary tooling and continuous coolant.
6. Bottom foil liner and spacer-rail salvage: the bottom tray was pre-emptively lined with foil, using the mirror pane as a cutting template. Salvaged aluminum cable strands measuring just over 1 mm thick are used as the spacer/support material. Sn60/Pb40 solder was rejected for this application because ordinary electronics solder does not reliably wet aluminum and results in solder blobs or cooked foil-tape adhesive.
7. Final mechanical support is a loose three-piece raft made from the salvaged aluminum strands. One straight edge locks in the bottom quartz pane. Two W-shaped pieces, each with short end legs, support the raised pane, prevent shifting, and add rigidity without overbuilding the tray. The raft is intended to provide distributed line support and anti-shift geometry.
8. External safety labeling: supplemental UV warning labels were made from stock photo source, printed on inkjet vinyl sticker paper, cut to size, and applied externally to improve bench visibility of the hazard.

Material/spec notes:

- 3M 3340 aluminum foil tape: high-temperature HVAC foil tape intended for ductwork sealing, with listing/spec language indicating UL 181A-P / UL 181B-FX style use and a service temperature range of -40 F to 300 F (-40 C to 149 C).
- Alpha Nanotech fused quartz 50 x 50 x 1 mm double-side-polished fused quartz plates. Listing specifications claim heat resistance up to 1450 C, resistance to acid/base/organic solvents, laboratory UV-Vis grade, claimed optical suitability over 190-2500 nm, and transmission above 83%.
- Fused quartz was selected over ordinary mirror glass because it is expected to transmit more of the approximately 254 nm UV-C used for EPROM erasure while still electrically isolating the EPROM legs from the aluminum reflector.

The quartz/aluminum lower tray replaces the cut household mirror as the active chip-contact surface. The compact mirror and cut mirror established the mechanical requirements: fitted tray support, EPROM-leg isolation, cleanable surface, and repeatable placement. The quartz iteration attempts to preserve mechanical benefits while reducing UV-C absorption from ordinary mirror glass.

The reflector work is to improve the UV-C cavity geometry, as a tube lamp emits in multiple directions, while the stock housing wastes much of the upward and sideward output into the shell. Side-wall foil, top-lid foil, and a lower aluminum reflector under fused quartz should redirect some of the otherwise wasted light toward the EPROM tray.

### UV-C card positive-control test, 2026-07-03

A QuantaDose / Quanta X Technology reusable UV-C test card stated germicidal UV-C response ranges, roughly 222-280 nm. The specific card contains fine text stating: `When green UV-C is shown 250-270 nm light is present.`

A positive-control video confirmed the card response with the eraser lamp. The lamp was powered for two seconds and the card showed immediate green fluorescence while on.

Video reference:
- https://youtube.com/shorts/X01eHRtFL3A

### Visible-spectrum and shutter tests, 2026-07-26

A small visible-light spectrometer was used to compare an ordinary LED flashlight, the operating eraser lamp, the peephole with its shutter open and closed, and the same flashlight viewed through the installed Kapton layer. The test was intended to document relative visible-light behavior, not to measure the approximately 254 nm UV-C erasure line.

The timestamped captures in the external photo album record the test sequence:

| Capture | Test | Result |
| --- | --- | --- |
| `20260726_152921.jpg` | LED flashlight control | Broad continuous visible-light response used as the baseline. |
| `20260726_153629.mp4` | Spectrometer pointed inside the operating eraser | Narrow mercury-discharge emission features were visible, distinct from the flashlight control. |
| `20260726_153951.jpg` | Peephole open | Detectable visible lamp output and narrow emission features reached the spectrometer through the open peephole. |
| `20260726_154316.jpg` | Peephole closed | The trace dropped to the baseline/no-detectable-output condition, confirming that the external metal shutter blocks the visible path. |
| `20260726_155028.jpg` | Same flashlight covered by Kapton | The response remained visible but was noticeably reduced and altered relative to the uncovered flashlight control. This provides a repeatable, instrument-visible demonstration that the Kapton layer filters some visible light. |

The eraser-lamp spectrum is consistent with a mercury-discharge source because it presents narrow visible emission features rather than the broad continuous response of the white LED flashlight. Exact wavelength labels from the inexpensive spectrometer are treated as approximate and are not used as a lamp calibration.

The flashlight comparison establishes measurable filtering in the visible range: the same source remained detectable through the Kapton, but with a noticeably different and attenuated response. This does not quantify Kapton transmission at 254 nm. UV-C safety evidence remains the separate QuantaDose card result, while the metal slider remains the primary opaque shutter.

### Peephole/shutter safety posture

The stock peephole is treated as a raw UV-C viewing path. The design problem is spectral separation of the hazardous shortwave UV-C, while the operator only needs a visible lamp-on indication.

Kapton tape is installed on the inside of the tray door as a filter containment layer. The metal laptop camera slider on the outside of the tray door is the primary opaque shutter. For a brief status check, the shutter can be opened, allowing a muted visible lamp-on glow without relying on a direct raw UV-C sightline.

The value of the Kapton layer is not simply that it is an electrical insulator. It is used as a thin, thermally tolerant, translucent filter layer that measurably attenuates and alters the visible-light path while still passing enough longer-wavelength glow as a status indicator. Its transmission at the approximately 254 nm erasure wavelength has not been quantitatively measured.

For the peephole test, the shutter window was opened so that only the Kapton layer remained in the sightline. The QuantaDose card was positioned near the peephole and observed by camera. A green ambient glow from the filter was visible, but the card's UV-C indicator did not glow. A baseline photo of the card outside exposure shows its normal appearance and confirms that the positive-control response remained distinguishable from the ambient green glow.

### Cord and strain-relief refurbishment

- The original cheap power cord was desoldered and the original grommet removed.
- The cord entry hole was drilled to fit a new 3/8-inch grommet, a donor cord from the bench stash was soldered in, and wiring was rerouted and secured with Kapton tape.

Photo and video reference:

- External Google Photos album: https://photos.app.goo.gl/2X9sLU1n8wPv37jN6