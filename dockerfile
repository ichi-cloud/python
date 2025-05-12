# ベースイメージ
FROM python:3.10-slim

# 作業ディレクトリを作成
WORKDIR /app

# 依存ファイルをコピーしてインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# アプリをコピー
COPY . .

# Flask起動（ポート5000を使用）
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]
