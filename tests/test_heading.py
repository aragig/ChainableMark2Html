import unittest
import ChainableMark2Html as m2h


class TestMarkdownToHtml(unittest.TestCase):

    def test_heading1(self):
        markdown_text = """# 見出し1
## 見出し2
### 見出し3
#### 見出し4
##### 見出し5
###### 見出し6
# 見出し1
"""

        actual_html = (m2h.ChainableMark2Html(markdown_text)
                       .heading()
                       .to_html())

        expected_html = """<h1>見出し1</h1>

<h2>見出し2</h2>

<h3>見出し3</h3>

<h4>見出し4</h4>

<h5>見出し5</h5>

<h6>見出し6</h6>

<h1>見出し1</h1>"""
        self.assertEqual(actual_html, expected_html)

    def test_custom_heading2(self):
        markdown_text = """
# Heading 1
Some text under heading 1.

## Heading 2
Some more text under heading 2.

    ## ここはヘッダーではない

### Heading 3
Text under heading 3.

"""
        actual_html = (m2h.ChainableMark2Html(markdown_text)
                       .heading()
                       .to_html())

        expected_html = """<h1>Heading 1</h1>

Some text under heading 1.

<h2>Heading 2</h2>

Some more text under heading 2.

    ## ここはヘッダーではない

<h3>Heading 3</h3>

Text under heading 3."""
        self.assertEqual(actual_html, expected_html)

    def test_heading3(self):
        markdown_text = """# 見出し1

[TOC]

## はじめに
内容内容内容内容内容内容内容内容内容内容内容

## 説明
ここからは説明が入ります。

### インストール
説明説明説明説明説明説明説明

### 使い方
説明説明説明説明説明説明

## 終わりに
"""

        actual_html = (m2h.ChainableMark2Html(markdown_text)
                       .toc()
                       .heading()
                       .link()
                       .li()
                       .ol()
                       .to_html())

        expected_html = """<h1><span id="%E8%A6%8B%E5%87%BA%E3%81%971" class="fragment"></span>見出し1</h1>

<div class="toc">
<ol>
<ol>
<li><a href="#%E3%81%AF%E3%81%98%E3%82%81%E3%81%AB">はじめに</a></li>
<li><a href="#%E8%AA%AC%E6%98%8E">説明</a></li>
<ol>
<li><a href="#%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB">インストール</a></li>
<li><a href="#%E4%BD%BF%E3%81%84%E6%96%B9">使い方</a></li>
</ol>
<li><a href="#%E7%B5%82%E3%82%8F%E3%82%8A%E3%81%AB">終わりに</a></li>
</ol>
</ol>
</div>

<h2><span id="%E3%81%AF%E3%81%98%E3%82%81%E3%81%AB" class="fragment"></span>はじめに</h2>

内容内容内容内容内容内容内容内容内容内容内容

<h2><span id="%E8%AA%AC%E6%98%8E" class="fragment"></span>説明</h2>

ここからは説明が入ります。

<h3><span id="%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB" class="fragment"></span>インストール</h3>

説明説明説明説明説明説明説明

<h3><span id="%E4%BD%BF%E3%81%84%E6%96%B9" class="fragment"></span>使い方</h3>

説明説明説明説明説明説明

<h2><span id="%E7%B5%82%E3%82%8F%E3%82%8A%E3%81%AB" class="fragment"></span>終わりに</h2>"""
        self.assertEqual(actual_html, expected_html)


if __name__ == '__main__':
    unittest.main()
