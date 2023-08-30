class AbstractRender:
    @staticmethod
    def replace_file_content(filename, content):
        try:
            fd = open(filename, mode="w", encoding="utf-8")
            fd.write(content)
            fd.close()
        except FileNotFoundError:
            print("ファイルをオープンできませんでした。")
            # raise RuntimeError("Can not open file")
