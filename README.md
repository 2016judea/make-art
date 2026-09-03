# make-art

One Python file, and a skill that teaches Claude Code to art-direct it.

The engine is Gemini 3 Pro Image ("Nano Banana Pro") over the REST API. No SDK,
no dependencies — `gen_art.py` is stdlib only. Native output up to 4K, ~35
seconds a plate, about $0.24 each.

## Quickstart

```bash
export GEMINI_API_KEY=...            # or GEMINI_API_KEY=... in a .env beside gen_art.py
python3 gen_art.py --prompt "..." --out plate.png --aspect 3:4 --size 2K
python3 gen_art.py --image base.png --prompt "..." --out out.png   # edit/compose around a base
```

`--aspect`: `1:1 2:3 3:2 3:4 4:3 4:5 5:4 9:16 16:9 21:9` · `--size`: `1K / 2K / 4K` (uppercase).
Draft at 2K, spend 4K when it's right.

## The two things that will bite you

1. **The model renders text unreliably.** Generate a text-free image and lay the
   type on yourself (HTML→screenshot, or PIL). End every prompt with *"no text,
   no lettering, no words anywhere in the image."*
2. **It invents borders — and worse.** A pale riso frame, a dark slide mount,
   and once a signature: *© 1962 A.M. Cassandre*, a real poster artist, forged
   onto a plate nobody asked him to sign. Probe the edges, check the corners,
   before anything ships.

## The skill

[`skill/SKILL.md`](skill/SKILL.md) is the working Claude Code skill, verbatim.
Drop it in `~/.claude/skills/make-art/` (with `gen_art.py` in `scripts/`) and
Claude drives the engine itself — picks aspect and size, writes the prompt,
probes the border. [`skill/image-riff.md`](skill/image-riff.md) is the method
layer on top: one reference image → a spread of original plates in its own
visual language.

Both files reference paths and albums from the machine they live on. That's the
point — a skill is harvested from real sessions, not authored in the abstract.
Adapt the paths, keep the rules.

## The example: The Consciousness Line

Six prompts, one per compound — 1950s magazine advertising in the Mad Men
register, each an ordinary post-war moment opening into what the drug does.
[`examples/consciousness-line/`](examples/consciousness-line/). Five plates
included; the LSD plate is the one the model signed, and it stays out until
it's repainted. The prompts are the interesting part anyway.

The essay these were made for: [The Consciousness Line](https://aidanjude.vercel.app/substack/consciousness-line).

## The persona: Leonardo

[`skill/leonardo.md`](skill/leonardo.md) is a third layer on the same engine: a fixed visual
language with six material modes — pen and ink, a codex page, red chalk, silverpoint on a
prepared ground, tempera on linen, the Deluge — each measured off two or three of Leonardo's
real sheets and anchored on them at generation time. The full skill folder (the fifteen
public-domain anchor sheets, his notebooks complete in Richter's arrangement, the prompt
STEMs, and `plate.py`) lives in the Claude config; this copy is the method. The grounding
run — four subjects, the losing rolls, and the three engine failures they exposed (it mirrors
your own prompt as "mirror script"; it hatches right-handed; it draws cartoon foliage) — is
in [`examples/leonardo/`](examples/leonardo/).

## From script to video

Plates are half the studio. [`script-to-video.md`](script-to-video.md) is the
other half: the full open-tool chain that turns a written episode into a
YouTube video on one Mac — narration, deterministic terminal footage
([`examples/terminal-replay/`](examples/terminal-replay/)), canvas animation,
ffmpeg assembly, captions, publish. Every choice carries its why; every
rejected tool carries its disqualifying fact.

## Contributing

Issues and PRs welcome. Useful directions: the border/luminance probe as a
standalone script, more worked examples with their full prompt sets, ports of
the skill to other agent harnesses.

## License

Code MIT. Plates and prompts CC BY 4.0.
