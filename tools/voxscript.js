// Write a voice script line for every text in the prototype, in Indonesian and English.
//
// The page's own text tables (T and GUIDE) are read from index.html in Chromium, so the script always matches
// what the game shows. Every text becomes a line in the asset kit's voices/<lang>/lines.json (who, file, text,
// src, and id_text for English), next to the lines the game already speaks. Lines that are already there are
// left untouched; only missing ones are added, without audio. `make voices` in the assets repo then generates
// the MP3s, and `make voxsync` here links them.
//
// Who speaks a line:
//   - a character's own words (greetings, suspect statements, the case giver) are spoken by that character;
//   - hints and praise in the feedback box are spoken by the screen's animal helper, exactly as the game says
//     them ("Correct! ..." / "Not quite. ..."), so the recording is found at runtime;
//   - everything else (story, questions, answers, labels, mission cards, lessons, parent view) by the narrator.
// Templated texts are written out for the values the game can show (counts, levels, names).
// It also writes voices/SCRIPT.md, the readable script grouped by screen, with ID and EN side by side.
//
// Usage: node tools/voxscript.js [path/to/assets]
const fs = require('fs'), path = require('path'), crypto = require('crypto');
const { chromium } = require('playwright');
const HERE = path.resolve(__dirname, '..');
const ASSETS = path.resolve(process.argv[2] || path.join(HERE, '..', 'assets'));

const PETS = { oyen: 'Oyen', kepi: 'Kepi', nyu: 'Nyu', cici: 'Cici', rangga: 'Rangga' };
const GIVER = { d2: 'ratna', s2: 'putri', e2: 'ijah' };

// Feedback-box texts: [path pattern, helper, good?]. The game says them as `${correct|notQuite} ${text}`.
const FB = [
  [/^d\.(mOpts\.\d+\.f|fbNone|fbDika|fbSari|fbWeak|why\.\d+\.f)$/, 'oyen', false], [/^d\.(mDone|fbGood)$/, 'oyen', true],
  [/^d2\.(tlWrong|fbJoko|fbPutri|fbWeak|why\.\d+\.f)$/, 'oyen', false], [/^d2\.(tlDone|fbGood)$/, 'oyen', true],
  [/^s2\.(rateWhy\.\w+|dec\.\d+\.f|why\.\d+\.f)$/, 'rangga', false], [/^s2\.csDone$/, 'rangga', true],
  [/^e2\.(matchNo|whoNo\.\w+|why\.\d+\.f)$/, 'kepi', false], [/^e2\.(matchOk|whoOk)$/, 'kepi', true],
  [/^e\.(wrong|why\.\d+\.f)$/, 'kepi', false], [/^e\.(gotIt|whyGood)$/, 'kepi', true],
  [/^s\.dec\.\d+\.f$/, 'rangga', false],
  [/^be\.(crash|short|empty)$/, ['kepi', 'nyu'], false],
  [/^bd\.(failN|noGate)$/, ['cici', 'nyu'], false], [/^bd\.lvlDone$/, ['cici', 'nyu'], true],
  [/^dy\.solvedT$/, 'nyu', true],
  [/^bs\.failN$/, 'rangga', false],
];
// Not text to speak: icon names, internal keys, the onboarding item icons, hour ticks on the number line.
const SKIP = [/\.icon$/, /^s\.parts\.\d+\.k$/, /^onb\.1\.items\.\d+\.0$/, /^d\.mHours\.\d+$/, /^gate\.ask$/, /^bs\.cols\.2$/];

const range = (a, b) => Array.from({ length: b - a + 1 }, (_, i) => a + i);
// Values each templated text can show in the game.
function expand(p, fn, T, lang) {
  const t = T[lang];
  switch (p) {
    case 'helperSays': return Object.values(PETS).map(n => fn(n));
    case 'lights': return range(0, 3).flatMap(a => range(0, 3).map(b => fn(a, b)));
    case 'd.need': return range(1, 8).map(fn);
    case 'e2.need': return range(1, 6).map(fn);
    case 's.found': return range(0, 4).map(fn);
    case 'be.crash': return range(1, 12).map(fn);
    case 'bd.test': return [2, 4, 8].map(fn);
    case 'bd.failN': return [4, 8].flatMap(n => range(1, n).map(k => fn(k, n)));
    case 'bs.failN': return range(1, 4).map(fn);
    case 'bs.capTest': return range(1, 4).map(i => fn(i, t.bs.sit[i - 1]));
    case 'dy.streak': return range(1, 7).map(fn);
    case 'gate.locked': return Object.values(t.tier).map(fn);
    case 'book.count': return range(0, 9).map(fn);
  }
  return null;
}

