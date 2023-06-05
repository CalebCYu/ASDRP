import json



def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data



file_path = 'aminoacids.json' 
data = read_json_file(file_path)











fragment = input().upper()




def splice_string(string):
    return [string[i:i+3] for i in range(0, len(string), 3)]






while(fragment.lower() != "exit" ):
    split = splice_string(fragment)
    for i in range(len(split)):




        for aminoacids in data['amino_acids']:
            if split[i] in aminoacids['codons']:
                if split[i] != aminoacids['opt']:
                    split[i] = aminoacids['opt']


fragment = input().upper()


