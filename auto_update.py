import pandas as pd
from datetime import datetime
import os

# Step 1: CSVデータを作成（ここは将来、APIやスクレイピングに置き換え可能）
data = {
    "銘柄": ["A社", "B社", "C社"],
    "配当利回り": [3.5, 4.2, 3.1],
    "株価": [1234, 980, 1520]
}
df = pd.DataFrame(data)
df.to_csv("filtered_rimawari.csv", index=False)

# Step 2: HTMLを生成
html_table = df.to_html(index=False, classes="table", border=0, justify="center")
today_str = datetime.today().strftime("%Y年%-m月%-d日")

html_page = f"""<!DOCTYPE html>
<html lang=\"ja\">
<head>
  <meta charset=\"UTF-8\">
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
  <title>kabupicks - 高配当株リスト</title>
  <style>
    body {{
      font-family: sans-serif;
      background-color: #f5f5f5;
      padding: 20px;
    }}
    h1 {{
      text-align: center;
      color: #333;
    }}
    .description {{
      text-align: center;
      font-size: 1rem;
      margin-bottom: 1.5rem;
      color: #555;
    }}
    table {{
      margin: 0 auto;
      width: 90%;
      border-collapse: collapse;
      background-color: white;
    }}
    th, td {{
      padding: 10px;
      border: 1px solid #ccc;
      text-align: center;
    }}
    th {{
      background-color: #f0f0f0;
    }}
  </style>
</head>
<body>
  <h1>📈 配当利回り3%以上の企業一覧</h1>
  <p class=\"description\">はじめての資産運用を考える大学生向けに、「配当金でお金を増やす」企業をまとめました（{today_str}更新）</p>
  {html_table}
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_page)

print("✅ index.html を生成しました！")

# Step 3: Gitで自動push
os.system("git add .")
os.system("git commit -m '✅ 自動更新: 配当利回りHTML反映'")
os.system("git push origin main")
