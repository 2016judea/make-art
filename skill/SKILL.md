---
name: make-art
description: Generate original AI art / images (backgrounds, plates, illustrations, wallpapers, composites) via the Gemini "Nano Banana Pro" image API — the same engine GLEAN uses. Use whenever Aidan wants to create, generate, or edit an image/plate/background/wallpaper/illustration, or compose art around an existing image. NOT for charts/dataviz.
grounded: 2026-08-21 — four 9:16 4K plates anchored on a pasted Moebius panel, delivered ranked to the Bricks Reels album (engine itself dates to 2026-07-15)
---

# make-art — Aidan's working AI-image engine

The engine is **Nano Banana Pro = Gemini 3 Pro Image** (`gemini-3-pro-image-preview`) via the Gemini REST API. A zero-dependency, stdlib-only wrapper lives at `scripts/gen_art.py` (in this skill folder). It reads `GEMINI_API_KEY` from `~/Desktop/bricks/.env`. Native output up to 4K, ~35s per image, ~$0.24 per 4K image.

**Do NOT use the local `mflux` / Z-Image path** — that was an abandoned experiment (removed 2026-07-15). This API engine is the real one.

## Two hard gotchas
1. **Sandbox must be OFF.** The Bash sandbox blocks DNS/network, so the API call fails. Run any `gen_art.py` invocation with the sandbox disabled (`dangerouslyDisableSandbox: true`).
2. **Bake text in HTML/PIL, not the prompt.** The model renders text unreliably. Generate a *text-free* image, then overlay type yourself (HTML→screenshot, or PIL) so it stays crisp. Always add "no text, no lettering" to prompts meant to carry an overlay.

## Usage
```bash
python3 scripts/gen_art.py --prompt "…" --out plate.png --aspect 3:2 --size 4K
python3 scripts/gen_art.py --prompt-file p.txt --out plate.png --aspect 9:16 --size 4K
python3 scripts/gen_art.py --image base.png --prompt "…" --out out.png   # anchor/edit around a base image (repeatable --image)
```
- `--aspect`: `1:1 2:3 3:2 3:4 4:3 4:5 5:4 9:16 16:9 21:9`. Phone wallpaper → `9:16`; magazine spread → `3:2`; single page → `3:4`.
- `--size`: `1K` / `2K` / `4K` (uppercase). `4K` for print/wallpaper; `2K` to save cost on drafts.
- Returns a JPEG or PNG (check the printed mime). For wallpaper, cover-crop to the exact device size afterward.

## When the base image is a paste, not a file

`--image` needs a path, but an image Aidan pastes into the conversation **is not on disk** — it
lives only as base64 in the session transcript. Don't search `~/Downloads`, `~/Desktop`, or the
`claude-cli-nodejs` caches; all three come back empty. Extract it:

```python
import json, base64, pathlib
p = pathlib.Path.home() / ".claude/projects/<slug>/<sessionId>.jsonl"   # slug e.g. -Users-aidan-Desktop-bricks
for line in p.open():
    for blk in (json.loads(line).get("message") or {}).get("content") or []:
        if isinstance(blk, dict) and blk.get("type") == "image":
            src = blk["source"]
            pathlib.Path("base.jpg").write_bytes(base64.b64decode(src["data"]))
```

Then `Read` the extracted file to confirm you got the right one before spending a 4K gen on it.
See the `claude-usage-mining` skill for the transcript layout this relies on.

## Prompt craft
- Name the medium + palette up front and keep it consistent across a set. GLEAN house style: *"35mm film photograph, visible film grain, muted sun-faded palette of ochre and dusty blue, soft natural light, analog imperfection, contemplative, vertical."* GLEAN print plates instead use: *bone paper, near-black ink, a single `#e8542b` accent, risograph texture, flat full-bleed*.
- For overlay-friendly backgrounds: ask for **deep negative space** where the text will sit, dark/low-contrast zones, and a single light source / light-leak for interest.
- Vary a pool by shifting time-of-day, weather, motif (sea, dunes, fog, rain, night stars, double-exposure, abstract light field) while holding the palette — gives variety without a unique gen per item.
- **Full-bleed warning:** the model likes to add a light "paper/riso frame" border (especially when you say "poster", "risograph", or "paper texture"). If you want edge-to-edge art (wallpapers), either omit those words or trim/overscan-crop the border afterward — see the `quote-wallpapers` skill's `_trim_border()`.
  **Don't trim on a visual hunch — probe it.** Measure the run inward from all four
  edges. A real frame is *uniform* on all four sides; wildly asymmetric runs (2026-08-21:
  166px bottom on one plate, 720px right on another) are *art* — cloud, snow, sky —
  legitimately hitting the bleed, and cropping it destroys the composition.
  **Probe luminance, not whiteness — the frame is not always pale.** A near-white test is
  blind to the dark "slide mount" border the model also likes, and will report a framed
  plate clean at L0 R0 T0 B0. Threshold on `0.299R+0.587G+0.114B` at both ends (`<42` and
  `>238`), sample three lines per edge and take the **median** so a patch of legitimate
  art-black doesn't fool one scanline, then apply the same uniform-vs-asymmetric test:

  ```
  p1-well      DARK run  L132  R1264  T0   B848   asymmetric -> art (crushed shade)
  p4-blocks    DARK run  L97   R83    T84  B86    UNIFORM    -> real frame, crop it
  ```

  Grounded 2026-08-24, four 3:2 photographic plates: all four passed the near-white probe,
  one had a rounded-corner dark slide mount ~85–97px on every side. Crop the **max plus
  clearance** for the corner rounding (150px worked), then restore the aspect ratio — a
  symmetric crop off a 3:2 frame is no longer 3:2. Note the TAIL negatives *"no border, no
  frame, no film strip, no sprocket holes, no white margin"* did **not** prevent it; the
  model appears to read those as being about pale borders only.

See also the `image-riff` skill — the TASK method built on this engine: turning a reference image into a
spread of original plates (the invariant-STEM / varying-SUBJECT / invariant-TAIL prompt, subjects chosen as
vantages, honest ranking, and cutting the destination crops). Grounded on the run that made the Brick &
Mortar YouTube banner and avatar.

Also the `glean-art-engine` and `quotes-db` memories, and the `glean-issue` skill (which uses this engine for issue plates).