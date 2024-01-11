import re
import urllib.parse


def replace_toc(processing_text, level=2):
    toc = __search_heading(processing_text, level)
    toc_text = ''
    for level, heading in toc:
        # toc_text += f'{"  " * (level - 1)}- [{heading}](#{heading.lower().replace(" ", "-")})\n'
        encoded_heading_text = urllib.parse.quote(heading)
        toc_text += f'{"    " * (level - 1)}1. <a href="#{encoded_heading_text}">{heading}</a>\n'
        # print(f'{"  " * (level - 1)}- {heading}')
    if toc_text != '':
        toc_text = '<div class="toc">\n' + toc_text + '</div>\n'

    processing_text = __replace_toc_tag_to_html(processing_text, toc_text)
    return processing_text


def __search_heading(markdown_text, max_level=6):
    pattern = r'^#{2,' + str(max_level) + r'}\s+(.*)'
    # 各見出しを探して、目次のエントリを作成する
    toc = []
    for line in markdown_text.split('\n'):
        match = re.match(pattern, line)
        if match:
            heading = match.group(1).strip()
            level = line.count('#')  # 見出しのレベルを数える
            toc.append((level, heading))

    return toc


def __replace_toc_tag_to_html(html, toc_html):
    lines = html.split('\n')
    for i, line in enumerate(lines):
        if re.match(r'^\[TOC\]$', line):
            lines[i] = toc_html

    html = '\n'.join(lines)
    return html
    # pattern = r'\s*\[TOC\]\s*'
    # return re.sub(pattern, toc_html, html)