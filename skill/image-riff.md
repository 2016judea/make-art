---
name: image-riff
description: Turn one or more reference images into original art in that reference's own visual language — then cut it to whatever surface it's for. Use when Aidan pastes or points at art and says "use this as the base image", "generate art from this", "riff on this", "do more of that YouTube channel art thing", "some creative ideation with these images", "make me a channel banner / avatar / cover / plate", "wilder version of this", or wants a spread of options off one piece of reference. This is the TASK skill; the engine is the `make-art` tool skill.
grounded: 2026-08-24 — the Madisen Avenue Instagram icon, 3 rounds, where the full-size ranking inverted at 44px (and 2026-08-21, the four plates that became the live banner + avatar on youtube.com/@bricks_journalism, shipping verified 2026-08-24)
---

# image-riff — original art in a borrowed visual language

The engine, its API key, its flags and its gotchas live in the **`make-art`** skill.
Read that first and don't restate it here. This skill is the *method* that produced
the Brick & Mortar YouTube channel art: how to turn a reference image into a set of
real options, and how to land them on the surface they're actually for.

**Done** is not four pretty images. Done is: N plates generated, every frame looked
at, ranked with honest critique, **the destination crops cut**, and the work landed in
**both** places below. A run that stops at "here are four images" hands him the last
two jobs — that is exactly what happened on 2026-08-21 and he finished it by hand
inside YouTube's uploader.

## Where the work lands — both places, every run, no exceptions

His instruction, 2026-08-24: *"update the skill to save all new art work to this
folder so i can go thru it. And to always make a new album on iphoto too … so i can
access it from my phone."* Two destinations because he uses two devices for two
different things: he **reviews** on the Mac in Finder and he **uses** the asset on the
phone (setting a profile picture, a wallpaper, posting). Delivering to only one is a
half-delivery, and a scratchpad is not a destination — it gets swept.

### 1. A source folder on disk

```
~/Desktop/workspace/art/<source-slug>/
  README.md                 dated title, the brief, a rank → plate table, and WHY the pick won
  1-<slug>.jpg …            the finals, full-resolution masters, numbered BY RANK
  upload-1024/              the actual sized deliverables, when the surface needs a specific size
  small-size-test.png       the proof, when legibility at size decided it
  prompts/                  the finals' prompts exactly as sent
  candidates/<round>/       the rounds that lost, each with its own prompts/
```

`<source-slug>` is the body of work, not the date — `madisen-avenue`,
`youtube-channel`, `july-2026-consciousness-line`. **This convention already exists;
match it, don't reinvent it** — read a sibling folder before writing a new one.

Rules, with their reasons:

- **The README is not optional.** He goes through this folder cold, weeks later, by
  eye. Without it a folder of numbered JPEGs can't tell him which one shipped, which
  one he rejected, or why. It must carry the rank table and the one paragraph
  explaining why the pick beat the prettier plate.
- **Keep the losing rounds.** `candidates/` is where the reusable knowledge is — the
  round-two Madisen plates are the only record of what a vignette does to a mark at
  44px. Deleting them keeps the folder tidy and throws away the lesson.
- **Keep the prompts verbatim.** They're the reproduction instructions and the
  provenance. Copy the files as sent; don't paraphrase them into the README.
- **Number the finals by rank, not by generation order.** The filename is where the
  ranking survives after the conversation is gone.

### 2. A new album in Photos, named for the source

Always a **new** album — never append to an existing one — named the same as the
source, with the ranked finals imported in rank order on sequential timestamps so
the album's own order *is* the ranking:

```bash
osascript -e 'tell application "Photos" to make new album named "Madisen Avenue"'
S=/Users/aidan/.claude/skills/apple-photos/scripts/photos.py
python3 $S import --file "$P/1-throat.jpg"  --album "Madisen Avenue" --date "August 24, 2026 3:10:01 PM"
python3 $S import --file "$P/2-arch.jpg"    --album "Madisen Avenue" --date "August 24, 2026 3:10:02 PM"
```

- `photos.py` has **no create verb** — its `import` uses `into album "NAME"` and fails
  if the album doesn't exist. Create it with the `osascript` line first. (Forward
  reference: the `apple-photos` skill.)
- **Get the names right before importing.** You cannot script-delete a photo from an
  album — that's a verified Photos limitation, not a missing flag — so a badly-named
  import is permanent until he fixes it by hand.
- The precedent for both halves is the Madisen Avenue run (2026-08-24) and the
  `Bricks Reels` album before it.

## Ask two questions, then spend

At ~$0.24 per 4K image, a four-plate spread is ~$1 — cheap enough that two questions
is the whole gate, expensive enough that zero questions is a waste. Both answers
change every plate, so neither can be inferred:

