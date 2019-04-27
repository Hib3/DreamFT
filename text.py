#coding:utf-8

import requests
import json
import urllib

#取得したアプリケーションIDを指定
appid = "dj00aiZpPXUyOHg5aTlsRXhkaSZzPWNvbnN1bWVyc2VjcmV0Jng9MGE-"

#キーフレーズ抽出APIのURL
pageurl = "https://jlp.yahooapis.jp/KeyphraseService/V1/extract"

#入力文
sentence = "おはようございます。今日はとてもいい天気ですね。明日は晴れです。"

#言語分析→json出力用のURL
url = (pageurl+"?appid="+appid+"&sentence="+sentence+"&output=json")

#出力結果のリスト
words = []

#出力結果をshift-jisにエンコードし、それを文字列として扱う
shift = ''

#json取得
with requests.get(url) as fin:
    body = fin.text

json = json.loads(body)

#整形
for jsonwords,jsonscore in json.items():
    words.append(jsonwords)

print(words)
print("\n\n")

#変換後エンコードし、str型に再変換、整形後、指定文字を追加
for i in words:
    shift += str((i.encode("shift-jis"))).replace("b'", '').replace("'", '')+"+"

DreamURL = ("http://yume-uranai.jp/keyword.php?keyword="+shift+"&q=1")

print(DreamURL)

"""
今後の予定
sentenceに入る文字を、botなどを使い、ユーザーが入力した物に対応させる。
DreamURLにアクセスし、出力結果をスクレイピングしてくる。
"""