// Make a screen text speakable: drop arrows and tick marks, read separators and age ranges out loud.
function speakable(s, lang) {
  let x = String(s).replace(/(\S)\s*→\s*(?=\S)/g, '$1, ').replace(/[→←✓✗]/g, '').replace(/[“”"]/g, '"');
  if (/^\s*\+/.test(x)) x = x.split('+').map(v => v.trim()).filter(Boolean).join(', ') + '.';
  x = x.replace(/(\d+)\s*[–-]\s*(\d+)(?!\s*(pm|am|:))/g, (m, a, b) => `${a} ${lang === 'id' ? 'sampai' : 'to'} ${b}`);
  x = x.replace(/\s+·\s+/g, ', ').replace(/\.\.\s/g, '. ');
  return x.replace(/\s+/g, ' ').trim();
}
const key = (who, text) => who + '|' + String(text).replace(/[“”"]/g, '').trim();
const fileFor = (lang, who, text) => `voices/${lang}/${who}/${who}-${crypto.createHash('sha1').update(`${who}|${text}`).digest('hex').slice(0, 10)}.mp3`;

function whoFor(p) {
  let m;
  if ((m = p.match(/^greet\.(\w+)$/))) return m[1];
  if ((m = p.match(/^(d|d2|s2|e2)\.sus\.(\w+)\.s$/))) return m[2];
  if ((m = p.match(/^(d2|s2|e2)\.giver$/))) return GIVER[m[1]];
  return 'narrator';
}
function screenOf(p, src) {
  const top = p.split('.')[0];
  const names = {
    d: 'Case #07 · The Missing Lighthouse Lamp (Detective)', d2: 'Case #08 · The Vanishing Donation Jar (Detective)',
    s2: 'Case #09 · The Viral Beach Photo (Strategist)', e2: 'Case #10 · Who Bit the Kue? (Explorer)',
    e: 'Pattern Isle · The Stuck Train (Explorer)', s: 'News Port · The Bridge Rumor (Strategist)',
    be: 'Build · Boat Home', bd: 'Build · Relight the Lighthouse', bs: 'Build · Fix the Drawbridge',
    dy: 'Daily puzzle', p: 'Parent view', greet: 'Character greetings',
    onb: 'Onboarding', gate: 'Age gate', m: 'Mission cards and lessons', book: 'My Learning Book', par: 'Parent view',
  };
  return names[top] || (src === 'GUIDE' ? 'Guide · buttons and labels' : 'Map, menus and labels');
}

(async () => {
  const b = await chromium.launch(), pg = await b.newPage();
  await pg.goto('file://' + path.join(HERE, 'index.html'));
  // Pull every leaf of T and GUIDE; functions are expanded in the page so their output is exact.
  const leaves = await pg.evaluate(src => {
    const out = [];
    const walk = (o, p, lang, from) => {
      if (typeof o === 'string') out.push({ from, lang, p, texts: [o] });
      else if (typeof o === 'function') out.push({ from, lang, p, fn: o.toString() });
      else if (o && typeof o === 'object') for (const k of Object.keys(o)) walk(o[k], p ? p + '.' + k : k, lang, from);
    };
    for (const lang of ['id', 'en']) { walk(T[lang], '', lang, 'T'); walk(GUIDE[lang], '', lang, 'GUIDE'); }
    return out;
  });
  const tables = await pg.evaluate(() => ({ id: { tier: T.id.tier, bs: { sit: T.id.bs.sit } }, en: { tier: T.en.tier, bs: { sit: T.en.bs.sit } }, nq: { id: T.id.notQuite, en: T.en.notQuite }, ok: { id: T.id.correct, en: T.en.correct } }));
  await b.close();

  // Build candidate lines per language, keyed by source path (+ variant index) so ID and EN pair up.
  const cand = { id: new Map(), en: new Map() };
  for (const l of leaves) {
    if (SKIP.some(r => r.test(l.p))) continue;
    let texts = l.texts;
    if (l.fn) { const fn = eval(l.fn); texts = expand(l.p, fn, tables, l.lang); if (!texts) continue; }
    const fb = FB.find(([r]) => r.test(l.p));
    texts.forEach((raw, i) => {
      if (!raw || !/[A-Za-z]/.test(raw)) return;
      const helpers = fb ? [].concat(fb[1]) : [null];
      helpers.forEach((h, j) => {
        let who = h || whoFor(l.p), text;
        if (fb) text = (fb[2] ? tables.ok[l.lang] : tables.nq[l.lang]) + ' ' + String(raw).trim();
        else text = speakable(raw, l.lang);
        const id = `${l.from}:${l.p}${texts.length > 1 ? '#' + i : ''}${helpers.length > 1 ? '@' + h : ''}`;
        cand[l.lang].set(id, { who, text, src: id, screen: screenOf(l.p, l.from), fb: !!fb });
      });
    });
  }

  const report = {};
  const byLang = {};
  for (const lang of ['id', 'en']) {
    const f = path.join(ASSETS, 'voices', lang, 'lines.json');
    const lines = JSON.parse(fs.readFileSync(f, 'utf8'));
    const have = new Map(lines.map(x => [key(x.who, x.text), x]));
    let added = 0;
    for (const c of cand[lang].values()) {
      const k = key(c.who, c.text);
      if (have.has(k)) { const x = have.get(k); c.file = x.file; if (x.src && !x.src.includes(c.src)) x.src.push(c.src); continue; }
      const line = { who: c.who, file: fileFor(lang, c.who, c.text), text: c.text, src: [c.src] };
      if (lang === 'en') { const twin = cand.id.get(c.src); if (twin) line.id_text = twin.text; }
      lines.push(line); have.set(k, line); c.file = line.file; added++;
    }
    fs.writeFileSync(f, JSON.stringify(lines, null, 1) + '\n');
    byLang[lang] = lines;
    report[lang] = { total: lines.length, added };
  }

  // Readable script: every line of the game grouped by screen, Indonesian and English side by side.
  const esc = s => String(s).replace(/\|/g, '\\|');
  const exists = file => fs.existsSync(path.join(ASSETS, file));
  const groups = new Map();
  for (const [id, c] of cand.id) {
    const e = cand.en.get(id); if (!groups.has(c.screen)) groups.set(c.screen, []);
    groups.get(c.screen).push({ id, c, e });
  }
  let md = `# Nusa Nalar · Voice script\n\nEvery text in the prototype, as a voice line in Indonesian and English. Made by \`node tools/voxscript.js\` in the prototype repo from the page's own text, so it always matches the game; edit the text in the prototype, not here.\n\n`;
  md += `- **Who** is the character whose preset (voices/presets/characters.json) speaks the line. Hints and praise are spoken by the screen's animal helper, starting with "Benar!" / "Belum tepat." ("Correct!" / "Not quite.") as in the game.\n`;
  md += `- **Audio**: ✅ the MP3 exists in voices/<lang>/, ⏳ still to generate with \`make voices\`.\n- Lines the game builds from several texts (titles joined with their story, a question with its answers) are in voices/<lang>/lines.json too, but not repeated here.\n\n`;
  md += `| | Lines | With audio | To generate |\n| --- | --- | --- | --- |\n`;
  for (const lang of ['id', 'en']) { const n = byLang[lang].length, a = byLang[lang].filter(x => exists(x.file)).length; md += `| ${lang.toUpperCase()} (all of lines.json) | ${n} | ${a} | ${n - a} |\n`; }
  for (const [screen, rows] of groups) {
    md += `\n## ${screen}\n\n| Who | Indonesian | English | ID | EN |\n| --- | --- | --- | --- | --- |\n`;
    for (const { c, e } of rows) md += `| ${c.who} | ${esc(c.text)} | ${esc(e ? e.text : '')} | ${exists(c.file) ? '✅' : '⏳'} | ${e && exists(e.file) ? '✅' : '⏳'} |\n`;
  }
  fs.writeFileSync(path.join(ASSETS, 'voices', 'SCRIPT.md'), md);
  for (const lang of ['id', 'en']) console.log(`[${lang}] ${report[lang].added} lines added · ${report[lang].total} in lines.json`);
  console.log(`${[...cand.id.keys()].length} screen texts · voices/SCRIPT.md written`);
})();
