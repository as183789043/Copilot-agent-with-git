# FastAPI 簡易服務專案開發規格

## 1. 專案目標
本專案目的是建立一個最小可運行的 FastAPI 服務，提供基本數學運算 API，作為團隊學習 Git Flow、API 設計、測試與 CI/CD 的示範項目。

預計功能如下：
- 兩數相加（add）
- 兩數相減（subtract）
- 兩數相乘（multiply）
- 兩數相除（divide）

本版本優先實作加法，後續版本逐步擴充其他運算。

---

## 2. 專案結構

```text
Copilot-agent-with-git/
├── .github/
│   └── copilot-instructions.md      # AI/開發規範
├── src/
│   └── main.py                       # FastAPI 應用程式入口
├── test/
│   ├── test_add.py                   # 加法測試
│   ├── test_subtract.py              # 減法測試
│   ├── test_multiply.py              # 乘法測試
│   └── test_divide.py                # 除法測試
├── .gitignore
├── README.md
├── pyproject.toml
├── poetry.lock
└── .venv/                            # Poetry/虛擬環境（本地）
```

---

## 3. 技術選型
- Python 3.12+
- FastAPI
- Pydantic
- Poetry 作為依賴與環境管理工具
- pytest 作為測試框架
- GitHub Actions 作為 CI/CD 流程
- OpenAPI / Swagger UI /docs 供 API 文件與測試

---

## 4. API 設計規格

### 4.1 應用入口
- 應用建立方式：`FastAPI()`
- 專案名稱：`Add Service` 或專案名稱的對應描述
- 版本：`0.1.0`
- API 文件路徑：`/docs`
- OpenAPI 文件路徑：`/openapi.json`

### 4.2 健康檢查
- Route: `GET /`
- 用途：確認服務正在運行
- 回應範例：

```json
{
  "message": "Add API is running"
}
```

### 4.3 加法 API
- Route: `POST /add`
- 請求格式：JSON body
- 請求範例：

```json
{
  "a": 10,
  "b": 20
}
```

- 回應格式：

```json
{
  "a": 10,
  "b": 20,
  "result": 30
}
```

- 計算規則：`result = a + b`
- 支援型別：整數與浮點數
- 若輸入不是數字，應由 Pydantic 產生 HTTP 422 錯誤

### 4.4 未來擴充 API
後續版本預計新增：
- `POST /subtract`
- `POST /multiply`
- `POST /divide`

每個 API 需遵循一致格式：
- 請求兩個參數
- 回應包含 `a`, `b`, `result`
- 若除數為 0 必須明確回傳錯誤

---

## 5. 程式設計規範

### 5.1 Python 程式碼規範
- 使用 Python 3.12 語法
- 保持程式簡潔且可讀
- 函式命名使用 snake_case
- 類別命名使用 PascalCase
- 常數使用大寫命名
- 所有 API 需有明確的 type hints

### 5.2 FastAPI 實作規範
- API 應使用 Pydantic model 進行資料驗證
- 每個 route 應明確定義 summary / description
- 返回資料應使用 response model
- 處理錯誤時盡量讓 FastAPI 自動產生標準 HTTP 錯誤回應

### 5.3 專案責任區分
- `src/main.py`：僅負責 API 初始化與路由定義
- 若後續功能增加，應拆分為 router / schema / service 層
- 避免將所有邏輯塞進主檔案

---

## 6. 測試要求

### 6.1 測試框架
- 使用 `pytest`
- 每個 API 應有至少 3 個主要測試案例：
  - 正常數值
  - 邊界值
  - 非法輸入

### 6.2 測試案例範例
對 `POST /add` 的測試應包含：
1. `{"a": 2, "b": 3}` => `result == 5`
2. `{"a": -1, "b": 5}` => `result == 4`
3. `{"a": 2.5, "b": 3.5}` => `result == 6.0`
4. `{"a": "abc", "b": 2}` => HTTP 422

