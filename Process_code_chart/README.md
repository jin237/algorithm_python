# python_code
Pythonに活用できるコードまとめ

5. データ構造
この章では、すでに学んだことについてより詳しく説明するとともに、いくつか新しいことを追加します。

5.1. リスト型についてもう少し
リストデータ型には、他にもいくつかメソッドがあります。リストオブジェクトのすべてのメソッドを以下に示します:

list.append(x)
リストの末尾に要素を一つ追加します。a[len(a):] = [x] と等価です。

list.extend(iterable)
イテラブルのすべての要素を対象のリストに追加し、リストを拡張します。a[len(a):] = iterable と等価です。

list.insert(i, x)
指定した位置に要素を挿入します。第 1 引数は、リストのインデクスで、そのインデクスを持つ要素の直前に挿入が行われます。従って、 a.insert(0, x) はリストの先頭に挿入を行います。また a.insert(len(a), x) は a.append(x) と等価です。

list.remove(x)
リスト中で x と等しい値を持つ最初の要素を削除します。該当する要素がなければ ValueError が送出されます。

list.pop([i])
リスト中の指定された位置にある要素をリストから削除して、その要素を返します。インデクスが指定されなければ、 a.pop() はリストの末尾の要素を削除して返します。この場合も要素は削除されます。 (メソッドの用法 (signature) で i の両側にある角括弧は、この引数がオプションであることを表しているだけなので、角括弧を入力する必要はありません。この表記法は Python Library Reference の中で頻繁に見ることになるでしょう。)

list.clear()
リスト中の全ての要素を削除します。del a[:] と等価です。

list.index(x[, start[, end]])
リスト中で x と等しい値を持つ最初の要素の位置をゼロから始まる添字で返します。 該当する要素がなければ ValueError が送出されます。

任意の引数である start と end はスライス記法として解釈され、リストの探索範囲を指定できます。返される添字は、start 引数からの相対位置ではなく、リスト全体の先頭からの位置になります。

list.count(x)
リストでの x の出現回数を返します。

list.sort(key=None, reverse=False)
リストの項目を、インプレース演算 (in place、元のデータを演算結果で置き換えるやりかた) でソートします。引数はソート方法のカスタマイズに使えます。 sorted() の説明を参照してください。

list.reverse()
リストの要素を、インプレース演算で逆順にします。

list.copy()
リストの浅い (shallow) コピーを返します。a[:] と等価です。

以下にリストのメソッドをほぼ全て使った例を示します:

