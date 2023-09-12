def read_classification_from_file(fpath):
    classification = {}
    with open(fpath, 'r', encoding='utf-8') as f:
        for row in f:
            k, v = row.rstrip().split()
            classification[k] = v
 
    return classification
