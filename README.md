# Nusa Nalar · Prototype

A single-file playable prototype of **Nusa Nalar** (earlier working title: *Pulau Misteri / Mystery Isles*). Open `index.html` in a browser: no build or server needed.

- Cases: Detective #07 (with a "Number check" step: a maths clue about Bu Sari's baking times) and #08, Strategist #09 (News Port), Explorer #10 (Pattern Isle), three Build puzzles, a daily puzzle and a parent view.
- Indonesian and English, with recorded AI voice lines (Indonesian for every character, English for the narrator once generated) and device voices as a fallback. `python3 tools/voxsync.py` embeds the asset kit's `voices/id` and `voices/en` lines. Light and dark modes.
- Guidance for kids:
  - **Onboarding** (first visit, replay with the **?** button): pick a detective, what the two tasks are, why it helps them, the animal helpers, and their age, which marks the island to start on.
  - **Mission card** on every activity: what to do, the skill they practise, and how it helps them in real life.
  - **Lesson to acknowledge** at the end of every activity: the child picks when they'd use it and taps "Aku paham!". Saved lessons appear in **Buku Pelajaranku** (My Learning Book) and in the parent view.
- `tests/`: Playwright scripts (`node tests/t17.js`; `_setup.js` skips onboarding for older tests), `tools/`: the Python scripts that injected cases, assets and voices into the page.

## Play-testing with kids

- Live: https://nusanalar.github.io/prototype/ (starts in Indonesian on devices set to Indonesian).
- Between children on the same device: **Parent view → New player** clears the daily puzzle, chosen detective, progress, saved lessons and age, and shows onboarding again. Language, sound and light/dark are kept.
- [observation-sheet.html](observation-sheet.html): a printable, bilingual sheet for watching one child play (session plan, which case per age, per-screen notes, closing questions for child and parent, top-3 problems).
