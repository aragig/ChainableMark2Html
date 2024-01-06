import unittest
import ChainableMark2Html as m2h


class TestMarkdownToHtml(unittest.TestCase):

    def test_strong(self):
        markdown_text = "ここには**強調**が含まれます。\n改行後にも**強調**が含まれます。"
        actual_html = (m2h.ChainableMark2Html(markdown_text)
                       .strong()
                       .to_html())
        expected_html = """ここには<strong>強調</strong>が含まれます。
改行後にも<strong>強調</strong>が含まれます。"""
        self.assertEqual(actual_html, expected_html)

    def test_bold_with_callback(self):
        def callback(text):
            return '<span class="strong">' + text + '</span>'

        markdown_text = "ここには**強調**が含まれます。\n改行後にも**強調**が含まれます。"
        actual_html = (m2h.ChainableMark2Html(markdown_text)
                       .strong(callback)
                       .to_html())
        expected_html = """ここには<span class="strong">強調</span>が含まれます。
改行後にも<span class="strong">強調</span>が含まれます。"""
        self.assertEqual(actual_html, expected_html)

    def test_em(self):
        markdown_text = """ここには*斜体*が含まれます。
改行後にも*斜体*が含まれます。"""
        actual_html = (m2h.ChainableMark2Html(markdown_text)
                       .em()
                       .to_html())
        expected_html = 'ここには<em>斜体</em>が含まれます。\n改行後にも<em>斜体</em>が含まれます。'
        self.assertEqual(actual_html, expected_html)

    def test_strike(self):
        markdown_text = "ここには~~取り消し~~が含まれます。\n改行後にも~~取り消し~~が含まれます。"
        actual_html = (m2h.ChainableMark2Html(markdown_text)
                       .strike()
                       .to_html())
        expected_html = 'ここには<strike>取り消し</strike>が含まれます。\n改行後にも<strike>取り消し</strike>が含まれます。'
        self.assertEqual(actual_html, expected_html)

    def test_em_strong(self):
        markdown_text = """
イタリック体は`*`で、ボールド体は`**`で作成できます。イタリックとボールドの両方を組み合わせることも可能です。

これは*イタリック*です

これは**ボールド**です

これは***イタリック＆ボールド***です
"""
        actual_html = (m2h.ChainableMark2Html(markdown_text)
                       .inline_code()
                       .strong()
                       .em()
                       .to_html())
        expected_html = """イタリック体は<span class="codeInline">*</span>で、ボールド体は<span class="codeInline">**</span>で作成できます。イタリックとボールドの両方を組み合わせることも可能です。

これは<em>イタリック</em>です

これは<strong>ボールド</strong>です

これは<em><strong>イタリック＆ボールド</strong></em>です"""
        self.assertEqual(actual_html, expected_html)


if __name__ == '__main__':
    unittest.main()
