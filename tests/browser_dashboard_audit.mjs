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
      const state = await page.evaluate(() => ({
          activeTab: [...document.querySelectorAll("button[data-tab]")].find(b => b.getAttribute("data-active") === "1")?.getAttribute("data-tab") || null,
          pulse: document.querySelector("#main-content")?.getAttribute("data-pulse") || null,
          mainTextLength: document.querySelector("#main-content")?.innerText?.trim().length ?? 0,
          canvases: document.querySelectorAll("#main-content canvas").length,
          visibleText: document.querySelector("#main-content")?.innerText?.slice(0, 240) ?? ""
        }));
        throw new Error(`${viewport.name} / ${tab.label}: tab content did not become ready; state=${JSON.stringify(state)}; pageErrors=${errors.join(" | ")}; cause=${error.message}`);
      }
      if (tab.key === "markets") {
        const marketText = await page.locator("#main-content").innerText();
        const requiredMarketChecks = ["VIX水準", "2Y–10Y", "重大新聞", "DATA_REPORT 第8節"];
        const missingMarketChecks = requiredMarketChecks.filter(item => !marketText.includes(item));
        if (missingMarketChecks.length) {
          throw new Error(`${viewport.name} / 重要市場: missing market-risk interpretation or DATA_REPORT linkage: ${missingMarketChecks.join(", ")}`);
        }
        if (!["正斜率", "倒掛", "近乎平坦", "斜率缺值"].some(state => marketText.includes(state))) {
          throw new Error(`${viewport.name} / 重要市場: missing dynamic 2Y–10Y curve classification`);
        }\n        for (const selector of [".v9-market-commodity-card", ".v9-market-news-card"]) {
          const node = page.locator("#main-content " + selector);
          if (await node.count() !== 1) throw new Error(`${viewport.name} / 重要市場: expected exactly one full-width card ${selector}`);
          const dimensions = await node.evaluate(el => ({
            width: el.getBoundingClientRect().width,
            parentWidth: el.parentElement.getBoundingClientRect().width,
            gridColumn: getComputedStyle(el).gridColumn
          }));
          if (dimensions.width < dimensions.parentWidth * 0.9) {
            throw new Error(`${viewport.name} / 重要市場: card is not full width: ${selector} ${JSON.stringify(dimensions)}`);
          }
        }
        const reportNews = await page.evaluate(() => window.DASHBOARD_DATA?.news || []);
        if (!reportNews.length) throw new Error(`${viewport.name} / 重要市場: DATA_REPORT news payload is empty`);
        const missingTitles = reportNews.filter(item => item.t && !marketText.includes(item.t)).map(item => item.t);
        if (missingTitles.length) throw new Error(`${viewport.name} / 重要市場: news cards do not display every DATA_REPORT title: ${missingTitles.join(" | ")}`);
      }
      if (tab.key === "futures") {
        const futuresText = await page.locator("#main-content").innerText();
        const requiredExplanations = [
          "開＝開盤、H＝最高、L＝最低、C＝收盤",
          "淨未平倉部位（淨 OI）",
          "屬於持倉存量",
          "日夜盤淨交易流量另行呈現",
          "往正方向移動",
          "往負方向移動",
          "交易流量",
          "持倉存量",
          "期貨高於現貨為正價差",
          "第一步｜觸發",
          "第二步｜確認",
          "第三步｜失效"
        ];
        const missingExplanations = requiredExplanations.filter(item => !futuresText.includes(item));
        if (missingExplanations.length) {
          throw new Error(`${viewport.name} / 期貨: missing plain-language explanations or decision steps: ${missingExplanations.join(", ")}`);
        }
        const flowDecisionStates = [
          "夜盤 K 棒開收方向與外資夜盤淨流量同向",
          "夜盤 K 棒開收方向與外資夜盤淨流量背離",
          "夜盤外資淨交易為零",
          "外資日盤或夜盤淨交易資料缺值",
          "期貨日盤漲跌或夜盤開收價資料不足"
        ];
        if (!flowDecisionStates.some(item => futuresText.includes(item))) {
          throw new Error(`${viewport.name} / 期貨: flow guidance is not linked to the actual same-session price-flow state`);
        }
        if (!futuresText.includes("目前 Dashboard 只有當期 OI 存量")) {
          throw new Error(`${viewport.name} / 期貨: OI text must disclose that historical comparable inventory is unavailable`);
        }
        if (!futuresText.includes("日盤流量：") || !futuresText.includes("夜盤流量：")) {
          throw new Error(`${viewport.name} / 期貨: night scenario must summarize both futures session flows`);
        }
        const futuresGrid = page.locator("#main-content .v9-futures-grid");
        if (await futuresGrid.count() !== 1) {
          throw new Error(`${viewport.name} / 期貨: expected exactly one preserved futures grid`);
        }
        const futuresColumns = await futuresGrid.evaluate(el => getComputedStyle(el).gridTemplateColumns.trim().split(" ").length);
        const expectedColumns = viewport.width >= 768 ? 2 : 1;
        if (futuresColumns !== expectedColumns) {
          throw new Error(`${viewport.name} / 期貨: expected ${expectedColumns} column(s) at ${viewport.width}px, got ${futuresColumns}`);
        }
      }
      if (tab.key === "options") {
        const optionsText = await page.locator("#main-content").innerText();
        const requiredOptions = [
          "選擇權整體判讀",
          "成交與 PCR 結構",
          "OI 集中與關鍵價位",
          "法人與大額交易人",
          "GEX 曝險分布",
          "PCR／成交量結構",
          "主要 OI 集中",
          "Call OI 分布 Top10",
          "Put OI 分布 Top10",
          "選擇權法人交易",
          "前十大選擇權",
          "履約價 GEX 分布",
          "分析",
          "判斷",
          "操作"
        ];
        const missingOptions = requiredOptions.filter(section => !optionsText.includes(section));
        if (missingOptions.length) throw new Error(`${viewport.name} / 選擇權: missing sections: ${missingOptions.join(", ")}`);
        const optionSections = page.locator("#main-content .v9-option-section");
        const sectionCount = await optionSections.count();
        if (sectionCount !== 4) throw new Error(`${viewport.name} / 選擇權: expected 4 analysis sections, got ${sectionCount}`);
        const oiCompareChart = page.locator('#main-content canvas[data-chart="oi-call-put-comparison"]');
        if (await oiCompareChart.count() !== 1) throw new Error(`${viewport.name} / 選擇權: missing dedicated Call／Put OI comparison chart`);
        const oiSingleSideCharts = page.locator('#main-content canvas[data-chart="oi-single-side-distribution"]');
        if (await oiSingleSideCharts.count() !== 2) throw new Error(`${viewport.name} / 選擇權: expected separate Call／Put OI Top10 charts, got ${await oiSingleSideCharts.count()}`);
        const optionChartWidths = await page.locator("#main-content .v9-option-section canvas").evaluateAll((nodes, maxWidth) => nodes.map(node => ({ width: Math.round(node.getBoundingClientRect().width), maxWidth })), viewport.width);
        if (optionChartWidths.some(item => item.width < 1 || item.width > item.maxWidth)) throw new Error(`${viewport.name} / 選擇權: invalid responsive chart widths: ${JSON.stringify(optionChartWidths)}`);
        const oiChartColors = await oiCompareChart.evaluate(canvas => {
          const ctx = canvas.getContext("2d");
          if (!ctx || !canvas.width || !canvas.height) return { red: 0, green: 0 };
          const pixels = ctx.getImageData(0, 0, canvas.width, canvas.height).data;
          let red = 0, green = 0;
          for (let i = 0; i < pixels.length; i += 4) {
            const [r, g, b, a] = pixels.slice(i, i + 4);
            if (a > 0 && r > 150 && g < 150 && b < 170) red++;
            if (a > 0 && g > 120 && r < 150 && b < 190) green++;
          }
          return { red, green };
        });
        if (oiChartColors.red < 3 || oiChartColors.green < 3) {
          throw new Error(`${viewport.name} / 選擇權: OI comparison chart must visibly render both Call(red) and Put(green) series; pixels=${JSON.stringify(oiChartColors)}`);
        }
        const volumeShareChart = page.locator('#main-content canvas[data-chart="option-volume-share"]');
        if (await volumeShareChart.count() !== 1) throw new Error(`${viewport.name} / 選擇權: missing PCR／成交量占比 chart`);
        const volumeShareColors = await volumeShareChart.evaluate(canvas => {
          const ctx = canvas.getContext("2d");
          if (!ctx || !canvas.width || !canvas.height) return { blue: 0, yellow: 0 };
          const pixels = ctx.getImageData(0, 0, canvas.width, canvas.height).data;
          let blue = 0, yellow = 0;
          for (let i = 0; i < pixels.length; i += 4) {
            const [r, g, b, a] = pixels.slice(i, i + 4);
            if (a > 0 && r >= 65 && r <= 155 && g > 135 && b > 195) blue++;
            if (a > 0 && r > 220 && g > 165 && g < 240 && b < 130) yellow++;
          }
          return { blue, yellow };
        });
        if (volumeShareColors.blue < 20 || volumeShareColors.yellow < 20) {
          throw new Error(`${viewport.name} / 選擇權: PCR／成交量占比 chart must visibly render both Call(blue) and Put(yellow) bars; pixels=${JSON.stringify(volumeShareColors)}`);
        }
        const optionCards = page.locator("#main-content .v9-option-section .group.relative");
        const optionCardCount = await optionCards.count();
        if (optionCardCount !== 8) throw new Error(`${viewport.name} / 選擇權: expected 8 existing analysis cards, got ${optionCardCount}`);
        const optionLinks = page.locator("#main-content .v9-decision-chain a");
        const optionLinkCount = await optionLinks.count();
        if (optionLinkCount !== 4) throw new Error(`${viewport.name} / 選擇權: expected 4 analysis navigation cards, got ${optionLinkCount}`);
        const invalidOptionLinks = await optionLinks.evaluateAll(nodes => nodes.filter(node => {
          const href = node.getAttribute("href");
          return !href?.startsWith("#v9-option-step-") || !document.querySelector(href) || node.innerText.trim().length < 30;
        }).map(node => ({ href: node.getAttribute("href"), text: node.innerText.trim() })));
        if (invalidOptionLinks.length) throw new Error(`${viewport.name} / 選擇權: invalid analysis navigation targets: ${JSON.stringify(invalidOptionLinks)}`);
        const optionsSummary = page.locator("#main-content .group.relative").first();
        const summaryText = await optionsSummary.innerText();
        const requiredCrossChecks = [
          "成交量反映當日交易活躍度",
          "OI PCR 與履約價分布反映未平倉存量",
          "日夜盤法人合計方向相反",
          "最大正曝險",
          "最大負曝險",
          "OI／GEX 履約價",
          "只有價格確認、法人日夜盤流量未持續背離"
        ];
        const missingCrossChecks = requiredCrossChecks.filter(item => !summaryText.includes(item));
        if (missingCrossChecks.length) throw new Error(`${viewport.name} / 選擇權: missing integrated synthesis checks: ${missingCrossChecks.join(", ")}`);
        for (const sectionIndex of [0, 3]) {
          const sectionGrid = optionSections.nth(sectionIndex).locator(":scope > div").nth(1);
          const columns = await sectionGrid.evaluate(el => getComputedStyle(el).gridTemplateColumns.trim().split(/\s+/).length);
          if (columns !== 1) throw new Error(`${viewport.name} / 選擇權: single-card section ${sectionIndex + 1} must use one full-width column, got ${columns}`);
        }
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
          "多方觸發",
          "空方觸發",
          "流量確認門檻",
          "因子交叉檢查",
          "日夜盤確認",
          "劇本失效",
          "風險控制",
          "分析步驟",
          "外資同一法人群跨市場",
          "全體法人背景"
        ];
        const missingSections = requiredSections.filter(section => !synthesisText.includes(section));
        if (missingSections.length) {
          throw new Error(`${viewport.name} / 綜合分析: missing sections: ${missingSections.join(", ")}`);
        }
        const nightScenarioStatus = synthesisText.match(/目前分類：夜(?:漲|跌)＋外資期貨淨交易偏(?:多|空)|至少一項訊號中性，未高亮劇本|資料不足，未分類/);
        if (!nightScenarioStatus) throw new Error(`${viewport.name} / 綜合分析: missing explicit dynamic night-scenario classification status`);
        const activeScenarioBadges = await page.locator("#main-content canvas").count();
        if (activeScenarioBadges < 1) throw new Error(`${viewport.name} / 綜合分析: missing night-scenario chart canvas`);
        const activeScenarioCount = (synthesisText.match(/目前分類/g) || []).length;
        const hasDirectionalScenario = nightScenarioStatus[0].startsWith("目前分類：");
        if (activeScenarioCount !== (hasDirectionalScenario ? 1 : 0)) {
          throw new Error(`${viewport.name} / 綜合分析: expected exactly one highlighted scenario only when both directions are valid; status=${nightScenarioStatus[0]}, active labels=${activeScenarioCount}`);
        }
        const staleTradeRules = ["重新站回則取消偏空候選", "跌回其下則取消偏多候選"];
        const staleTradeText = staleTradeRules.filter(rule => synthesisText.includes(rule));
        if (staleTradeText.length) throw new Error(`${viewport.name} / 綜合分析: stale non-scenario-specific trade rules: ${staleTradeText.join(", ")}`);
        const decisionCards = page.locator(".v9-decision-chain a");
        const decisionCount = await decisionCards.count();
        if (decisionCount !== 4) throw new Error(viewport.name + " / 綜合分析: expected 4 decision navigation cards, got " + decisionCount);
        const decisionLinks = await decisionCards.evaluateAll(nodes => nodes.map(node => ({
          href: node.getAttribute("href"),
          summary: node.innerText.trim(),
          targetExists: !!document.querySelector(node.getAttribute("href"))
        })));
        const invalidDecisionLinks = decisionLinks.filter(item => !item.href?.startsWith("#v9-step-") || !item.targetExists || item.summary.length < 30);
        if (invalidDecisionLinks.length) throw new Error(viewport.name + " / 綜合分析: decision cards must have live summaries and valid in-page targets: " + JSON.stringify(invalidDecisionLinks));
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
