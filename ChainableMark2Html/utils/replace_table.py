import re


def table_restore_callback(text):
    # ヘッダー行とデータ行を分割（区切り行を除外）
    header, _, *rows = text.strip().split('\n')

    # ヘッダー行をHTML形式に変換（左右のスペースを除去）
    header = '<th>' + '</th><th>'.join(cell.strip() for cell in header.strip('|').split('|')) + '</th>'
    header = f'<tr>{header}</tr>'

    # データ行をHTML形式に変換（左右のスペースを除去）
    html_rows = []
    for row in rows:
        row = '<td>' + '</td><td>'.join(cell.strip() for cell in row.strip('|').split('|')) + '</td>'
        html_rows.append(f'<tr>{row}</tr>')

    # 全体をtableタグで囲む
    html_table = f'\n<table class="defaultTable"><thead>{header}</thead><tbody>' + ''.join(html_rows) + '</tbody></table>\n'

    return html_table
