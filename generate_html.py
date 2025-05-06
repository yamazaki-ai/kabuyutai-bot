import pandas as pd

# フィルタ済みCSVを読み込み
csv_file = "filtered_rimawari.csv"
df = pd.read_csv(csv_file)

# HTMLに変換（テーブル形式）
html_table = df.to_html(index=False, classes="table", border=0, justify="center")

# HTML全体に整形
html_page = f"""
<!DOCTYPE html>
<html lang=\"ja\">
<head>
    <meta charset=\"UTF-8\">
    <title>kabupicks - 高配当株リスト</title>
    <style>
        body {{ font-family: sans-serif; padding: 2rem; background-color: #f9f9f9; }}
        h1 {{ text-align: center; }}
        .table {{ width: 100%; border-collapse: collapse; background-color: white; }}
        .table th, .table td {{ border: 1px solid #ddd; padding: 8px; text-align: center; }}
        .table th {{ background-color: #f2f2f2; }}
    </style>
</head>
<body>
    <h1>配当利回り3%以上の高配当株リスト</h1>
    {html_table}
</body>
</html>
"""

# 書き出し
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_page)

print("✅ index.html を作成しました！")
