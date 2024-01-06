import re


def br(text):
    """
    Converts markdown line breaks (double space followed by a newline) to HTML <br> tags.
    """
    # Pattern for markdown line breaks (two spaces followed by a newline)
    pattern = r'  \n'

    # Replace markdown line breaks with HTML <br> tags
    text = re.sub(pattern, '<br>\n', text)

    return text


def horizon(text):
    # Pattern matches horizontal lines in Markdown (***, ---, ___) with optional spaces,
    # and removes spaces before and after the line.
    pattern = r'\s*\n\s*(---)\s*\n\s*'
    text = re.sub(pattern, r'\n<hr>\n', text)
    return text


def paragraph(text):
    """
    Wraps sections of text with two or more consecutive line breaks in <p> tags,
    excluding sections that start with Markdown headers.
    """
    # Split the text by two or more consecutive line breaks
    paragraphs = text.split('\n\n')

    # Wrap each paragraph with <p> tags, excluding headers
    wrapped_text = ''
    for paragraph in paragraphs:
        # Remove any leading or trailing whitespace
        trimmed_paragraph = paragraph.strip()

        # Only wrap non-empty paragraphs and exclude headers
        if trimmed_paragraph and not trimmed_paragraph.startswith('$$$'):
            wrapped_text += f'<p>{trimmed_paragraph}</p>\n'
        else:
            # Add headers without <p> tags
            wrapped_text += f'{trimmed_paragraph}'

    return wrapped_text


def consolidate_newlines(text):
    # print(text)
    # Replace any occurrence of two or more newlines with exactly two newlines
    return re.sub(r'\n{2,}', '\n\n', text)

