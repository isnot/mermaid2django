from mermaid2django.render.abstract import AbstractRender


class RenderDjangoAdmin(AbstractRender):
    MODULE_HEADER = "from django.contrib import admin"

    def __init__(self, all_entities=[]):
        self.all = sorted(list(map(lambda e: e.get_name().capitalize(), all_entities)))

    def get_import(self):
        lines = ["from .models import ("]
        lines.extend(list(map(lambda model: f"    {model},", self.all)))
        lines.append(")")
        return "\n".join(lines)

    def get_model_admin(self, class_name):
        class_def = "class {name}Admin(admin.ModelAdmin):".format(name=class_name)
        lines = [class_def]
        lines.append(
            """    fields = ["id"]  # ["name", "title", "type", "memo"]
    # fieldsets = []
    # list_filter = ["title"]
    # search_fields = ["title"]
    # list_display = ("id", "name", "title")
    # list_display_links = ("id", "name", "title")
"""
        )
        return "\n".join(lines)

    def get_admin(self):
        buf = self.MODULE_HEADER + "\n\n" + self.get_import() + "\n\n"
        for name in self.all:
            buf = (
                buf
                + "\n\n@admin.register({name})\n".format(name=name)
                + self.get_model_admin(name)
            )
        return buf
