# Script → video

How a written episode becomes a YouTube video on one Mac, with open tools, no
cloud render, and nothing synthetic where the story claims to be real.

Grounded: 2026-08-24 — a six-agent primary-source sweep (licenses and commit
dates read off the repos, policies off the live docs) plus a working VHS proof
render, run to turn ten build-episode scripts into videos. The scripts
themselves were mined from real Claude Code session transcripts — the prompts
in them are quoted as typed.

## The chain

**0 · Script.** One markdown file per episode: hook, the original prompt
verbatim, the build beat by beat, showcase, description box. The script is the
contract — everything below renders it, nothing below edits it.

**1 · Narration — record yourself first.** QuickTime, $0. On a channel whose
premise is "I built this," the real voice is the authenticity asset, and a
builder audience is precisely the audience that smells TTS. The scale lane is
Chatterbox (MIT — weights, cloning, and output all unrestricted) cloning your
own voice via `mlx-audio` on Apple Silicon; adopt it only if it beats your
QuickTime take blind. Its honest value is retake economics: fix one flubbed
sentence without re-recording. Runner-up: Qwen3-TTS (Apache-2.0).

**2 · Timing is audio-first.** `ffprobe` each narration segment's duration and
derive the beat schedule from it — picture conforms to voice, never the
reverse. (The one idea worth taking from the faceless-channel generators,
owed to their shape, not their code.)

**3 · Terminal footage is scripted, not screen-recorded.** VHS
(charmbracelet/vhs, MIT, brew) renders a `.tape` — the verbatim prompt typed at
a controlled cadence, then a deterministic replay script faking the session
output with real ANSI: spinner, tool lines, token counter. Sharp at 1080p and
true 4K under a custom theme. Never run the live agent on camera: API calls
make the beat nondeterministic and cost money — replay what happened, exactly.
Worked example: [`examples/terminal-replay/`](examples/terminal-replay/).
**Trap:** `Set Framerate 30` silently emitted 25fps — render `Output frames/`
PNGs and encode yourself, or retime in ffmpeg.

**4 · Animation segments: a pure canvas `render(t)`.** One function draws the
complete frame for time `t` — no wall clock, no randomness, so `render(3.5)`
is identical forever. Puppeteer screenshots the frames; ffmpeg encodes. Typed
text is `str.slice(0, floor((t-start)*cps))`; counts ease with `easeOut`. QA by
*looking at* downscaled frames at each story beat, not by trusting the code.

**5 · Real footage stays real.** Demos are hand-captured screen recordings.
No stock clips, no generated b-roll, ever: in a video about a real build, a
synthetic clip is a hand-typed number in video form — the footage is the
receipts. The one legitimately synthetic surface is the thumbnail (below),
which is stylized art, not fake evidence.

**6 · Assembly is ffmpeg, not a framework.** Normalize every segment once to a
single mezzanine spec (same codec, resolution, fps, timebase; stills via
`-loop 1 -t N`), then the concat demuxer with `-c copy` — a lossless join in
seconds — and mux narration as its own track. Crossfade (`xfade`/`acrossfade`)
only where a specific cut wants it. Drive it from a JSON edit list through a
small generator script; `filter_complex` is never hand-edited. Why no
framework: every one surveyed re-renders embedded mp4s frame-by-frame through
a browser, turning a seconds-long join into an hours-long render — and the
most mature one is free only up to a three-employee company (see dead ends).

**7 · Captions and chapters.** `mlx_whisper vo.wav --model
mlx-community/whisper-large-v3-turbo --word-timestamps True -f srt` — under a
minute on M-series. Upload the `.srt` as closed captions; don't burn karaoke
captions into narrated long-form (a Shorts aesthetic — keep the word JSON for
canvas-captioned vertical cutdowns). Chapters are plain description lines
generated from the script's beats: first at `00:00`, at least three, each
≥10 s — that's YouTube's own parser contract.

**8 · Thumbnail.** A `gen_art.py` plate (~$0.24 at 4K), type overlaid in
HTML/PIL — the model doesn't render text; same rule as everywhere in this
repo. Export 1280×720 JPEG under the API's 2 MB cap.

**9 · Publish by hand.** YouTube Studio, ~2 minutes per episode with srt,
chapters, and thumbnail attached in one screen. The API path is a trap at
small scale: `videos.insert` from an unverified project uploads **locked
private, permanently** — a locked video can never be flipped public, and the
compliance audit takes weeks and lapses after ~90 idle days. If cadence goes
weekly: file the audit first, then automate (porjo/youtubeuploader, or the
no-audit hybrid — manual upload plus API `thumbnails.set` / `captions.insert`,
which carry no lock).

## Dead ends, with the disqualifying fact

| tool | the fact |
|---|---|
| Remotion | source-available, not open: free ≤3 employees, paid license at #4; embedded video re-renders through Chrome |
| Revideo | MIT but pre-1.0; repo changed owners 2026-07; telemetry on by default |
| HyperFrames | watchlist, not adopt: Apache-2.0, agent-native, 42k stars — but four months old and embedded-video seek unproven frame-accurate |
| Motion Canvas | twenty months without a release; no headless audio path (Revideo forked to add it) |
| MoviePy | every frame through Python — the layer `render(t)` already does, slower |
| F5-TTS | repo says MIT; the **weights** are CC-BY-NC (training data), NC survives fine-tuning; a monetized channel is commercial use. The trap hides on the model card, not the LICENSE file |
| XTTS-v2 | CPML non-commercial; company defunct |
| Dia | 5–20 s generations with voice drift between them — wrong shape for a 7-minute narrator |
| Piper | original repo archived 2025-10; successor GPL-3.0, no cloning — right for a Pi, wrong for narration |
| ffmpeg MCP servers | the category's most-starred ship **no license at all**; the licensed one is 15 months stale. Runner-up if post-production ever hurts: kinocut (Apache-2.0, 2026-08), loaded per-session — 196 tools is real context weight |
| youtube-uploader-mcp | MIT and active, but gated by the same unverified-project lock — only after the audit |
| ShortGPT / MoneyPrinterTurbo / the faceless crop | the architecture exists to fake experience: stock footage + TTS dub. Nothing salvageable but the audio-first timing idea |
| local video-gen (Wan 2.2, LTX-2, Hunyuan) | 82 min per 2-second clip on an M1 Max / Metal failures / a license void in the EU-UK-KR — and editorially banned here regardless |
| WhisperX on macOS | its speed claims are CUDA-only; its own README prescribes `--device cpu`. `mlx-whisper` is the M-series pick |
| termsvg / t-rec / agg | SVG-only / live-window capture at 4–15 fps / GIF's 256-color tax |

## One method note

Two research lanes disagreed on API upload — one read the README, one read
Google's live policy doc and a field report of a permanently locked video. The
deeper primary source won, and that's the rule worth keeping: **verify a
tool's claim against the document that governs it, not the document that
markets it.** Same discipline as reading a license off the weights card, not
the repo badge.