>>>
>>> fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
>>> fruits.count('apple')
2
>>> fruits.count('tangerine')
0
>>> fruits.index('banana')
3
>>> fruits.index('banana', 4)  # Find next banana starting a position 4
6
>>> fruits.reverse()
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
>>> fruits.append('grape')
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
>>> fruits.sort()
>>> fruits
['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
>>> fruits.pop()
'pear'
insert, remove, sort などのリストを操作するメソッドの戻り値が表示されていないことに気が付いたかもしれません。これらのメソッドは None を返しています。1 これは Python の変更可能なデータ構造全てについての設計上の原則となっています。

気がつくかもしれないもう一つのことは、すべてのデータをソートまたは比較できるわけではないということです。例えば、整数は文字列と比較できず、 None は他の型と比較できないため、 [None, 'hello', 10] はソートされません。また、定義された順序関係を持たないタイプもあります。たとえば、 3+4j < 5+7j は有効な比較ではありません。

5.1.1. リストをスタックとして使う
リスト型のメソッドのおかげで、簡単にリストをスタックとして使えます。スタックでは、最後に追加された要素が最初に取り出されます ("last-in, first-out")。スタックの一番上に要素を追加するには append() を使います。スタックの一番上から要素を取り出すには pop() をインデクスを指定せずに使います。例えば以下のようにします:

>>>
>>> stack = [3, 4, 5]
>>> stack.append(6)
>>> stack.append(7)
>>> stack
[3, 4, 5, 6, 7]
>>> stack.pop()
7
>>> stack
[3, 4, 5, 6]
>>> stack.pop()
6
>>> stack.pop()
5
>>> stack
[3, 4]
5.1.2. リストをキューとして使う
リストをキュー (queue) として使うことも可能です。この場合、最初に追加した要素を最初に取り出します ("first-in, first-out")。しかし、リストでは効率的にこの目的を達成することが出来ません。追加（append）や取り出し（pop）をリストの末尾に対して行うと速いのですが、挿入（insert）や取り出し（pop）をリストの先頭に対して行うと遅くなってしまいます（他の要素をひとつずつずらす必要があるからです）。

キューの実装には、 collections.deque を使うと良いでしょう。このクラスは良く設計されていて、高速な追加（append）と取り出し（pop）を両端に対して実現しています。例えば以下のようにします:

>>>
>>> from collections import deque
>>> queue = deque(["Eric", "John", "Michael"])
>>> queue.append("Terry")           # Terry arrives
>>> queue.append("Graham")          # Graham arrives
>>> queue.popleft()                 # The first to arrive now leaves
'Eric'
>>> queue.popleft()                 # The second to arrive now leaves
'John'
>>> queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])
5.1.3. リストの内包表記
リスト内包表記はリストを生成する簡潔な手段を提供しています。主な利用場面は、あるシーケンスや iterable (イテレート可能オブジェクト) のそれぞれの要素に対してある操作を行った結果を要素にしたリストを作ったり、ある条件を満たす要素だけからなる部分シーケンスを作成することです。

例えば、次のような平方のリストを作りたいとします:

>>>
>>> squares = []
>>> for x in range(10):
...     squares.append(x**2)
...
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
これはループが終了した後にも存在する x という名前の変数を作る (または上書きする) ことに注意してください。以下のようにして平方のリストをいかなる副作用もなく計算することができます:

squares = list(map(lambda x: x**2, range(10)))
もしくは、以下でも同じです:

squares = [x**2 for x in range(10)]
これはより簡潔で読みやすいです。

リスト内包表記は、括弧の中の 式、 for 句、そして0個以上の for か if 句で構成されます。 リスト内包表記の実行結果は、 for と if 句のコンテキスト中で式を評価した結果からなる新しいリストです。 例えば、次のリスト内包表記は2つのリストの要素から、違うもの同士をペアにします。

>>>
>>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
これは次のコードと等価です:

>>>
>>> combs = []
>>> for x in [1,2,3]:
...     for y in [3,1,4]:
...         if x != y:
...             combs.append((x, y))
...
>>> combs
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
for と if 文が両方のコードで同じ順序になっていることに注目してください。

式がタプルの場合 (例: 上の例で式が (x, y) の場合) は、タプルに円括弧が必要です。

