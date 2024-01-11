def unordered_list(markdown_text):
    lines = markdown_text.split('\n')
    html = ""
    prev_indent = 0
    inside_list = False

    for line in lines:
        # Check if the line is a list item
        if line.strip().startswith('- '):
            indent = len(line) - len(line.lstrip(' '))

            # Start a new list if not already inside one
            if not inside_list:
                html += "<ul>"
                inside_list = True
                prev_indent = 0

            # If we are in a deeper level, start a new nested list
            if indent > prev_indent:
                html += "<ul>" * ((indent - prev_indent) // 4) + ""

            # If we are in a shallower level, close the previous nested list
            elif indent < prev_indent:
                html += "</ul>" * ((prev_indent - indent) // 4)

            # Add the list item
            html += f"<li>{line.strip()[2:]}</li>\n"
            prev_indent = indent

        else:
            # If not a list item and we are inside a list, close the list
            if inside_list:
                html += "</ul>\n" * (prev_indent // 4) + "\n"
                inside_list = False
                prev_indent = 0

            # Add the non-list line as is
            html += f"{line}\n"

    # Close any remaining open lists
    if inside_list:
        html += "</ul>\n" * (prev_indent // 4) + "\n"

    if html.endswith('\n'):
        return html[:-1]
    else:
        return html


def ordered_list(markdown_text):
    lines = markdown_text.split('\n')
    html = ""
    prev_indent = 0
    inside_list = False
    #TODO ネストでバグあり

    for line in lines:
        if line.strip().split('. ', 1)[0].isdigit():  # 文字が数値であるかどうか判定

            indent = len(line) - len(line.lstrip(' '))

            if not inside_list:  # リストのスタート
                # html += "<ol>\n"
                inside_list = True
                prev_indent = 0

            if indent > prev_indent:  # インデントが深くなった場合
                html += "<ol>" * ((indent - prev_indent) // 4) + ""

            elif indent < prev_indent: # インデントが浅くなった場合
                html += "</ol>" * ((prev_indent - indent) // 4)

            # Add the list item
            html += f"<li>{line.split('. ', 1)[1]}</li>\n"
            prev_indent = indent

        else:
            if inside_list:  # 最後にリストを閉じる
                #print(prev_indent // 4)
                html += "</ol></li>\n" * (prev_indent // 4) + ""
                inside_list = False
                prev_indent = 0

            # Add the non-list line as is
            html += f"{line}\n"

    if inside_list:
        # 基本的にここを通ることはないが、安全のため
        html += "</ol></li>\n" * (prev_indent // 4) + "\n"

    if html.endswith('\n'):
        return html[:-1]
    else:
        return html
