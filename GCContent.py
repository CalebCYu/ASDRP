

def gcContent(string):
    
    parsed = [string[i:i+1] for i in range(0, len(string))]
    
        
    length = len(string)
    gc = length
    
    for i in range(len(parsed)):
        if parsed[i] == "A":
            gc -= 1
        if parsed[i] =="T":
            gc -= 1
    print(gc)
    return gc/length

def TM(string):
    parsed = [string[i:i+1] for i in range(0, len(string))]
    
        
    length = len(string)
    gc = length
    
    for i in range(len(parsed)):
        if parsed[i] == "A":
            gc -= 1
        if parsed[i] =="T":
            gc -= 1
    return 64.9+41*(gc-16.4)/(length)

template_sequence = input("Enter the mRNA template sequence: ")

print(gcContent(template_sequence))
print(TM(template_sequence))
