from playwright.sync_api import sync_playwright

def scrape_amazon_product(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)

        try:
            title = page.query_selector("#productTitle").inner_text().strip()
        except:
            title = "N/A"

        try:
            price = (
                page.query_selector("#priceblock_ourprice") or
                page.query_selector("#priceblock_dealprice") or
                page.query_selector(".a-price .a-offscreen")
            )
            price = price.inner_text().strip() if price else "Price Not Found"
        except:
            price = "N/A"

        try:
            image_element = page.query_selector("#imgTagWrapperId img")
            image_url = image_element.get_attribute("src") if image_element else ""
        except:
            image_url = ""

        browser.close()

        return {"title": title, "price": price, "image": image_url}