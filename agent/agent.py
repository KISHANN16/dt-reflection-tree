import csv

# Load tree from TSV

def load_tree(filename):
tree = {}
with open(filename, newline='', encoding='utf-8') as file:
reader = csv.DictReader(file, delimiter='\t')
for row in reader:
tree[row['id']] = row
return tree

# Get children of a node

def get_children(tree, parent_id):
return [node for node in tree.values() if node['parentId'] == parent_id]

# Find next node based on decision logic

def handle_decision(node, last_answer):
rules = node['options']
for rule in rules.split(';'):
if not rule.strip():
continue
condition, target = rule.split(':')
if last_answer in condition:
return target
return None

# Run the agent

def run_agent(tree):
current_id = "START"
last_answer = ""

```
while True:
    node = tree[current_id]
    node_type = node['type']
    text = node['text']

    # Show text
    if text:
        print("\n" + text)

    # Handle node types
    if node_type == "start" or node_type == "bridge":
        children = get_children(tree, current_id)
        if children:
            current_id = children[0]['id']
        else:
            break

    elif node_type == "question":
        options = node['options'].split('|')
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")
        
        choice = int(input("Choose option: ")) - 1
        last_answer = options[choice]

        children = get_children(tree, current_id)
        if children:
            current_id = children[0]['id']

    elif node_type == "decision":
        next_id = handle_decision(node, last_answer)
        if next_id:
            current_id = next_id
        else:
            break

    elif node_type == "reflection":
        input("\nPress Enter to continue...")
        children = get_children(tree, current_id)
        if children:
            current_id = children[0]['id']

    elif node_type == "summary":
        input("\nPress Enter to finish...")
        children = get_children(tree, current_id)
        if children:
            current_id = children[0]['id']

    elif node_type == "end":
        print("\nSession Ended.")
        break

    else:
        break
```

# Run

if **name** == "**main**":
tree = load_tree("reflection-tree.tsv")
run_agent(tree)
