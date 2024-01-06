import re


def convert_markdown_link(text, callback=None):
    # [title](url)にマッチするパターン
    # url_pattern = r'(?<!\!)\[(.*?)\]\((.*?)\)'
    url_pattern = r'(?<!\!)\[(.*?)\]\((http[s]?://.*?)\)'

    def default_callback(url, title):
        return f'<a href="{url}">{title}</a>'

    # 提供されたコールバックを使用するか、デフォルトのコールバックを使用
    effective_callback = callback if callback is not None else default_callback

    # URLをHTMLの <a> タグに置換
    text = re.sub(url_pattern, lambda match: effective_callback(match.group(2), match.group(1)), text)
    return text


def url_callback(url, title):
    return f'<a href="{url}">{title}</a>'



def convert_urls_to_links(text, callback=None):
    """
    Converts URLs in the text to HTML links, excluding Markdown links and already linked URLs.
    If a callback function is provided, it is used to customize the HTML tag for each URL.
    """
    # Regular expression pattern for basic HTTP and HTTPS URLs,
    # excluding URLs in Markdown links, images, and already linked URLs
    url_pattern = r'(?<!\]\()(?<!href=")https?://[^\s|\r|\<]+(?![^\(\[]*\))(?![^<]*>)'

    def default_callback(url):
        return f'<a href="{url}">{url}</a>'

    # Use the provided callback if available, otherwise use the default callback
    effective_callback = callback if callback is not None else default_callback

    # Replace URLs with HTML anchor tags using the effective callback
    text = re.sub(url_pattern, lambda match: effective_callback(match.group(0)), text)
    return text

# def convert_urls_to_links(text, callback=None):
#     # 正規表現パターンを変更して、URLの前のスペースを保持
#     url_pattern = r'(\s|\r)(https?://[^\s|\r]+)'
#
#     def default_callback(url):
#         return f'<a href="{url}">{url}</a>'
#
#     # 提供されたコールバックを使用するか、デフォルトのコールバックを使用
#     effective_callback = callback if callback is not None else default_callback
#
#     # URLをHTMLアンカータグに置換
#     text = re.sub(url_pattern, lambda match: match.group(1) + effective_callback(match.group(2)), text)
#     return text
