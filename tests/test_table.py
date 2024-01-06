import unittest
import ChainableMark2Html as m2h


class TestMarkdownToHtml(unittest.TestCase):

    def test_table1(self):
        markdown_text = """
ここから
| Header 1 | Header 2 | Header 3 | Header 4 | Header 5 |
|----------|----------|----------|----------|----------|
| Data 1   | Data 2   | **Data 3**   | Data 4   | Data 5   |
| Data 1   | Data 2   | Data 3   | Data 4   | Data 5   |
| Data 1   | Data 2   | Data 3   | Data 4   | Data 5   |
ここまで
"""
        actual_html = (m2h.ChainableMark2Html(markdown_text)
                       .strong()  # !store_managerのためtable()より後に実行する必要がある
                       .table()
                       .to_html())
        expected_html = """ここから

<table class="defaultTable"><thead><tr><th>Header 1</th><th>Header 2</th><th>Header 3</th><th>Header 4</th><th>Header 5</th></tr></thead><tbody><tr><td>Data 1</td><td>Data 2</td><td><strong>Data 3</strong></td><td>Data 4</td><td>Data 5</td></tr><tr><td>Data 1</td><td>Data 2</td><td>Data 3</td><td>Data 4</td><td>Data 5</td></tr><tr><td>Data 1</td><td>Data 2</td><td>Data 3</td><td>Data 4</td><td>Data 5</td></tr></tbody></table>

ここまで"""
        self.assertEqual(actual_html, expected_html)

    def test_table2(self):
        markdown_text = """
ここから
| TH1 | TH2 |
|-----|----|
| TD1 | TD3 |
| TD2 | TD4 |
ここまで
"""
        actual_html = (m2h.ChainableMark2Html(markdown_text)
                       .table()
                       .to_html())
        expected_html = """ここから

<table class="defaultTable"><thead><tr><th>TH1</th><th>TH2</th></tr></thead><tbody><tr><td>TD1</td><td>TD3</td></tr><tr><td>TD2</td><td>TD4</td></tr></tbody></table>

ここまで"""
        self.assertEqual(actual_html, expected_html)


if __name__ == '__main__':
    unittest.main()
