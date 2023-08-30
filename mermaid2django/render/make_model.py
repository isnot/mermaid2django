from mermaid2django.render.django_model import RenderDjangoModel


def model_maker(task, entities, filename):
    entitiy_renders = {}
    buf = RenderDjangoModel.MODULE_HEADER + "\n"

    for entity in entities:
        name = entity.get_name()
        render = RenderDjangoModel(entity, task.get_relationship_set())
        entitiy_renders[name] = render
        render.setup_relationship_map()

    for entity in entities:
        name = entity.get_name()
        render = entitiy_renders[name]
        tmp = render.get_model()
        if tmp is None or tmp == "":
            continue
        buf += tmp

    RenderDjangoModel.replace_file_content(filename, buf)
