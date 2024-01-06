---
description: MarkdownをHTMLに変換するPythonパッケージです。
keywords: Python、package、markdown、html、変換、コンパイル
update: 20240104
---
# ChainableMark2Html

MarkdownをHTMLに変換するPythonパッケージです。 以下はChainableMark2HtmlでコンパイルできるMarkdownの基本的な要素とその使用方法の概要です。


## 見出し (Headers)

見出しはドキュメントの構造を整理するのに役立ちます。`#`を使用して異なるレベルの見出しを作成できます。たとえば、`#`は最も大きな見出し（見出し1）を、`##`は少し小さな見出し（見出し2）を作成します。


# 見出し1
## 見出し2
### 見出し3
#### 見出し4
##### 見出し5
###### 見出し6

## 段落 (Block)
Markdownでは、新しい段落を作成するために空白行を使用します。これは文章の読みやすさを向上させます。

段落はpタグで囲まれます。

## 改行 (Br)
改行は、行末にスペースを2つ入れることで作成できます。これは、段落内で改行を入れる際に特に便利です。

```markdown
コメント
ここは改行されない(スペース2つ)
ここは改行される
```

コメント
ここは改行されない  
ここは改行される

## 引用 (Blockquotes)
引用は、`>`を行の先頭に置くことで作成できます。


> 引用  
> 引用
>> ただし多重引用には対応してません
>>> ただし多重引用には対応してません
> 引用

## コード (Code)

Markdownでは、コードを`バッククオート`3つで囲むことにより表示できます。インラインコードは、単語を`バッククオート`で囲むことで作成できます。


```python
    def output(self, output_file_path, overwrite=False):
        if overwrite or not os.path.exists(output_file_path):
            with open(output_file_path, 'w') as file:
                file.write(self.to_html())
        else:
            print(f"File {output_file_path} already exists. Set overwrite=True to overwrite.")
        return self

```

ファイル名もつけられます。
```python:chainable_mark2html.py
    def output(self, output_file_path, overwrite=False):
        if overwrite or not os.path.exists(output_file_path):
            with open(output_file_path, 'w') as file:
                file.write(self.to_html())
        else:
            print(f"File {output_file_path} already exists. Set overwrite=True to overwrite.")
        return self

```

```
ラベルなしのプレーンテキストです。
```



整形済みテキスト (pre)
半角スペース4つまたはタブを使用すると、整形済みテキストを作成できます。これは特にコードブロックに適しています。


## チルダ

```markdown
チルダを使います
~~~
チルダの中身はこんな感じ。
改行も入れたりなんかりして。  
**強調表現**もできます！
~~~
チルダの外
```

チルダを使います
~~~
チルダの中身はこんな感じ。
改行も入れたりなんかりして。  
**強調表現**もできます！
~~~
チルダの外


## 水平線 (Hr)
ハイフン`---`の3つを使用して水平線を作成できます。

---

## リスト (Lists)
Markdownでは、箇条書きリストと番号付きリストを作成することができます。箇条書きリストは`-`で作成できます。



- リスト1
    - リスト1_1
        - リスト1_1_1
        - リスト1_1_2
    - リスト1_2
- リスト2
- リスト3


また番号.を文の先頭に配置することで、番号付きリストを作成できます。リスト内での階層化はタブを使って表現します。番号付きリストでは、番号は自動で割り振られます。そのため、効率のためにすべての項目を1.で始めることが推奨されます。これにより、項目の追加や削除が簡単になり、リストの順序を手動で管理する必要がなくなります。

```markdown
1. 番号付きリスト1
    1. 番号付きリスト1-1
    1. 番号付きリスト1-2
1. 番号付きリスト2
1. 番号付きリスト3
```

1. 番号付きリスト1
    1. 番号付きリスト1-1
    1. 番号付きリスト1-2
1. 番号付きリスト2
1. 番号付きリスト3



## リンク (Link)
リンクは、次の形式で作成できます。これにより、テキストにリンクを埋め込むことができます。

```markdown
[表示文字](URL)

https://github.com/aragig/ChainableMark2Html
```

[ChainableMark2Html](https://github.com/aragig/ChainableMark2Html)

テキスト内にも[ChainableMark2Html](https://github.com/aragig/ChainableMark2Html)入れられます。

urlを直接貼ることもできます。  
https://github.com/aragig/ChainableMark2Html


## 強調 (Emphasis)
イタリック体は`*`で、ボールド体は`**`で作成できます。イタリックとボールドの両方を組み合わせることも可能です。


これは*イタリック*です

これは**ボールド**です

これは***イタリック＆ボールド***です

## 画像 (Images)
画像は、次の形式で挿入できます。

```markdown
![altテキスト](画像URL)
```


![ChainableMark2Htmlロゴ](chainable_mark2html_logo.png)

独自のプロセッサーを用意することで、次のような拡張も可能です。詳細は`ImageProcessor`を参照してください。

```markdown
![altテキスト](画像URL w:maxWidth h:maxHeight c:showCaptionFlag)
```

![ChainableMark2Htmlロゴ](chainable_mark2html_logo.png w:400 h:300 c:false)

画像を横に並べるとFlexboxでレイアウトされます。

![ここに解説コメントを複数行にまたがって入れることができる](chainable_mark2html_logo.png w:200 h:200)![ここに解説コメントを複数行にまたがって入れることができる](chainable_mark2html_logo.png w:200 h:200)
![ここに解説コメントを複数行にまたがって入れることができる](chainable_mark2html_logo.png w:200 h:200)![ここに解説コメントを複数行にまたがって入れることができる](chainable_mark2html_logo.png w:200 h:200)![ここに解説コメントを複数行にまたがって入れることができる](chainable_mark2html_logo.png w:200 h:200)![ここに解説コメントを複数行にまたがって入れることができる](chainable_mark2html_logo.png w:200 h:200)![ここに解説コメントを複数行にまたがって入れることができる](chainable_mark2html_logo.png w:200 h:200)

## 表 (Table)
`-`と`|`を使用して表を作成できます。これにより、データを整理して表示することができます。

これらの要素を使って、Markdownで効果的に情報を整理し、文書を魅力的にすることができます。

| 項目        | 値    |
|-----------|------|
| アイテム1     | 1000 |
| **アイテム2** | 2000 |
| *アイテム3*   | 3000 |

