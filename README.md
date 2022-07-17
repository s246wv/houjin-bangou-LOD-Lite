# 法人番号LOD-Lite
## 説明
法人番号は、日本で登記されている会社や団体を識別するための番号です。国税庁は、法人番号公表サイトにおいて、法人番号を用いた企業情報を提供しています。以前、IgataさんとMorikawaさんは法人番号のLOD版として[日本の法人LOD](http://idea.linkdata.org/idea/idea1s1417i)を発表しました。「日本の法人LOD」は、様々な標準スキーマを用いてデータセットを整理するためによく設計されていました。しかし、このデータセットには、現在、アクセスすることができません。このような背景から、私は法人番号の情報をLinked Dataとして利用したいと考えています。そこで、このシンプルなデータセットを作成しました。しかし，以下のような不足があることが分かっています．どなたかこのデータセットを改良していただければ幸いです。

## データセットの既知の不足
1. **スキーマの不足**  
   このデータセットでは、オリジナルのプロパティを定義なしで使用しています。他のオントロジーやリンクデータから利益を得ることはできません。
2. **他のリソースとのリンクがない**  
   このデータセットは法人番号の情報のみによって作成されています。他のリソースとのリンクは一切行っていません。そのため、まだ「LOD」とは言えないかもしれません。
3. **メンテナ不足**  
   私はこのデータセットをメンテナンスする予定を持っていません。誰かがこのデータセットを維持するか、あるいは、より優れた法人番号のLODバージョンを発表してくれることを願っています。 

## Pythonスクリプトの使い方

自分でttlファイルを作成する場合は、pythonスクリプトのhoujinLOD.pyを使用してください。
1. csvファイルを、https://www.houjin-bangou.nta.go.jp/ からダウンロードしてください。 
2. 必要なパッケージをインストールします。
3. [houjinLOD.pyの9行目](https://github.com/s246wv/houjin-bangou-LOD-Lite/blob/98ce1b75d8462f40ed17de9a5afb657f4bd5e21b/houjinLOD.py#L9)を、ダウンロードしたファイル名に合わせて編集してください。
4. 動かしてください．

*このスクリプトは、かなりストレートに作成しているため、多くのメモリを必要とするのかもしれません。どなたか、より洗練されたコードに改良していただければ幸いです。*

## 必要なパッケージ
pandas  
rdflib  

## 謝辞
このデータセットの作成にあたり、以下の方々に感謝します。

- [国税庁 法人番号公表サイト](https://www.houjin-bangou.nta.go.jp/)
- [PURL service](https://purl.archive.org/) provided by an initiative of the [Internet Archive](http://archive.org/)

## ライセンス 
法人番号LOD-Lite は https://www.houjin-bangou.nta.go.jp/riyokiyaku/ に基づいて [Creative Commons Attribution-4.0 International License.](https://creativecommons.org/licenses/by/4.0/) で提供されます。