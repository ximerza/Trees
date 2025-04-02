import json

def cargar_arbol(archivo="adivinanzas.json"):
    try:
        with open(archivo, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: No se encontró el archivo JSON.")
        exit()


def guardar_arbol(arbol, archivo="adivinanzas.json"):
    with open(archivo, "w", encoding="utf-8") as file:
        json.dump(arbol, file, indent=2, ensure_ascii=False)


def recorrido_preorden(nodo):
    if "pregunta" in nodo:
        print(nodo["pregunta"])
        if "si" in nodo:
            recorrido_preorden(nodo["si"])
        if "no" in nodo:
            recorrido_preorden(nodo["no"])


def jugar(nodo):
    if "adivinanza" in nodo:
        respuesta = input(f"¿Estás pensando en {nodo['adivinanza']}? (si/no): ").strip().lower()
        if respuesta == "si":
            print(" Adiviné. ")
            return
        else:
            actualizar_arbol(nodo)

    respuesta = input(f"{nodo['pregunta']} (si/no): ").strip().lower()

    if respuesta == "si":
        jugar(nodo["si"])
    elif respuesta == "no":
        jugar(nodo["no"])
    else:
        print("Por favor, responde con 'si' o 'no'.")
        jugar(nodo)


def actualizar_arbol(nodo):
    print("\n No adiviné. Ayúdame a mejorar el juego.")

    nuevo_objeto = input("¿En qué estabas pensando?: ").strip()
    nueva_pregunta = input(
        f"Escribe una pregunta para diferenciar '{nuevo_objeto}' de '{nodo['adivinanza']}': ").strip()
    respuesta_correcta = input(
        f"Para '{nuevo_objeto}', la respuesta a '{nueva_pregunta}' es 'si' o 'no'?: ").strip().lower()

    nodo["pregunta"] = nueva_pregunta
    nodo["si" if respuesta_correcta == "si" else "no"] = {"adivinanza": nuevo_objeto}
    nodo["no" if respuesta_correcta == "si" else "si"] = {"adivinanza": nodo.pop("adivinanza")}

    print("¡Gracias! ")
    guardar_arbol(arbol)


arbol = cargar_arbol("adivinanzas.json")


print("\n🎮 Bienvenido al juego de adivinanza.")
jugar(arbol)
