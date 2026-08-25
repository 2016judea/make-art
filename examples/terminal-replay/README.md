# terminal-replay

The heart of a build video is the prompt, typed, in a terminal. Never run the
live agent on camera — API calls make the beat nondeterministic and cost
money. Replay what happened instead:

- `fake_claude.sh` — the session beat as a script: prompt box, spinner, tool
  lines, token counter, all real ANSI, all timing fixed.
- `episode.tape` — VHS types the command at a human cadence and renders the
  replay to mp4 under the phosphor theme. `vhs episode.tape`.

Full pipeline: [../../script-to-video.md](../../script-to-video.md).
