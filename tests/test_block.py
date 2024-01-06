import unittest
import ChainableMark2Html as m2h


class TestMarkdownToHtml(unittest.TestCase):
    def test_blockquote(self):
        markdown_text = "引用します\n> Quote line 1\n>  Quote line 2\nNormal line"
        actual_html = m2h.ChainableMark2Html(markdown_text).blockquote().to_html()
        expected_html = """引用します
<blockquote>
Quote line 1
Quote line 2
</blockquote>
Normal line"""
        self.assertEqual(actual_html, expected_html)

    def test_tilde1(self):
        markdown_text = """
チルダを使います
~~~
チルダの中身はこんな感じ。
改行も入れたりなんかりして。
**強調表現**もできます！
~~~
チルダの外
"""
        actual_html = m2h.ChainableMark2Html(markdown_text).tilde().strong().to_html()
        expected_html = """チルダを使います
<div class="tilde">チルダの中身はこんな感じ。
改行も入れたりなんかりして。
<strong>強調表現</strong>もできます！</div>
チルダの外"""
        self.assertEqual(actual_html, expected_html)

    def test_tilde2(self):
        markdown_text = """
ここから
~~~
チルダの中身はこんな感じ。
改行も入れたりなんかりして。
~~~
チルダの外
~~~
チルダの中身はこんな感じ。
改行も入れたりなんかりして。
~~~
ここまで
"""
        actual_html = m2h.ChainableMark2Html(markdown_text).tilde().strong().to_html()
        expected_html = """ここから
<div class="tilde">チルダの中身はこんな感じ。
改行も入れたりなんかりして。</div>
チルダの外
<div class="tilde">チルダの中身はこんな感じ。
改行も入れたりなんかりして。</div>
ここまで"""
        self.assertEqual(actual_html, expected_html)


if __name__ == '__main__':
    unittest.main()
