from mermaid2django.entity import Entity
from mermaid2django.render.abstract import AbstractRender


class RenderCsv(AbstractRender):
    DEFAULT_OUTPUT = "db.tsv"
    SEPARATOR_COL = "\t"
    SEPARATOR_ROW = "\n"
    HEADER = (
        [
            "システム名",
            "作者",
            "RDB SYSTEM",
        ],
        [
            "vsdb",
            "naoto",
            "sqlite3",
        ],
    )
    ENTITY_LIST_HEAD = [
        "No",
        "物理名",
        "論理名",
        "用途",
        "作成日",
        "更新日",
    ]
    ENTITY_HEAD = [
        "No",
        "主キー",
        "外部キー",
        "カラム名",
        "項目名",
        "データ型",
        "NOT NULL",
        "一意制",
        "default",
        "更新",
        "備考",
    ]

    @staticmethod
    def bool2str(bool):
        return "✔" if bool else ""

    @classmethod
    def output_file(cls, entities, filename=""):
        if filename is None or filename == "":
            filename = RenderCsv.DEFAULT_OUTPUT
        render = RenderCsv(entities)
        RenderCsv.replace_file_content(filename, render.get_csv())

    def __init__(self, entities={}):
        self.entities = entities
        self.entity_names = sorted(list(entities.keys()))
        self._num_of_cols = len(list(self.ENTITY_HEAD))

    def extend_list(self, input, *args):
        if len(args) < 1:
            num_of_cols = self._num_of_cols
        else:
            num_of_cols = int(args[0])
        output = list(input)
        num = len(output)
        if num > num_of_cols:
            raise RuntimeError("out of range for list extends")
        elif num < num_of_cols:
            output.extend([""] * (num_of_cols - num))
        return output

    def get_empty_line(self):
        return self.SEPARATOR_COL.join(self.extend_list([])) + self.SEPARATOR_ROW

    def get_entity_header(self):
        header = self.SEPARATOR_COL.join(self.extend_list(self.ENTITY_HEAD))
        return header

    def get_header(self):
        header = self.SEPARATOR_COL.join(self.extend_list(self.HEADER[0]))
        content = self.SEPARATOR_COL.join(self.extend_list(self.HEADER[1]))
        list_head = self.SEPARATOR_COL.join(self.extend_list(self.ENTITY_LIST_HEAD))

        lines = []
        lines_index = 0
        for entity_name in self.entity_names:
            lines_index += 1
            entity: Entity = self.entities[entity_name]
            entity_desc = entity.get_description()
            desc = entity_desc.split(sep=" ", maxsplit=1)[1]
            cols = [
                str(lines_index),  # "No",
                entity_name,  # "物理名",
                entity_name.capitalize(),  # "論理名",
                desc,  # "用途",
                "",  # "作成日",
                "",  # "更新日",
            ]
            lines.append(self.SEPARATOR_COL.join(cols))

        return self.SEPARATOR_ROW.join(
            [
                header,
                content,
                self.get_empty_line(),
                list_head,
                self.SEPARATOR_ROW.join(lines),
                self.get_empty_line(),
            ]
        )

    def get_entity_csv(self, entity_name):
        entity: Entity = self.entities[entity_name]
        lines = [
            self.get_empty_line(),
            self.SEPARATOR_COL.join(self.extend_list([entity_name])),
            self.get_entity_header(),
        ]
        index_num = 0
        for name in entity.get_attribute_names():
            prop = entity.get_attribute(name)
            index_num += 1
            cols = [
                str(index_num),  # "No",
                self.bool2str(prop["isPK"]),  # "主キー",
                self.bool2str(prop["isFK"]),  # "外部キー",
                name,  # "カラム名",
                prop["verbose"],  # "項目名",
                prop["type"],  # "データ型",
                "",  # "NOT NULL",
                "",  # "一意制",
                "",  # "default",
                "",  # "更新",
                prop["annotation"],  # "備考",
            ]
            lines.append(self.SEPARATOR_COL.join(self.extend_list(cols)))
        return self.SEPARATOR_ROW.join(lines) + self.SEPARATOR_ROW

    def get_csv(self):
        buf = self.get_header()
        buf += self.get_empty_line()
        for entity_name in self.entity_names:
            buf += self.get_entity_csv(entity_name)
        return buf
