import pandas as pd

# CSV読み込み
df = pd.read_csv("japan-all-stock-data_20250502.csv")

# 列を数値に変換（エラーはNaNに）
df["配当利回り（予想）"] = pd.to_numeric(df["配当利回り（予想）"], errors='coerce')

# 3%以上のものだけ抽出
df_filtered = df[df["配当利回り（予想）"] >= 3.0]

# 結果を保存
df_filtered.to_csv("filtered_rimawari.csv", index=False)

print("✅ 配当利回り3%以上の銘柄を抽出しました！")
