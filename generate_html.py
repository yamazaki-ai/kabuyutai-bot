import pandas as pd

# フィルタ済みCSVを読み込み
<<<<<<< HEAD
csv_file = "filtered_rimawari.csv"
df = pd.read_csv(csv_file)

# HTMLに変換（テーブル形式）
html_table = df.to_html(index=False, classes="table", border=0, justify="center")
=======
df = pd.read_csv("filtered_rimawari.csv")

# HTMLに変換（テーブル形式）
html = df.to_html(index=False, classes="table", border=0, justify="center")
>>>>>>> a263ef4 (first commit)

# HTML全体に整形
html_page = f"""
<!DOCTYPE html>
<<<<<<< HEAD
<html lang=\"ja\">
<head>
    <meta charset=\"UTF-8\">
    <title>kabupicks - 高配当株リスト</title>
    <style>
        body {{ font-family: sans-serif; padding: 2rem; background-color: #f9f9f9; }}
        h1 {{ text-align: center; }}
        .table {{ width: 100%; border-collapse: collapse; background-color: white; }}
=======
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>配当利回りフィルター銘柄</title>
    <style>
        body {{ font-family: sans-serif; padding: 2rem; }}
        h1 {{ text-align: center; }}
        .table {{ width: 100%; border-collapse: collapse; }}
>>>>>>> a263ef4 (first commit)
        .table th, .table td {{ border: 1px solid #ddd; padding: 8px; text-align: center; }}
        .table th {{ background-color: #f2f2f2; }}
    </style>
</head>
<body>
<<<<<<< HEAD
    <h1>配当利回り3%以上の高配当株リスト</h1>
    {html_table}
=======
    <h1>配当利回り3%以上の銘柄一覧</h1>
    {html}
>>>>>>> a263ef4 (first commit)
</body>
</html>
"""

# 書き出し
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_page)

<<<<<<< HEAD
print("✅ HTMLファイル(index.html)を作成しました！")
>>>>>>> a263ef4 (first commit)
