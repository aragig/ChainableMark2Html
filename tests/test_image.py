import re
import unittest
import ChainableMark2Html as m2h
from processor.custom_image_callback import CustomImage


class TestMarkdownToHtml(unittest.TestCase):

    def test_image(self):
        markdown_text = """
ここから
![alt](画像URL1)
![alt](画像URL2)
先頭の`!`で画像の<img>と認識されます。画像の大きさなどの指定をする場合はimgタグを使用します。
![alt](画像URL3)
ここまで
"""

        actual_html = (m2h.ChainableMark2Html(markdown_text)
                       .img()
                       .to_html())
        # TODO <img> はエスケープする必要あり
        expected_html = """ここから
<img src="画像URL1" alt="alt" title="alt">
<img src="画像URL2" alt="alt" title="alt">
先頭の`!`で画像の<img>と認識されます。画像の大きさなどの指定をする場合はimgタグを使用します。
<img src="画像URL3" alt="alt" title="alt">
ここまで"""
        self.assertEqual(actual_html, expected_html)

    def test_custom_image(self):
        markdown_text = """
ここから
![タイトル1](画像URL1)
![タイトル2](画像URL2)
先頭の`!`で画像の<img>と認識されます。画像の大きさなどの指定をする場合はimgタグを使用します。
![タイトル3](画像URL3)
ここまで
"""
        actual_html = (m2h.ChainableMark2Html(markdown_text)
                       .img()
                       .to_html())

        expected_html = """ここから
<img src="画像URL1" alt="タイトル1" title="タイトル1">
<img src="画像URL2" alt="タイトル2" title="タイトル2">
先頭の`!`で画像の<img>と認識されます。画像の大きさなどの指定をする場合はimgタグを使用します。
<img src="画像URL3" alt="タイトル3" title="タイトル3">
ここまで"""
        self.assertEqual(actual_html, expected_html)


    def test_callback_img(self):
        custom_image = CustomImage("/images", "/images_medium", "/images_small")

        markdown_text = """
![ChainableMark2Htmlロゴ1](chainable_mark2html_logo.png)
![ChainableMark2Htmlロゴ2](chainable_mark2html_logo.png w:400 h:300)
![ChainableMark2Htmlロゴ2](chainable_mark2html_logo.png h:300)
"""
        actual_html = (m2h.ChainableMark2Html(markdown_text)
                       .img(custom_image.callback_with_optional)
                       .to_html())

        expected_html = """<figure><picture><source media="(max-width: 560px)" srcset="chainable_mark2html_logo.jpg"><a href="/images/chainable_mark2html_logo.jpg" class="img-zoom"><img src="/images_medium/chainable_mark2html_logo.jpg" alt="ChainableMark2Htmlロゴ1" title="ChainableMark2Htmlロゴ1" loading="lazy" data-original="/images/chainable_mark2html_logo.jpg"></a></picture><figcaption>ChainableMark2Htmlロゴ1</figcaption></figure>
<figure><picture><source media="(max-width: 560px)" srcset="chainable_mark2html_logo.jpg"><a href="/images/chainable_mark2html_logo.jpg" class="img-zoom"><img src="/images_medium/chainable_mark2html_logo.jpg" alt="ChainableMark2Htmlロゴ2" title="ChainableMark2Htmlロゴ2" loading="lazy" data-original="/images/chainable_mark2html_logo.jpg" style="max-width:400px;max-height:300px"></a></picture><figcaption>ChainableMark2Htmlロゴ2</figcaption></figure>
<figure><picture><source media="(max-width: 560px)" srcset="chainable_mark2html_logo.jpg"><a href="/images/chainable_mark2html_logo.jpg" class="img-zoom"><img src="/images_medium/chainable_mark2html_logo.jpg" alt="ChainableMark2Htmlロゴ2" title="ChainableMark2Htmlロゴ2" loading="lazy" data-original="/images/chainable_mark2html_logo.jpg" style="max-height:300px"></a></picture><figcaption>ChainableMark2Htmlロゴ2</figcaption></figure>"""

        self.assertEqual(actual_html, expected_html)


if __name__ == '__main__':
    unittest.main()
