# ベースイメージ
FROM python:3.12-slim

# 作業ディレクトリ
WORKDIR /app

# 必要ファイルをコピー
COPY requirements.txt .
COPY . .

# パッケージインストール
RUN pip install --no-cache-dir -r requirements.txt

# ポート公開
EXPOSE 8080

# 環境変数
ENV PYTHONUNBUFFERED=1

# アプリ起動
CMD ["python", "app.py"]
