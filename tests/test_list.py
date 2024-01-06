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


別のセクション
- アイテムA
- アイテムB
終わり
"""
        actual_html = m2h.ChainableMark2Html(markdown_text).li().to_html()

        expected_html = """ここから
<ul>
<li>リスト1</li>
<ul>
<li>リスト1_1</li>
<ul>
<li>リスト1_1_1</li>
<li>リスト1_1_2</li>
</ul>
<li>リスト1_2</li>
</ul>
<li>リスト2</li>
<li>リスト3</li>
</ul>
ここまで

別のセクション
<ul>
<li>アイテムA</li>
<li>アイテムB</li>
</ul>
終わり"""
        self.assertEqual(actual_html, expected_html)

    def test_ordered_list(self):
        markdown_text = """
ここから
1. 項目1
    1. 項目1_1
        1. 項目1_1_1
        2. 項目1_1_2
    2. 項目1_2
2. 項目2
3. 項目3
ここまで


別のセクション
1. 項目1
2. 項目2
3. 項目3
終わり
"""
        actual_html = m2h.ChainableMark2Html(markdown_text).ol().to_html()

        expected_html = """ここから
<ol>
<li>項目1</li>
<ol>
<li>項目1_1</li>
<ol>
<li>項目1_1_1</li>
<li>項目1_1_2</li>
</ol>
<li>項目1_2</li>
</ol>
<li>項目2</li>
<li>項目3</li>
</ol>
ここまで

別のセクション
<ol>
<li>項目1</li>
<li>項目2</li>
<li>項目3</li>
</ol>
終わり"""
        self.assertEqual(actual_html, expected_html)

    def test_ordered_list2(self):
        markdown_text = """
`番号.`を先頭に記述します。ネストはタブで表現します。  
番号は自動的に採番されるため、すべての行を1.と記述するのがお勧めです。
1. 番号付きリスト1
    1. 番号付きリスト1-1
    1. 番号付きリスト1-2
1. 番号付きリスト2
1. 番号付きリスト3
"""

        actual_html = m2h.ChainableMark2Html(markdown_text).inline_code().ol().to_html()

        expected_html = """<span class="codeInline">番号.</span>を先頭に記述します。ネストはタブで表現します。  
番号は自動的に採番されるため、すべての行を1.と記述するのがお勧めです。
<ol>
<li>番号付きリスト1</li>
<ol>
<li>番号付きリスト1-1</li>
<li>番号付きリスト1-2</li>
</ol>
<li>番号付きリスト2</li>
<li>番号付きリスト3</li>
</ol>"""
        self.assertEqual(actual_html, expected_html)

    def test_chatgpt_markdown(self):
        markdown_text = """
macOSやiPhoneでハガキの宛名を作成する方法にはいくつかのオプションがあります。以下にいくつかの方法を紹介します。

### macOS用の方法
1. **Pagesを使用する**: AppleのPagesはmacOSにプリインストールされていることが多く、ハガキの宛名のデザインに便利です。テンプレートを利用するか、新規にデザインを作成できます。
2. **Microsoft Wordを使用する**: Wordには多くのテンプレートが用意されており、ハガキの宛名の作成に使用できます。
3. **専用のアプリを利用する**: ハガキ作成に特化した専用アプリがいくつかあります。これらのアプリは、宛名の印刷に便利な機能を提供します。

### iPhoneアプリ
1. **Appleの「連絡先」アプリ**: 連絡先アプリを使用して宛名を管理し、それを印刷に使うことができます。
2. **専用のハガキ作成アプリ**: App Storeにはハガキ作成のための専用アプリがいくつかあります。これらのアプリは、デザインのカスタマイズや印刷設定に特化しています。

### 共通のヒント
- **宛名のレイアウト**: 日本のハガキの宛名は特有のフォーマットがありますので、適切なレイアウトを選ぶことが重要です。
- **印刷設定**: ハガキのサイズや印刷の方向（縦書きか横書きか）を正しく設定することが大切です。

これらのツールを使用することで、macOSやiPhone上で簡単にハガキの宛名を作成し、印刷することができます。
"""
        actual_html = (m2h.ChainableMark2Html(markdown_text)
                       .inline_code()
                       .heading()
                       .strong()
                       .li()
                       .ol()
                       .to_html())

        expected_html = """macOSやiPhoneでハガキの宛名を作成する方法にはいくつかのオプションがあります。以下にいくつかの方法を紹介します。

<h3>macOS用の方法</h3>

<ol>
<li><strong>Pagesを使用する</strong>: AppleのPagesはmacOSにプリインストールされていることが多く、ハガキの宛名のデザインに便利です。テンプレートを利用するか、新規にデザインを作成できます。</li>
<li><strong>Microsoft Wordを使用する</strong>: Wordには多くのテンプレートが用意されており、ハガキの宛名の作成に使用できます。</li>
<li><strong>専用のアプリを利用する</strong>: ハガキ作成に特化した専用アプリがいくつかあります。これらのアプリは、宛名の印刷に便利な機能を提供します。</li>
</ol>

<h3>iPhoneアプリ</h3>

<ol>
<li><strong>Appleの「連絡先」アプリ</strong>: 連絡先アプリを使用して宛名を管理し、それを印刷に使うことができます。</li>
<li><strong>専用のハガキ作成アプリ</strong>: App Storeにはハガキ作成のための専用アプリがいくつかあります。これらのアプリは、デザインのカスタマイズや印刷設定に特化しています。</li>
</ol>

<h3>共通のヒント</h3>

<ul>
<li><strong>宛名のレイアウト</strong>: 日本のハガキの宛名は特有のフォーマットがありますので、適切なレイアウトを選ぶことが重要です。</li>
<li><strong>印刷設定</strong>: ハガキのサイズや印刷の方向（縦書きか横書きか）を正しく設定することが大切です。</li>
</ul>

これらのツールを使用することで、macOSやiPhone上で簡単にハガキの宛名を作成し、印刷することができます。"""

        self.assertEqual(actual_html, expected_html)


if __name__ == '__main__':
    unittest.main()
