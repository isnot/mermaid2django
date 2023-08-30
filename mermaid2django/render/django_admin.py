from mermaid2django.render.abstract import AbstractRender


class RenderDjangoAdmin(AbstractRender):
    MODULE_HEADER = "from django.contrib import admin"

    def __init__(self, all_entity=[]):
        self.all = all_entity

    def get_import(self):
        lines = ["from .models import ("]
        lines.extend(list(map(lambda model: f"    {model},", self.all)))
        lines.append(")")
        return "\n".join(lines)

    def get_admin(self):
        buf = self.MODULE_HEADER + self.get_import(self)
        for name in self.all:
            buf += f"admin.site.register({name})\n"
        return buf
