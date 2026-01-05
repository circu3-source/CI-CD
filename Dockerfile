# 使用內建 Chrome 與 Driver 的官方映像檔 (這能省去你手動安裝瀏覽器的麻煩)
FROM joyzoursky/python-chromedriver:3.9-selenium

WORKDIR /app

# 1. 複製依賴清單並安裝
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 2. 複製程式碼
COPY . .

# 3. 執行
CMD ["python", "selenium_test.py"]