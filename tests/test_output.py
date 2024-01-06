import unittest
import ChainableMark2Html as m2h
from processor.custom_image_callback import CustomImage
from processor.parse_yaml_processor import ParseYamlProcessor


class TestMarkdownToHtml(unittest.TestCase):

    def test_wrap(self):
        markdown_text = """
```html
<html>
    <script>
        ここはコードブロック内
    </script>
    <style>
        ここはコードブロック内
    </style>
</html>
```

<style>
スタイルタグの中はエスケープされるので、**強調**や_イタリック_など色々書いても大丈夫。
</style>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.3/Chart.min.js"></script>
<script type="application/ld+json">
JavaScriptタグの中は**強調**や_イタリック_など色々書いても大丈夫。
</script>
"""
        actual_html = (m2h.ChainableMark2Html(markdown_text)
                       .import_code()  # !最初に実行
                       .code()  # !最初に実行
                       .style()
                       .script()
                       .strong()  # !italicより前に実行
                       .em()  # !boldより後に実行
                       .wrap(
            '<html><head><title>ChainableMark2Html</title><link rel="stylesheet" type="text/css" href="cm2h.css"></head><body>{}</body></html>')
                       .to_html())

        expected_html = """<html><head><title>ChainableMark2Html</title><link rel="stylesheet" type="text/css" href="cm2h.css"></head><body>

<div class="code-block"><span class="code-label">html</span><pre class="code"><code class="html">&lt;html&gt;
    &lt;script&gt;
        ここはコードブロック内
    &lt;/script&gt;
    &lt;style&gt;
        ここはコードブロック内
    &lt;/style&gt;
&lt;/html&gt;</code></pre></div>

<style>
スタイルタグの中はエスケープされるので、**強調**や_イタリック_など色々書いても大丈夫。
</style>

<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.3/Chart.min.js"></script>

<script type="application/ld+json">
JavaScriptタグの中は**強調**や_イタリック_など色々書いても大丈夫。
</script>

</body></html>"""

        self.assertEqual(actual_html, expected_html)

    def is_exist_file(self, path):
        import os
        return os.path.exists(path)

    def test_output1(self):
        markdown_text = """
```html
<html>
    <script>
        ここはコードブロック内
    </script>
    <style>
        ここはコードブロック内
    </style>
</html>
```

<style>
スタイルタグの中はエスケープされるので、**強調**や_イタリック_など色々書いても大丈夫。
</style>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.3/Chart.min.js"></script>
<script type="application/ld+json">
JavaScriptタグの中は**強調**や_イタリック_など色々書いても大丈夫。
</script>
"""
        output_file_path = '../public/test_output1.html'

        (m2h.ChainableMark2Html(markdown_text)
         .import_code()  # !最初に実行
         .code()  # !最初に実行
         .style()
         .script()
         .strong()  # !italicより前に実行
         .em()  # !boldより後に実行
         .wrap(
            '<html><head><meta charset="UTF-8"><title>ChainableMark2Html</title><link rel="stylesheet" type="text/css" href="cm2h.css"></head><body>{}</body></html>')
         .output(output_file_path, overwrite=True))

        self.assertTrue(self.is_exist_file(output_file_path))

    def test_output2(self):
        custom_image = CustomImage("./images", "./images_medium", "./images_medium")

        with open("sample.md", 'r') as file:
            output_file_path = '../public/test_output2.html'
            wrap_html = """<html>
<head>
<meta charset="UTF-8">
<title>ChainableMark2Html</title>
<link rel="stylesheet" type="text/css" href="cm2h.css">
</head>
<body>
{}
</body>
</html>"""
            markdown_text = file.read()

            (m2h.ChainableMark2Html(markdown_text)
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
             .wrap(wrap_html)
             .output(output_file_path, overwrite=True))

            self.assertTrue(self.is_exist_file(output_file_path))

    def test_output3(self):
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
             .url()
             .link()
             .img(custom_image.callback_with_optional)
             .table()
             .paragraph()
             .wrap(wrap_html, **replace_data)
             .output(output_file_path, overwrite=True))

            self.assertTrue(self.is_exist_file(output_file_path))


if __name__ == '__main__':
    unittest.main()
