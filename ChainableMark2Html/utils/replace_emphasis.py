import re

import re


def em(text):
    italic_pattern = r'(\*)([^\n*]+?)(\*)'
    text = re.sub(italic_pattern, r'<em>\2</em>', text)
    return text


def strong(text, callback=None):
    pattern = r'\*\*([^\n*]+?)\*\*'

    def default_callback(phrase):
        return f'<strong>{phrase}</strong>'

    effective_callback = callback if callback is not None else default_callback

    return re.sub(pattern, lambda match: effective_callback(match.group(1)), text)


def strike(text):
    # Markdownの打ち消し線にマッチする正規表現
    pattern = r'~~([^~]+?)~~'

    # パターンにマッチする部分を<strike>タグで置換
    return re.sub(pattern, r'<strike>\1</strike>', text)
