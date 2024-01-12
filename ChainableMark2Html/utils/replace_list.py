import re


def replace_list(markdown_text):
    # Function to convert a single list (not nested) to HTML
    def convert_list_to_html(list_items, list_type):
        html_list = f'<{list_type}>\n'
        for item in list_items:
            html_list += f'  <li>{item}</li>\n'
        html_list += f'</{list_type}>\n'
        return html_list

    # Function to handle nested lists
    def handle_nested_list(lines):
        html_output = ''
        current_list = []
        list_type = None

        for line in lines:
            # Check for unordered list
            if line.startswith('- '):
                if list_type == 'ol':
                    html_output += convert_list_to_html(current_list, list_type)
                    current_list = []
                list_type = 'ul'
                current_list.append(line.strip()[2:])

            # Check for ordered list
            elif re.match(r'\d+\. ', line):
                if list_type == 'ul':
                    html_output += convert_list_to_html(current_list, list_type)
                    current_list = []
                list_type = 'ol'
                current_list.append(re.sub(r'\d+\.\s', '', line.strip()))

            # Handle nested lists
            elif line.startswith('    ') or line.startswith('\t'):
                print('ネスト')
                nested_lines = handle_nested_list([line[4:]])
                if current_list:
                    current_list[-1] += nested_lines
                else:
                    html_output += nested_lines

            # Non-list line
            else:
                if current_list:
                    html_output += convert_list_to_html(current_list, list_type)
                    current_list = []
                    list_type = None
                html_output += line + '\n'

        # Convert any remaining list items
        if current_list:
            html_output += convert_list_to_html(current_list, list_type)

        return html_output

    # Split the markdown text into lines and process each line
    lines = markdown_text.split('\n')
    return handle_nested_list(lines)


if __name__ == '__main__':
    markdown_example = """
- Item 1
- Item 2
    - Subitem 2.1
    - Subitem 2.2
        1. Sub-subitem 2.2.1
        2. Sub-subitem 2.2.2
1. Item 3
2. Item 4
    1. Subitem 4.1
    2. Subitem 4.2
"""

    # Convert and display the HTML
    html_output = replace_list(markdown_example)
    print(html_output)