1. **What is it for?** Decides aspect, and whether to leave negative space for type.
2. **How far from the base?** Faithful reproduction ↔ wild reinterpretation.

On 2026-08-21 he answered *standalone art piece* and *wilder reinterpretation*, which
is why the four went to full-bleed composition with no type-safe zone. Guessing either
would have produced four wrong plates. Back-reference:
`[[feedback_ask_before_creative_style]]` — ask on the subjective axis, decide the
technical one yourself.

## The prompt is three parts, and only one of them varies

This is the reproducible core. Build it in code, one file per subject:

```
STEM   (identical for every plate)  — the rendering language, read off the image
SUBJECT (the only variable)         — one paragraph, one composition
TAIL   (identical for every plate)  — geometry + the negatives
```

The STEM that worked, verbatim, as a template of the *moves* rather than the words:

> Use the attached image strictly as the style and colour anchor. Reproduce its exact
> rendering language: **‹period + medium›**, **‹how colour is laid down›**, **‹line
> behaviour›**, **‹texture / shading technique›**, **‹named pigments, 2–3 max, plus the
> small accent›**, **‹what the light does›**. **Do NOT copy the subject of the attached
> image. Compose something new.**
>
> SUBJECT:

And the TAIL:

> ‹aspect› composition, full bleed edge to edge. No border, no frame, no paper texture,
> no white margin. No text, no lettering, no signature, no logo.

**A photographic base is an UNPROVEN case — probe at 2K before spending on a spread.**
Everything in this skill is grounded on one run against a *stylized* comic panel, where
"reproduce the rendering language, change the subject" necessarily yields art. Tried
against a 35mm photograph on 2026-08-24 (`seen-from-above`), the method executed
perfectly — both gate questions answered, four genuinely distinct vantages, clean
delivery — and Aidan rejected all four: *"these were interesting, but didnt like them
that much."* He gave no reason, so none is recorded as method here. The mechanical
lesson stands and the creative one does not: **ask a third question when the base is a
photograph — *should this end up looking like a photograph, or like something else?* —
and spend one or two 2K plates before four 4K ones.** Reproducing a photograph's
rendering language may simply not be a creative act; the variable might have to be the
medium itself. See `[[feedback_photographic_base_riff_missed]]`.

**When the base is a photograph, the STEM's slots change but its job doesn't.** Those
slots above describe mark-making, and a photograph has none. Swap them for the six things
a camera actually decides — *‹stock + format›, ‹shadow response›, ‹quality and angle of
light›, ‹palette, 3–4 named colours plus the one accent›, ‹grain / halation / vignette›,
‹what it is NOT›*. The last slot matters more here than with an illustration, because the
engine's default for any photographic prompt is contemporary digital: say *no HDR, no
lifted shadows, no digital clarity, no cinematic teal-and-orange grade* or you get all
four. Grounded 2026-08-24 on a 35mm garden snapshot — `seen-from-above`, where **"deep
crushed blacks that hold no shadow detail at all"** was the single most load-bearing
clause, and the one plate that ignored it is the one that drifted into travel stock.

Also: read the base for its **implied subject**, not just its rendering. That photograph's
real subject was *a private place, seen from above, with nobody in it* — empty loungers,
implied people, no permission. Naming that in one sentence before writing any SUBJECT is
what keeps a spread coherent, and `no people visible anywhere in the frame` belongs in the
TAIL as an invariant when it does.

Why it's built this way, rule by rule:

- **The image carries the style; the STEM only has to name what is visibly there.**
  Describe the mark-making you can actually see — *hard black contour lines of varying
  weight, visible ben-day halftone dot shading, airbrushed mechanical blends only, no
  photographic light*. Naming the technique is what stops the model modernising it.
  Don't write art history you can't see in the frame.
