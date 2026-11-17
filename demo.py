import json
from pathlib import Path
from motion import point_path
from task import plan_abstract

cases = json.loads((Path(__file__).parent / 'fixtures/cases.json').read_text())
n = cases['normal']
print(json.dumps({
    'point_path': point_path(n['width'], n['height'], n['blocked'], n['start'], n['goal']),
    'abstract_plan': plan_abstract(**n['abstract']),
}))
