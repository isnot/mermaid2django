from mermaid2django.entity import Entity
from mermaid2django.relationship import RelationshipSet  # RelationshipItem
from mermaid2django.render.abstract import AbstractRender


class RenderDjangoModel(AbstractRender):
    FIELD_OPTIONS = {
        "int": (
            'verbose_name="{verbose}",',
            "null=True,",
            "blank=True",
        ),
        "char": (
            'verbose_name="{verbose}",',
            "max_length=255,",
            "null=True,",
            "blank=True",
        ),
        "text": (
            'verbose_name="{verbose}",',
            "null=True,",
            "blank=True",
        ),
        "url": (
            'verbose_name="{verbose}",',
            "null=True,",
            "blank=True",
        ),
        "date": (
            'verbose_name="{verbose}",',
            "null=True",
        ),
        "datetime": (
            'verbose_name="{verbose}",',
            "null=True",
        ),
        "rel": (
            '"{relation}",',
            'verbose_name="{verbose}",',
            'related_name="{related_name}",',
        ),
        "one2many": (
            "null=True,",
            "on_delete=models.DO_NOTHING",
        ),
        "one2one": (
            "null=True,",
            "on_delete=models.CASCADE",
        ),
        "many2many": tuple(),
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
        myset = self.relationship_set.find_by_entity_name(table_name)

        for attribute_name in self.entity.get_attribute_names():
            self.relationship_map[table_name][attribute_name] = {}
            attribute = self.entity.get_attribute(attribute_name)

            if not attribute["isFK"]:
                continue

            # ToDo define forein_table
            if attribute["annotation"] is not None and attribute["annotation"] != "":
                e_forein_table = attribute["annotation"].split(" ")[0]
            else:
                raise RuntimeError(
                    "forein table name is not found, but also attribute was FK"
                )
                continue

            for relation_item in myset:
                c_table_name = relation_item.leaf[1]
                c_forein_table = relation_item.leaf[0]
                if table_name != c_table_name:
                    continue
                if e_forein_table != c_forein_table:
                    continue
                if (
                    len(relation_item.attribute_name) > 0
                    and relation_item.attribute_name != attribute_name
                ):
                    continue

                if self.relationship_set.is_valid_entity_name(attribute_name):
                    related_name = table_name
                else:
                    related_name = attribute_name

                self.relationship_map[table_name][attribute_name] = {
                    "type": relation_item.type,
                    "forein_table": c_forein_table,
                    "related_name": related_name,
                }

    def get_template(self, attribute_type="", relation_type=""):
        options = list(RenderDjangoModel.FIELD_OPTIONS[attribute_type])
        if attribute_type == "rel":
            options.extend(list(RenderDjangoModel.FIELD_OPTIONS[relation_type]))
        options = list(map(lambda line: "    " + line, options))

        template = [
            "\n    {mark}{name} {verbose} {annotation}{mark}",
            "{name} = models.{model_type}(",
        ]
        template.extend(options)
        template.append(")")
        return "\n    ".join(template)

    def get_relation(self, table_name, attribute_name):
        return self.relationship_map[table_name][attribute_name]

    def get_attribute(self, name):
        table_name = self.entity.get_name()
        attribute = self.entity.get_attribute(name)
        type = attribute["type"]
        if type not in Entity.VALID_TYPES or type == "serial":
            return ""
        elif type == "rel":
            relation = self.get_relation(table_name, name)
            temp = self.get_template(
                attribute_type=type, relation_type=relation["type"]
            )
            if relation["type"] == "one2one":
                model_type = "OneToOneField"
            elif relation["type"] == "many2many":
                model_type = "ManyToManyField"
            elif relation["type"] == "one2many":
                model_type = "ForeignKey"
            else:
                model_type = "Error"
            line = temp.format(
                name=attribute["name"],
                verbose=attribute["verbose"],
                annotation=attribute["annotation"],
                model_type=model_type,
                relation=relation["forein_table"].capitalize(),
                related_name=relation["related_name"],
                mark='"""',
            )
        else:
            temp = self.get_template(attribute_type=type)
            if type == "int":
                model_type = "PositiveIntegerField"
            elif type == "url":
                model_type = "URLField"
            elif type == "datetime":
                model_type = "DateTimeField"
            else:
                model_type = type.capitalize() + "Field"
            line = temp.format(
                name=attribute["name"],
                verbose=attribute["verbose"],
                annotation=attribute["annotation"],
                model_type=model_type,
                mark='"""',
            )

        return line.replace('verbose_name="",', "", 1).replace("        \n", "", 1)

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

    def get_model(self):
        entity_name = self.entity.get_name()
        if self.relationship_set.is_link_table(entity_name):
            return None
        buf = self.get_entity_header()

        for name in self.entity.get_attribute_names():
            attribute = self.get_attribute(name)
            if attribute == "":
                continue
            buf += attribute

        return buf + "\n"
