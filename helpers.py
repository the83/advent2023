def parse(file_path):
    with open(file_path) as f:
        return [line.replace('\n', '') for line in f.readlines()]
