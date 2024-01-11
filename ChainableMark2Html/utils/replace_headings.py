import re
import urllib.parse


class HeadingManager:

    def __init__(self):
        pass

    def headings_callback(self, markdown_text):
        # print(markdown_text)
        def toc(html_heading, level, heading_text):
            return html_heading

        def replace_heading(match):
            level = len(match.group(1))  # Determine the heading level based on the number of '#'
            heading_text = match.group(2).strip()
            encoded_heading_text = urllib.parse.quote(heading_text)

            html_heading = f'<h{level}><span id="{encoded_heading_text}" class="fragment"></span>{heading_text}</h{level}>\n'
            html_heading = toc(html_heading, level, heading_text)
            return html_heading

        for i in range(6, 0, -1):
            markdown_text = re.sub(r'^(#{' + str(i) + r'})\s*(.*?)\s*$', replace_heading, markdown_text, flags=re.MULTILINE)

        return markdown_text
