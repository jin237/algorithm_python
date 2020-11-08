理系大学で絶対に習う線形代数をわかりやすく、かつ論理的にまとめる。ちなみにそれをPythonで実装。たまに、Juliaで実装するかも。。。

・Pythonで動かして学ぶ！あたらしい数学の教科書 -機械学習・深層学習に必要な基礎知識-
amazon: https://www.amazon.co.jp/dp/B07TZ57B5X/ref=dp-kindle-redirect?_encoding=UTF8&btkr=1

・世界基準MIT教科書 ストラング線形代数イントロダクション
amazon: https://www.amazon.co.jp/dp/B01I4TPXLE/ref=dp-kindle-redirect?_encoding=UTF8&btkr=1

を基に線形代数を理解し、pythonで実装。


# 環境
・JupyterNotebook
・言語：Python3, Julia1.4

# 線形結合(ベクトル入門)
線形結合は**スカラー積**と**ベクトル和**によって構成される。
2つのスカラーをa,bとして、ベクトル和をv,wとする。

スカラー積は、

```math
av,bw
```
のように掛けられたもの。

ベクトル和は、

```math
v + w
```
のように足されたもの。
これら二つの組み合わせを***線形結合***という。よって、

```math
av + bw
```
のような形のことである。ちなみにこれは項数が2つなので、***2次元面を張る***。（v=w>の場合、違うが。）

pythonで実装

```python
import numpy as np

# ベクトル 
v = np.array([1, 2, 3])
w = np.array([4, 5, 6])
# スカラー
a = 2
b = 5

# 線形結合の形
linearcomb = a * v + b * w
print(linearcomb) 
```

juliaで実装

```julia
# ベクトル 
v = [1, 2, 3]
w = [4, 5, 6]
# スカラー
a = 2
b = 5

linearcomb = a * v + b * w
print(linearcomb)
```

どちらも以下のようにターミナルに出てくる

```terminal
[22 29 36]
```

# 数式表記
Markdown記法による記述なので、*などの積を表すものについて一部出来ていないところがある。また、数式については、`バックフォード`の部分については、数式の見やすさを重視するためであり、コードの一部ではない。

# 長さと内積
v = (v₁, v₂)
w = (w₁, w₂)
というベクトルとする。
### 内積
内積は、***v・w***と表す。ほかにも***ドット積と***呼ぶこともある。
`v・w = v₁w₁ + v₂*w₂`
となる。
このとき、***v・w = 0 であれば 直交する***。

### 長さ
長さは、内積のベクトルが同じものになった時 => 2乗となった時 である。
***(内積v・v) = (長さの2乗)***

