import pandas as pd

# 読み込むCSVファイル名（事前にKABU+からダウンロードしたものを指定）
input_file = "japan-all-stock-prices-2_20250502.csv"

# 保存するファイル名
output_file = "yutai_filtered.csv"

# CSV読み込み
df = pd.read_csv(input_file)

# 優待情報が含まれている行だけを抽出（「優待」という列が存在する前提）
if "優待" in df.columns:
    yutai_df = df[df["優待"].notna()]  # 空欄じゃないところだけ
else:
    print("優待列が見つかりません。列名を確認してください。")
    exit()

# フィルタした結果を保存
yutai_df.to_csv(output_file, index=False)
print(f"✅ フィルタ完了！{output_file} に保存しました。")
