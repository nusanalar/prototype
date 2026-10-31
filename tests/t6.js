require('./_setup');
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1000, height: 900 } });
  await p.addInitScript(() => { const o = window.scrollTo.bind(window); window.scrollTo = () => o(0, 0); });
  const errs = []; p.on('pageerror', e => errs.push(e.message));
  await p.goto('file://' + require('path').resolve(__dirname, '../index.html')); await p.waitForTimeout(1200);
  // generator health over 120 days
  console.log(await p.evaluate(() => {
    let boatFallback = 0, circFallback = 0, layouts = {};
    for (let d = 0; d < 120; d++) {
      const base = 20261000 + d;
      if (genBoat(base * 10) === GRID) boatFallback++;
      for (const hard of [false, true]) { const lv = genCircuit(base * 10 + (hard ? 2 : 1), hard); if (lv === LV[0]) circFallback++; const k = Object.keys(lv.slots).join('') + Object.keys(lv.ins).length; layouts[k] = (layouts[k] || 0) + 1; }
    }
    return { boatFallback, circFallback, layouts };
  }));
  await p.click('.daily-card');
  for (const tier of ['detective', 'strategist']) {
    await p.click(`[data-action="dy-tier"][data-v="${tier}"]`);
    // brute-force a solution, then place blocks by tap
    const sol = await p.evaluate(() => {
      const lv = dailyLv, ks = Object.keys(lv.slots), rows = combos(Object.keys(lv.ins));
      const opts = ks.map(k => GATES[lv.slots[k].t]);
      const tryAll = (i, cur) => { if (i === ks.length) return rows.every(v => nodeVal(lv, cur, v, lv.out) === lv.target(v)) ? { ...cur } : null;
        for (const g of opts[i]) { const r = tryAll(i + 1, { ...cur, [ks[i]]: g }); if (r) return r; } return null; };
      return tryAll(0, {});
    });
    console.log(tier, 'solution:', JSON.stringify(sol));
    for (const [slot, g] of Object.entries(sol)) { await p.click(`[data-slot="${slot}"]`); await p.click(`[data-action="bd-place"][data-v="${g}"]`); }
    await p.click('[data-action="bd-test"]');
    console.log(tier, 'solved:', await p.evaluate(() => st.dc.done));
    if (tier === 'strategist') await p.screenshot({ path: 'daily-hard.png', fullPage: true });
  }
  await p.click('[data-action="dy-tier"][data-v="explorer"]');
  const path = await p.evaluate(() => {
    const b = st.be, g = b.grid, prev = {}, k = a => a.join(); let q = [b.start]; prev[k(b.start)] = null;
    while (q.length) { const n = []; for (const c of q) for (const [d, [dx, dy]] of Object.entries(DIRS)) { const nx = c[0] + dx, ny = c[1] + dy; if (nx < 0 || ny < 0 || nx >= g[0].length || ny >= g.length || g[ny][nx] === 'R' || k([nx, ny]) in prev) continue; prev[k([nx, ny])] = [k(c), d]; n.push([nx, ny]); } q = n; }
    const out = []; let cur = k(b.harbor); while (prev[cur]) { out.unshift(prev[cur][1]); cur = prev[cur][0]; } return out;
  });
  console.log('boat path', path.join(','));
  for (const d of path) await p.click(`[data-action="be-add"][data-v="${d}"]`);
  await p.screenshot({ path: 'daily-easy.png' });
  await p.click('[data-action="be-run"]'); await p.waitForTimeout(path.length * 400 + 800);
  console.log('easy solved:', await p.evaluate(() => st.dailyDone));
  await p.click('[data-action="dy-day"][data-v="1"]');
  console.log('tomorrow grid differs:', await p.evaluate(() => st.be.grid.join('|')));
  await p.click('.back');
  console.log('map card text:', await p.textContent('.daily-card'));
  console.log('errors:', errs);
  await b.close();
})();