- **"Do NOT copy the subject… compose something new" is load-bearing.** Without it a
  base-anchored gen returns a variation of the base. With it, all four came back as
  original compositions still speaking the base's language — and the best of them
  *quoted* the base (the panel's machine head reappeared as a half-buried wreck)
  rather than repeating it. That quote is the good case, and you get it by forbidding
  the copy, not by asking for the quote.
- **Name pigments, and cap the accent.** The base was cobalt/ultramarine + cadmium
  yellow with *small* magenta star-flares. On the one plate where the accent wasn't
  held down, magenta and violet took the whole frame into blacklight-poster territory.
  Say "small" and say it about the accent specifically.
- **The negatives are not boilerplate.** The engine adds a paper/riso border on its own
  initiative; `make-art` documents this. Four negatives in the TAIL cost nothing and
  none of the four plates came back framed.
- **Identical STEM + TAIL is what makes the set comparable.** Every difference you see
  between plates is a difference you asked for. Vary two things at once and you can't
  tell which one worked.

## The subjects must be VANTAGES, not decorations

The single most important creative decision, and the reason this run is worth
repeating. Four subjects that differ in *where the camera is*:

| plate | vantage | what it is |
|---|---|---|
| spire | looking straight **up** a vertical axis | machine cathedral out of a cloud sea, narrowing into perspective |
| wreck | looking **across** an empty plain | half-buried armoured wreck, one wing up, tiny robed figure walking to it |
| descent | looking steeply **down** through cloud | ocean of armour plate to a curved horizon, one winged figure falling away |
| mandala | looking **at** pure pattern, no horizon | symmetrical biomechanical rosette, corner to corner |

**Why vantage and not subject matter:** the two plates that shipped shipped *for their
vantage*. The vertical one is the banner because a vertical column survives a letterbox
crop; the wide-horizon one is the avatar because a square crop wants one readable
silhouette against sky. Four plates that differ only in furniture all crop the same way
— that's one option in four costumes. Give each plate a different relationship to scale
and you get four genuinely different answers.

Also: one idea per plate. Every subject above is a single sentence of situation plus a
single sentence of scale. Nothing has two ideas in it.

## Rank against the brief — then say which one each SURFACE wants

Two separate orderings, and giving only the first is the failure this skill exists to
prevent.

On 2026-08-21 I ranked the spire **4 of 4** and wrote that it was "the weakest —
contemporary digital comic, not 1977 Métal Hurlant, the halftone nearly gone." That
plate is the live channel banner. Rank #1, the desert wreck, is the live avatar. The
rank order was correct about fidelity to the base and **completely silent about use** —
and use is what he was choosing for.

So: rank honestly and name the one that drifted (`[[feedback_rank_the_creative_set]]`),
then add one line per destination surface saying which plate that surface wants and why
the crop makes it so. A low rank is not a veto; it's one axis.

## Cut the crops. Every surface has a geometry.

Deliver files sized for the destination, not source plates. The measurement below is off
the live channel on 2026-08-24, not from documentation:

**YouTube channel banner** — you upload one 16:9 image; YouTube serves a different slice
per device.

- Stored / TV: **2560×1441**.
- Desktop strip: **2560×424** — the vertical **middle 29.4%** of the image (top 35.3% →
  bottom 64.7%). Everything that must be seen lives in that band.
- So: a subject filling the frame's vertical centre survives; a subject sitting high or
  low in the frame is simply absent on desktop. This is the whole reason the "weakest"
  plate won.
- The spire banner is a full-width 16:9 crop out of a 3072×5504 vertical plate — a 9:16
  plate has ~3.1× more height than a 16:9 crop needs, so there is a lot of freedom in
  where you take the band. Pick the band, don't accept the middle by default.

**Channel avatar** — square, served from 900×900 down to **88×88**. Judge the candidate
at 88px, not at full size: silhouette and one colour contrast are all that survive.

To read either back (WebFetch cannot read a YouTube channel page — see
`[[reference_youtube_channel_and_video_ids]]`):

```bash
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"
curl -sL -A "$UA" "https://www.youtube.com/@bricks_journalism" | grep -o '"banner".\{0,400\}'
# the fcrop64 hex is four 16-bit fractions of 0xffff: left, top, right, bottom
python3 -c "h='00005a57ffffa5a8'; print([round(int(h[i:i+4],16)/0xffff,4) for i in range(0,16,4)])"
```

For other surfaces, measure the same way before cropping — read the real served asset,
don't trust a remembered spec sheet.

## Mechanics that cost time on the real run

- **A pasted base image is not on disk.** Extract it from the session transcript's
  base64 — `make-art` has the snippet and the list of three places that come back empty.
  Then `Read` it before spending a 4K gen on the wrong image.
- **Generate the spread in parallel**, one Bash call per plate, `dangerouslyDisableSandbox: true`
  (the sandbox blocks the API). Four 4K plates land in ~2 minutes.
- **`--out foo.png` can write a JPEG.** Check the printed mime and rename, or every
  downstream tool lies about the format.
- **Look at every frame yourself before he does** (`[[feedback_qa_while_waiting]]`), and
  probe for the paper border rather than eyeballing it: asymmetric near-white edge runs
  are sky or cloud hitting the bleed, not a frame. `make-art` carries the numbers from
  the run where I nearly cropped 720px of legitimate cloud away.
- **Delivery is the two destinations at the top of this skill** — the source folder and a
  new Photos album — not a scratchpad path in a message.

## When there is no base image

The same three-part prompt works with no anchor at all — the STEM becomes a house style you
*define* rather than one you read off a panel, and everything else is unchanged. Give it a
thematic anchor from his own material so it isn't generic: `the-upward-glance` (his hand-picked
quotes — aspiration, Atlas, the first man who made fire, "the higher we soar…") is the one he
reaches for, and he'll say so. Read it, then let the quotes choose the subjects.

