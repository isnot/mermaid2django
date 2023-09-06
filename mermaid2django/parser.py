from mermaid2django.entity import Entity
from mermaid2django.relationship import RelationshipItem, RelationshipSet


class ParseMermaidErDiagram:
    """
    Mermaid記法で記述したER図を、字句解析および構文解析します

    Mermaid.jsのサブセットです。独自の拡張と制限、未対応があります

    Params
    -------
    <str>
        ER図を記述したファイルのパス・ファイル名

    Raises
    ------
    TypeError
        内部エラーです。LEX_TOKEN定義にエラーがある可能性
    RuntimeError
        未対応の形式です。入力を解析できませんでした。
    """

    LEX_TOKENS = (
        {
            "type": "blank_line",
            "command": "equals",
            "mark": "",
        },
        {
            "type": "comment",
            "command": "starts",
            "mark": "%%",
        },
        {
            "type": "entity_start",
            "command": "ends",
            "mark": "{",
        },
        {
            "type": "entity_end",
            "command": "ends",
            "mark": "}",
        },
        {
            "type": "entity_item",
            "command": "in_entity_block",
            "split": {"sep": " ", "max": 2},
        },
        {
            "type": "relationship",
            "command": "contains",
            "mark": "--",
            "split": {"sep": " ", "max": 4},
        },
        {
            "type": "unknown",
            "command": "noop",
        },
    )

    def __init__(self, *args, **kwargs):
        """
        __init__ _summary_

        インスタンス変数:
            entities: <dict>
            relations: <list<>>
            relationship_set: <RelationshipSet>
            input_filename: <str>
        """
        self.entities = {}
        self.relations = []
        self.relationship_set = None  # RelationshipSet
        self.input_filename = "mermaid.mmd"
        if "input_filename" in kwargs:
            self.input_filename = kwargs["input_filename"]
        if len(args):
            self.input_filename = args[0]
        self.__last_comment = ""
        self.__now_entity_name = ""

    def read_input(self):
        """
        read_input ファイルの内容を読み込む

        全体をいっぺんに読み込みます。
        STREAMINGではありません。、

        Returns
        -------
        <list<str>>
            ファイルの中身（行指向）
        """
        try:
            fd = open(self.input_filename, "r", encoding="utf-8")
            lines = fd.readlines()
            fd.close()
        except FileNotFoundError:
            print("ファイルをオープンできませんでした。")
            # raise RuntimeError("Can not open file")

        if len(lines):
            return lines

    def get_entities(self, via="list"):
        if via == "dict":
            return self.entities
        if via == "only_names":
            return self.entities.keys()
        return self.entities.values()

    def get_relationship_set(self):
        return self.relationship_set

    def get_current_entity(self):
        if self.__now_entity_name != "":
            return self.entities[self.__now_entity_name]

    def split_tokenizer(self, source="", options={}):
        """
        split_tokenizer 1行をトークンに分割します

        parse()の中から呼ばれます。このメソッド単体で使うことはありません

        Parameters
        ----------
        source : str, optional
            1行分の文字列, by default ""
        options : dict, optional
            定義の要素, by default {}

        Returns
        -------
        <list<str>>
            文字列を分割したもの

        Raises
        ------
        TypeError
            定義の違反
        """
        if "split" not in options:
            return [source]
        if "sep" not in options["split"]:
            raise TypeError("illegal options in split")
        if "max" in options["split"]:
            num = options["split"]["max"]
            choped = source.split(sep=options["split"]["sep"], maxsplit=num)
            while len(choped) <= num:
                choped.extend([""])
            return choped
        else:
            return source.split(options["split"]["sep"])

    def lexicalize_single(self, line=""):
        """
        lexicalize_single 1行の字句解析

        クラス変数LEX_TOKENSで定義した内容
        parse()の中から呼ばれます。このメソッド単体で使うことはありません

        Parameters
        ----------
        line : str, optional
            1行分の入力文字列, by default ""

        Returns
        -------
        tuple<<str>, <list<str>>>
            字句解析の結果
        """
        line = line.strip().rstrip("\n")
        for item in ParseMermaidErDiagram.LEX_TOKENS:
            parser_command = f"on_{item['type']}"
            lexicalized = self.split_tokenizer(line, item)
            if item["command"] == "starts" and line.startswith(item["mark"]):
                break
            elif item["command"] == "ends" and line.endswith(item["mark"]):
                break
            elif item["command"] == "contains" and line.find(item["mark"]) != -1:
                break
            elif item["command"] == "equals" and line == item["mark"]:
                break
            elif item["command"] == "in_entity_block" and self.__now_entity_name != "":
                break
        return (
            parser_command,
            lexicalized,
        )

    def parse(self):
        """
        parse 実際にファイルから内容を読み込んで解析します

        解析結果をインスタンスに保持します

        Returns
        -------
        <list<Entity>>
            エンティティのリスト
        """
        self.on_start()
        for line in self.read_input():
            parser_command, lexicalized = self.lexicalize_single(line)
            self.on_pre_command()
            getattr(self, parser_command)(lexicalized)
            self.on_post_command()
        self.on_finish()
        return self.get_entities()

    def on_start(self):
        """
        on_start 解析処理全体の始まり

        ファイルの先頭
        """
        pass

    def on_pre_command(self):
        """
        on_pre_command 行毎の処理（開始前）

        1行の先頭
        """
        pass

    def on_post_command(self):
        """
        on_post_command 行毎の処理（完了後）

        一行の末尾
        """
        pass

    def on_finish(self):
        """
        on_finish 解析処理全体の終わり

        ファイルの末尾
        """
        self.relationship_set = RelationshipSet(self.relations)

    def on_comment(self, line=[]):
        """
        on_comment コメント行

        %% で始まる行

        Parameters
        ----------
        line : list, optional
            字句解析済みデータ, by default []
        """
        self.__last_comment += line[0].lstrip("%").strip()

    def on_entity_start(self, line=[]):
        """
        on_entity_start エンティティ定義ブロックの開始

        ブロックは「{}」で囲まれた部分

        Parameters
        ----------
        line : list, optional
            字句解析済みデータ, by default []
        """
        name = line[0].rstrip(" {")
        self.__now_entity_name = name
        if name not in self.entities.keys():
            self.entities[name] = Entity(
                name,
                description=self.__last_comment,
            )
        self.__last_comment = ""

    def on_entity_end(self, _):
        """
        on_entity_end エンティティ定義ブロックの終わり

        Parameters
        ----------
        _ : Any
            単に無視します
        """
        self.__now_entity_name = ""

    def on_entity_item(self, line=[]):
        """
        on_entity_item 属性（アトリビュート）の1行分の処理

        Parameters
        ----------
        line : list, optional
            字句解析済みデータ, by default []
        """
        m = self.get_current_entity()
        verbose = line[2].strip()
        if verbose.find("PK") != -1:
            isPK = True
            verbose = verbose.removeprefix("PK")
        else:
            isPK = False
        if verbose.find("FK") != -1:
            isFK = True
            verbose = verbose.removeprefix("FK")
        else:
            isFK = False
        if verbose is None:
            verbose = ""
        else:
            verbose = verbose.replace('"', "").strip()
        m.set_attributes(
            type=line[0],
            name=line[1],
            isPK=isPK,
            isFK=isFK,
            verbose=verbose,
            annotation=self.__last_comment.strip(),
        )
        self.__last_comment = ""

    def on_relationship(self, items=[]):
        """
        on_relationship リレーションシップ、1行分の処理

        エンティティ・ブロックの内部に記述することはできない

        Parameters
        ----------
        items : list, optional
            字句解析済みデータ, by default []
        """
        cad = RelationshipItem(items, annotation=self.__last_comment)
        cad.parse()
        self.relations.append(cad)
        self.__last_comment = ""

    def on_blank_line(self, _):
        """
        on_blank_line 空行の処理

        Parameters
        ----------
        _ : Any
            単に無視します
        """
        self.__last_comment = ""

    def on_unknown(self, _):
        """
        on_unknown 未知の形式

        Parameters
        ----------
        _ : Any
            単に無視します

        Raises
        ------
        RuntimeError
            字句解析の時点で未対応の形式だった場合
        """
        if _[0] != "erDiagram":
            raise RuntimeError("unknown token", _)
