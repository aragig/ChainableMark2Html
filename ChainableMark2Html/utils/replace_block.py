import re
from html import escape


def blockquote(markdown_text):
    # TODO >> 多重引用に対応させる
    lines = markdown_text.split('\n')
    html_outputs = []
    in_blockquote = False

    for line in lines:
        if line.startswith('>'):
            if not in_blockquote:
                html_outputs.append('<blockquote>')
                in_blockquote = True
            # Remove the '>' character and any leading whitespace
            content = line[1:].lstrip()
            html_outputs.append(content)
        else:
            if in_blockquote:
                html_outputs.append('</blockquote>')
                in_blockquote = False
            html_outputs.append(line)

    # Close the blockquote tag if the text ends within a blockquote
    if in_blockquote:
        html_outputs.append('</blockquote>')

    return '\n'.join(html_outputs)


def tilde(markdown_text):
    # コードブロックを見つけて、HTMLに変換する
    def convert_to_html(match):
        code = match.group(1).strip()  # 先頭と末尾の空白を削除
        escaped_code = escape(code)
        return f'<div class="tilde">{escaped_code}</div>'

    pattern = r'~~~\s*\n(.*?)\n\s*~~~'
    return re.sub(pattern, convert_to_html, markdown_text, flags=re.DOTALL)
