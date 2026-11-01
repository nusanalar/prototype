# Nusa Nalar · Prototype

A single-file playable prototype of **Nusa Nalar** (earlier working title: *Pulau Misteri / Mystery Isles*). Open `index.html` in a browser: no build or server needed.

- Cases: Detective #07 (with a "Number check" step: a maths clue about Bu Sari's baking times) and #08, Strategist #09 (News Port), Explorer #10 (Pattern Isle), three Build puzzles, a daily puzzle and a parent view.
- Indonesian and English, with recorded AI voice lines (Indonesian for every character, English for the narrator once generated) and device voices as a fallback. `make voxsync` copies the asset kit's `voices/id` and `voices/en` MP3s into `voices/` next to the page and links them from `index.html`, so the page stays small and loads only the line it plays. Commit `voices/` together with `index.html` when deploying. Light and dark modes.
- Guidance for kids:
  - **Onboarding** (first visit, replay with the **?** button): pick a detective, what the two tasks are, why it helps them, the animal helpers, and their age, which marks the island to start on.
  - **Mission card** on every activity: what to do, the skill they practise, and how it helps them in real life.
  - **Lesson to acknowledge** at the end of every activity: the child picks when they'd use it and taps "Aku paham!". Saved lessons appear in **Buku Pelajaranku** (My Learning Book) and in the parent view.
- **Age band** (after the 6-year-old playtest): the age picked in onboarding is enforced. Islands and daily levels above it show a lock and open only after a grown-up answers a times-table question; the daily puzzle opens on the child's level. For 6–9 the mission card starts collapsed and is read aloud, answer buttons are icon-only (spoken labels stay), and the map marker moves to **Next** once the start island is under way. Hints and wins scroll into view, the pattern train rolls away with a horn after the third (colour) train, and the easy boat routes are 4–6 steps.
- Run `make` for the commands: `make serve`, `make test`, `make voxsync` (copy voice lines from the assets repo into the page). Voices are generated in the assets repo (`make voices` there), which is the single source for the prototype and the future app.
- `tests/`: Playwright scripts (`node tests/t17.js`; `_setup.js` skips onboarding for older tests), `tools/`: the Python scripts that injected cases, assets and voices into the page.

## Play-testing with kids

- Live: https://nusanalar.github.io/prototype/ (starts in Indonesian on devices set to Indonesian).
- Between children on the same device: **Parent view → New player** clears the daily puzzle, chosen detective, progress, saved lessons, age and grown-up unlocks, and shows onboarding again. Language, sound and light/dark are kept.
- [observation-sheet.html](observation-sheet.html): a printable, bilingual sheet for watching one child play (session plan, which case per age, per-screen notes, closing questions for child and parent, top-3 problems).
