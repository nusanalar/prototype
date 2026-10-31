// Shared test setup: older tests start on the map, so mark onboarding as already seen in every page they open.
const pw = require('playwright');
const SEEN = () => { try { if (!localStorage.getItem('mi-onboard')) localStorage.setItem('mi-onboard', 'done'); } catch (e) {} };
const launch = pw.chromium.launch.bind(pw.chromium);
pw.chromium.launch = async (...a) => {
  const b = await launch(...a);
  const newContext = b.newContext.bind(b), newPage = b.newPage.bind(b);
  b.newContext = async (...x) => { const c = await newContext(...x); await c.addInitScript(SEEN); return c; };
  b.newPage = async (...x) => { const p = await newPage(...x); await p.addInitScript(SEEN); return p; };
  return b;
};

module.exports.serve = require('./_server').serve;
