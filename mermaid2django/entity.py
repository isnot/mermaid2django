class Entity:
    """
    ER図におけるエンティティ（※テーブル）1つを表す

    PROP_KEYS<tuple>: クラス定数。各プロパティが持つ属性
        type<str>: アトリビュート（※カラム）の型
        name<str>: アトリビュート名称（英数字）
        verbose<str>: アトリビュートの、分かりやすい表示名
        description<str>: アトリビュートのメモ（アノテーション）

        usage: 使用例
        book = Entity("book", "蔵書目録")
        book.set_props(
            type="char",
            name="title",
            verbose="タイトル",
            description="本のタイトルは、honto等の書誌情報で確認してから正式な名前をつける",
            isPK=False,
            isFK=False,
        )
        ※アトリビュートの数だけset_props()繰り返す
    """

    PROP_KEYS = (
        "type",
        "name",
        "isPK",
        "isFK",
        "verbose",
        "description",
    )
    VALID_TYPES = (
        "serial",
        "int",
        "char",
        "text",
        "url",
        "date",
        "datetime",
        "rel",
    )

    def __init__(self, *args):
        """
        __init__ インスタンス生成

        インスタンス変数:
        name<str>: エンティティ名（英数字、命名規則による）
        description<str>: エンティティの説明（アノテーション）
        props<dict>: 全アトリビュートの定義を格納する
        index_def<dict>: インデックス（未実装）

        Raises
        ------
        RuntimeError
            必須の引数 name がない
        """
        self.props = {}
        self.index_def = {}

        opt_size = len(args)
        if opt_size > 1:
            # a.k.a. table description
            self.description = args[1]
        if opt_size > 0:
            # a.k.a. table name
            self.name = args[0]
        else:
            raise RuntimeError("Entity name is required")

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_prop_names(self):
        """
        get_prop_names アトリビュートのリストを得る

        Returns
        -------
        <list<str>>
            アトリビュートのリスト
        """
        return sorted(self.props.keys())

    def get_prop(self, name):
        """
        get_prop アトリビュートの定義をひとつ得る

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
            未知のプロパティ名
        """
        if name in self.props:
            return self.props[name]
        raise TypeError("unknown prop name")

    def set_attributes(self, **kwargs):
        """
        set_props アトリビュートの定義を追加する

        引数: PROP_KEYSの各要素をキーにした、名前付き引数

        Raises
        ------
        RuntimeError
            必須の引数 type, name がない
        """
        prop = {}
        for key in Entity.PROP_KEYS:
            if key in kwargs:
                prop[key] = kwargs[key]

        if "type" not in prop or "name" not in prop:
            raise RuntimeError("missing property of required")

        if prop["type"] not in self.VALID_TYPES:
            raise TypeError("invalid type at entity.attribute")

        if prop["name"] not in self.props:
            self.props[prop["name"]] = prop

    def __str__(self) -> str:
        p = []
        for name, i in self.props.items():
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
