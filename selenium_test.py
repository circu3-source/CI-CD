from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import datetime

# 設定 Chrome 參數
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# 初始化 Driver
driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get("https://www.google.com")
    title = driver.title
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    result_text = f"[{now}] 網頁標題是: {title}\n"
    
    # 將結果附加 (append) 到 result.txt
    with open("result.txt", "a", encoding="utf-8") as f:
        f.write(result_text)
    
    print(f"成功記錄資料: {result_text}")

finally:
    driver.quit()