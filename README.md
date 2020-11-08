# アルゴリズム学習
AtCorder Problems  
Pythonで始めるアルゴリズム入門  
  
などのPythonの理解を深めるためのアルゴリズム学習記録


# ファイル構造
num = the number of problems on AtCorder Beginner Contest or ArCorder Regular Contest
problemname = the name of problems on AtCorder Beginner Contest or ArCorder Regular Contest

- atcorderproblem
    - ABC
        -  A_rank
            - num_problemname.ipynb...
        -  B_rank
        -  C_rank
        - (D_rank)
        - (E_rank)
        - (F_rank)
   - ARC
        - (A_rank)
        - (B_rank)
        - (C_rank)
        - (D_rank)
        - (E_rank)
        - (F_rank)
- algorithm_problem
   - fibonacci
   - fizz_buzz_problem
   - prime_num
   - radix_convert
   - vendingmachine_problem
 

# 参考資料
[AtCorder URL](https://atcoder.jp/)

[AtCorder Problems URL](https://kenkoooo.com/atcoder/#/table/)

[Pythonではじめるアルゴリズム入門ー伝統的なアルゴリズムで学ぶ定石と計算量](https://www.amazon.co.jp/Python%E3%81%A7%E3%81%AF%E3%81%98%E3%82%81%E3%82%8B%E3%82%A2%E3%83%AB%E3%82%B4%E3%83%AA%E3%82%BA%E3%83%A0%E5%85%A5%E9%96%80-%E4%BC%9D%E7%B5%B1%E7%9A%84%E3%81%AA%E3%82%A2%E3%83%AB%E3%82%B4%E3%83%AA%E3%82%BA%E3%83%A0%E3%81%A7%E5%AD%A6%E3%81%B6%E5%AE%9A%E7%9F%B3%E3%81%A8%E8%A8%88%E7%AE%97%E9%87%8F-%E5%A2%97%E4%BA%95-%E6%95%8F%E5%85%8B-ebook/dp/B0822N5RMS/ref=sr_1_2?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&dchild=1&keywords=python+%E3%82%A2%E3%83%AB%E3%82%B4%E3%83%AA%E3%82%BA%E3%83%A0&qid=1603549421&sr=8-2) 
- 増井 敏克 著
- 形式：書籍
- 発売日：2020年01月24日
- ISBN：9784798163239
- 定価：本体2,200円＋税
- 仕様：A5・288ページ
- 分類：プログラミング・開発


# 目次 (Pythonではじめるアルゴリズム入門ー伝統的なアルゴリズムで学ぶ定石と計算量)
### 第1章　Pythonの基本とデータ構造を知る
- 1.1　プログラミング言語の選択
- 1.2　プログラミング言語Pythonの概要
- 1.3　四則演算と優先順位
- 1.4　変数と代入、リスト、タプル
- 1.5　文字と文字列
- 1.6　条件分岐と繰り返し
- 1.7　リスト内包表記
- 1.8　関数とクラス
- 理解度Check！

### 第2章　基本的なプログラムを作ってみる
- 2.1　フローチャートを描く
- 2.2　FizzBuzzを実装する
- 2.3　自動販売機でお釣りを計算する　
- 2.4　基数を変換する
- 2.5　素数を判定する
- 2.6　フィボナッチ数列を作る
- 理解度Check！

### 第3章　計算量について学ぶ
- 3.1　計算コストと実行時間、時間計算量
- 3.2　データ構造による計算量の違い
- 3.3　アルゴリズムの計算量と問題の計算量
- 理解度Check！

### 第4章　いろいろな探索方法を学ぶ
- 4.1　線形探索
- 4.2　二分探索
- 4.3　木構造での探索
- 4.4　さまざまな例を実装する
- 理解度Check！

### 第5章　データの並べ替えにかかる時間を比べる
- 5.1　身近な場面でも使われる「並べ替え」とは？
- 5.2　選択ソート　
- 5.3　挿入ソート
- 5.4　バブルソート
- 5.5　ヒープソート
- 5.6　マージソート
- 5.7　クイックソート
- 5.8　処理速度を比較する
- 理解度Check！

### 第6章　実務に役立つアルゴリズムを知る
- 6.1　最短経路問題とは？
- 6.2　ベルマン・フォード法
- 6.3　ダイクストラ法
- 6.4　A*アルゴリズム
- 6.5　文字列探索の力任せ法
- 6.6　Boyer-Moore法
- 6.7　逆ポーランド記法
- 6.8　ユークリッドの互除法
- 理解度Check！

 
# 正誤表

| 発生刷 | ページ数 | 書籍改訂刷 | 電子書籍訂正 | 内容（誤） | 内容（訂正） |
|:---------:|:---------|:---------:|:---------:|:---------|:---------| 
| 1刷 | 006「表1.2　インタプリタとコンパイラの比較」のインタプリタのデメリット | 未 | 未 | 配布時に実行環境が必要 | 実行時に実行環境が必要 |
| 1刷 | 084図「エラトステネスの篩」内 | 未 | 未 | 上限＞奇数の先頭 | 上限≧奇数の先頭 |
| 1刷 | 084リスト2.19　eratosthenes.py　下から6行目 | 未 | 未 | while limit > data[0]: | while limit >= data[0]:|
| 1刷 | 112問題1の（3）上から7行目 | 未 | 未 | result += plus_minus * 4 / (i * 2 - 1) | result += plus_minus * 4 / (i * 2 + 1) |
| 1刷 | 117図「線形探索」内 | 未 | 未 | 位値を返す | 位置を返す |

