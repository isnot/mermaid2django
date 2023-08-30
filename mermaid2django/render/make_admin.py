from mermaid2django.render.django_admin import RenderDjangoAdmin


def admin_maker(entities, filename):
    render = RenderDjangoAdmin(entities)
    RenderDjangoAdmin.replace_file_content(filename, render.get_admin())
