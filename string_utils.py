import re

def split_before_uppercases(formula):
    """
    Splits a chemical formula (string) into a list of elements based on uppercase letters.
    Example: 'Fe2O3' -> ['Fe2', 'O3']
    """
    # חיפוש אות גדולה ואחריה אותיות קטנות (אופציונלי) ומספרים (אופציונלי)
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
        # אם אין מספר, הכמות היא 1
        count = int(number_str) if number_str else 1
        return name, count
    return element_string, 1

def count_atoms_in_molecule(molecular_formula):
    """Takes a molecular formula (string) and returns a dictionary of atom counts.
    Example: 'H2O' → {'H': 2, 'O': 1}"""

    # Step 1: Initialize an empty dictionary
    atom_counts = {}

    # שינינו כאן את שם הפונקציה ל-split_before_uppercases (במקום split_by_capitals)
    for atom in split_before_uppercases(molecular_formula):
        # שינינו כאן את שם הפונקציה ל-split_at_digit (במקום split_at_number)
        atom_name, atom_count = split_at_digit(atom)
        
        # Step 2: Update the dictionary
        atom_counts[atom_name] = atom_counts.get(atom_name, 0) + atom_count

    # Step 3: Return the completed dictionary
    return atom_counts

def parse_chemical_reaction(reaction_equation):
    reaction_equation = reaction_equation.replace(" ", "")
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")

def count_atoms_in_reaction(molecules_list):
    molecules_atoms_count = []
    for molecule in molecules_list:
        molecules_atoms_count.append(count_atoms_in_molecule(molecule))
    return molecules_atoms_count
