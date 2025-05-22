from scraper import scrape_amazon_product

url = "https://www.amazon.in/dp/B0DMFDNDD5/?_encoding=UTF8&ref_=cct_cg_Budget_2b1&pf_rd_p=e8815a08-bffe-481f-9fa4-ec1eea68e8db&pf_rd_r=T4NPTGFVXESD1ZF9E7AP&th=1"  
result = scrape_amazon_product(url)
print(result)