from mermaid2django.parser import ParseMermaidErDiagram
from mermaid2django.render.csv import RenderCsv
from mermaid2django.render.django_admin import RenderDjangoAdmin
from mermaid2django.render.django_model import RenderDjangoModel

input_mermaid = "./examples/plan.mmd"
output_model = "./dist/models.py"
output_admin = "./dist/admin.py"
output_csv = "./dist/database.tsv"

task = ParseMermaidErDiagram(input_mermaid)
entities = task.parse()
RenderDjangoAdmin.output_file(filename=output_admin, entities=entities)
RenderDjangoModel.output_file(filename=output_model, entities=entities, parser=task)
RenderCsv.output_file(filename=output_csv, entities_dict=task.get_entities(via="dict"))
