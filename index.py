from mermaid2django.parser import ParseMermaidErDiagram
from mermaid2django.render.csv import csv_maker
from mermaid2django.render.make_admin import admin_maker
from mermaid2django.render.make_model import model_maker

input_mermaid = "./examples/plan.mmd"
output_model = "./dist/models.py"
output_admin = "./dist/admin.py"

task = ParseMermaidErDiagram(input_mermaid)
entities = task.parse()
model_maker(task, entities, output_model)
admin_maker(entities, output_admin)
csv_maker(task.get_entities(via="dict"))