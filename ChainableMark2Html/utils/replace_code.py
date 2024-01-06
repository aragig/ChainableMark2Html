import re
import os
from html import escape


# TODO store_managerを使うように変更する
def inline_code(text):
    lines = text.split('\n')
    processed_lines = []

    for line in lines:
        # Replace markdown inline code with HTML span element
        line = re.sub(r'`(.*?)`', lambda match: f'<span class="codeInline">{escape(match.group(1))}</span>', line)
        processed_lines.append(line)

    return '\n'.join(processed_lines)


def replace_import_code(text, base_dir):
    # コードブロック外の @import 文にのみマッチする正規表現
    pattern = r'(?<!```\n)@import "(.*?)"\n(?!.*?```)'
    # pattern = r'\n@import "(.*?)"\n'

    matches = re.findall(pattern, text)

    for match in matches:
        file_path = match
        file_name = os.path.basename(file_path)
        file_ext = file_path.split('.')[-1]
        path = os.path.join(base_dir, file_path)
        # ファイルの存在を確認
        if not os.path.exists(path):
            print(f'@import file not found: {path}')
            quit()


        with open(path, 'r') as file:
            source_code = file.read()
        # テキスト内の@import文を置換
        text = text.replace(f'\n@import "{match}"\n', f'\n```{file_ext}:{file_name}\n{source_code}\n```\n')
    return text


def inline_code_restore_callback(text):
    pattern = r'`(.*)`'
    match = re.search(pattern, text, re.S)
    if match is None:
        print("ここを通ることは通常あり得ない。")
        return text

    content = match.group(1)

    return f'<span class="codeInline">{escape(content)}</span>'


def code_restore_callback(text):
    #print(text)

    pattern = r'```(.*?)\n(.+?)\n```'
    match = re.search(pattern, text, re.S)

    if match is None:
        print("ここを通ることは通常あり得ない。")
        return text

    label = match.group(1)
    content = match.group(2)

    if label == "math":
        return f'{content}'

    elif label == "mermaid":
        return f'<div class="mermaid">{content}</div>'

    else:
        if label != '':
            if ':' in label:
                type = label.split(':')[0]
                label = label.split(':')[1]
                class_lang = f' class="{type}"'
            else:
                class_lang = f' class="{label}"'
        else:
            class_lang = ' class="plaintext"'

        code_label = f'<span class="code-label">{label}</span>'
        code = escape(content)  # HTMLエスケープが必要
        return f'<div class="code-block">{code_label}<pre class="code"><code{class_lang}>{code}</code></pre></div>'
