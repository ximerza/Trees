import json


def diagnostico(nodo):
    if "diagnostico" in nodo:
        print(f"Diagnóstico: {nodo['diagnostico']}")
        return nodo['diagnostico']

    respuesta = input(f"{nodo['pregunta']} (si/no): ").strip().lower()

    if respuesta == "si":
        return diagnostico(nodo["si"])
    elif respuesta == "no":
        return diagnostico(nodo["no"])
    else:
        print("Por favor, responde con 'si' o 'no'.")
        return diagnostico(nodo)


def recorrido_postorden(nodo):
    if "diagnostico" in nodo:
        return [nodo["diagnostico"]]

    diagnosticos = []
    if "si" in nodo:
        diagnosticos.extend(recorrido_postorden(nodo["si"]))
    if "no" in nodo:
        diagnosticos.extend(recorrido_postorden(nodo["no"]))

    return diagnosticos



with open("diagnostico.json", "r", encoding="utf-8") as file:
    arbol = json.load(file)


print("Bienvenido al sistema de diagnóstico médico.")
diagnostico(arbol)


