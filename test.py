


import json
import random

# Load the JSON data from the file
with open('aminoacids.json') as json_file:
    data = json.load(json_file)
    amino_acids = data['amino_acids']

# Function to randomize the fragments every three codons
def randomize_fragments(template_sequence):
    # Split the template sequence into codons
    codons = [template_sequence[i:i+9] for i in range(0, len(template_sequence), 9)]
    
    # Randomize the fragments
    random.shuffle(codons)
    
    # Reconstruct the randomized sequence
    randomized_sequence = ''.join(codons)
    
    return randomized_sequence

# Function to calculate molecular weight in kDa
def calculate_molecular_weight(amino_acid_sequence):
    molecular_weights = {
        "A": 89.1, "R": 174.2, "N": 132.1, "D": 133.1, "C": 121.2,
        "E": 147.1, "Q": 146.2, "G": 75.1, "H": 155.2, "I": 131.2,
        "L": 131.2, "K": 146.2, "M": 149.2, "F": 165.2, "P": 115.1,
        "S": 105.1, "T": 119.1, "W": 204.2, "Y": 181.2, "V": 117.1
    }
    
    weight = sum(molecular_weights.get(aa, 0) for aa in amino_acid_sequence)
    return weight / 1000.0  # Convert to kDa

# Get user input for mRNA template sequence
template_sequence = input("Enter the mRNA template sequence: ")
template_sequence.upper()
print(template_sequence)
# Fragment and randomize the sequence
fragments = [template_sequence[i:i+9] for i in range(0, len(template_sequence), 9)]
random.shuffle(fragments)

# Assemble fragments up to 20 and calculate molecular weight
amino_acid_sequence = []
molecular_weight = 0.0
for fragment in fragments[:20]:
    randomized_fragment = randomize_fragments(fragment)
    for i in range(0, len(randomized_fragment), 3):
        codon = randomized_fragment[i:i+3]
        amino_acid = next((aa["name"] for aa in amino_acids if codon in aa["codons"]), "Unknown")
        amino_acid_sequence.append(amino_acid)
    
    molecular_weight += calculate_molecular_weight(amino_acid_sequence)

# Print assembled fragments and molecular weight
print("Assembled Fragments (up to 20):")
for i, fragment in enumerate(amino_acid_sequence[:20], 1):
    print(f"Fragment {i}: {fragment}")
    
print(f"Molecular Weight: {molecular_weight:.2f} kDa")


