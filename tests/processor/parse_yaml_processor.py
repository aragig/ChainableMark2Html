import re
import yaml


class ParseYamlProcessor:
    def __init__(self):
        self.extracted_yaml = None

    def process(self, markdown_text):
        # YAML部分を抽出するための正規表現
        yaml_regex = r"^---\n(.+?)\n---"
        yaml_content = re.search(yaml_regex, markdown_text, re.DOTALL)

        # 抽出されたYAMLデータ（存在する場合）
        self.extracted_yaml = yaml_content.group(1) if yaml_content else None

        markdown_only = re.sub(yaml_regex, '', markdown_text, flags=re.DOTALL).strip()

        return markdown_only

    def parse_yaml(self):
        if self.extracted_yaml:
            return yaml.safe_load(self.extracted_yaml)
        else:
            return None
