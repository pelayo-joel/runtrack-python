def DevType(langage):
    match langage:
        case "javascript":
            return "Tu es un developpeur web"
        case "python":
            return "Tu es un developpeur IA"
        case "java":
            return "Tu es un developpeur logiciel"
        case "reactjs":
            return "Tu es un developpeur mobile"
        case _:
            return "Un jour, je serai le meilleur developpeur"

myLang = input("Quel langage : ")
print(DevType(myLang))