v = (1, 2, 3)としたとき、
***`│v│² = 1² + 2² + 3² = 14`***
->これは***長さの2乗を表す***
すなわち、この2乗を外せば、長さとなるので、
***`│v│ = √14`***
となる。別の書き方として、
***`norm(v) = √14`***
と書く。これからはnorm()で書く。
これに関しては、実際には[三平方の定理](https://ja.wikipedia.org/wiki/%E3%83%94%E3%82%BF%E3%82%B4%E3%83%A9%E3%82%B9%E3%81%AE%E5%AE%9A%E7%90%86)と比較してみれば明らかである。

#### 単位ベクトル
長さが１となるベクトルである。
上のようなベクトルvのとき、長さは√14なので、これを１にするには√14で割ればよい。すなわち、そのベクトルをもとの長さ自身で割れば単位ベクトルとなる。
単位ベクトルをuとするとき、
***`u = v/norm(v)`***
このことから、uはvと同方向の長さ１のベクトルを表すことになる。
具体的な数字で表すと、v = (1, 2, 3)としたとき、`norm(v) = √14`でなのでそれで割ると、
***`u = (1/√14, 2/√14, 3/√14)`***
となることがわかる。

ここで、内積を求めるプログラムと長さを算出するプログラムを書いてみよう。

Python

```python
import numpy as np
import math

v = list()
w = list()
# 要素が3つのベクトルの要素記入
for i in range(3):
    vvec = int(input())
    v.append(vvec)
for i in range(3):
    wvec = int(input())
    w.append(wvec)
# 配列の中身の変換
v = np.array(v)
w = np.array(w)
# 内積の計算
print(np.dot(v, w))
# 長さの計算
normv = math.sqrt(np.dot(v, v))
print(normv)
# 実際に計算する際には√をもちいるので
print("√",np.dot(v, v))
```

Juliaはpythonより難しいので、簡単なコードにする。

```julia
v = [1 2 3]
w = [3; 2; 1]
# 内積計算
v*w

# 長さの2乗
normv2 = sum(v.^ 2)
# 長さ
sqrt(normv2)
```
juliaのコードに関しては、内積計算では無理やり持って行ってるので、もう少し効率のいいコードを後程上げたいと思う。

# 行列
行列について、少し深く触れてみる。基本的に、

```math
A x = b
```
という、形にするのがスタンダード

### 行列について、
行列には、***行***と***列***が存在する。
・横に並ぶのが、行
・盾に並ぶのが、列
いままで、
u = (1, 2, 3)のようにあらわしてきたのは、列ベクトルのことである。
***`行ベクトル : u = [1, 2, 3]`***
***`列ベクトル : u = (1, 2, 3)`***

とする。
本来であれば、以下のように表記しなければならない。

```math
u =
\begin{bmatrix}
1 \\
2 \\
3
\end{bmatrix}
```
ただし、この記事はマークダウン方式により、めんどくさいので今まで通りに記述する。

### 線形方程式とベクトル
ex)連立方程式について

```math
\begin{matrix}
 x - 2y =  1 \\
3x + 2y = 11
\end{matrix}
```
を列ベクトルで考える。(= 線形的思考)
線形方程式のメリットは負数の指揮を一つの式で表すことができること。
以下のように変形できる、

```math
x
\begin{bmatrix}
1 \\
3
\end{bmatrix}
+
y
\begin{bmatrix}
-2 \\
2
\end{bmatrix}
=
\begin{bmatrix}
1 \\
11
\end{bmatrix}
```

この時、

```math
u =
\begin{bmatrix}
1 \\
3
\end{bmatrix}
,
v = 
\begin{bmatrix}
-2 \\
2
\end{bmatrix}
,
b = 
\begin{bmatrix}
1 \\
11
\end{bmatrix}
```
とおける。これは、u, vについてまとめてAとするとき、以下のようにAx=bの形で書くことができる。

```math
Ax =
\begin{bmatrix}
1 & -2\\
3 & 2
\end{bmatrix}
\begin{bmatrix}
x\\
y
\end{bmatrix}
=
\begin{bmatrix}
1 \\
11
\end{bmatrix}
= b
```
となる。この線形方程式で、あてはまるx, yを考える必要がある。
ちなみ解析学的に考えると、直線同士の交点を示す。

# 行列の計算(プログラム)

```math
a =
\begin{bmatrix}
0 & 1 & 2 \\
1 & 2 & 3
\end{bmatrix}
,
b =
\begin{bmatrix}
2 & 1 \\
2 & 1\\
2 & 1
\end{bmatrix}
```
とする。行列の計算を行う。

### Pythonのコード

```python
import numpy as np

a =  ([[0, 1 ,2],
       [1, 2, 3]])
b = ([[2, 1],
      [2, 1],
      [2, 1]])
print(np.dot(a, b))

#=>[[ 6  3]
#   [12  6]]
```

### Juliaのコード

```julia
using LinearAlgebra
a = [0 1 2; 1 2 3]
b = [2 1; 2 1; 2 1]
a*b

#=>2×2 Array{Int64,2}:
#   6  3
#  12  6
```

# 単位行列

```math
E = \begin{pmatrix}1 & 0\\0 & 1\end{pmatrix},\begin{pmatrix}1 & 0 & 0\\0 & 1 & 0\\0 & 0 & 1\end{pmatrix}
```
のような左上から右下にかけて対角線上に1が並び、そのほかの要素は0になるという行列である。

