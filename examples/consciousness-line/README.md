# The Consciousness Line — 2026-07-08

Six plates, 1792x2400 each. 1950s–60s American magazine advertisement illustration
in the Mad Men register — mid-century gouache and airbrush, halftone/offset grain,
idealized aspirational scene — one per compound, each an ordinary post-war moment
that opens into what the drug does.

| plate | the scene |
|---|---|
| `1-psilocybin` | a man home at golden hour, mycelial gold threads running through lawn, walls and people |
| `2-lsd` | an executive at a high office window; the skyline recedes into an infinite fractal blueprint |
| `3-dmt` | behind the wheel of a night coupe; the windshield peels into a jewelled hyperspace lattice |
| `4-mdma` | two people close in a convertible at dusk, their hard edges melting and merging |
| `5-mescaline` | a figure on a terrace facing the desert; mesas and sky become a slow cathedral |
| `6-ketamine` | one figure in an empty Eames interior, weightless, drifting slightly apart from itself |

- `prompts/` — the six prompts as sent. Every one ends "no text, no lettering, no
  words anywhere in the image."
- `plates/` — five of the six finished plates. See below for why the LSD plate is missing.
- `run.sh` — regenerates the set with `../../gen_art.py`. `./run.sh <base-image> 4K`
  for a bigger pass.

The essay these were built for is live:
[The Consciousness Line](https://aidanjude.vercel.app/substack/consciousness-line).

## Why plate 2 isn't here

`2-lsd.png` came back with a signature baked into the lower left: **"© 1962
A.M. Cassandre."** The prompt never asked for it — the model invented it.
Cassandre was a real poster artist (1901–1968), so that reads as a false
attribution to a real person, not a period flourish. The other five plates are
clean; all six corners were checked. The prompt ships; the plate stays out
until it's repainted or regenerated clean.

Check your corners.
