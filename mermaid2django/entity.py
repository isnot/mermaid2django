class Entity:
    """
    ER図におけるエンティティ（※テーブル）1つを表す

    props_keys<tuple>: クラス定数。各プロパティが持つ属性
        name<str>: カラム名（英数字）
        verbose<str>: カラム名の、分かりやすい表示名
        description<str>: カラムのメモ（アノテーション）
        type<str>: カラムの型

        usage: 使用例
        book = Entity("book", "蔵書目録")
        book.set_props(
            name="title",
            verbose="タイトル",
            description="本のタイトルは、honto等の書誌情報で確認してから正式な名前をつける",
            type="text",
            isPK=False,
            isFK=False,
        )
        ※カラムの数だけset_props()繰り返す
    """

    props_keys = (
        "name",
        "type",
        "isPK",
        "isFK",
        "verbose",
        "description",
    )

    def __init__(self, *args):
        """
        __init__ インスタンス生成

        インスタンス変数:
        name<str>: テーブル名（英数字、命名規則による）
        description<str>: テーブルの説明（アノテーション）
        props<dict>: 全カラムの定義を格納する
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
        get_prop_names カラム名のリストを得る

        Returns
        -------
        <list<str>>
            カラム名のリスト
        """
        return sorted(self.props.keys())

    def get_prop(self, name):
        """
        get_prop カラムの定義をひとつ得る

        Parameters
        ----------
        name : <str>
            カラム名

        Returns
        -------
        <dict>
            カラムの定義

        Raises
        ------
        TypeError
            未知のプロパティ名
        """
        if name in self.props:
            return self.props[name]
        raise TypeError("unknown prop name")

    def set_props(self, **kwargs):
        """
        set_props カラムの定義を追加する

        引数: props_keysの各要素をキーにした、名前付き引数

        Raises
        ------
        RuntimeError
            必須の引数 name がない
        """
        prop = {}
        for key in Entity.props_keys:
            if key in kwargs:
                prop[key] = kwargs[key]

        if "name" not in prop:
            raise RuntimeError("name of property is required")

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
                "\t".join(
                    (
                        i["name"],
                        i["type"],
                        pkfk,
                        i["verbose"],
                    )
                )
            )
        return "Table {} :=> {}".format(self.name, "\n".join(p).strip())
