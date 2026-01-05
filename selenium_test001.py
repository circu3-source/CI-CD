import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options # 匯入 Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# --- 設定變數 ---
TARGET_URL = "https://www.google.com"
SEARCH_TERM = "top 10 news"
SEARCH_BOX_LOCATOR = 'q' 

# --- 步驟一：設定反偵測選項 ---
chrome_options = Options()
chrome_options.add_argument("--incognito") # 使用無痕模式
chrome_options.add_argument("--disable-blink-features=AutomationControlled") # 禁用自動化控制功能

# --- 初始化 WebDriver ---
driver = None
try:
    service = ChromeService(ChromeDriverManager().install())
    # 將 options 傳入
    driver = webdriver.Chrome(service=service, options=chrome_options) 
    driver.maximize_window() 
    print("瀏覽器成功開啟 (無痕模式)。")

    # 在導航前執行 JavaScript，隱藏 WebDriver 標記
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    
    # 步驟二：導航到 Google 首頁
    driver.get(TARGET_URL)
    print(f"成功導航到：{TARGET_URL}")

    # ... 後續的搜尋步驟保持不變 ...
    
    wait = WebDriverWait(driver, 10) 
    print("正在等待 Google 搜尋框出現...")
    
    search_box = wait.until(
        EC.presence_of_element_located((By.NAME, SEARCH_BOX_LOCATOR))
    )
    
    print(f"在搜尋框輸入：'{SEARCH_TERM}'")
    search_box.send_keys(SEARCH_TERM)
    
    search_box.send_keys(Keys.ENTER)
    print("成功按下 Enter 鍵執行搜尋！")

    # 保持開啟觀察結果
    print("腳本執行完畢，瀏覽器將保持開啟 5 秒供您觀察搜尋結果。")
    time.sleep(5) 
    
except Exception as e:
    print("\n發生錯誤！")
    print(f"錯誤類型: {type(e).__name__}")
    print(f"詳細訊息: {e}")
    
finally:
    if driver:
        driver.quit()
        print("\n瀏覽器已關閉。")