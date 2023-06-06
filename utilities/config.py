from json import load

def getProductionStatus():
    with open('config.json', 'r') as f:
        config = load(f)
    return config['production']