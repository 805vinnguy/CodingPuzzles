# Transcribing Emergency Calls
# Author: Vinh Nguyen

def matchNames(inputNames, dmvRecords): # inputNames: [] dmvRecords: []
    output = [None] * len(inputNames)
    records = to_dictionary(dmvRecords)
    for i in range(len(inputNames)):
        output[i] = records.get(inputNames[i])
    return output

def edit_distance(input, record):
    dist = abs(len(input) - len(record)) # account for insertion/deletions
    

def to_dictionary(dmvRecords):
    records = {}
    for record in dmvRecords:
        semicolon = record.index(";")
        name = record[:semicolon]
        address = record[semicolon + 1:]
        records[name] = address
    return records

# END OF FILE
