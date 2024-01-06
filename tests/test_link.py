import unittest
import ChainableMark2Html as m2h


class TestMarkdownToHtml(unittest.TestCase):

    def test_url1(self):
        markdown_text = "URLを紹介します: https://www.example.com URLの後にはスペースまたは改行を入れてください。 http://www.testsite.com\n"
        actual_html = (m2h.ChainableMark2Html(markdown_text)
                       .url()
                       .link()
                       .to_html())
        expected_html = 'URLを紹介します: <a href="https://www.example.com">https://www.example.com</a> URLの後にはスペースまたは改行を入れてください。 <a href="http://www.testsite.com">http://www.testsite.com</a>'
        self.assertEqual(actual_html, expected_html)

    def test_url2(self):
        markdown_text = "なぜか分かりませんが、2つ目のURLに改行がなくても機能します:\nhttps://www.example.com\nhttp://www.testsite.com"
        actual_html = (m2h.ChainableMark2Html(markdown_text)
                       .url()
                       .link()
                       .to_html())
        expected_html = """なぜか分かりませんが、2つ目のURLに改行がなくても機能します:
<a href="https://www.example.com">https://www.example.com</a>
<a href="http://www.testsite.com">http://www.testsite.com</a>"""
        self.assertEqual(actual_html, expected_html)

    def test_url3(self):
        markdown_text = """
urlをリンク形式で表示
- https://www.example.com
- https://www.example.com
ここまで 
"""
        actual_html = (m2h.ChainableMark2Html(markdown_text)
                       .li()
                       .ol()
                       .url()
                       .to_html())
        expected_html = """urlをリンク形式で表示
<ul>
<li><a href="https://www.example.com">https://www.example.com</a></li>
<li><a href="https://www.example.com">https://www.example.com</a></li>
</ul>
ここまで"""
        self.assertEqual(actual_html, expected_html)

    def test_custom_url(self):
        markdown_text = "Check out this website: https://www.example.com"
        actual_html = (m2h.ChainableMark2Html(markdown_text)
                       .url()
                       .link()
                       .to_html())
        expected_html = 'Check out this website: <a href="https://www.example.com">https://www.example.com</a>'
        self.assertEqual(actual_html, expected_html)

    def test_markdown_url(self):
        markdown_text = """
ここから
Check out this website: https://www.example.com
http://www.testsite.com
[Google](https://www.google.com/)にマッチするパターン
ここまで
"""
        actual_html = (m2h.ChainableMark2Html(markdown_text)
                       .url()
                       .link()
                       .to_html())
        expected_html = """ここから
Check out this website: <a href="https://www.example.com">https://www.example.com</a>
<a href="http://www.testsite.com">http://www.testsite.com</a>
<a href="https://www.google.com/">Google</a>にマッチするパターン
ここまで"""
        self.assertEqual(actual_html, expected_html)

    def test_markdown_url_callback(self):
        def callback(url):
            # TODO ここでurlへアクセスしてタイトルを取得する
            return f'<a href="{url}">ここでurlへアクセスしてタイトルを取得する</a>'

        markdown_text = """
https://101010.fun
https://kitchen-note.fun
"""
        actual_html = (m2h.ChainableMark2Html(markdown_text)
                       .url(callback)
                       .link()
                       .to_html())
        expected_html = """<a href="https://101010.fun">ここでurlへアクセスしてタイトルを取得する</a>
<a href="https://kitchen-note.fun">ここでurlへアクセスしてタイトルを取得する</a>"""
        self.assertEqual(actual_html, expected_html)

    def test_markdown_inline_url(self):
        markdown_text = "テキスト内にも[表示文字1](http://101010.fun/)入れられます。テキスト内にも[表示文字2](http://101010.fun/)入れられます。\nテキスト内にも[表示文字3](http://101010.fun/)入れられます。"
        actual_html = (m2h.ChainableMark2Html(markdown_text)
                       .url()
                       .link()
                       .to_html())
        expected_html = """テキスト内にも<a href="http://101010.fun/">表示文字1</a>入れられます。テキスト内にも<a href="http://101010.fun/">表示文字2</a>入れられます。
テキスト内にも<a href="http://101010.fun/">表示文字3</a>入れられます。"""
        self.assertEqual(actual_html, expected_html)

    def test_markdown_inline_url2(self):
        markdown_text = "\n![画像の表示](https://101010.fun/images/site-logo.jpg)\n"
        actual_html = (m2h.ChainableMark2Html(markdown_text)
                       .url()
                       .link()
                       .img()
                       .to_html())
        expected_html = '<img src="https://101010.fun/images/site-logo.jpg" alt="画像の表示" title="画像の表示">'
        self.assertEqual(actual_html, expected_html)


if __name__ == '__main__':
    unittest.main()
