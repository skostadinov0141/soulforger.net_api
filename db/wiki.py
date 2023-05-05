from bson import ObjectId
from db.general import GeneralDbManipulator
from pymongo.cursor import Cursor


class WikiDbManipulator(GeneralDbManipulator):

    def __init__(self):
        super().__init__()

    
    """Get a list of wiki entries based on a list of tags."""
    def findEntriesByTags(self, tags:list) -> list:
        return list(self.getCollection('wiki').find(
            {'category_path':{'$in':tags}},
            {'_id':{'$toString':'$_id'},'category_path':1,'title':1,'link':1}
        ))
    

    """Get all unique tags"""
    def findUniqueTags(self) -> list:
        return self.getCollection('wiki').distinct('category_path')
    

    """Get all unique titles"""
    def findUniqueTitles(self) -> list:
        return self.getCollection('wiki').distinct('title')
    

    """Find entry by ObjectID."""
    def findEntryById(self, entry_id: str) -> list:
        return self.getCollection('wiki').find_one({'_id':ObjectId(entry_id)},{'_id':{'$toString':'$_id'},'category_path':1,'title':1,'link':1})
    

    """Get the sub-categories of a category."""
    def findUniqueSubCategories(self, category: str) -> list:
        full_tags = list(self.getCollection('wiki').find({'category_path':{'$in':[category]}}).distinct('category_path'))
        full_titles = list(self.getCollection('wiki').find({'category_path':{'$in':[category]}}).distinct('title'))
        final_list = list(set(full_tags) - set(full_titles))
        final_list.remove(category)
        return sorted(final_list)
