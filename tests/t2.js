const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1000, height: 900 } });
  await p.addInitScript(() => { const o = window.scrollTo.bind(window); window.scrollTo = () => o(0, 0); }); const errs = []; p.on('pageerror', e => errs.push(e.message)); p.on('console', m => m.type()==='error' && errs.push(m.text()));
  await p.goto('file://' + require('path').resolve(__dirname, '../index.html')); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(1500);
  // Boat: drag
  await p.click('[data-case="b-explorer"]');
  const dragTo = async (src, dst) => {
    const s = await p.locator(src).first().boundingBox(); const d = await p.locator(dst).first().boundingBox();
    await p.mouse.move(s.x + s.width/2, s.y + s.height/2); await p.mouse.down();
    await p.mouse.move(s.x + s.width/2 + 10, s.y + s.height/2 + 10, { steps: 3 });
    const tx = dst.includes('pblock') ? d.x + 4 : dst === '.prog' ? d.x + d.width - 8 : d.x + d.width/2;
    await p.mouse.move(tx, d.y + d.height/2, { steps: 8 }); await p.mouse.up(); await p.waitForTimeout(100);
  };
  for (const d of ['right','right','right','right','right','up','up','up']) await dragTo(`[data-drag="arrow"][data-v="${d}"]`, '.prog');
  console.log('prog after drag:', await p.evaluate(() => st.be.prog.join(',')));
  // reorder: drag block 0 to trash then re-add
  await dragTo('.pblock >> nth=0', '.trash');
  console.log('after trash:', await p.evaluate(() => st.be.prog.join(',')));
  await dragTo('[data-drag="arrow"][data-v="right"]', '.pblock >> nth=0');
  await p.click('[data-action="be-run"]'); await p.waitForTimeout(4000);
  console.log('explorer built:', await p.evaluate(() => st.built.explorer));
  // Lighthouse levels
  await p.click('.back'); await p.click('[data-case="b-detective"]');
  const sol = [{A:'or'},{A:'and'},{U:'not',A:'and'},{A:'or',U:'not',B:'and'},{A:'xor'}];
  for (let i = 0; i < 5; i++) {
    for (const [slot, g] of Object.entries(sol[i])) {
      if (i === 0) await dragTo(`[data-drag="gate"][data-v="${g}"]`, `[data-slot="${slot}"]`);
      else { await p.click(`[data-slot="${slot}"]`); await p.click(`[data-drag="gate"][data-v="${g}"]`); }
    }
    if (i === 3) await p.screenshot({ path: 'lvl4.png' });
    await p.click('[data-action="bd-test"]');
    console.log('level', i+1, 'done:', await p.evaluate(() => st.bd.lvlDone));
    if (i < 4) await p.click('[data-action="bd-next"]');
  }
  console.log('detective built:', await p.evaluate(() => st.built.detective));
  // Bridge
  await p.click('.back'); await p.click('[data-case="b-strategist"]');
  await p.click('[data-action="bs-test"]'); await p.waitForTimeout(2000);
  await p.screenshot({ path: 'bridge.png' });
  await p.waitForTimeout(12000);
  console.log('bridge results (buggy):', await p.evaluate(() => st.bs.results.map(r => r.pass).join(',')));
  await p.click('#blk-if'); await p.click('[data-action="bs-cond"][data-v="and"]');
  await p.click('#blk-a1'); await p.click('[data-action="bs-swap"]');
  await p.click('[data-action="bs-test"]'); await p.waitForTimeout(500); await p.click('[data-action="bs-skip"]');
  console.log('strategist built:', await p.evaluate(() => st.built.strategist));
  console.log('errors:', errs);
  await b.close();
})();
