from mermaid2django.parser import ParseMermaidErDiagram
from mermaid2django.render.django_model import RenderDjangoModel

task = ParseMermaidErDiagram("./examples/plan.mmd")
entities = task.parse()
cmap = {}
entitiy_renders = {}
print(RenderDjangoModel.MODULE_HEADER)

for entity in entities:
    name = entity.get_name()
    render = RenderDjangoModel(entity, task.get_relationship_set())
    entitiy_renders[name] = render
    cmap[name] = render.setup_relationship_map()

for entity in entities:
    name = entity.get_name()
    render = entitiy_renders[name]
    tmp = render.get_model(cmap)
    if tmp is None or tmp == "":
        continue
    print(tmp)
