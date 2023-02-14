def read_lsystem_file(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    data = {}
    for line in lines:
        line = line.strip()
        key, value = line.split(':')
        key = key.strip()
        value = value.strip()
        if key == 'rules':
            rules = {}
            for rule in value.split(','):
                rule = rule.strip()
                var, expansion = rule.split('→')
                var = var.strip()
                expansion = expansion.strip()
                rules[var] = expansion
            data[key] = rules
        elif key in ('variables', 'constants'):
            data[key] = tuple(value.split(','))
        else:
            data[key] = value
    return data
binary_tree = read_lsystem_file('binary_tree.txt')
print(binary_tree)