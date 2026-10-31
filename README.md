# Nusa Nalar · Prototype

A single-file playable prototype of **Nusa Nalar** (earlier working title: *Pulau Misteri / Mystery Isles*). Open `index.html` in a browser: no build or server needed.

- Cases: Detective #07 and #08, Strategist #09 (News Port), Explorer #10 (Pattern Isle), three Build puzzles, a daily puzzle and a parent view.
- Indonesian and English, with recorded Indonesian AI voice lines and device voices as a fallback.
- `tests/`: Playwright scripts (`node tests/t11.js`), `tools/`: the Python scripts that injected cases, assets and voices into the page.

## Play-testing with kids

- Live: https://nusanalar.github.io/prototype/ (starts in Indonesian on devices set to Indonesian).
- Between children on the same device: **Parent view → New player** clears the daily puzzle, chosen detective and progress, and keeps language and sound.
- [observation-sheet.html](observation-sheet.html): a printable, bilingual sheet for watching one child play (session plan, which case per age, per-screen notes, closing questions for child and parent, top-3 problems).
