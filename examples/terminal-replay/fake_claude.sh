#!/bin/bash
# Deterministic replay of a fake Claude Code session beat. All timing scripted.
DIM=$'\e[2m'; RST=$'\e[0m'; ORANGE=$'\e[38;5;209m'; GREEN=$'\e[32m'; CYAN=$'\e[36m'; GRAY=$'\e[38;5;244m'

printf '%s╭──────────────────────────────────────────────────────────────────╮%s\n' "$GRAY" "$RST"
printf '%s│%s > i need to generate some custom AI art, with this as the base   %s│%s\n' "$GRAY" "$RST" "$GRAY" "$RST"
printf '%s│%s   image to start from                                             %s│%s\n' "$GRAY" "$RST" "$GRAY" "$RST"
printf '%s╰──────────────────────────────────────────────────────────────────╯%s\n' "$GRAY" "$RST"
sleep 0.8

# spinner — the Claude Code "thinking" register
frames=('✻' '✢' '·' '✻' '✽' '✻' '✢' '·')
for i in $(seq 0 14); do
  f=${frames[$((i % 8))]}
  printf '\r%s%s Conjuring… %s(%ds · ↓ %d tokens)%s   ' "$ORANGE" "$f" "$DIM" $((i/2)) $((i*312)) "$RST"
  sleep 0.25
done
printf '\r%s✻ Conjuring… done.%s                              \n\n' "$ORANGE" "$RST"
sleep 0.4

printf '%s⏺%s Bash%s(python3 gen_art.py --prompt-file prompts/1-spire.txt --aspect 16:9 --size 4K)%s\n' "$ORANGE" "$RST" "$GRAY" "$RST"
sleep 0.6
printf '  %s⎿%s  wrote plate-1.png  %s(1792×2400 · 35.2s · $0.24)%s\n\n' "$GRAY" "$RST" "$DIM" "$RST"
sleep 0.5
printf '%s⏺%s I generated four plates in the panel'\''s own visual language —\n' "$GREEN" "$RST"
printf '  four vantages of the same sentinel. Ranked: the %sspire%s reads\n' "$CYAN" "$RST"
printf '  strongest at the banner crop.\n\n'
sleep 1.2
printf '%s> %s' "$CYAN" "$RST"
sleep 1.5
