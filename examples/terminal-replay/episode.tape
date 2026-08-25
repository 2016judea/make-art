# One episode beat as deterministic terminal footage.
# Render: vhs episode.tape   (brew install vhs)
# 4K variant: double Width/Height/FontSize/Padding.
# TRAP: "Set Framerate 30" has silently emitted 25fps — verify with
# ffprobe, or render "Output frames/" PNGs and encode with ffmpeg yourself.
Output out.mp4
Set Shell bash
Set Width 1920
Set Height 1080
Set FontSize 30
Set FontFamily "Menlo"
Set LineHeight 1.35
Set Padding 40
Set WindowBar Colorful
Set Framerate 30
# phosphor register — green-on-near-black custom theme
Set Theme { "name": "phosphor", "background": "#0a0f0a", "foreground": "#c8ffc8", "cursor": "#7dff7d", "black": "#0a0f0a", "red": "#ff6b6b", "green": "#7dff7d", "yellow": "#e8ff8a", "blue": "#8ad2ff", "magenta": "#ff9de2", "cyan": "#8affd2", "white": "#c8ffc8", "brightBlack": "#4a5f4a", "brightRed": "#ff9b9b", "brightGreen": "#aaffaa", "brightYellow": "#f2ffb8", "brightBlue": "#b8e4ff", "brightMagenta": "#ffc4ee", "brightCyan": "#b8ffe4", "brightWhite": "#eaffea" }

Hide
Type "clear"
Enter
Show

Set TypingSpeed 80ms
Type "bash fake_claude.sh"
Sleep 500ms
Enter
Sleep 12s
