import re


class StoreManager:
    def __init__(self):
        self.__stored_datas = []
        self.__temp_codes_index = 0

    def __store_datas(self, key, content, callback):
        self.__stored_datas.append((key, content, callback))
        self.__temp_codes_index += 1

        # print(key)

    def store(self, text, pattern, callback=None):
        # 引数を展開
        matches = re.findall(pattern, text, re.DOTALL)
        # matches = re.findall(pattern, text, re.S)

        for match in matches:
            if isinstance(match, tuple):
                # matchがタプルだった場合
                match_text = match[0]
                # print("matchがタプル")
            else:
                match_text = match
                # print("matchがタプルでない")
            #print(repr(match_text))
            replace_pattern = f'$$$STOREDKEY{self.__temp_codes_index}$$$'
            # text = text.replace(match_text, replace_pattern)
            text = re.sub(pattern, f'\n\n{replace_pattern}\n\n', text, flags=re.DOTALL, count=1)

            # print(replace_pattern)
            self.__store_datas(replace_pattern, match_text, callback)
        # print(repr(text))
        return text

    def store_line(self, text, pattern, callback=None, spacer=''):
        # テキストを行ごとに分割
        lines = text.split('\n')
        new_lines = []  # 変更後のテキストを保持

        for line in lines:
            matches = re.findall(pattern, line, re.DOTALL)
            for match in matches:

                replace_pattern = f'$$$STOREDKEY{self.__temp_codes_index}$$$'
                line = line.replace(match, f'{spacer}{replace_pattern}{spacer}', 1)
                # print(line)
                self.__store_datas(replace_pattern, match, callback)
            # 変更後の行を新しいリストに追加
            new_lines.append(line)

        # 変更後のテキストを結合して返す
        return '\n'.join(new_lines)

    def restore(self, text):
        # print(text)
        for key, content, callback in self.__stored_datas:
            # print(key)
            # print(content)

            if callback is None:
                text = text.replace(key, content, 1)
                # text = re.sub(key, content, text, flags=re.DOTALL, count=1)
            else:
                replacement = callback(content)
                text = text.replace(key, replacement, 1)
                # text = re.sub(key, text, replacement, flags=re.DOTALL, count=1)
        return text

    # def consolidate_newlines(self, text):
    #     return re.sub(r'\n{2,}', '\n\n', text)
