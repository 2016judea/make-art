#!/usr/bin/env bash
# The Consciousness Line — generate all six base-anchored ad creatives.
# Usage: ./run.sh /path/to/base-image.png   [1K|2K|4K]
set -euo pipefail
BASE="${1:?pass the base image path}"
SIZE="${2:-2K}"
HERE="$(cd "$(dirname "$0")" && pwd)"
ENGINE="$HERE/../../gen_art.py"
mkdir -p "$HERE/out"
for f in "$HERE"/prompts/*.txt; do
  name="$(basename "$f" .txt)"
  echo "== $name =="
  python3 "$ENGINE" --image "$BASE" --prompt-file "$f" \
    --out "$HERE/out/$name.png" --aspect 3:4 --size "$SIZE"
done
echo "done -> $HERE/out/"
