from mermaid2django.entity import Entity
from mermaid2django.render.abstract import AbstractRender


class RenderDjangoAdmin(AbstractRender):
    DEFAULT_OUTPUT = "./admin.py"
    MODULE_HEADER = "from django.contrib import admin"

    @classmethod
    def output_file(cls, filename=DEFAULT_OUTPUT, **kwargs):
        entities = RenderDjangoAdmin.check_args("entities", **kwargs)
        render = RenderDjangoAdmin(entities)
        RenderDjangoAdmin.replace_file_content(filename, render.get_admin())

    def __init__(self, entities=[]):
        self.entities = entities

    def get_import(self):
        all = sorted(list(map(lambda e: e.get_name().capitalize(), self.entities)))
        lines = ["from .models import ("]
        lines.extend(list(map(lambda model: f"    {model},", all)))
        lines.append(")")
        return "\n".join(lines)

    def get_template(self):
        return """    fields = [{fields}]
    # list_filter = ["type_master", ""]
    # search_fields = ["title", "name", "memo"]
    list_display = ("id", {fields})
    list_display_links = ({fields})
"""

    def get_model_admin(self, class_name, entity: Entity):
        attr_names = entity.get_attribute_names()
        fields = ", ".join(
            filter(
                lambda item: item is not None,
                list(
                    map(
                        lambda name: '"{0}"'.format(name) if name != "id" else None,
                        attr_names,
                    )
                ),
            )
        )
        class_def = "class {name}Admin(admin.ModelAdmin):".format(
            name=class_name.capitalize()
        )
        lines = [class_def]
        lines.append(self.get_template().format(fields=fields))
        return "\n".join(lines)

    def get_admin(self):
        buf = self.MODULE_HEADER + "\n\n" + self.get_import() + "\n"
        for entity in self.entities:
            name = entity.get_name()
            buf = (
                buf
                + "\n\n@admin.register({name})\n".format(name=name.capitalize())
                + self.get_model_admin(name, entity)
            )
        return buf
