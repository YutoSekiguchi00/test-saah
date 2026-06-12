"""
my_test_lib.py

AWS Lambda Layer の動作確認用の簡易独自ライブラリdayodayodayodayo
"""

from datetime import datetime, timezone


__version__ = "0.1.0"


def hello(name="Lambda"):
    """
    挨拶メッセージを返す
    """
    return f"Hello, {name}! This message is from my_test_lib."


def add_numbers(a, b):
    """
    数値を加算する
    """
    return a + b


def get_timestamp():
    """
    UTC時刻を返す
    """
    return datetime.now(timezone.utc).isoformat()


def make_response(message, success=True, data=None):
    """
    Lambda向けレスポンス形式を作成
    """
    return {
        "success": success,
        "message": message,
        "timestamp": get_timestamp(),
        "data": data or {}
    }


def health_check():
    """
    ライブラリ疎通確認用
    """
    return {
        "status": "OK",
        "library": "my_test_lib",
        "version": __version__
    }