## Icons and avatars: the small-size test is the only test

Grounded 2026-08-24, the Madisen Avenue profile icon. Three rounds, and the ranking **inverted
between full size and real size** — the same law as the YouTube banner, now with a second
instance. Do not skip this.

- **Build the contact sheet before you have an opinion.** Downscale each candidate to its true
  render size, circle-crop it the way the app does, then nearest-neighbour upscale so you can see
  what actually survives:

```python
from PIL import Image, ImageDraw
for s in (110, 44, 32):                      # IG: profile / DM row / feed+story ring
    small = Image.open(f"{n}.jpg").convert("RGB").resize((s, s), Image.LANCZOS)
    mask = Image.new("L", (s*4, s*4), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, s*4-1, s*4-1), fill=255)
    out = Image.new("RGB", (s, s), (245, 245, 247))
    out.paste(small, (0, 0), mask.resize((s, s), Image.LANCZOS))
    out.resize((s*5, s*5), Image.NEAREST).save(f"{n}_{s}.png")   # NEAREST = see the pixels
```

- The most beautiful plate of round two — a brass head thrown back on oxblood, genuinely
  gorgeous at 110px — was an **unreadable brown smear at 44px**. It would have been the pick off
  a full-size review.
- **Instagram geometry:** upload square (1024×1024 is the proven size here — see
  `[[reference_brand_assets]]`), rendered as a **circle**, at roughly 110px on the profile, 44px
  in a DM row, 32px in a feed or story ring. Judge at 32.

**Four constraints that made the difference, all of them invisible at full size:**

1. **Three flat colours, and no more.** Every extra colour is a mid-tone, and mid-tones merge.
2. **Nothing thinner than 1/40 of the frame.** Say it in the prompt as a number. Fine deco
   rule-lines and hairline keylines dissolve completely; the round where the arch bands were
   "at least a twelfth of the frame" is the round that survived.
3. **The emblem must fill ≥85% of the width.** State it in caps. Left to itself the engine
   centres a modest mark in a lot of empty ground, which is fatal when the whole thing is 32px.
4. **The hot colour belongs to the GROUND, not to a glint.** A specular highlight is worth
   nothing at 32px. A full flat field of hot magenta is what stops a thumb. "Sexy" came from the
   curve and the palette — not from gloss; every metallic-sheen instruction read as mud when
   shrunk.

## Two things the engine adds on its own initiative

Both cost a round on 2026-08-24 and both are one line to prevent:

- **Never mention the circle crop in the prompt.** Telling it "this image will be cropped to a
  circle" makes it *draw the circle* — two of four round-one plates came back with a white
  circular mask or clipped octagonal corners baked into the art. Say instead: *"flat unbroken
  ground runs all the way to all four edges of the square; the emblem is contained well within
  the central three quarters."* Then put `no circle, no ring, no roundel, no enclosing shape` in
  the TAIL negatives.
- **It adds a radial vignette unless forbidden.** A dark corner falloff is nearly invisible at
  full size and lethal small — it is exactly the figure-ground contrast the mark needs. Demand
  *"every fill absolutely flat — no gradient, no vignette, no radial darkening at the corners
  or edges."*

## Never credit the base image

The 2026-08-21 base was a comic panel Aidan pasted; he calls its author "the artist of
the sentinel," a Spanish artist. **The prompt's "Métal Hurlant / Moebius tradition" was
a style description I wrote, not an attribution** — do not let it become a credit
downstream. If a credit is going anywhere public, ask him for the name. A wrong credit
on a real artist is worse than a blank; same rule as `[[annotate-inspo]]`.

## More than one base image

`gen_art.py --image` is repeatable, so multiple anchors are possible — **untested here;
the real run used exactly one.** If you try it, say in the prompt which image supplies
what ("image 1 is the colour and line language; image 2 is the structure") rather than
attaching two and hoping, and treat the first spread as a probe.

## See also

**`brand-direction-plates`** — the inverse spread, for a real business's brand design:
several LANGUAGES across one subject rather than one language across several subjects.
Also carries the artefact-photo trap and the heritage-trademark rule. ·
`make-art` (the engine, the flags, the paste-extraction, the border probe) ·
`apple-photos` (album delivery) · `city-reel` + `reel-render` (where Bricks vertical
plates end up) · `[[journal_2026_08_21_channel_art_from_a_base_panel]]` (the run this
came from, with the four prompts as shipped).
