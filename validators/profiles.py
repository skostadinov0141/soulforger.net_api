from models.profile import Profile


def validateProfile(profile: Profile) -> dict:
    response = {
        'result':True,
        'details':[]
    }
    if len(profile.bio) > 2000:
        response['result'] = False
        response['details'].append({
            'category':'bio',
            'detail':'Über Mich ist zu lang. (max. 2000)'
        })
        
    if len(profile.display_name) < 5:
        response['result'] = False
        response['details'].append({
            'category':'display_name',
            'detail':'Anzeigename ist zu kurz. (min. 5)'
        })
    if len(profile.display_name) > 20:
        response['result'] = False
        response['details'].append({
            'category':'display_name',
            'detail':'Anzeigename ist zu lang. (max. 20)'
        })
    return response