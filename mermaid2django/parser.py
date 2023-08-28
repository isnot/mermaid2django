from mermaid2django.entity import Entity
from mermaid2django.relationship import RelationshipItem, RelationshipSet


class ParseMermaidErDiagram:
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
        self.entities = {}
        self.cardinalities = []
        self.relationship_set = None  # RelationshipSet
        self.input_filename = "mermaid.mmd"
        if "input_filename" in kwargs:
            self.input_filename = kwargs["input_filename"]
        if len(args):
            self.input_filename = args[0]
        self.__last_comment = ""
        self.__now_entity_name = ""

    def read_input(self):
        try:
            fd = open(self.input_filename, "r", encoding="utf-8")
            lines = fd.readlines()
            fd.close()
        except FileNotFoundError:
            print("ファイルをオープンできませんでした。")
            # raise RuntimeError("Can not open file")

        if len(lines):
            return lines

    def get_entities(self):
        return self.entities.values()

    def get_relationship_set(self):
        return self.relationship_set

    def get_current_entity(self):
        if self.__now_entity_name != "":
            return self.entities[self.__now_entity_name]

    def split_tokenizer(self, source="", options={}):
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
        self.on_start()
        for line in self.read_input():
            parser_command, lexicalized = self.lexicalize_single(line)
            self.on_pre_command()
            getattr(self, parser_command)(lexicalized)
            self.on_post_command()
        self.on_finish()
        return self.get_entities()

    def on_start(self):
        pass

    def on_pre_command(self):
        pass

    def on_post_command(self):
        pass

    def on_finish(self):
        self.relationship_set = RelationshipSet(self.cardinalities)

    def on_comment(self, line=[]):
        self.__last_comment += line[0].lstrip("%")

    def on_entity_start(self, line=[]):
        name = line[0].rstrip(" {")
        self.__now_entity_name = name
        if name not in self.entities.keys():
            self.entities[name] = Entity(
                name,
                self.__last_comment,
            )
        self.__last_comment = ""

    def on_entity_end(self, _):
        self.__now_entity_name = ""

    def on_entity_item(self, line=[]):
        m = self.get_current_entity()
        verbose = line[2].strip('"')
        if verbose.find("PK") != -1:
            isPK = True
            verbose = verbose.removeprefix("PK").strip()
        else:
            isPK = False
        if verbose.find("FK") != -1:
            isFK = True
            verbose = verbose.removeprefix("FK").strip()
        else:
            isFK = False
        if verbose is None:
            verbose = ""
        m.set_props(
            name=line[0],
            type=line[1],
            isPK=isPK,
            isFK=isFK,
            verbose=verbose,
            description=self.__last_comment.strip(),
        )
        self.__last_comment = ""

    def on_relationship(self, items=[]):
        cad = RelationshipItem(items)
        cad.parse()
        self.cardinalities.append(cad)

    def on_blank_line(self, _):
        self.__last_comment = ""

    def on_unknown(self, _):
        if _[0] != "erDiagram":
            raise RuntimeError("unknown token", _)
