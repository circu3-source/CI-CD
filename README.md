Python Selenium 雲端自動化爬蟲 (CI/CD 專案)
這是一個結合 Python Selenium、Docker 與 GitHub Actions 的自動化爬蟲專案。透過 CI/CD 流程，實現了「環境隔離」與「雲端定時排程執行」。

🚀 專案特點
環境隔離：使用 Docker 封裝 Chrome 瀏覽器與 Python 環境，解決「我電腦能跑、伺服器不能跑」的問題。

雲端自動化：透過 GitHub Actions，即使本機電腦關機，程式仍會自動在雲端運行。

定時排程：設定為每小時的 0 分鐘自動觸發執行。

🛠 技術棧
語言：Python 3.9+

工具：Selenium (Headless Mode)

容器化：Docker

自動化平台：GitHub Actions
檔案結構說明
selenium_test.py: 爬蟲主程式，已配置無頭模式 (Headless) 以符合容器執行環境。

Dockerfile: 定義了包含 Chrome 瀏覽器的執行環境映像檔。

requirements.txt: 列出專案所需的 Python 套件 (如 selenium)。

.github/workflows/run_scraper.yml: GitHub Actions 設定檔，負責定時排程與自動化流程。

🤖 自動化流程 (GitHub Actions)
目前腳本設定了三種觸發方式：

Push 觸發：當程式碼推送到 main 分支時自動執行。

定時觸發：每小時執行一次 (0 * * * *)。

手動觸發：可在 GitHub 網頁的 Actions 分頁手動點擊 Run workflow 執行。

💻 本機開發指令
如果你想在自己的電腦測試，請確保已安裝 Docker 並執行：

Bash

# 1. 構建映像檔
docker build -t my-scraper .

# 2. 執行容器
docker run my-scraper