n次正方行列に対して、同じ要素数の単位行列っをかけたとしても出力される値は同値となる。さらに積の順番は問わない。

```math
AE = \begin{pmatrix}a & b\\c & d\end{pmatrix}\begin{pmatrix}1 & 0\\0 & 1\end{pmatrix}=\begin{pmatrix}a & b\\c & d\end{pmatrix}=\begin{pmatrix}1 & 0\\0 & 1\end{pmatrix}\begin{pmatrix}a & b\\c & d\end{pmatrix}=EA
```

### 単位行列のPythonコード

```python
import numpy as np

# print("2×2単位行列は")
print(np.eye(2))
# print("3×3単位行列は")
print(np.eye(3))
# print("4×4単位行列は")
print(np.eye(4))
```

```terminal
#実装
2×2単位行列は
[[1. 0.]
 [0. 1.]]
3×3単位行列は
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
4×4単位行列は
[[1. 0. 0. 0.]
 [0. 1. 0. 0.]
 [0. 0. 1. 0.]
 [0. 0. 0. 1.]]
```


### 単位行列のJuliaコード

```julia
using LinearAlgebra
Matrix{Int}(I, 2, 2) 
Matrix{Int}(I, 3, 3) 
Matrix{Int}(I, 4, 4) 
```

```terminal
2×2 Array{Int64,2}:
 1  0
 0  1

3×3 Array{Int64,2}:
 1  0  0
 0  1  0
 0  0  1

4×4 Array{Int64,2}:
 1  0  0  0
 0  1  0  0
 0  0  1  0
 0  0  0  1
```

# 逆行列
逆行列は、

```math
AA^{-1} = A^{-1}A = E
```
という関係を持つものである。例を示すと、

```math
A =\begin{pmatrix}1 & 1 \\1 & 2\end{pmatrix},
B =\begin{pmatrix}2 & -1 \\-1 & 1\end{pmatrix}
```
という二つの行列があるときに対して、ABの積を求める。

```math
AB =\begin{pmatrix}1 & 1 \\1 & 2\end{pmatrix}\begin{pmatrix}2 & -1 \\-1 & 1\end{pmatrix}=\begin{pmatrix}1 & 0\\0 & 1\end{pmatrix}
```
これより

```math
AB = E = BA \Longrightarrow B = A^{-1}
```

# 行列式

```math
A = \begin{pmatrix}a & b\\c & d\end{pmatrix}
\Longleftrightarrow
\begin{vmatrix}A\end{vmatrix}= det A = ad-bc
```

さらに2×2行列の時には、

```math
A^{-1} = \frac{1}{ad-bc}\begin
{pmatrix}d & -b\\-c & a\end{pmatrix}
```
と表すことができ、この時、

```math
ad-bc = 0 \Longleftrightarrow A^{-1}は存在しない
\\
ad-bc \neq 0 \Longleftrightarrow A^{-1}が存在する。
```
と書くことができる。

### 行列式を含めた逆行列のPythonコード

```python
import numpy as np


a = [input().split() for i in range(2)]
#数字入力
#=>1 2
#=>3 4

a = np.array(a)
print(a)
#=>[['1' '2']
#   ['3' '4']]

a = a.astype(np.float64)
print(np.linalg.det(a))
#=>-2.0000000000000004

if np.linalg.det(a) != 0:
    print(np.linalg.inv(a))
else:
    print("No exist")
#=>[[-2.   1. ]
#   [ 1.5 -0.5]]
```
実際には、if文を用いなくても`np.linalg.inv()関数`でそのまま計算しても、逆行列が存在しない場合にはエラーが起こる。ただ、行列式を今回は使いたいので、`np.linalg.det()関数`を用いて書いた。

### 行列式を含めた逆行列のJuliaコード

