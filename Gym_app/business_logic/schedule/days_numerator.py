class Numerator:
    def __init__(self):
        pass

    def numerate(self, collection):
        collection_dict = {}
        i = 0
        for item in collection:
            collection_dict[item] = i
            i = i + 1

        return collection_dict
