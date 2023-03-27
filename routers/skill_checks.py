from fastapi import APIRouter, HTTPException, Request, Depends
from pymongo import MongoClient
from bson.objectid import ObjectId
from urllib.parse import quote_plus 
import random
import bson
import yaml
import uuid


# region Router
router = APIRouter(
    prefix='/dice',
    tags=['dice']
)
# endregion

@router.get('/talent')
async def talent_check(att1: int, att2: int, att3: int, fw: int, mod: int):

    atts = [
        att1,
        att2,
        att3
    ]

    dice = [
        random.randint(1,20),
        random.randint(1,20),
        random.randint(1,20),
    ]

    neededFw = 0

    for i in range(len(atts)):
        checkResult = dice[i] - (atts[i] + mod)
        if checkResult > 0:
            neededFw += checkResult
    
    success = False
    if neededFw <= fw:
        success = True

    finalFw = fw - neededFw
    qs = getQs(finalFw)
    
    finalFw = fw - neededFw

    result = {
        'roll1':{
            'att': atts[0],
            'dice': dice[0],
        },
        'roll2':{
            'att': atts[1],
            'dice': dice[1],
        },
        'roll3':{
            'att': atts[2],
            'dice': dice[2],
        },
        'neededFw': neededFw,
        'availableFw': fw,
        'finalFw': finalFw,
        'qs': qs
    }

    return result


def getQs(fw: int):
    if 0 <= fw <= 3:
        return 1
    elif 3 <= fw <= 6:
        return 2
    elif 7 <= fw <= 9:
        return 3
    elif 10 <= fw <= 12:
        return 4
    elif 13 <= fw <= 15:
        return 5
    elif 16 <= fw:
        return 6