from mermaid2django.parser import ParseMermaidErDiagram
from mermaid2django.render.django_model import RenderDjangoModel

print(RenderDjangoModel.MODULE_HEADER)

task = ParseMermaidErDiagram("./examples/plan.mmd")
entities = task.parse()
entitiy_renders = {}
cmap = {}
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
