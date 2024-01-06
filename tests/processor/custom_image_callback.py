import os
import re


class CustomImage:
    def __init__(self, high_quality_image_dir, medium_quality_image_dir, low_quality_image_dir):
        self.high_quality_image_dir = high_quality_image_dir
        self.medium_quality_image_dir = medium_quality_image_dir
        self.low_quality_image_dir = low_quality_image_dir
        self.caption_flag = True

    def callback_with_optional(self, path_info, title):
        # 画像属性を格納する辞書を初期化
        attributes = {
            'src': '',
            'alt': title,
            'title': title,
            'loading': 'lazy',  # TODO eyecatchなど最初の画像の場合はlazyを外す
            'data-original': '',
        }

        src_path, optional = self.__parse_image_src(path_info)

        if optional:
            # optional 辞書から幅と高さを取得
            width = optional.get('w')
            height = optional.get('h')
            caption_flag = optional.get('c')
            if caption_flag == 'false':
                self.caption_flag = False
            else:
                self.caption_flag = True

            # スタイル属性の文字列を構築
            style_parts = []
            if width:
                style_parts.append(f"max-width:{width}px")
            if height:
                style_parts.append(f"max-height:{height}px")

            # スタイル属性を設定（幅または高さが存在する場合のみ）
            if style_parts:
                attributes['style'] = ';'.join(style_parts)

        src_path = self.__replace_ext_png_to_jpg(src_path)
        attributes['src'] = os.path.join(self.medium_quality_image_dir, src_path)
        attributes['data-original'] = os.path.join(self.high_quality_image_dir, src_path)

        # HTMLを生成
        result_html = self.__generate_img_html(attributes)
        result_html = self.__wrap_anchor_tag(result_html, src_path)
        result_html = self.__wrap_picture_tag(result_html, src_path)
        result_html = self.__wrap_figure(result_html, title)

        return result_html

    def __generate_img_html(self, attributes):
        # 属性辞書からHTMLを生成
        attrs = ' '.join([f'{key}="{value}"' for key, value in attributes.items()])
        return f'<img {attrs}>'


    def __wrap_anchor_tag(self, html, src_path):
        href = os.path.join(self.high_quality_image_dir, src_path)
        return f'<a href="{href}" class="img-zoom">{html}</a>'

    def __wrap_picture_tag(self, html, url):
        source = f'<source media="(max-width: 560px)" srcset="{url}">'
        return f'<picture>{source}{html}</picture>'

    def __wrap_figure(self, html, title):
        figcaption = ''
        if title and self.caption_flag:
            figcaption = f'<figcaption>{title}</figcaption>'
        return f'<figure>{html}{figcaption}</figure>'

    def __replace_ext_png_to_jpg(self, text):
        pattern = r'^(.*)\.png$'
        match = re.match(pattern, text)
        if match:
            return match.groups()[0] + '.jpg'
        else:
            return text

    def __parse_image_src(self, img_src):
        # ファイル名とその後のオプション部分を分割
        parts = img_src.split(maxsplit=1)
        file_name = parts[0]
        options = None

        if len(parts) > 1:
            options_str = parts[1]
            # オプション（キー:値）を抽出する正規表現
            option_matches = re.findall(r'(\w+):([^ ]+)', options_str)
            if option_matches:
                options = {key: value for key, value in option_matches}

        return file_name, options
