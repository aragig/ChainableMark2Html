import unittest
import ChainableMark2Html as m2h


class TestMarkdownToHtml(unittest.TestCase):

    def test_unordered_list(self):
        markdown_text = """
ここから
- リスト1
    - リスト1_1
        - リスト1_1_1
        - リスト1_1_2
    - リスト1_2
- リスト2
- リスト3
ここまで


ここから
1. 項目1
    1. 項目1_1
        1. 項目1_1_1
        2. 項目1_1_2
    2. 項目1_2
2. 項目2
3. 項目3
ここまで"""
        actual_html = m2h.ChainableMark2Html(markdown_text).list().to_html()

        expected_html = """ここから
<ul>
  <li>リスト1<ul>
  <li>リスト1_1</li>
</ul>
<ul>
  <li>リスト1_1_1</li>
</ul>
<ul>
  <li>リスト1_1_2</li>
</ul>
<ul>
  <li>リスト1_2</li>
</ul>
</li>
  <li>リスト2</li>
  <li>リスト3</li>
</ul>
ここまで

ここから
<ol>
  <li>項目1<ol>
  <li>項目1_1</li>
</ol>
<ol>
  <li>項目1_1_1</li>
</ol>
<ol>
  <li>項目1_1_2</li>
</ol>
<ol>
  <li>項目1_2</li>
</ol>
</li>
  <li>項目2</li>
  <li>項目3</li>
</ol>
ここまで"""
        self.assertEqual(actual_html, expected_html)



if __name__ == '__main__':
    unittest.main()
