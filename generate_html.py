import pandas as pd

# フィルタ済みCSVを読み込み
<<<<<<< HEAD
<<<<<<< HEAD

df = pd.read_csv("filtered_rimawari.csv")

>>>>>>> a263ef4 (first commit)
=======
csv_file = "filtered_rimawari.csv"
df = pd.read_csv(csv_file)

# HTMLに変換（テーブル形式）
html_table = df.to_html(index=False, classes="table", border=0, justify="center")
>>>>>>> ed36ecf (WIP: 一時コミット)

# HTML全体に整形
html_page = f"""
<!DOCTYPE html>
<<<<<<< HEAD
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
=======
<html lang=\"ja\">
>>>>>>> ed36ecf (WIP: 一時コミット)
<head>
    <meta charset=\"UTF-8\">
    <title>kabupicks - 高配当株リスト</title>
    <style>
        body {{ font-family: sans-serif; padding: 2rem; background-color: #f9f9f9; }}
        h1 {{ text-align: center; }}
<<<<<<< HEAD
        .table {{ width: 100%; border-collapse: collapse; background-color: white; }}
>>>>>>> ed36ecf (WIP: 一時コミット)
        .table th, .table td {{ border: 1px solid #ddd; padding: 8px; text-align: center; }}
        .table th {{ background-color: #f2f2f2; }}
    </style>
</head>
<body>
<<<<<<< HEAD
<<<<<<< HEAD
    <h1>配当利回り3%以上の高配当株リスト</h1>
    {html_table}

>>>>>>> a263ef4 (first commit)
=======
    <h1>配当利回り3%以上の高配当株リスト</h1>
    {html_table}
>>>>>>> ed36ecf (WIP: 一時コミット)
</body>
</html>
"""

# 書き出し
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_page)

<<<<<<< HEAD
<<<<<<< HEAD
print("✅ HTMLファイル(index.html)を作成しました！")
>>>>>>> a263ef4 (first commit)
=======
print("✅ index.html を作成しました！")
>>>>>>> ed36ecf (WIP: 一時コミット)

# ① CSVを自動で生成する処理（ダミー例）
import pandas as pd

# ここでスクレイピングやAPI処理などでデータ取得
data = {
    "銘柄": ["A社", "B社"],
    "配当利回り": [3.2, 4.1]
}
df = pd.DataFrame(data)
df.to_csv("filtered_rimawari.csv", index=False)

# ② HTML変換処理（既存の処理）
df = pd.read_csv("filtered_rimawari.csv")
html_table = df.to_html(index=False, classes="table", border=0, justify="center")
html_page = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <title>kabupicks - 高配当株リスト</title>
  <style>
    body {{ font-family: sans-serif; padding: 2rem; background-color: #f9f9f9; }}
    h1 {{ text-align: center; }}
    .table {{ width: 100%; border-collapse: collapse; background-color: white; }}
  </style>
</head>
<body>
  <h1>配当利回り3%以上の高配当株リスト</h1>
  {html_table}
</body>
</html>"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_page)

