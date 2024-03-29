class Entity:
    """
    ER図におけるエンティティ（※テーブル）1つを表す

    ATTR_KEYS<tuple>: クラス定数。各属性が持つ属性
        type<str>: アトリビュート（※カラム）の型
        name<str>: アトリビュート名称（英数字）
        verbose<str>: アトリビュートの、分かりやすい表示名
        annotation<str>: アトリビュートのメモ（アノテーション）

        usage: 使用例
        book = Entity("book", "蔵書目録")
        book.set_attributes(
            type="char",
            name="title",
            verbose="タイトル",
            annotation="本のタイトルは、honto等の書誌情報で確認してから正式な名前をつける",
            isPK=False,
            isFK=False,
        )
        ※アトリビュートの数だけ set_attributes() 繰り返す

    コメントをアノテーションとして扱う
        エンティティ定義ブロック直前のコメントは、そのエンティティに関連付ける
        エンティティ定義ブロック内のコメントは、次の行のアトリビュートに関連付ける

    以下では、Django Modelを前提にした設計について説明しています
    VALID_TYPES: アトリビュートの型は、一部のModelフィールド型にのみ対応
    PKについて、「id」「シーケンス」が常に使われるものとしています
    ひとつのアトリビュートにPKとFKが同時に設定されるケースは対応しない
    アトリビュートが外部キーである場合の型は「rel」とする（独自定義）
    未対応事項
        デフォルト値、NULL制約、ユニーク制約、インデックス
    """

    ATTR_KEYS = (
        "type",
        "name",
        "isPK",
        "isFK",
        "verbose",
        "annotation",
    )
    VALID_TYPES = (
        "serial",
        "int",
        "decimal",
        "bool",
        "char",
        "text",
        "url",
        "email",
        "isbn",
        "date",
        "datetime",
        "rel",
    )

    def __init__(self, name, description=""):
        """
        __init__ インスタンス生成

        インスタンス変数:
        name<str>: エンティティ名（英数字、命名規則による）
        description<str>: エンティティの説明（アノテーション）
        attrs<dict>: 全アトリビュートの定義を格納する
        index_def<dict>: インデックス（未実装）

        Raises
        ------
        RuntimeError
            必須の引数 name がない
        """
        self.attrs = {}
        self.index_def = {}

        if name is None or name == "":
            raise RuntimeError("Entity name is required")
        # a.k.a. table name
        self.name = name
        # a.k.a. table description
        self.description = description

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_attribute_names(self):
        """
        get_attribute_names アトリビュートのリストを得る

        Returns
        -------
        <list<str>>
            アトリビュートのリスト
        """
        return sorted(self.attrs.keys())

    def get_attribute(self, name):
        """
        get_attribute アトリビュートの定義をひとつ得る

        Parameters
        ----------
        name : <str>
            アトリビュート名称

        Returns
        -------
        <dict>
            アトリビュートの定義

        Raises
        ------
        TypeError
            未知の属性名
        """
        if name in self.attrs:
            return self.attrs[name]
        raise TypeError("unknown attribute name")

    def set_attributes(self, **kwargs):
        """
        set_attributes アトリビュートの定義を追加する

        引数: ATTR_KEYSの各要素をキーにした、名前付き引数

        Raises
        ------
        RuntimeError
            必須の引数 type, name がない
        """
        attribute = {}
        for key in Entity.ATTR_KEYS:
            if key in kwargs:
                attribute[key] = kwargs[key]

        if "type" not in attribute or "name" not in attribute:
            raise RuntimeError("missing attribute of required")

        if attribute["type"] not in self.VALID_TYPES:
            raise TypeError("invalid type at entity.attribute")

        if attribute["name"] not in self.attrs:
            self.attrs[attribute["name"]] = attribute

    def __str__(self) -> str:
        p = []
        for name, i in self.attrs.items():
            if i["isPK"] and i["isFK"]:
                pkfk = "PK,FK"
            elif i["isPK"]:
                pkfk = "PK"
            elif i["isFK"]:
                pkfk = "FK"
            else:
                pkfk = ""
            p.append(
                " ".join(
                    (
                        i["name"],
                        i["type"],
                        pkfk,
                        i["verbose"],
                    )
                )
            )
        return "{} :=> {}".format(self.name, "\n".join(p).strip())