```julia
using LinearAlgebra
A = [1 2; 3 4]
if det(A) == 0
    print("No exist")
else
    inv(A)
end

#=>2×2 Array{Float64,2}:
# -2.0   1.0
#  1.5  -0.5
```
`inv()関数`によって逆行列はすぐに求められる。

# 線形変換
行列Aをベクトルvにかけたとき、***Avに変換する***という表現を用いる。別の言い方をすると、***vを入力して、T(v)=Avを出力する***という。このときのTは関数扱い。
このことから***線形***であるとするための条件は、線形代数の核ともいえる線形結合の形に似ている。
確認のために。
##### 線形結合
引用元：https://qiita.com/jin237/items/ebeae3018b5ab190c2bf
>線形結合は**スカラー積**と**ベクトル和**によって構成される。
>2つのスカラーをa,bとして、ベクトル和をv,wとする。
>
>スカラー積は、

>```math
>av,bw
>```
>のように掛けられたもの。
>
>ベクトル和は、
>
>```math
>v + w
>```
>のように足されたもの。
>これら二つの組み合わせを***線形結合***という。よって、
>
>```math
>av + bw
>```
>のような形のことである。ちなみにこれは項数が2つなので、***2次元面を張る***。（v=w>の場合、違うが。）

このことから得られる線形変換は、以下のようになる。
### 線形変換
引用元：線形代数イントロダクション/ストラング
>変換Tはん入力されたVの各ベクトルｖに対して出力T(v)をしている。変換Tはすべてのvとwに対して以下の条件を満たすとき、***線形***であるという.

>```math
(a) : T(v+w)  =T(v) + T(w)\\
(b) : T(cv) = cT(v),すべてのcに対して.
>```

文章はそんなに気にしなくていいので、式に注目してもらえればわかる。
このことから言えるのが、

```math
T(cv+dw)  =cT(v) + dT(w)
```
が成り立つということだ。

線形変換について書くと膨大な量になりそうなので、軽くここまでにする。プログラムをしよう。

# ベクトルの描画
線形変換することにより、ベクトルを変換できることが上からわかる。これは人工知能ではニューラルネットワーク上における情報伝達させるために使う。
とりあえず、ベクトルをグラフ上で表してみる。

```math
\vec{a}=
\begin{pmatrix}
2 \\
3
\end{pmatrix}
,
\vec{b}=
\begin{pmatrix}
1 \\
-2
\end{pmatrix}
```
というベクトルを描写する。今回からmatplotlibを使う。
##### pythonコード(ベクトルの描画)

```python:5pythonvectordrawing.py
%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt


plt.quiver(0, 0, 2, 3, angles="xy", scale_units="xy", scale=1, color="red")
# plt.text(2.3, 2.5, "[2, 3]", color = "red", size =13)
plt.quiver(0, 0, 1, -2, angles="xy", scale_units="xy", scale=1, color="blue")
# plt.text(1.3, -2, "[1,-2]", color = "blue", size = 13)


plt.xlim([-6,6])  
plt.ylim([-6,6])  
plt.xlabel("x", size=10)
plt.ylabel("y", size=10)
plt.grid(color = "black")
plt.grid(which = "minor", axis = "x", color = "gray", alpha = 0.8,
        linestyle = "--", linewidth = 1)
plt.grid(which = "minor", axis = "y", color = "gray", alpha = 0.8,
        linestyle = "--", linewidth = 1)
plt.axes().set_aspect("equal")  
plt.title('Vectors')
# plt.savefig('vector.png')
plt.show()
```

##### 結果(グラフ)
![vector.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/533115/e92643a7-d89e-8a1a-5991-dc78cf5e4b1a.png)


##### コードの解説

```python
%matplotlib inline
import matplotlib.pyplot as plt
```
↑　
&nbsp;インポートする際にjupyternotebookでグラフを書く場合に使われるのでセットで覚えておくとよい。

