●実装内容
https://cookpad.com のhtml解析を行い、
「メーカーこだわりレシピ」の
レシピ名、レシピのURL、画像のURL、スポンサー名、スポンサー紹介ページへのURLの一覧を
jsonファイルに出力する
コマンドラインアプリケーションです。


●利用する前に
必要なライブラリをインストールします。
scraping.pyを保管しているディレクトリに移動し、下記のコマンドを実行してください。

pip3 install -r requirements.txt


●実行方法
1. URLから直接html解析を行う方法

①コマンドライン上で、scraping.pyを保管しているディレクトリに移動します。

②下記のコマンドを実行します。
すると、scrapingフォルダに入っているscraping.jsonに実行結果が登録されています。
なお、出力先のjsonファイル名は適宜変更していただいても問題ありません。

python3 scraping.py  > scraping.json 


2. まずURLからhtmlファイルを取得し、取得したhtmlファイルを解析に利用する方法
※1の方法で頻繁に実行し、短時間の間で何回もリクエストを送ると
URL先のサーバに負荷がかかりますので
開発段階では、②の方法で実行してください。


①コマンドライン上で、scraping.pyを保管しているディレクトリに移動します。

②下記のコマンドを実行し、htmlファイルを取得します。

wget https://cookpad.com

index.htmlで取得されますが、もしhtmlファイル名を変更される場合は、
scraping_from_html.pyの7行目のopenの引数を
変更したhtmlファイル名に変更してください。


④下記のコマンドを実行します。
すると、scrapingフォルダに入っているscraping.jsonに実行結果が登録されています。
なお、出力先のjsonファイル名は適宜変更していただいても問題ありません。

python3 scraping_from_html.py  > scraping.json 
