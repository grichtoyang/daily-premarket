import { chromium } from "playwright";
import fs from "node:fs";
import path from "node:path";

const htmlPath = process.env.DASHBOARD_HTML || "dashboards/v9-pro-20261030.html";
const outDir = process.env.AUDIT_OUT || "artifacts/dashboard-browser-audit";
if (!fs.existsSync(htmlPath)) throw new Error(`Dashboard HTML not found: ${htmlPath}`);
fs.mkdirSync(outDir, { recursive: true });

const tabs = ["總覽", "現貨", "重要市場", "期貨", "選擇權", "綜合分析"];
const errors = [];
const results = [];
const browser = await chromium.launch({ headless: true });
try {
  for (const viewport of [{ name: "desktop", width: 1440, height: 1000 }, { name: "mobile", width: 390, height: 844 }]) {
    const page = await browser.newPage({ viewport: { width: viewport.width, height: viewport.height }, deviceScaleFactor: 1 });
    page.on("pageerror", error => errors.push(`${viewport.name}: ${error.message}`));
    await page.goto("file://" + path.resolve(htmlPath), { waitUntil: "domcontentloaded" });
    await page.waitForSelector("#root", { state: "attached" });
    await page.waitForFunction(() => document.querySelector("#root")?.innerText?.trim().length > 0, null, { timeout: 30000 });

    for (const tab of tabs) {
      const button = page.locator("button").filter({ hasText: tab }).first();
      await button.waitFor({ state: "visible", timeout: 15000 });
      await button.click();
      await page.waitForTimeout(250);
      const state = await page.evaluate(() => ({
        width: window.innerWidth,
        documentWidth: document.documentElement.scrollWidth,
        bodyWidth: document.body.scrollWidth,
        rootTextLength: document.querySelector("#root")?.innerText?.trim().length ?? 0,
        canvases: [...document.querySelectorAll("canvas")].filter(c => c.getBoundingClientRect().width > 0 && c.getBoundingClientRect().height > 0).length,
        visibleText: document.querySelector("#root")?.innerText?.slice(0, 240) ?? ""
      }));
      if (state.rootTextLength < 100) throw new Error(`${viewport.name} / ${tab}: dashboard content unexpectedly empty`);
      if (state.documentWidth > viewport.width + 1 || state.bodyWidth > viewport.width + 1) {
        throw new Error(`${viewport.name} / ${tab}: horizontal overflow document=${state.documentWidth}, body=${state.bodyWidth}, viewport=${viewport.width}`);
      }
      if (state.canvases < 1) throw new Error(`${viewport.name} / ${tab}: no visible chart canvas`);
      const safeTab = tabs.indexOf(tab) + 1;
      await page.screenshot({ path: path.join(outDir, `${viewport.name}-${safeTab}.png`), fullPage: true });
      results.push({ viewport: viewport.name, tab, ...state, status: "PASS" });
    }
    await page.close();
  }
} finally {
  await browser.close();
}
const report = { html: htmlPath, tabs, results, pageErrors: errors, status: errors.length ? "FAIL" : "PASS" };
fs.writeFileSync(path.join(outDir, "report.json"), JSON.stringify(report, null, 2));
if (errors.length) throw new Error("Browser page errors: " + errors.join("; "));
console.log(JSON.stringify(report, null, 2));