```python
plt.quiver(0, 0, 2, 3, angles="xy", scale_units="xy", scale=1, color="red")
plt.quiver(0, 0, 1, -2, angles="xy", scale_units="xy", scale=1, color="blue")
```
↑　
&nbsp;ベクトルの描画するために、*quiver()関数*を用いる。ちなみに*quiverは日本語で直訳すると「小刻みに震える」のような意味になるが、数学上では箙(えびら)と呼ばれる*。中身は調べて(笑)
quiver関数の表し方は、

```terminal
quiver(始点のx, 始点のy, 矢印のx成分, 矢印のy成分, 
       angle=矢印の角度決定方法, scale_units="スケール単位", 
       scale=スケール, color=矢印の色)
```
のようにして書く。
そのあとのコードについては後日別の記事で、matplotlibの扱い方について書くつもり。

# ベクトル計算を含めた描画
```math
\vec{a}=
\begin{pmatrix}
2 \\
3
\end{pmatrix}
,
\vec{b}=
\begin{pmatrix}
1 \\
-2
\end{pmatrix}
```
二つのベクトルの関係は、Aa=bで表すと、

```math
A\vec{a}=
\begin{pmatrix}
2 & -1\\
2 & -2
\end{pmatrix}
\begin{pmatrix}
2 \\
3
\end{pmatrix}
=
\begin{pmatrix}
1 \\
-2
\end{pmatrix}
=\vec{b}
```
という関係であるこれを表すグラフは同様であるが、計算したものをプログラムに表すのには上とは異なる方法となる。

##### pythonコード(ベクトル計算を含めた描画)

```python:5pythonvectorcalc.py
%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt


def arrow(start, size, color):
    plt.quiver(start[0], start[1], size[0], size[1], 
               angles="xy", scale_units="xy", scale=1, color=color)
a = np.array([2,3])
A = np.array([[2, -1],
              [2, -2]])
b = np.dot(A, a)
s = np.array([0, 0])


arrow(s, a, color="red")
arrow(s, b, color="blue")
plt.xlim([-6,6])  
plt.ylim([-6,6])  
plt.xlabel("x", size=10)
plt.ylabel("y", size=10)
plt.grid(color = "black")
plt.axes().set_aspect("equal")  
plt.title('Vectorscalc')
plt.savefig('vectorcalc.png')
plt.show()
```
##### 結果(グラフ)
![vectorcalc.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/533115/a940b124-d8f5-d675-43e2-5ebbe5d95671.png)



defからのところに関数を定義として入れ、計算した値をそのまま代入してベクトルとして表示できるようにした。コード量が多くなるので、補助目盛とテキストはなくした。


# 線形独立
##### 線形独立イメージ
線形結合である

```math
av + bw
```
の形のことを基に話す。v,wというベクトルは方向ベクトルが違う必要がある。
例えば、

```math
\vec{v}=\begin{pmatrix}2\\3\end{pmatrix}
,
\vec{w}=\begin{pmatrix}1\\-2\end{pmatrix}
```
のような関係のことである。これは前回やったように、二つのベクトルが角度をnπ(n=0, 1, 2,...)を満たさない角度をなすことをいう。すなわち、

```math
\vec{v}=\begin{pmatrix}2\\3\end{pmatrix}
,
\vec{w}=\begin{pmatrix}4\\6\end{pmatrix}
\\
\\
\vec{v}=α\vec{w}
```
上のように`スカラー積関係、倍数関係になったものを線形従属`という。`ならないもの線形独立`という。たとえ2つでなく、3つでもそれぞれが独立しなければならない。
イメージではこんな感じでいいだろう。

##### 線形独立の定義
<font color="Red">定義</font>
Ax= 0のかいがx=0のみであるとき,列ベクトルは線形代数である.列ベクトルの線形結合Axにおいて零ベクトルとなるものは他にない.
ベクトルの列v_1,v_2,....,v_nは,零ベクトルとなる線形結合が

```math
0v_1+0v_2+...+0v_n
```
のみであるとき,線形独立である.

すなわち、


```math

すべてのx_iが零のときのみ,\\
x_1v_1+x_2v_2+...+x_nv_n=0\\
となる.
```
このようにならない場合が線形従属という。

