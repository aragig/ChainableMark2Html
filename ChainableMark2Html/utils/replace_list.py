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
                html += "<ul>\n"
                inside_list = True
                prev_indent = 0

            # If we are in a deeper level, start a new nested list
            if indent > prev_indent:
                html += "<ul>" * ((indent - prev_indent) // 4) + "\n"

            # If we are in a shallower level, close the previous nested list
            elif indent < prev_indent:
                html += "</ul>\n" * ((prev_indent - indent) // 4)

            # Add the list item
            html += f"<li>{line.strip()[2:]}</li>\n"
            prev_indent = indent

        else:
            # If not a list item and we are inside a list, close the list
            if inside_list:
                html += "</ul>\n" * (prev_indent // 4) + "</ul>\n"
                inside_list = False
                prev_indent = 0

            # Add the non-list line as is
            html += f"{line}\n"

    # Close any remaining open lists
    if inside_list:
        html += "</ul>\n" * (prev_indent // 4) + "</ul>\n"

    if html.endswith('\n'):
        return html[:-1]
    else:
        return html


def ordered_list(markdown_text):
    lines = markdown_text.split('\n')
    html = ""
    prev_indent = 0
    inside_list = False

    for line in lines:
        # Check if the line is an ordered list item
        if line.strip().split('. ', 1)[0].isdigit():
            indent = len(line) - len(line.lstrip(' '))

            # Start a new list if not already inside one
            if not inside_list:
                html += "<ol>\n"
                inside_list = True
                prev_indent = 0

            # If we are in a deeper level, start a new nested list
            if indent > prev_indent:
                html += "<ol>" * ((indent - prev_indent) // 4) + "\n"

            # If we are in a shallower level, close the previous nested list
            elif indent < prev_indent:
                html += "</ol>\n" * ((prev_indent - indent) // 4)

            # Add the list item
            html += f"<li>{line.split('. ', 1)[1]}</li>\n"
            prev_indent = indent

        else:
            # If not a list item and we are inside a list, close the list
            if inside_list:
                html += "</ol>\n" * (prev_indent // 4) + "</ol>\n"
                inside_list = False
                prev_indent = 0

            # Add the non-list line as is
            html += f"{line}\n"

    # Close any remaining open lists
    if inside_list:
        html += "</ol>\n" * (prev_indent // 4) + "</ol>\n"

    if html.endswith('\n'):
        return html[:-1]
    else:
        return html
