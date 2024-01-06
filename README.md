# ChainableMark2Html

ChainableMark2Htmlは、Markdown文書をHTMLに変換するためのPythonパッケージです。このパッケージは、特定のタグ変換時にコールバック関数を使用してタグのカスタマイズを可能にし、オリジナルのプロセッサを追加することで独自のMarkdown表記を拡張できる機能を備えています。
![ChainableMark2Html](chainable_mark2html_logo.png)

## 特徴
- **カスタマイズ可能**: コールバック関数を使用してHTMLタグをカスタマイズ可能。
- **拡張性**: 独自のプロセッサを追加し、Markdownの機能を拡張できます。

## インストール
このパッケージはpipを通じて簡単にインストールできます。
```
pip3 install git+https://github.com/aragig/ChainableMark2Html.git@develop
```

## 使い方
以下は、ChainableMark2Htmlを使用してMarkdownファイルをHTMLに変換する基本的なプロセスを示しています。

```python
import ChainableMark2Html as m2h
from processor.custom_image_callback import CustomImage
from processor.parse_yaml_processor import ParseYamlProcessor


custom_image = CustomImage("./images", "./images_medium", "./images_medium")
yaml_processor = ParseYamlProcessor()

with open("sample.md", 'r') as file:
    output_file_path = '../public/test_output3.html'
    wrap_html = """<html>
<head>
<meta charset="UTF-8">
<title>ChainableMark2Html</title>
<meta name="description" content="{meta_description}">
<meta name="keywords" content="{meta_keywords}">
<link rel="stylesheet" type="text/css" href="cm2h.css">
</head>
<body>
<article class="cm2h">
<!-- HTMLへ変換されたMarkdwon文章が入ります: ここから -->
{}
<!-- HTMLへ変換されたMarkdwon文章が入ります: ここまで -->
</article>
</body>
</html>"""
    markdown_text = file.read()

    mark2html = (m2h.ChainableMark2Html(markdown_text)
                 .my(yaml_processor))

    meta_data = yaml_processor.parse_yaml()
    replace_data = {
        "meta_description": meta_data['description'],
        "meta_keywords": meta_data['keywords'].replace('、', ',')
    }

    (mark2html
     .import_code()  # !最初に実行
     .code()  # !最初に実行
     .inline_code()
     .style()  # !最初に実行
     .script()  # !最初に実行
     .heading()
     .tilde()  # !strikeより前に実行
     .li()
     .ol()
     .horizon()  # !strongより前に実行
     .strong()  # !emより前に実行
     .em()
     .strike()
     .blockquote()
     .br()
     .link()
     .img(custom_image.callback_with_optional)
     .table()
     .paragraph()
     .wrap(wrap_html, **replace_data)
     .output(output_file_path, overwrite=True))

```

## カスタムプロセッサの追加
ChainableMark2Htmlでは、独自のMarkdown表記を処理するためのカスタムプロセッサを追加することができます。詳細は`ImageProcessor`クラスを参照してください。

