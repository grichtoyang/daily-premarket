import { chromium } from "playwright";
import fs from "node:fs";
import path from "node:path";

const htmlPath = process.env.DASHBOARD_HTML || "dashboards/v9-pro-20261030.html";
const outDir = process.env.AUDIT_OUT || "artifacts/dashboard-browser-audit";
if (!fs.existsSync(htmlPath)) throw new Error(`Dashboard HTML not found: ${htmlPath}`);
fs.mkdirSync(outDir, { recursive: true });

const tabs = [
  { label: "總覽", key: "overview" },
  { label: "現貨", key: "spot" },
  { label: "重要市場", key: "markets" },
  { label: "期貨", key: "futures" },
  { label: "選擇權", key: "options" },
  { label: "綜合分析", key: "synthesis" }
];
const errors = [];
const results = [];
let fatal = null;
const browser = await chromium.launch({ headless: true });
try {
  for (const viewport of [{ name: "desktop", width: 1440, height: 1000 }, { name: "tablet", width: 1024, height: 900 }, { name: "mobile", width: 390, height: 844 }]) {
    const page = await browser.newPage({ viewport: { width: viewport.width, height: viewport.height }, deviceScaleFactor: 1 });
    page.on("pageerror", error => errors.push(`${viewport.name}: ${error.message}`));
    page.on("console", message => {
      if (message.type() === "error") errors.push(`${viewport.name} console: ${message.text()}`);
    });
    await page.goto("file://" + path.resolve(htmlPath), { waitUntil: "domcontentloaded" });
    await page.waitForSelector("#root", { state: "attached" });
    await page.waitForFunction(() => document.querySelector("#main-content")?.innerText?.trim().length > 0, null, { timeout: 30000 });

    for (let index = 0; index < tabs.length; index++) {
      const tab = tabs[index];
      const button = page.locator(`button[data-tab="${tab.key}"]`);
      await button.waitFor({ state: "visible", timeout: 15000 });
      const beforePulse = await page.locator("#main-content").getAttribute("data-pulse");
      await button.click();
      try {
        await page.waitForFunction(({ key, beforePulse }) => {
          const nav = document.querySelector(`button[data-tab="${key}"]`);
          const main = document.querySelector("#main-content");
          const pulse = main?.getAttribute("data-pulse");
          const text = main?.innerText?.trim() || "";
          const canvases = [...(main?.querySelectorAll("canvas") || [])]
            .filter(c => c.getBoundingClientRect().width > 0 && c.getBoundingClientRect().height > 0).length;
          return nav?.getAttribute("data-active") === "1" &&
            pulse !== beforePulse && text.length >= 100 && canvases >= 1;
        }, { key: tab.key, beforePulse }, { timeout: 10000 });
      } catch (error) {
        if (tab.key === "synthesis") {
        const synthesisText = await page.locator("#main-content").innerText();
        const requiredSections = [
          "區塊A 多空籌碼結構",
          "區塊B 選擇權法人多空力道",
          "區塊C 日夜盤劇本",
          "三劇本路徑",
          "多空因子方向貢獻",
          "相關性熱圖",
          "交易計畫"
        ];
        const missingSections = requiredSections.filter(section => !synthesisText.includes(section));
        if (missingSections.length) {
          throw new Error(`${viewport.name} / 綜合分析: missing sections: ${missingSections.join(", ")}`);
        }
        if (viewport.name === "tablet") {
          const columns = await page.locator(".v9-market-ab-grid").evaluate(el => getComputedStyle(el).gridTemplateColumns.trim().split(/\s+/).length);
          if (columns !== 1) throw new Error(`tablet / 綜合分析: expected one-column synthesis layout, got ${columns}`);
        }
      }
      const state = await page.evaluate(() => ({
          activeTab: [...document.querySelectorAll("button[data-tab]")].find(b => b.getAttribute("data-active") === "1")?.getAttribute("data-tab") || null,
          pulse: document.querySelector("#main-content")?.getAttribute("data-pulse") || null,
          mainTextLength: document.querySelector("#main-content")?.innerText?.trim().length ?? 0,
          canvases: document.querySelectorAll("#main-content canvas").length,
          visibleText: document.querySelector("#main-content")?.innerText?.slice(0, 240) ?? ""
        }));
        throw new Error(`${viewport.name} / ${tab.label}: tab content did not become ready; state=${JSON.stringify(state)}; pageErrors=${errors.join(" | ")}; cause=${error.message}`);
      }
      if (tab.key === "synthesis") {
        const synthesisText = await page.locator("#main-content").innerText();
        const requiredSections = [
          "區塊A 多空籌碼結構",
          "區塊B 選擇權法人多空力道",
          "三市場交叉判讀",
          "區塊C 日夜盤劇本",
          "三劇本路徑",
          "多空因子方向貢獻",
          "相關性熱圖",
          "交易計畫",
          "三市場狀態",
          "交易前提",
          "觸發／取消",
          "決策鏈"
        ];
        const missingSections = requiredSections.filter(section => !synthesisText.includes(section));
        if (missingSections.length) {
          throw new Error(`${viewport.name} / 綜合分析: missing sections: ${missingSections.join(", ")}`);
        }
        if (viewport.name === "tablet") {
          const columns = await page.locator(".v9-market-ab-grid").evaluate(el => getComputedStyle(el).gridTemplateColumns.trim().split(/\s+/).length);
          if (columns !== 1) throw new Error(`tablet / 綜合分析: expected one-column synthesis layout, got ${columns}`);
        }
      }
      const state = await page.evaluate(() => ({
        width: window.innerWidth,
        documentWidth: document.documentElement.scrollWidth,
        bodyWidth: document.body.scrollWidth,
        rootTextLength: document.querySelector("#main-content")?.innerText?.trim().length ?? 0,
        canvases: [...document.querySelectorAll("#main-content canvas")].filter(c => c.getBoundingClientRect().width > 0 && c.getBoundingClientRect().height > 0).length,
        visibleText: document.querySelector("#main-content")?.innerText?.slice(0, 240) ?? ""
      }));
      if (state.documentWidth > viewport.width + 1 || state.bodyWidth > viewport.width + 1) {
        throw new Error(`${viewport.name} / ${tab.label}: horizontal overflow document=${state.documentWidth}, body=${state.bodyWidth}, viewport=${viewport.width}`);
      }
      if (state.canvases < 1) throw new Error(`${viewport.name} / ${tab.label}: no visible chart canvas`);
      await page.screenshot({ path: path.join(outDir, `${viewport.name}-${index + 1}.png`), fullPage: true });
      results.push({ viewport: viewport.name, tab: tab.label, ...state, status: "PASS" });
    }
    await page.close();
  }
} catch (error) {
  fatal = error;
} finally {
  await browser.close();
}
const report = { html: htmlPath, tabs: tabs.map(t => t.label), results, pageErrors: errors, failure: fatal?.message || null, status: fatal || errors.length ? "FAIL" : "PASS" };
fs.writeFileSync(path.join(outDir, "report.json"), JSON.stringify(report, null, 2));
if (fatal) throw fatal;
if (errors.length) throw new Error("Browser page or console errors: " + errors.join("; "));
console.log(JSON.stringify(report, null, 2));
