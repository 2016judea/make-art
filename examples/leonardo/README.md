# Leonardo — the grounding run for the `leonardo` skill

**2026-09-03.** Four subjects, four of his material modes, generated with
`~/.claude/skills/leonardo/scripts/plate.py` on the make-art engine, each anchored on two or
three of his real sheets. 2K drafts; nothing here has been spent to 4K. The brief was Aidan's:
*"a Leonardo da Vinci persona built on his real work … capable of generating hand-stenciled
drawings/designs in the way that he used to."*

| rank | plate | mode | why it placed here |
|---|---|---|---|
| 1 | `1-city-block-codex.jpg` | codex | The most *his*: a page of thought, not a picture. Ruled plan, lettered lots, compass circle for a cart's turning radius, arithmetic column, a row of houses in the margin, script filling the rest. Two English words leaked ("alley", "cart") — small enough to live with at this stage. |
| 2 | `2-espresso-lever-ink.jpg` | ink | Cutaway boiler, lever at three positions, seal in section, basket from below, the a-b-c force diagram — the sheet logic is right. Second roll; the first wrote "Piston seal" and "Leonardo" in plain English. This one still leaks three half-English labels beside the small studies. Cleaner than his sheets (too finished, too little wash). |
| 3 | `3-sleeping-cat-silverpoint.jpg` | silverpoint | Material fidelity is the best of the four — pink prepared ground, white heightening, placement lines and an abandoned study left faint. Second roll; the first mirrored my own prompt words along the bottom edge. Placed third only because it is a beautiful drawing rather than a working page. |
| 4 | `4-birches-on-the-bluff-chalk.jpg` | chalk | Second roll after the first drew scalloped cartoon foliage; the tone rule fixed it. **Mirrored horizontally** so the engine's right-handed `/` hatching reads as his left-handed `\`; the unflipped plate is in `candidates/`. Still the least Leonardo of the set — his trees are sparer and stranger than this. |

**Why 1 beat 3.** The silverpoint cat is the prettier object. The codex page is the one that
could only be *his* — the thing the skill exists to make. A pretty drawing on old paper is
what every "Renaissance style" prompt produces; a page where the diagram sits inside the
argument is not.

`prompts/` holds each final's prompt exactly as sent (STEM + SUBJECT + NOTES + TAIL, with the
anchor sheets named in the header). `candidates/r1/` keeps the losing rolls — they are the
record of the three failure modes the skill now guards against.
