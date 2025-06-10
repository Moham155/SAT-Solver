# main.py – Supports basic, dlis, and watched modes

import sys
import time
import argparse
from parser import parse_dimacs_cnf
from dpll import dpll, dpll_watched

def get_all_vars(clauses):
    return sorted(set(abs(lit) for clause in clauses for lit in clause))

def format_output(result, vars_list, elapsed):
    if result is None:
        print("RESULT:UNSAT")
    else:
        print("RESULT:SAT")
        shown = ' '.join(f"{var}={int(result.get(var, False))}" for var in vars_list[:15])
        print(f"ASSIGNMENT:{shown}")
        if len(vars_list) > 15:
            print(f"... ({len(vars_list)-15} more variables not shown)")
    print(f"Time taken: {elapsed:.4f} seconds")

def main():
    parser = argparse.ArgumentParser(description="Run SAT solver in different modes.")
    parser.add_argument("cnf_file", help="Path to the CNF file")
    parser.add_argument("--mode", choices=["basic", "dlis", "watched"], default="dlis", help="Solving mode")
    args = parser.parse_args()

    filename = args.cnf_file
    mode = args.mode

    num_vars, clauses = parse_dimacs_cnf(filename)
    all_vars = get_all_vars(clauses)
    assignment = {}

    start = time.time()

    if mode == "basic":
        result = dpll(clauses, assignment)
    elif mode == "dlis":
        result = dpll(clauses, assignment)
    elif mode == "watched":
        result = dpll_watched(clauses, assignment)
    else:
        raise ValueError("Unknown mode")

    elapsed = time.time() - start
    format_output(result, all_vars, elapsed)

if __name__ == "__main__":
    main()
