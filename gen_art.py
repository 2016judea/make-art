#!/usr/bin/env python3
"""
GLEAN art engine — Nano Banana Pro (Gemini 3 Pro Image) via the Gemini REST API.
Zero deps (stdlib only). Key is read from the GEMINI_API_KEY env var, or a .env beside this file.

Usage:
  python3 gen_art.py --prompt-file prompt.txt --out plate.png --aspect 3:2 --size 4K
  python3 gen_art.py --prompt "a lone figure at a black hole's edge..." --out p.png
  python3 gen_art.py --image base.png --prompt "..." --out ad.png   # base-anchored (edit/compose)
"""
import argparse, base64, json, os, sys, urllib.request, urllib.error, pathlib

MODEL = "gemini-3-pro-image-preview"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"

def load_key():
    if os.environ.get("GEMINI_API_KEY"):
        return os.environ["GEMINI_API_KEY"]
    env = pathlib.Path(__file__).parent / ".env"
    if env.exists():
        for line in env.read_text().splitlines():
            if line.startswith("GEMINI_API_KEY"):
                return line.split("=", 1)[1].strip().strip('"').strip("'")
    sys.exit("Set GEMINI_API_KEY (env var, or GEMINI_API_KEY=... in a .env beside gen_art.py)")

def main():
    ap = argparse.ArgumentParser()
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--prompt")
    src.add_argument("--prompt-file")
    ap.add_argument("--image", action="append", default=[])  # base image(s) to anchor/edit around
    ap.add_argument("--out", required=True)
    ap.add_argument("--aspect", default="3:2")   # 3:2 ~ full spread; 3:4 ~ single page
    ap.add_argument("--size", default="4K")       # 1K / 2K / 4K  (uppercase required)
    args = ap.parse_args()

    if args.prompt_file and not pathlib.Path(args.prompt_file).is_file():
        sys.exit(f"--prompt-file {args.prompt_file}: no such file")
    prompt = args.prompt or pathlib.Path(args.prompt_file).read_text()
    if not prompt.strip():
        sys.exit("the prompt is empty")
    for img in args.image:
        if not pathlib.Path(img).is_file():
            sys.exit(f"--image {img}: no such file")
    parts = []
    for img in args.image:
        p = pathlib.Path(img)
        ext = p.suffix.lower()
        mime = "image/png" if ext == ".png" else "image/webp" if ext == ".webp" else "image/jpeg"
        parts.append({"inlineData": {"mimeType": mime, "data": base64.b64encode(p.read_bytes()).decode()}})
    parts.append({"text": prompt})
    body = {
        "contents": [{"parts": parts}],
        "generationConfig": {
            "responseModalities": ["IMAGE"],
            "imageConfig": {"aspectRatio": args.aspect, "imageSize": args.size},
        },
    }
    req = urllib.request.Request(
        URL, data=json.dumps(body).encode(),
        headers={"Content-Type": "application/json", "x-goog-api-key": load_key()},
    )
    try:
        resp = json.load(urllib.request.urlopen(req, timeout=180))
    except urllib.error.HTTPError as e:
        sys.exit(f"HTTP {e.code}\n{e.read().decode()[:2000]}")

    parts = resp.get("candidates", [{}])[0].get("content", {}).get("parts", [])
    for p in parts:
        blob = p.get("inlineData") or p.get("inline_data")
        if blob and blob.get("data"):
            pathlib.Path(args.out).write_bytes(base64.b64decode(blob["data"]))
            print(f"wrote {args.out}  ({blob.get('mimeType', blob.get('mime_type','?'))})")
            return
    sys.exit("No image in response:\n" + json.dumps(resp, indent=2)[:2000])

if __name__ == "__main__":
    main()
