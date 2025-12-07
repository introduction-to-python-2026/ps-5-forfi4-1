import re

def split_before_uppercases(formula):
    """
    Splits a chemical formula (string) into a list of elements based on uppercase letters.
    Example: 'Fe2O3' -> ['Fe2', 'O3']
    """
    # שימוש ב-Regex כדי למצוא אות גדולה ואחריה אותיות קטנות או מספרים
    return re.findall(r'[A-Z][a-z]*\d*', formula)

def split_at_digit(element_string):
    """
    Splits an element string into a tuple of (element name, count).
    Example: 'Fe2' -> ('Fe', 2), 'O' -> ('O', 1)
    """
    match = re.match(r"([A-Za-z]+)(\d*)", element_string)
    if match:
        name = match.group(1)
        number_str = match.group(2)
        count = int(number_str) if number_str else 1
        return name, count
    return element_string, 1

def count_atoms_in_molecule(molecular_formula):
    """Takes a molecular formula (string) and returns a dictionary of atom counts.
    Example: 'H2O' → {'H': 2, 'O': 1}"""

    # Step 1: Initialize an empty dictionary to store atom counts
    atom_counts = {}

    # שיניתי כאן את שם הפונקציה ל-split_before_uppercases כדי שתתאים למה שמימשנו למעלה
    for atom in split_before_uppercases(molecular_formula):
        # שיניתי כאן את שם הפונקציה ל-split_at_digit כדי שתתאים למה שמימשנו למעלה
        atom_name, atom_count = split_at_digit(atom)
        
        # Step 2: Update the dictionary with the atom name and count
        # אם האטום כבר קיים (במקרים נדירים כמו CH3COOH), נוסיף לו, אחרת ניצור חדש
        atom_counts[atom_name] = atom_counts.get(atom_name, 0) + atom_count

    # Step 3: Return the completed dictionary
    return atom_counts

def parse_chemical_reaction(reaction_equation):
    """Takes a reaction equation (string) and returns reactants and products as lists.
    Example: 'H2 + O2 -> H2O' → (['H2', 'O2'], ['H2O'])"""
    reaction_equation = reaction_equation.replace(" ", "")  # Remove spaces for easier parsing
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")

def count_atoms_in_reaction(molecules_list):
    """Takes a list of molecular formulas and returns a list of atom count dictionaries.
    Example: ['H2', 'O2'] → [{'H': 2}, {'O': 2}]"""
    molecules_atoms_count = []
    for molecule in molecules_list:
        molecules_atoms_count.append(count_atoms_in_molecule(molecule))
    return molecules_atoms_count
