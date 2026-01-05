from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 設定 Chrome 參數
chrome_options = Options()
chrome_options.add_argument('--headless')  # 必備：無頭模式
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# 直接初始化 (在該 Docker 環境中，driver 已經在系統路徑裡了)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.google.com")
print(f"成功！網頁標題是: {driver.title}")
driver.quit()