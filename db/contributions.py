from db.general import GeneralDbManipulator
from pymongo.collection import Collection


class ContributionsDbManipulator(GeneralDbManipulator):

    def __init__(self):
        super().__init__()

    def getUniqueStagedTitles(self):
        col: Collection = self.getCollection('wiki_staged')
        return col.find().distinct('title')
    
    def getUniqueComittedTitles(self):
        col: Collection = self.getCollection('wiki_comitted')
        return col.find().distinct('title')
