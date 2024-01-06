import re


def image(text, callback):
    # ![altテキスト](画像URL)にマッチするパターン
    image_tag_pattern = r'!\[(.*?)\]\((.*?)\)'

    def default_callback(img_src, img_alt):
        return f'<img src="{img_src}" alt="{img_alt}" title="{img_alt}">'

    # 提供されたコールバックを使用するか、デフォルトのコールバックを使用
    effective_callback = callback if callback is not None else default_callback

    # Split the text into lines and process each line
    lines = text.split('\n')
    processed_lines = []

    for line in lines:
        image_tags = re.findall(image_tag_pattern, line)

        # Check if the line contains multiple images
        if len(image_tags) > 1:
            # Replace image markdown with HTML using the callback
            line_html = "".join([effective_callback(img_src, img_alt) for img_alt, img_src in image_tags])
            # Wrap the line with Flexbox div
            processed_line = f"<div class='flex-box-images'>{line_html}</div>"
        else:
            # For lines with a single image or no images, just replace markdown with HTML
            processed_line = re.sub(image_tag_pattern, lambda match: effective_callback(match.group(2), match.group(1)),
                                    line)

        processed_lines.append(processed_line)

    # Join the processed lines back into a single text
    return '\n'.join(processed_lines)

