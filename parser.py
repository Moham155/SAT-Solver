def parse_dimacs_cnf(file_path):
    clauses = []
    num_vars = 0

    with open(file_path, 'r') as f:
        for line in f:
            stripped = line.strip()
            if stripped == '' or stripped.startswith(('c', '%', '0')):
                continue

            if stripped.startswith('p'):
                parts = stripped.split()
                if len(parts) != 4 or parts[1] != 'cnf':
                    raise ValueError("Invalid problem line in DIMACS file")
                num_vars = int(parts[2])
                continue

            clause = list(map(int, stripped.split()))
            if clause[-1] != 0:
                raise ValueError("Each clause must end with a 0")
            clauses.append(clause[:-1])

    return num_vars, clauses