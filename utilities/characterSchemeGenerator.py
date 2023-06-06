def generateTalentList():
    talents = {
        "Fliegen":{"level_factor":"B","check":"MU/IN/GE","fw":0,"category":"Körpertalente"},
        "Gaukeleien":{"level_factor":"A","check":"MU/CH/FF","fw":0,"category":"Körpertalente"},
        "Klettern":{"level_factor":"B","check":"MU/GE/KK","fw":0,"category":"Körpertalente"},
        "Körperbeherrschung":{"level_factor":"D","check":"GE/GE/KO","fw":0,"category":"Körpertalente"},
        "Kraftakt":{"level_factor":"B","check":"KO/KK/KK","fw":0,"category":"Körpertalente"},
        "Reiten":{"level_factor":"B","check":"CH/GE/KK","fw":0,"category":"Körpertalente"},
        "Schwimmen":{"level_factor":"B","check":"GE/KO/KK","fw":0,"category":"Körpertalente"},
        "Selbstbeherrschung":{"level_factor":"D","check":"MU/MU/KO","fw":0,"category":"Körpertalente"},
        "Singen":{"level_factor":"A","check":"KL/CH/KO","fw":0,"category":"Körpertalente"},
        "Sinnesschärfe":{"level_factor":"D","check":"KL/IN/IN","fw":0,"category":"Körpertalente"},
        "Tanzen":{"level_factor":"A","check":"KL/CH/GE","fw":0,"category":"Körpertalente"},
        "Taschendiebstahl":{"level_factor":"B","check":"MU/FF/GE","fw":0,"category":"Körpertalente"},
        "Verbergen":{"level_factor":"C","check":"MU/IN/GE","fw":0,"category":"Körpertalente"},
        "Zechen":{"level_factor":"A","check":"KL/KO/KK","fw":0,"category":"Körpertalente"},

        "Bekehren & Überzeugen":{"level_factor":"B","check":"MU/KL/CH","fw":0,"category":"Gesellschaftstalente"},
        "Betören":{"level_factor":"B","check":"MU/CH/CH","fw":0,"category":"Gesellschaftstalente"},
        "Einschüchtern":{"level_factor":"B","check":"MU/IN/CH","fw":0,"category":"Gesellschaftstalente"},
        "Etikette":{"level_factor":"B","check":"KL/IN/CH","fw":0,"category":"Gesellschaftstalente"},
        "Gassenwissen":{"level_factor":"C","check":"KL/IN/CH","fw":0,"category":"Gesellschaftstalente"},
        "Menschenkenntnis":{"level_factor":"C","check":"KL/IN/CH","fw":0,"category":"Gesellschaftstalente"},
        "Überreden":{"level_factor":"C","check":"MU/IN/CH","fw":0,"category":"Gesellschaftstalente"},
        "Verkleiden":{"level_factor":"B","check":"IN/CH/GE","fw":0,"category":"Gesellschaftstalente"},
        "Willenskraft":{"level_factor":"D","check":"MU/IN/CH","fw":0,"category":"Gesellschaftstalente"},

        "Fährtensuchen":{"level_factor":"C","check":"MU/IN/GE","fw":0,"category":"Naturtalente"},
        "Fesseln":{"level_factor":"A","check":"KL/FF/KK","fw":0,"category":"Naturtalente"},
        "Fischen & Angeln":{"level_factor":"A","check":"FF/GE/KO","fw":0,"category":"Naturtalente"},
        "Orientierung":{"level_factor":"B","check":"KL/IN/IN","fw":0,"category":"Naturtalente"},
        "Pflanzenkunde":{"level_factor":"C","check":"KL/FF/KO","fw":0,"category":"Naturtalente"},
        "Tierkunde":{"level_factor":"C","check":"MU/MU/CH","fw":0,"category":"Naturtalente"},
        "Wildnisleben":{"level_factor":"C","check":"MU/GE/KO","fw":0,"category":"Naturtalente"},

        "Brett- & Glücksspiel ":{"level_factor":"A","check":"KL/KL/IN","fw":0,"category":"Wissenstalente"},
        "Geographie":{"level_factor":"B","check":"KL/KL/IN","fw":0,"category":"Wissenstalente"},
        "Geschichtswissen":{"level_factor":"B","check":"KL/KL/IN","fw":0,"category":"Wissenstalente"},
        "Götter & Kulte":{"level_factor":"B","check":"KL/KL/IN","fw":0,"category":"Wissenstalente"},
        "Kriegskunst":{"level_factor":"B","check":"MU/KL/IN","fw":0,"category":"Wissenstalente"},
        "Magiekunde":{"level_factor":"C","check":"KL/KL/IN","fw":0,"category":"Wissenstalente"},
        "Mechanik":{"level_factor":"B","check":"KL/KL/FF","fw":0,"category":"Wissenstalente"},
        "Rechnen":{"level_factor":"A","check":"KL/KL/IN","fw":0,"category":"Wissenstalente"},
        "Rechtskunde":{"level_factor":"A","check":"KL/KL/IN","fw":0,"category":"Wissenstalente"},
        "Sagen & Legenden":{"level_factor":"B","check":"KL/KL/IN","fw":0,"category":"Wissenstalente"},
        "Sphärenkunde":{"level_factor":"B","check":"KL/KL/IN","fw":0,"category":"Wissenstalente"},
        "Sternkunde":{"level_factor":"A","check":"KL/KL/IN","fw":0,"category":"Wissenstalente"},

        "Alchimie":{"level_factor":"C","check":"MU/KL/FF","fw":0,"category":"Handwerkstalente"},
        "Boote & Schiffe":{"level_factor":"B","check":"FF/GE/KK","fw":0,"category":"Handwerkstalente"},
        "Fahrzeuge":{"level_factor":"A","check":"CH/FF/KO","fw":0,"category":"Handwerkstalente"},
        "Handel":{"level_factor":"B","check":"KL/IN/CH","fw":0,"category":"Handwerkstalente"},
        "Heilkunde Gift":{"level_factor":"B","check":"MU/KL/IN","fw":0,"category":"Handwerkstalente"},
        "Heilkunde Krankheiten":{"level_factor":"B","check":"MU/IN/KO","fw":0,"category":"Handwerkstalente"},
        "Heilkunde Seele":{"level_factor":"B","check":"IN/CH/KO","fw":0,"category":"Handwerkstalente"},
        "Heilkunde Wunden":{"level_factor":"D","check":"KL/FF/FF","fw":0,"category":"Handwerkstalente"},
        "Holzbearbeitung":{"level_factor":"B","check":"FF/GE/KK","fw":0,"category":"Handwerkstalente"},
        "Lebensmittelbearbeitung":{"level_factor":"A","check":"IN/FF/FF","fw":0,"category":"Handwerkstalente"},
        "Lederbearbeitung":{"level_factor":"B","check":"FF/GE/KO","fw":0,"category":"Handwerkstalente"},
        "Malen & Zeichnen":{"level_factor":"A","check":"IN/FF/FF","fw":0,"category":"Handwerkstalente"},
        "Metallbearbeitung":{"level_factor":"C","check":"FF/KO/KK","fw":0,"category":"Handwerkstalente"},
        "Musizieren":{"level_factor":"A","check":"CH/FF/KO","fw":0,"category":"Handwerkstalente"},
        "Schlösserknacken":{"level_factor":"C","check":"IN/FF/FF","fw":0,"category":"Handwerkstalente"},
        "Steinbearbeitung":{"level_factor":"A","check":"FF/FF/KK","fw":0,"category":"Handwerkstalente"},
        "Stoffbearbeitung":{"level_factor":"A","check":"KL/FF/FF","fw":0,"category":"Handwerkstalente"},
    }
    output = []
    for k,v in talents.items():
        splitAtts = v["check"].split("/")
        output.append({
            "name":k,
            "category":v["category"],
            "fw":0,
            "att_1":splitAtts[0],
            "att_2":splitAtts[1],
            "att_3":splitAtts[2],
            "level_factor":v['level_factor']
        })
    return output

