import unittest
import ChainableMark2Html as m2h


class TestMarkdownToHtml(unittest.TestCase):

    def test_import_code(self):
        markdown_text = """
ソースコードを読み込みます。
@import "__init__.py"
終わり
"""
        actual_html = (m2h.ChainableMark2Html(markdown_text)
                       .import_code()
                       .to_html())

        expected_html = """ソースコードを読み込みます。

<div class="code-block"><span class="code-label">__init__.py</span><pre class="code"><code class="py">#from .main import *
from .chainable_mark2html import ChainableMark2Html

__all__ = [&quot;ChainableMark2Html&quot;]
</code></pre></div>

終わり"""
        self.assertEqual(actual_html, expected_html)

    def test_code_inline(self):
        markdown_text = "This is a line with `inline code` and here is another `piece of code`.\nThis line doesn't have any."
        actual_html = (m2h.ChainableMark2Html(markdown_text)
                       .inline_code()
                       .to_html())
        expected_html = """This is a line with <span class="codeInline">inline code</span> and here is another <span class="codeInline">piece of code</span>.
This line doesn't have any."""
        self.assertEqual(actual_html, expected_html)

    def test_code_inline2(self):
        markdown_text = """
`番号.`を先頭に記述します。ネストはタブで表現します。
"""
        actual_html = (m2h.ChainableMark2Html(markdown_text)
                       .inline_code()
                       .to_html())
        expected_html = '<span class="codeInline">番号.</span>を先頭に記述します。ネストはタブで表現します。'

        self.assertEqual(actual_html, expected_html)

    def test_code1(self):
        markdown_text = """
ここから
```cpp:main.cpp
#include <iostream>
/**コメント**/
int main() {
std::cout << "Hello, World!" << std::endl;
return 0;
}
```
ここまで
"""
        actual_html = (m2h.ChainableMark2Html(markdown_text)
                       .code()
                       .to_html())

        expected_html = """ここから

<div class="code-block"><span class="code-label">main.cpp</span><pre class="code"><code class="cpp">#include &lt;iostream&gt;
/**コメント**/
int main() {
std::cout &lt;&lt; &quot;Hello, World!&quot; &lt;&lt; std::endl;
return 0;
}</code></pre></div>

ここまで"""
        self.assertEqual(actual_html, expected_html)

    def test_code2(self):
        markdown_text = """
ここからコードを表現します。
```cpp
#include <iostream>
/*** コメント ***/

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
```
ここでコードは終了します。
ファイル名もつけられます。
```cpp:main.cpp
#include <iostream>
/**コメント**/
int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}

```
以上です。
"""
        actual_html = (m2h.ChainableMark2Html(markdown_text)
                       .code()
                       .to_html())

        expected_html = """ここからコードを表現します。

<div class="code-block"><span class="code-label">cpp</span><pre class="code"><code class="cpp">#include &lt;iostream&gt;
/*** コメント ***/

int main() {
    std::cout &lt;&lt; &quot;Hello, World!&quot; &lt;&lt; std::endl;
    return 0;
}</code></pre></div>

ここでコードは終了します。
ファイル名もつけられます。

<div class="code-block"><span class="code-label">main.cpp</span><pre class="code"><code class="cpp">#include &lt;iostream&gt;
/**コメント**/
int main() {
    std::cout &lt;&lt; &quot;Hello, World!&quot; &lt;&lt; std::endl;
    return 0;
}
</code></pre></div>

以上です。"""
        self.assertEqual(actual_html, expected_html)

    def test_style(self):
        markdown_text = """
ここから
<style>
スタイルタグの中はエスケープされるので、**強調**や_イタリック_など色々書いても大丈夫。
</style>
ここまで
"""
        actual_html = (m2h.ChainableMark2Html(markdown_text)
                       .style()
                       .to_html())

        expected_html = """ここから

<style>
スタイルタグの中はエスケープされるので、**強調**や_イタリック_など色々書いても大丈夫。
</style>

ここまで"""
        self.assertEqual(actual_html, expected_html)

    def test_style_script(self):
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
                       .code()  # TODO scriptより前に実行しないとダメ
                       .script()
                       .to_html())

        expected_html = """<div class="code-block"><span class="code-label">html</span><pre class="code"><code class="html">&lt;html&gt;
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
</script>"""
        self.assertEqual(actual_html, expected_html)


if __name__ == '__main__':
    unittest.main()
