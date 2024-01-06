import unittest
import ChainableMark2Html as m2h


class TestMarkdownToHtml(unittest.TestCase):


    def test_br(self):
        markdown_text = """
スペース二つで<br>の改行を入れられます。  
And this is a new line.
"""

        actual_html = (m2h.ChainableMark2Html(markdown_text)
                       .br()
                       .to_html())

        expected_html = """スペース二つで<br>の改行を入れられます。<br>
And this is a new line."""
        self.assertEqual(actual_html, expected_html)

    def test_horizon(self):
        markdown_text = "Some text\n---\nSome more text\n   ---   \nAnd even more text\n   ---\nEnd of text."

        actual_html = (m2h.ChainableMark2Html(markdown_text)
                       .horizon()
                       .to_html())

        expected_html = """Some text
<hr>
Some more text
<hr>
And even more text
<hr>
End of text."""

        self.assertEqual(actual_html, expected_html)

    def test_paragraph1(self):
        markdown_text = """コンテンツ1
コンテンツ1

コンテンツ2
コンテンツ2
"""

        actual_html = (m2h.ChainableMark2Html(markdown_text)
                       .paragraph()
                       .to_html())

        expected_html = """<p>コンテンツ1
コンテンツ1</p>
<p>コンテンツ2
コンテンツ2</p>"""

        self.assertEqual(actual_html, expected_html)

    def test_paragraph2(self):
        markdown_text = """
## 見出し1
コンテンツ1

## 見出し2
コンテンツ2
コンテンツ2


"""

        actual_html = (m2h.ChainableMark2Html(markdown_text)
                       .heading()
                       .paragraph()  # !paragraph()は一番最後に実行
                       .to_html())

        expected_html = """<h2>見出し1</h2>
<p>コンテンツ1</p>
<h2>見出し2</h2>
<p>コンテンツ2
コンテンツ2</p>"""

        self.assertEqual(actual_html, expected_html)


if __name__ == '__main__':
    unittest.main()
