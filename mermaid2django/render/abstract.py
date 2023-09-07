class AbstractRender:
    DEFAULT_OUTPUT = "define_your_file_name"

    @staticmethod
    def check_args(key="", **kwargs):
        if key not in kwargs:
            raise RuntimeError(f"{key} is requierd")
        return kwargs[key]

    @staticmethod
    def replace_file_content(filename, content):
        try:
            fd = open(filename, mode="w", encoding="utf-8")
            fd.write(content)
            fd.close()
        except FileNotFoundError:
            print("ファイルをオープンできませんでした。")
            # raise RuntimeError("Can not open file")

    @classmethod
    def output_file(cls, filename=DEFAULT_OUTPUT, **kwargs):
        raise NotImplementedError()

    def __init__(self) -> None:
        if self.DEFAULT_OUTPUT == AbstractRender.DEFAULT_OUTPUT:
            raise NotImplementedError()
