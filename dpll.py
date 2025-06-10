from collections import defaultdict

# ------------------------------
# BASIC variable selection
# ------------------------------
def basic_variable_selection(clauses, assignment):
    for clause in clauses:
        for lit in clause:
            if abs(lit) not in assignment:
                return abs(lit), True  # Try True first
    return None

# ------------------------------
# BASIC DPLL (no heuristics)
# ------------------------------
def dpll_basic(clauses, assignment):
    while any(len(c) == 1 for c in clauses):
        unit = next(c[0] for c in clauses if len(c) == 1)
        assignment[abs(unit)] = unit > 0
        clauses = [c for c in clauses if unit not in c]
        clauses = [[l for l in c if l != -unit] for c in clauses]

    if not clauses:
        return assignment
    if any(len(c) == 0 for c in clauses):
        return None

    result = basic_variable_selection(clauses, assignment)
    if result is None:
        return None
    var, prefer_true = result

    for value in [prefer_true, not prefer_true]:
        lit = var if value else -var
        new_assignment = assignment.copy()
        new_assignment[var] = value
        simplified = [c for c in clauses if lit not in c]
        simplified = [[l for l in c if l != -lit] for c in simplified]
        result = dpll_basic(simplified, new_assignment)
        if result is not None:
            return result

    return None

# ------------------------------
# DLIS variable selection
# ------------------------------
def dlis_variable_selection(clauses, assignment):
    literal_counts = defaultdict(int)
    for clause in clauses:
        for lit in clause:
            if abs(lit) not in assignment:
                literal_counts[lit] += 1
    if not literal_counts:
        return None
    best_lit = max(literal_counts, key=lambda k: literal_counts[k])
    return abs(best_lit), best_lit > 0

# ------------------------------
# Core DPLL with DLIS
# ------------------------------
def dpll(clauses, assignment):
    while any(len(c) == 1 for c in clauses):
        unit = next(c[0] for c in clauses if len(c) == 1)
        assignment[abs(unit)] = unit > 0
        clauses = [c for c in clauses if unit not in c]
        clauses = [[l for l in c if l != -unit] for c in clauses]

    if not clauses:
        return assignment
    if any(len(c) == 0 for c in clauses):
        return None

    result = dlis_variable_selection(clauses, assignment)
    if result is None:
        return None
    var, prefer_true = result

    for value in [prefer_true, not prefer_true]:
        lit = var if value else -var
        new_assignment = assignment.copy()
        new_assignment[var] = value
        simplified = [c for c in clauses if lit not in c]
        simplified = [[l for l in c if l != -lit] for c in simplified]
        result = dpll(simplified, new_assignment)
        if result is not None:
            return result

    return None

# ------------------------------
# Watched Literals + DLIS
# ------------------------------
def dpll_watched(clauses, assignment):
    def simplify(clauses, lit):
        new_clauses = []
        for clause in clauses:
            if lit in clause:
                continue
            new_clause = [l for l in clause if l != -lit]
            new_clauses.append(new_clause)
        return new_clauses

    def propagate(clauses, assignment):
        queue = [lit for clause in clauses if len(clause) == 1 for lit in clause]
        while queue:
            unit = queue.pop()
            val = unit > 0
            assignment[abs(unit)] = val
            updated_clauses = simplify(clauses, unit)
            for clause in updated_clauses:
                unassigned = [lit for lit in clause if abs(lit) not in assignment]
                if len(unassigned) == 0:
                    if not any((lit > 0 and assignment.get(abs(lit), False)) or (lit < 0 and not assignment.get(abs(lit), False)) for lit in clause):
                        return None, None
                elif len(unassigned) == 1:
                    queue.append(unassigned[0])
            clauses = updated_clauses
        return clauses, assignment

    def solve(clauses, assignment):
        clauses, assignment = propagate(clauses, assignment)
        if clauses is None:
            return None
        if not clauses:
            return assignment

        result = dlis_variable_selection(clauses, assignment)
        if result is None:
            return None
        var, prefer_true = result

        for value in [prefer_true, not prefer_true]:
            lit = var if value else -var
            new_assignment = assignment.copy()
            new_assignment[var] = value
            new_clauses = simplify(clauses, lit)
            result = solve(new_clauses, new_assignment)
            if result is not None:
                return result

        return None

    return solve(clauses, assignment)
