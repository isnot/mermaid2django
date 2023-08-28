from mermaid2django.entity import Entity
from mermaid2django.relationship import RelationshipItem, RelationshipSet
from mermaid2django.render.abstract import AbstractRender


class RenderDjangoModel(AbstractRender):
    FIELD_OPTIONS = {
        "int": "blank=True,",
        "char": "max_length=255, blank=True,",
        "text": "blank=True,",
        "url": "blank=True,",
        "date": "auto_now_add=True,",
        "datetime": "auto_now_add=True,",
        "rel": ' "{relation}", related_name="{relname}",',
        "one2many": "on_delete=models.CASCADE,",
        "one2one": "on_delete=models.CASCADE,",
    }
    MODULE_HEADER = "from django.db import models"
    # null=True, blank=True, default=''

    def __init__(self, entity: Entity, relationship_set: RelationshipSet):
        self.entity = entity
        self.relationship_set = relationship_set
        self.relationship_map = {}
        self.index_def = []

    def setup_relationship_map(self):
        table_name = self.entity.get_name()
        self.relationship_map[table_name] = {}
        cset = self.relationship_set.find_by_entity_name(table_name)

        for attribute_name in self.entity.get_attribute_names():
            self.relationship_map[table_name][attribute_name] = {}
            attribute = self.entity.get_attribute(attribute_name)
            pieces = attribute_name.split("_")
            pieces_len = len(pieces)

            if not attribute["isFK"]:
                continue
            if attribute["description"] is not None and attribute["description"] != "":
                # original named FK
                e_forein_table = attribute["description"].split(" ")[0]
            elif pieces_len == 2 and pieces[1] == "id":
                # simple FK
                e_forein_table = pieces[0]
            else:
                raise RuntimeError(
                    "forein table name is not found, but also attribute was FK"
                )
                continue

            # print("#scm p    ", table_name, attribute_name, e_forein_table)
            for citem in cset:
                c_table_name = citem.leaf[1]
                c_forein_table = citem.leaf[0]
                if table_name != c_table_name:
                    continue
                if e_forein_table != c_forein_table:
                    continue
                if len(citem.attribute_name) > 0 and citem.attribute_name != attribute_name:
                    continue
                self.relationship_map[table_name][attribute_name] = {
                    "type": citem.type,
                    "forein_table": c_forein_table,
                }

                print(
                    "     #$",
                    table_name,
                    e_forein_table,
                    citem.type,
                    attribute["description"],
                    citem.description,
                    citem.annotation,
                )

    def get_template(self):
        return """{mark}{name} {verbose} {description}{mark}
    {name} = models.{model_type}(
        {options}verbose_name="{verbose}",
    )"""

    def get_relation(self, table_name, attribute_name):
        return self.relationship_map[table_name][attribute_name]

    def get_attribute(self, name):
        table_name = self.entity.get_name()
        attribute = self.entity.get_attribute(name)
        type = attribute["type"]
        if type == "rel":
            relation = self.get_relation(table_name, name)

        # print(self.relationship_map["series"]["title"])
        temp = self.get_template()
        options = RenderDjangoModel.FIELD_OPTIONS[type]
        if type not in Entity.VALID_TYPES:
            line = ""
        elif type == "rel":
            line = temp.format(
                name=attribute["name"],
                verbose=attribute["verbose"],
                description=attribute["description"],
                mark='"""',
                quote='"',
                delete="CASCADE",
                relation=relation["forein_table"].capitalize(),
                relname=table_name,
            )
        else:
            line = temp.format(
                name=attribute["name"],
                verbose=attribute["verbose"],
                description=attribute["description"],
                mark='"""',
                quote='"',
            )
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
        if self.relationship_set.is_link_table(entity_name):
            return None

        # self.relationship_map = self.relationship_set.get_map()
        one2one = self.relationship_set.get_one2one_by_entity_name(entity_name)
        m2m = self.relationship_set.get_many2many_by_entity_name(entity_name)
        one2m = self.relationship_set.get_one2many_by_entity_name(entity_name)

        buf = self.get_entity_header()
        for i in self.entity.get_attribute_names():
            attribute = self.get_attribute(i)
            if attribute == "":
                continue
            buf += attribute

        # for xxx in m2m:
        # print(xxx)

        return buf
