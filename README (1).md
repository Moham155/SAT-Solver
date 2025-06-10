
# 🧠 SAT Solver using DPLL, DLIS, and Watched Literals

This project implements a complete SAT (Boolean Satisfiability) Solver in Python using the **Davis–Putnam–Logemann–Loveland (DPLL)** algorithm. It supports advanced heuristics like **DLIS (Dynamic Largest Individual Sum)** and **Watched Literals** to enhance performance over the basic recursive approach.

## 📂 Project Structure

```
.
├── main.py          # Command-line interface and solver entry point
├── dpll.py          # DPLL logic with heuristics (Basic, DLIS, Watched Literals)
├── parser.py        # DIMACS CNF parser
├── benchmarks/      # (Optional) DIMACS-format CNF test cases
```

## 🚀 Features

- ✅ **Supports three solving modes**: `basic`, `dlis`, and `watched`
- ✅ Implements **unit propagation**, **backtracking**, and **variable selection heuristics**
- ✅ Parses standard **DIMACS CNF files**
- ✅ Outputs SAT/UNSAT result, variable assignment, and solving time
- ✅ Designed for readability, modularity, and ease of extension

## 📌 Usage

### ▶️ Run the Solver

```bash
python main.py path/to/file.cnf --mode [basic|dlis|watched]
```

**Example:**

```bash
python main.py benchmarks/sample.cnf --mode watched
```

### ✅ Output Format

```
RESULT: SAT
ASSIGNMENT: 1=1 2=0 3=1 ...
Time taken: 0.0042 seconds
```

## 🧪 Benchmarking

Tested with 30+ CNF formulas from SATLIB and custom benchmarks.  
- Watched Literals mode reduced runtime by up to **35%** on large inputs.
- All heuristics validated for correctness and efficiency.

## 📖 Background

This solver was developed as part of a graduate-level Digital Systems Design Automation course.  
It demonstrates core concepts in:
- **Constraint solving**
- **Search space pruning**
- **Heuristic optimization**

## 🛠️ Dependencies

- Python 3.x (no external libraries required)

## 👨‍💻 Author

**Mohammed Misbahuddin**  
Purdue University – M.S. Electrical and Computer Engineering  
📧 uddin9893@gmail.com  
📎 [LinkedIn](https://www.linkedin.com/in/misbahuddin2001)  
📎 [GitHub](https://github.com/Moham155)

## 📄 License

This project is open-source and available under the MIT License.
