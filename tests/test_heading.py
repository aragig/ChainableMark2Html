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


if __name__ == '__main__':
    unittest.main()