def generateCombatSkillList():
    returnValue = [
        {'name' : 'Armbrüste', 'lf' : 'FF', 'at' : 0, 'pa' : 0},
        {'name' : 'Bögen', 'lf' : 'FF', 'at' : 0, 'pa' : 0},
        {'name' : 'Dolche', 'lf' : 'GE', 'at' : 0, 'pa' : 0},
        {'name' : 'Fechtwaffen', 'lf' : 'GE', 'at' : 0, 'pa' : 0},
        {'name' : 'Hiebwaffen', 'lf' : 'KK', 'at' : 0, 'pa' : 0},
        {'name' : 'Kettenwaffen', 'lf' : 'KK', 'at' : 0, 'pa' : 0},
        {'name' : 'Lanzen', 'lf' : 'KK', 'at' : 0, 'pa' : 0},
        {'name' : 'Raufen', 'lf' : 'GE/KK', 'at' : 0, 'pa' : 0},
        {'name' : 'Schilde', 'lf' : 'KK', 'at' : 0, 'pa' : 0},
        {'name' : 'Schwerter', 'lf' : 'GE/KK', 'at' : 0, 'pa' : 0},
        {'name' : 'Stangenwaffen', 'lf' : 'GE/KK', 'at' : 0, 'pa' : 0},
        {'name' : 'Wurfwaffen', 'lf' : 'FF', 'at' : 0, 'pa' : 0},
        {'name' : 'Zweihandhiebwaffen', 'lf' : 'KK', 'at' : 0, 'pa' : 0},
        {'name' : 'Zweihandschwerter', 'lf' : 'KK', 'at' : 0, 'pa' : 0},
    ]
    return returnValue