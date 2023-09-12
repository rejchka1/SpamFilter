def read_classification_from_file(fpath):
    with open(fpath, "r", encoding="utf-8") as f:
        dict = {}
        for line in f:
            line = line.replace('\n', '')
 
            key = line.split(' ')[0]
            value = line.split(' ')[1]
            dict[key] = value
    return dict