### プログラム
##### 2つの2要素を持つ列ベクトル同士の判定するプログラム

```python:6pythonlinearindependece
import numpy as np

v = list()
w = list()
for i in range(2):
    vbec = int(input())
    v.append(vbec)
for i in range(2):
    wbec = int(input())
    w.append(wbec)
v = np.array(v)
w = np.array(w)

sarrus = v[0]*v[1] - v[1]*v[0]
if sarrus == 0:
    print("線形従属")
else:
    print("線形独立")
```
[Pythonで線形代数をやってみた(2)](
https://qiita.com/jin237/items/d3c4b2d32d7e87db3b69)にあるコードを少しだけ書き換えたものである。
これは2つの要素を持つベクトル同士でないと判定できない。
最初に要素数をしてして、独立か従属かを判定するプログラムは以下のようになる。
##### 2つのn要素を持つ列ベクトル同士の判定するプログラム

```python:6pythonlinearindependece2
import numpy as np

n = int(input())
# =>3

v = list()
w = list()
for i in range(n):
    vbec = int(input())
    v.append(vbec)
for i in range(n):
    wbec = int(input())
    w.append(wbec)
v = np.array(v)
w = np.array(w)
# =>1
# =>2
# =>3
# =>3
# =>2
# =>1

x = list()
c = v[0]/w[0]

for i in range(n): 
    if v[i] == c*w[i]:
        x.append("True")
        continue
    else:
        break

if len(x) == n:
    print("線形従属")
elif len(x) < n:
    print("線形独立")
# =>線形独立
```
### 基底
##### ベクトル空間の基底の定義
<font color="Red">定義</font>
`ベクトル空間の基底とは,次の2つの性質を持つようなベクトルの列である:
***基底ベクトルは,線形独立であり,空間を張る.***`

ここでの基底についての詳しい説明は省く。

##### 標準基底
具体例

```math
I =
\begin{bmatrix}
1 & 0\\
0 & 1
\end{bmatrix}
の列ベクトルはR^2の標準基底である.
```
これより以下のように言える。

```math
(n×n)単位行列の列ベクトルはR^nの「標準基底」である.
さらに、
すべての(n×n)行列の列ベクトルはR^nの「標準基底」である
```
次元についてもここでは省略。

### プログラム

```math
\vec{e_x}=\begin{pmatrix}1\\0\end{pmatrix},
\vec{e_y}=\begin{pmatrix}0\\1\end{pmatrix}
```
とするとき,a=(2,3)は次のように表せる。

```math
\vec{a}=\begin{pmatrix}2\\3\end{pmatrix}=2\vec{e_x}+3\vec{e_y}
=2\begin{pmatrix}0\\1\end{pmatrix}+3\begin{pmatrix}1\\0\end{pmatrix}
```
これより

```math
\vec{a},\vec{e_x},\vec{e_y}
```
の3つのベクトルを描写する。
[Pythonで線形代数をやってみた(5)](https://qiita.com/jin237/items/2fdfe6de984eaff637b8)のベクトル3つverなので、新しくはない。

##### 元のベクトルと標準基底の描写プログラム

```python

import numpy as np
import matplotlib.pyplot as plt

a = np.array([2, 3])
e_x = np.array([1, 0]) 
e_y = np.array([0, 1])  

print("a:", a)
print("e_x:", e_x)
print("e_y:", e_y)
      
def arrow(start, size, color):
    plt.quiver(start[0], start[1], size[0], size[1], 
               angles="xy", scale_units="xy", scale=1, color=color)

s = np.array([0, 0])  # 原点

arrow(s, a, color="blue")
arrow(s, e_x, color="red")
arrow(s, e_y, color="red")

# グラフ表示
plt.xlim([-3,3])  # xの表示範囲
plt.ylim([-3,3])  # yの表示範囲
plt.xlabel("x", size=14)
plt.ylabel("y", size=14)
plt.grid()
plt.axes().set_aspect("equal")  # 縦横比を同じに
plt.show()
```