>>>
>>> vec = [-4, -2, 0, 2, 4]
>>> # create a new list with the values doubled
>>> [x*2 for x in vec]
[-8, -4, 0, 4, 8]
>>> # filter the list to exclude negative numbers
>>> [x for x in vec if x >= 0]
[0, 2, 4]
>>> # apply a function to all the elements
>>> [abs(x) for x in vec]
[4, 2, 0, 2, 4]
>>> # call a method on each element
>>> freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
>>> [weapon.strip() for weapon in freshfruit]
['banana', 'loganberry', 'passion fruit']
>>> # create a list of 2-tuples like (number, square)
>>> [(x, x**2) for x in range(6)]
[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
>>> # the tuple must be parenthesized, otherwise an error is raised
>>> [x, x**2 for x in range(6)]
  File "<stdin>", line 1, in <module>
    [x, x**2 for x in range(6)]
               ^
SyntaxError: invalid syntax
>>> # flatten a list using a listcomp with two 'for'
>>> vec = [[1,2,3], [4,5,6], [7,8,9]]
>>> [num for elem in vec for num in elem]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
リスト内包表記の式には、複雑な式や関数呼び出しのネストができます:

>>>
>>> from math import pi
>>> [str(round(pi, i)) for i in range(1, 6)]
['3.1', '3.14', '3.142', '3.1416', '3.14159']
5.1.4. ネストしたリストの内包表記
リスト内包表記中の最初の式は任意の式なので、そこに他のリスト内包表記を書くこともできます。

次の、長さ4のリスト3つからなる、3x4 の matrix について考えます:

>>>
>>> matrix = [
...     [1, 2, 3, 4],
...     [5, 6, 7, 8],
...     [9, 10, 11, 12],
... ]
次のリスト内包表記は、matrix の行と列を入れ替えます:

>>>
>>> [[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
前の節で見たように、ネストしたリスト内包表記は、続く for のコンテキストの中で評価されます。なので、この例は次のコードと等価です:

>>>
>>> transposed = []
>>> for i in range(4):
...     transposed.append([row[i] for row in matrix])
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
これをもう一度変換すると、次のコードと等価になります:

>>>
>>> transposed = []
>>> for i in range(4):
...     # the following 3 lines implement the nested listcomp
...     transposed_row = []
...     for row in matrix:
...         transposed_row.append(row[i])
...     transposed.append(transposed_row)
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
実際には複雑な流れの式よりも組み込み関数を使う方が良いです。この場合 zip() 関数が良い仕事をしてくれるでしょう:

>>>
>>> list(zip(*matrix))
[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
この行にあるアスタリスクの詳細については 引数リストのアンパック を参照してください。

5.2. del 文
リストから要素を削除する際、値を指定する代わりにインデックスを指定する方法があります。それが del 文です。これは pop() メソッドと違い、値を返しません。 del 文はリストからスライスを除去したり、リスト全体を削除することもできます(以前はスライスに空のリストを代入して行っていました)。例えば以下のようにします:

>>>
>>> a = [-1, 1, 66.25, 333, 333, 1234.5]
>>> del a[0]
>>> a
[1, 66.25, 333, 333, 1234.5]
>>> del a[2:4]
>>> a
[1, 66.25, 1234.5]
>>> del a[:]
>>> a
[]
del は変数全体の削除にも使えます:

>>>
>>> del a
この文の後で名前 a を参照すると、(別の値を a に代入するまで) エラーになります。 del の別の用途についてはまた後で取り上げます。

5.3. タプルとシーケンス
リストや文字列には、インデクスやスライスを使った演算のように、数多くの共通の性質があることを見てきました。これらは シーケンス (sequence) データ型 (シーケンス型 --- list, tuple, range を参照) の二つの例です。 Python はまだ進歩の過程にある言語なので、他のシーケンスデータ型が追加されるかもしれません。標準のシーケンス型はもう一つあります: タプル (tuple) 型です。

タプルはコンマで区切られたいくつかの値からなります。例えば以下のように書きます:

>>>
>>> t = 12345, 54321, 'hello!'
>>> t[0]
12345
>>> t
(12345, 54321, 'hello!')
>>> # Tuples may be nested:
... u = t, (1, 2, 3, 4, 5)
>>> u
((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
>>> # Tuples are immutable:
... t[0] = 88888
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> # but they can contain mutable objects:
... v = ([1, 2, 3], [3, 2, 1])
>>> v
([1, 2, 3], [3, 2, 1])
ご覧のとおり、タプルの表示には常に丸括弧がついていて、タプルのネストが正しく解釈されるようになっています。タプルを書くときは必ずしも丸括弧で囲まなくてもいいですが、(タプルが大きな式の一部だった場合は) 丸括弧が必要な場合もあります。タプルの要素を代入することはできません。しかし、タプルにリストのような変更可能型を含めることはできます。

タプルはリストと似ていますが、たいてい異なる場面と異なる目的で利用されます。タプルは 不変 で、複数の型の要素からなることもあり、要素はアンパック(この節の後半に出てきます)操作やインデックス (あるいは namedtuples の場合は属性)でアクセスすることが多いです。一方、リストは 可変 で、要素はたいてい同じ型のオブジェクトであり、たいていイテレートによってアクセスします。

問題は 0 個または 1 個の項目からなるタプルの構築です。これらの操作を行うため、構文には特別な細工がされています。空のタプルは空の丸括弧ペアで構築できます。一つの要素を持つタプルは、値の後ろにコンマを続ける (単一の値を丸括弧で囲むだけでは不十分です) ことで構築できます。美しくはないけれども、効果的です。例えば以下のようにします:

>>>
>>> empty = ()
>>> singleton = 'hello',    # <-- note trailing comma
>>> len(empty)
0
>>> len(singleton)
1
>>> singleton
('hello',)
文 t = 12345, 54321, 'hello!' は タプルのパック (tuple packing) の例です。値 12345, 54321, 'hello!' が一つのタプルにパックされます。逆の演算も可能です:

>>>
>>> x, y, z = t
この操作は、シーケンスのアンパック (sequence unpacking) とでも呼ぶべきもので、右辺には全てのシーケンス型を使うことができます。シーケンスのアンパックでは、等号の左辺に列挙されている変数が、右辺のシーケンスの長さと同じ数だけあることが要求されます。複数同時の代入が実はタプルのパックとシーケンスのアンパックを組み合わせたものに過ぎないことに注意してください。

5.4. 集合型
Python には、 集合 (set) を扱うためのデータ型もあります。集合とは、重複する要素をもたない、順序づけられていない要素の集まりです。 Set オブジェクトは、和 (union)、積 (intersection)、差 (difference)、対称差 (symmetric difference)といった数学的な演算もサポートしています。

中括弧、または set() 関数は set を生成するために使用することができます。注: 空集合を作成するためには set() を使用しなければなりません ({} ではなく)。後者は空の辞書を作成します。辞書は次のセクションで議論するデータ構造です。

簡単なデモンストレーションを示します:

>>>
>>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
>>> print(basket)                      # show that duplicates have been removed
{'orange', 'banana', 'pear', 'apple'}
>>> 'orange' in basket                 # fast membership testing
True
>>> 'crabgrass' in basket
False

>>> # Demonstrate set operations on unique letters from two words
...
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a                                  # unique letters in a
{'a', 'r', 'b', 'c', 'd'}
>>> a - b                              # letters in a but not in b
{'r', 'd', 'b'}
>>> a | b                              # letters in a or b or both
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
>>> a & b                              # letters in both a and b
{'a', 'c'}
>>> a ^ b                              # letters in a or b but not both
{'r', 'd', 'b', 'm', 'z', 'l'}
リスト内包 と同様に、 set 内包もサポートされています:

>>>
>>> a = {x for x in 'abracadabra' if x not in 'abc'}
>>> a
{'r', 'd'}
5.5. 辞書型 (dictionary)
もう一つ、有用な型が Python に組み込まれています。それは 辞書 (dictionary) (マッピング型 --- dict を参照)です。辞書は他の言語にも "連想記憶 (associated memory)" や "連想配列 (associative array)" という名前で存在することがあります。ある範囲の数でインデクス化されているシーケンスと異なり、辞書は キー (key) でインデクス化されています。このキーは何らかの変更不能な型になります。文字列、数値は常にキーにすることができます。タプルは、文字列、数値、その他のタプルのみを含む場合はキーにすることができます。直接、あるいは間接的に変更可能なオブジェクトを含むタプルはキーにできません。リストをキーとして使うことはできません。これは、リストにスライスやインデクス指定の代入を行ったり、 append() や extend() のようなメソッドを使うと、インプレースで変更することができるためです。

辞書は キー(key): 値(value) のペアの集合であり、キーが (辞書の中で)一意でなければならない、と考えるとよいでしょう。波括弧 (brace) のペア: {} は空の辞書を生成します。カンマで区切られた key: value のペアを波括弧ペアの間に入れると、辞書の初期値となる key: value が追加されます; この表現方法は出力時に辞書が書き出されるのと同じ方法です。

辞書での主な操作は、ある値を何らかのキーを付けて記憶することと、キーを指定して値を取り出すことです。 del で key: value のペアを削除することもできます。すでに使われているキーを使って値を記憶すると、以前そのキーに関連づけられていた値は忘れ去られてしまいます。存在しないキーを使って値を取り出そうとするとエラーになります。

辞書オブジェクトに対し list(d) を実行すると、辞書で使われている全てのキーからなるリストをキーが挿入された順番で返します (ソートされたリストが欲しい場合は、代わりに sorted(d) を使ってください)。ある単一のキーが辞書にあるかどうか調べるには、 in キーワードを使います。

以下に、辞書を使った簡単な例を示します:

>>>
>>> tel = {'jack': 4098, 'sape': 4139}
>>> tel['guido'] = 4127
>>> tel
{'jack': 4098, 'sape': 4139, 'guido': 4127}
>>> tel['jack']
4098
>>> del tel['sape']
>>> tel['irv'] = 4127
>>> tel
{'jack': 4098, 'guido': 4127, 'irv': 4127}
>>> list(tel)
['jack', 'guido', 'irv']
>>> sorted(tel)
['guido', 'irv', 'jack']
>>> 'guido' in tel
True
>>> 'jack' not in tel
False
dict() コンストラクタは、キーと値のペアのタプルを含むリストから辞書を生成します:

>>>
>>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'guido': 4127, 'jack': 4098}
さらに、辞書内包表現を使って、任意のキーと値のペアから辞書を作れます:

>>>
>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}
キーが単純な文字列の場合、キーワード引数を使って定義する方が単純な場合もあります:

>>>
>>> dict(sape=4139, guido=4127, jack=4098)
{'sape': 4139, 'guido': 4127, 'jack': 4098}
5.6. ループのテクニック
辞書に対してループを行う際、 items() メソッドを使うと、キーとそれに対応する値を同時に取り出せます。

>>>
>>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
>>> for k, v in knights.items():
...     print(k, v)
...
gallahad the pure
robin the brave
シーケンスにわたるループを行う際、 enumerate() 関数を使うと、要素のインデックスと要素を同時に取り出すことができます。

>>>
>>> for i, v in enumerate(['tic', 'tac', 'toe']):
...     print(i, v)
...
0 tic
1 tac
2 toe
二つまたはそれ以上のシーケンス型を同時にループするために、関数 zip() を使って各要素をひと組みにすることができます。

>>>
>>> questions = ['name', 'quest', 'favorite color']
>>> answers = ['lancelot', 'the holy grail', 'blue']
>>> for q, a in zip(questions, answers):
...     print('What is your {0}?  It is {1}.'.format(q, a))
...
What is your name?  It is lancelot.
What is your quest?  It is the holy grail.
What is your favorite color?  It is blue.
シーケンスを逆方向に渡ってループするには、まずシーケンスの範囲を順方向に指定し、次いで関数 reversed() を呼び出します。

>>>
>>> for i in reversed(range(1, 10, 2)):
...     print(i)
...
9
7
5
3
1
シーケンスをソートされた順序でループするには、 sorted() 関数を使います。この関数は元の配列を変更せず、ソート済みの新たな配列を返します。

>>>
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for i in sorted(basket):
...     print(i)
...
apple
apple
banana
orange
orange
pear
シーケンスに set() を使うと、重複要素が除去されます。 シーケンスに set() を使った上で、 sorted() を使うという組み合わせ方は、順番が整列されているシーケンスで、同一要素に 1 度のみループでアクセスする慣用的な方法です。

>>>
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for f in sorted(set(basket)):
...     print(f)
...
apple
banana
orange
pear
ときどきループ内でリストを変更したい誘惑に駆られるでしょうが、代わりに新しいリストを作ってしまうほうがより簡単で安全なことが、ままあります

>>>
>>> import math
>>> raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
>>> filtered_data = []
>>> for value in raw_data:
...     if not math.isnan(value):
...         filtered_data.append(value)
...
>>> filtered_data
[56.2, 51.7, 55.3, 52.5, 47.8]
5.7. 条件についてもう少し
while や if 文で使った条件 (condition) には、値の比較だけでなく、他の演算子も使うことができます。

比較演算子 in および not in は、ある値があるシーケンス中に存在するか (または存在しないか) どうかを調べます。演算子 is および is not は、二つのオブジェクトが実際に同じオブジェクトであるかどうかを調べます。この比較は、リストのような変更可能なオブジェクトにだけ意味があります。全ての比較演算子は同じ優先順位を持っており、ともに数値演算子よりも低い優先順位となります。(訳注: is は、 is None のように、シングルトンの変更不能オブジェクトとの比較に用いる場合もあります。(「変更可能なオブジェクトにだけ意味があります」の部分を削除することを Doc-SIG に提案中。))

比較は連結させることができます。例えば、 a < b == c は、 a が b より小さく、かつ b と c が等しいかどうかをテストします。

ブール演算子 and や or で比較演算を組み合わせることができます。そして、比較演算 (あるいは何らかのブール式) の結果の否定は not でとれます。これらの演算子は全て、比較演算子よりも低い優先順位になっています。 A and not B or C と (A and (not B)) or C が等価になるように、ブール演算子の中で、 not の優先順位が最も高く、 or が最も低くなっています。もちろん、丸括弧を使えば望みの組み合わせを表現できます。

ブール演算子 and と or は、いわゆる 短絡 (short-circuit) 演算子です。これらの演算子の引数は左から右へと順に評価され、結果が確定した時点で評価を止めます。例えば、 A と C は真で B が偽のとき、 A and B and C は式 C を評価しません。一般に、短絡演算子の戻り値をブール値ではなくて一般的な値として用いると、値は最後に評価された引数になります。

比較や他のブール式の結果を変数に代入することもできます。例えば、

>>>
>>> string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
>>> non_null = string1 or string2 or string3
>>> non_null
'Trondheim'
Pythonでは、Cとは異なり、式の中での代入は セイウチ演算子 := を使用して明示的に行う必要があることに注意してください。これにより、 == が意図されていたところに = を入力してしまうという、Cプログラムで発生する一般的なクラスの問題を回避できます。

5.8. シーケンスとその他の型の比較
概して、シーケンスオブジェクトは、同じシーケンス型の他のオブジェクトと比較できます。比較には 辞書的な (lexicographical) 順序が用いられます。まず、最初の二つの要素を比較し、その値が等しくなければその時点で比較結果が決まります。等しければ次の二つの要素を比較し、以降シーケンスの要素が尽きるまで続けます。比較しようとする二つの要素がいずれも同じシーケンス型であれば、そのシーケンス間での辞書比較を再帰的に行います。二つのシーケンスの全ての要素の比較結果が等しくなれば、シーケンスは等しいとみなされます。片方のシーケンスがもう一方の先頭部分にあたる部分シーケンスならば、短い方のシーケンスが小さいシーケンスとみなされます。文字列に対する辞書的な順序づけには、個々の文字ごとに ASCII 順序を用います。以下に、同じ型のオブジェクトを持つシーケンス間での比較を行った例を示します:

(1, 2, 3)              < (1, 2, 4)
[1, 2, 3]              < [1, 2, 4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4)           < (1, 2, 4)
(1, 2)                 < (1, 2, -1)
(1, 2, 3)             == (1.0, 2.0, 3.0)
(1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)
違う型のオブジェクト同士を < や > で比較することも、それらのオブジェクトが適切な比較メソッドを提供しているのであれば許可されます。例えば、異なる数値型同士の比較では、その数値によって比較が行われます。例えば、 0 と 0.0 は等価です。一方、適切な比較順序がない場合は、インタープリターは TypeError 例外を発生させます。




