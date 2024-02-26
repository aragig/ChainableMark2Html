import os

from .utils.store_manager import StoreManager
from .utils import replace_code
from .utils import replace_emphasis
from .utils import replace_block
from .utils import replace_paragraph
from .utils import replace_url
from .utils import replace_table
from .utils import replace_image
from .utils import replace_list
from .utils import replace_headings
from .utils import replace_toc


class ChainableMark2Html:
    """
    MarkdownをHTMLに変換する
    """
    def __init__(self, markdown):
        self.__html = markdown
        self.store_manager = StoreManager()

    def my(self, processor):
        """
        独自プロセッサーで任意の処理を行う
        例えばヘッダーのyamlを取得するなど

        :param processor: 独自プロセッサー
        """
        self.__html = processor.process(self.__html)
        return self

    def to_html(self):
        """
        HTMLを返す
        """
        self.__html = self.store_manager.restore(self.__html)
        self.__html = replace_paragraph.consolidate_newlines(self.__html)  # TODO コードブロック内の改行にも影響するはず
        return self.__html.strip()

    def import_code(self, src_dir=None):
        """
        外部ファイルのソースコードコードをインポートする

        :param src_dir: importするファイルのディレクトリ
        """
        if src_dir is None:
            src_dir = os.path.dirname(os.path.abspath(__file__))
        self.__html = replace_code.replace_import_code(self.__html, src_dir)
        return self.code()

    def code(self):
        """
        コードブロックをHTMLのコードに変換する
        """
        self.__html = self.store_manager.store(self.__html,
                                               r'(```[^\n]*\n.*?```)',
                                               replace_code.code_restore_callback)
        return self

    def inline_code(self):
        self.__html = self.store_manager.store_line(self.__html,
                                                    r'(`.*?`)',
                                                    replace_code.inline_code_restore_callback)
        # self.__html = replace_code.inline_code(self.__html)
        return self

    def style(self):
        self.__html = self.store_manager.store(self.__html, r'(<style[^>]*>.*?</style>)')
        return self

    def script(self):
        self.__html = self.store_manager.store(self.__html, r'(<script[^>]*>.*?</script>)')
        return self

    def toc(self):
        self.__html = replace_toc.replace_toc(self.__html, level=3)
        return self

    def heading(self):
        # ! 最初の処理はh1タグ用
        headingManager = replace_headings.HeadingManager()
        self.__html = self.store_manager.store_line(self.__html,
                                                    r'^(#{1,6}\s+.*)',
                                                    headingManager.headings_callback,
                                                    '\n\n')
        return self

    def tilde(self):
        self.__html = replace_block.tilde(self.__html)
        return self

    def em(self):
        self.__html = replace_emphasis.em(self.__html)
        return self

    def strong(self, callback=None):
        self.__html = replace_emphasis.strong(self.__html, callback)
        return self

    def strike(self):
        self.__html = replace_emphasis.strike(self.__html)
        return self

    def blockquote(self):
        self.__html = replace_block.blockquote(self.__html)
        return self

    def br(self):
        self.__html = replace_paragraph.br(self.__html)
        return self

    def paragraph(self):
        self.__html = replace_paragraph.paragraph(self.__html)
        return self

    def horizon(self):
        self.__html = replace_paragraph.horizon(self.__html)
        return self

    def link(self):
        """Markdown形式のURLをHTMLのリンクに変換する"""
        self.__html = replace_url.convert_markdown_link(self.__html)
        return self

    def url(self, callback=None):
        """httpから始まるURLをHTMLのリンクに変換する"""
        # self.__html = self.store_manager.store_line(self.__html,
        #                                             r'^(#{1,6}\s+.*)',
        #                                             replace_url.url_callback)
        self.__html = replace_url.convert_urls_to_links(self.__html, callback)
        return self

    def table(self):
        # ! store_managerを使った方が置換がラク
        self.__html = self.store_manager.store(self.__html,
                                               r'\n(\|.*?\|\n\|[-| ]+\|(\n\|.*?\|)+)\n',
                                               replace_table.table_restore_callback)
        return self

    def img(self, callback=None):
        self.__html = replace_image.image(self.__html, callback)
        return self

    def list(self):
        self.__html = replace_list.replace_list(self.__html)
        return self

    def wrap(self, wrap_html, **kwargs):
        formatted_html = wrap_html.format(self.__html, **kwargs)
        """<html>{}</html>"""
        self.__html = formatted_html.format(self.__html)
        return self

    def output(self, output_file_path, overwrite=False):
        if overwrite or not os.path.exists(output_file_path):
            with open(output_file_path, 'w') as file:
                file.write(self.to_html())
        else:
            print(f"File {output_file_path} already exists. Set overwrite=True to overwrite.")
        return self
