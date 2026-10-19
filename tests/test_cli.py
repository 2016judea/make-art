"""gen_art.py must refuse bad arguments with a message, before any key is read or any
request is made. Each case here used to be a traceback (2026-10-18). No network."""
import os, subprocess, sys
from pathlib import Path

ENGINE = Path(__file__).resolve().parents[1] / "gen_art.py"
# a key in the environment must not be reachable by these runs
ENV = {k: v for k, v in os.environ.items() if k != "GEMINI_API_KEY"}


def run(*args):
    return subprocess.run([sys.executable, str(ENGINE), *args], capture_output=True, text=True, env=ENV)


def test_no_prompt_is_a_usage_error_not_a_traceback():
    r = run("--out", "/tmp/x.png")
    assert r.returncode == 2 and "Traceback" not in r.stderr and "--prompt" in r.stderr


def test_missing_prompt_file_is_named():
    r = run("--prompt-file", "/nonexistent/p.txt", "--out", "/tmp/x.png")
    assert r.returncode == 1 and "Traceback" not in r.stderr and "/nonexistent/p.txt" in r.stderr


def test_empty_prompt_file_is_refused(tmp_path):
    f = tmp_path / "p.txt"; f.write_text("  \n")
    r = run("--prompt-file", str(f), "--out", "/tmp/x.png")
    assert r.returncode == 1 and "empty" in r.stderr


def test_missing_base_image_is_named():
    r = run("--prompt", "x", "--image", "/nonexistent/base.png", "--out", "/tmp/x.png")
    assert r.returncode == 1 and "Traceback" not in r.stderr and "/nonexistent/base.png" in r.stderr