### 6.3 測試結果保存
- 測試執行後，需產生測試結果檔案
- 建議儲存路徑：`assets/` 或 `test-results/`
- 可使用 pytest-html / JUnit XML / coverage report 等格式
- 檔案需在 PR 中可被檢視

### 6.4 測試執行命令
請使用下列方式執行：

```bash
poetry run pytest
```

若需要產生覆蓋率：

```bash
poetry run pytest --cov=src --cov-report=term-missing
```

---

## 7. Git Flow 分支規則

### 7.1 分支命名規則
- `main`：正式主分支，僅接受已驗證之合併
- `feature/xxx`：功能開發分支
- `fix/xxx`：錯誤修正分支
- `docs/xxx`：文件更新分支

### 7.2 分支策略
- 禁止直接 push 到 `main`
- 所有功能開發都需透過分支建立後，再提交 Pull Request
- `main` branch 由專案負責人或 maintainer 進行合併

### 7.3 PR 規範
- 每個 PR 需包含：
  - 說明本次修改目的
  - 影響範圍
  - 測試方式
  - 是否涉及 API 變更
- PR 需至少有一位 reviewer 審查
- 若測試失敗，不得合併

---

## 8. CI/CD 規範

### 8.1 GitHub Actions
專案需有 CI 流程，自動執行：
- 安裝依賴
- 啟動測試
- 執行 pytest
- 收集測試結果
- 上傳報告檔案

### 8.2 目標行為
每次 push 或 PR 時：
- 自動執行測試
- 若測試失敗，標記 workflow 為失敗
- 若測試成功，保留結果供檢查

### 8.3 建議的 CI 流程
1. 安裝 Poetry
2. `poetry install`
3. `poetry run pytest`
4. 上傳 coverage / test report

---

## 9. 版本控制與提交規範

### 9.1 提交訊息規範
使用清楚的提交訊息，例如：
- `feat: add arithmetic API endpoint`
- `test: add unit tests for add endpoint`
- `docs: update API usage instructions`
- `fix: resolve divide by zero validation`

### 9.2 提交要求
- 每次提交應只處理一個主題
- 不要混入無關調整
- 變更前先確認測試是否可執行

---

## 10. README 與文件要求
- README 必須說明：
  - 專案用途
  - 安裝方式
  - 啟動方式
  - API 路由列表
  - Swagger /docs 範例
  - 測試指令

---

## 11. 設計原則
- 保持第一版簡單、可讀、可測試
- 先做最小可用功能，再迭代
- 避免過度工程化
- 一切設計應以 API 可用性與團隊協作效率為優先

---

## 12. 開發順序建議
1. 建立 FastAPI app
2. 實作 `GET /`
3. 實作 `POST /add`
4. 建立 pytest 測試
5. 確認 `/docs` 可正常顯示
6. 推送至 feature branch
7. 開 PR
8. CI 測試通過後進行合併

---

## 13. 允許與禁止事項

### 允許
- 使用 FastAPI 自帶的 OpenAPI 文件
- 使用 Pydantic 進行請求驗證
- 使用 Poetry 管理依賴
- 加入測試與 CI 驗證

### 禁止
- 直接 push 到 `main`
- 不寫測試直接提交功能
- 不更新 README 或 API 文件
- 不使用過度複雜架構做第一版

---

## 14. 交付標準
本專案視為完成的最低標準：
- FastAPI 應用可成功啟動
- `POST /add` 可正常計算
- Swagger UI 能顯示並測試 API
- 至少有基本 pytest 測試覆蓋
- 代碼已推到 feature branch 並準備 PR

---

## 15. 最終目標
希望此專案成為一個簡單且具教育意義的 FastAPI 範例，讓團隊能同時練習：
- API 開發
- 測試驅動
- Git Flow 管理
- 自動化 CI/CD
- OpenAPI 文件撰寫
