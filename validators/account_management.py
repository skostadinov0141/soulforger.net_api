import re
from pymongo.database import Database

from db._db_manager import DbManager

def validate_pw(password:str):
    response = {
        'result':True,
        'details':[]
    }
    if password == '': 
        response['result'] = False
        response['details'].append({
            'category':'password',
            'detail':'Bitte ein Passwort eingeben.'
        })
    # Define a dictionary of regular expressions for different password requirements
    # and the error messages to use if the password doesn't meet those requirements
    expressions = {
        r'(?=.*[a-z])': 'Das Passwort muss mindestens einen Kleinbuchstaben enthalten.',        # contains lowercase letter
        r'(?=.*[A-Z])': 'Das Passwort muss mindestens einen Großbuchstaben enthalten.',         # contains uppercase letter
        r'(?=.*[0-9])': 'Das Passwort muss mindestens eine Zahl enthalten.',                    # contains number
        r'(?=.*[^A-Za-z0-9])': 'Das Passwort muss mindestens ein Sonderzeichen enthalten.',     # contains special character
    }
    # Iterate over the regular expressions and check the password against each one
    for k, v in expressions.items():
        # If the password doesn't match the regular expression,
        # add the corresponding error message to the result details
        if re.match(k, password) is None:
            response['result'] = False
            response['details'].append({
                'category':'password',
                'detail':v
            })
    # If the password is less than 10 characters long, add an error message
    if len(password) < 10:
        response['result'] = False
        response['details'].append({
            'category':'password',
            'detail':'Passwort ist zu kurz.' # password too short
        }) 
    # Return the result dictionary
    return response



def validate_email(email:str):
    response = {
        'result':True,
        'details':[]
    }
    if email == '':
        response['result'] = False
        response['details'].append({
            'category':'email',
            'detail':'Bitte eine E-Mail eingeben.'
        })
    # Regex to verify email formatting
    regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if re.search(regex, email) is None:
        response['result'] = False
        response['details'].append({
            'category':'email',
            'detail':'Die E-Mail ist nicht gültig.'
        })
    return response