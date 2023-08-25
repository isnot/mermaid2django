from mermaid2django.cardinality import CardinalityItem, CardinalitySet
from mermaid2django.entity import Entity

from .abstract import AbstractRender


class RenderDjangoModel(AbstractRender):
    TYPE2FIELD = {
        "serial": "",
        "int": """
    {mark}{name} {verbose} {description}{mark}
    {name} = models.PositiveIntegerField(
        verbose_name="{verbose}",
        blank=True
    )""",
        "text": """
    {mark}{name} {verbose} {description}{mark}
    {name} = models.CharField(
        verbose_name="{verbose}",
        max_length=255,
        blank=True
    )""",
        "date": """
    {mark}{name} {verbose} {description}{mark}
    {name} = models.DateField(
        verbose_name="{verbose}",
        auto_now_add=True
    )""",
        "datetime": """
    {mark}{name} {verbose} {description}{mark}
    {name} = models.DateTimeField(
        verbose_name="{verbose}",
        auto_now_add=True
    )""",
        "one2many": """
    {mark}{name} {verbose} {description}{mark}
    {name} = models.ForeignKey(
        "{relation}",
        verbose_name="{verbose}",
        related_name="{rel}",
        on_delete=models.{delete},
    )""",
        "one2one": """
    {mark}{name} {verbose} {description}{mark}
    {name} = models.OneToOneField(
        "{relation}",
        verbose_name="{verbose}",
        related_name="{rel}",
        on_delete=models.{delete},
    )""",
        "many2many": """
    {mark}{name} {verbose} {description}{mark}
    {name} = models.ManyToManyField(
        "{relation}",
        verbose_name="{verbose}",
        related_name="{rel}",
        on_delete=models.{delete},
    )""",
    }
    MODULE_HEADER = "from django.db import models"

    def __init__(self, entity: Entity, cardinality_set: CardinalitySet):
        self.entity = entity
        self.cardinality_set = cardinality_set
        self.cardinality_map = {}
        self.index_def = []

    def setup_cardinality_map(self):
        table_name = self.entity.get_name()
        data = {}
        cset = self.cardinality_set.find_by_entity_name(table_name)

        # print("scm t", table_name)
        for prop_name in self.entity.get_prop_names():
            prop = self.entity.get_prop(prop_name)
            pieces = prop_name.split("_")
            pieces_len = len(pieces)

            if not prop["isFK"]:
                continue
            # print("scm p    ", prop_name, prop["isFK"])
            if prop["description"] is not None and prop["description"] != "":
                # original named FK
                e_forein_table = prop["description"].split(" ")[0]
            elif pieces_len == 2 and pieces[1] == "id":
                # simple FK
                e_forein_table = pieces[0]
            else:
                raise RuntimeError(
                    "forein table name is not found, but also property was FK"
                )
                continue

            # print("scm p    ", table_name, e_forein_table)
            data[prop_name] = {}

            for citem in cset:
                c_table_name = citem.leaf[1]
                c_forein_table = citem.leaf[0]
                if table_name != c_table_name:
                    # print("##### T", citem.leaf, citem.type)
                    continue
                if e_forein_table != c_forein_table:
                    # print("##### F", citem.leaf, citem.type)
                    continue
                # if table_name == c_table_name and e_forein_table == c_forein_table:
                # print(citem)
                # print("     ", table_name, c_table_name, c_forein_table, e_forein_table, citem.type)

    def get_property(self, name):
        property = self.entity.get_prop(name)
        type = property["type"]
        temp = RenderDjangoModel.TYPE2FIELD[type]
        if type in (
            "int",
            "text",
            "date",
            "datetime",
        ):
            line = temp.format(
                name=property["name"],
                verbose=property["verbose"],
                description=property["description"],
                mark='"""',
                quote='"',
            )
        elif type in (
            "one2many",
            "one2one",
            "many2many",
        ):
            line = temp.format(
                name=property["name"],
                verbose=property["verbose"],
                description=property["description"],
                mark='"""',
                quote='"',
                delete="CASCADE",
                relation="",
                rel="",
            )
        else:
            line = ""
        return line

    def get_entity_header(self):
        name = self.entity.get_name()
        desc = self.entity.get_description()
        if desc is None or desc == "":
            desc = name
        return """

class {name}(models.Model):
    {mark} {description}
    {mark}
""".format(
            name=name.capitalize(),
            description=desc,
            mark='"""',
        )

    def get_entity_footer(self):
        return """
    def __str__(self):
        return self.id
"""

    def get_model(self, cmap={}):
        entity_name = self.entity.get_name()
        if self.cardinality_set.is_link_table(entity_name):
            return None

        # self.cardinality_map = self.cardinality_set.get_map()
        one2one = self.cardinality_set.get_one2one_by_entity_name(entity_name)
        m2m = self.cardinality_set.get_many2many_by_entity_name(entity_name)
        one2m = self.cardinality_set.get_one2many_by_entity_name(entity_name)

        buf = self.get_entity_header()
        for i in self.entity.get_prop_names():
            prop = self.get_property(i)
            if prop == "":
                continue
            buf += prop

        # for xxx in m2m:
        # print(xxx)

        return buf
