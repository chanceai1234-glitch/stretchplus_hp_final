const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  
  // iPhone 14 Pro Dimensions
  await page.setViewport({
    width: 393,
    height: 852,
    deviceScaleFactor: 3,
    isMobile: true,
    hasTouch: true,
  });

  const url = 'https://stretch-plus.co.jp/v2/?nocache=' + Date.now();
  console.log("Loading URL:", url);
  await page.goto(url, { waitUntil: 'networkidle0', timeout: 60000 });

  await page.screenshot({ path: '/Users/ai_stretch/.gemini/antigravity/brain/5b227e4a-2e93-4b73-b436-af64a60dd58c/local_iphone14.png', fullPage: true });

  console.log("Screenshot saved successfully!");
  await browser.close();
})();
