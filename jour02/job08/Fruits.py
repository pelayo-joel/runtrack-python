def SeasonalFruit(typeSeason, saison):
    match typeSeason:
        case "fruit":
            if saison == "hiver":
                return "orange, mandarine et kiwi"
            elif saison == "ete":
                return "Poire, fraise, cassis"
        case "legume":
            if saison == "hiver":
                return "carotte, topinambour, endive"
            elif saison == "ete":
                return "artichaut, aubergine,navet"
        case _:
            return "Invalid type or season"

typeS = input("Choose a type : ")
season = input("Choose a season : ")
print(SeasonalFruit(typeS, season))