def calcular_objetivo_ml(peso_kg, nivel_actividad):
    """
    Calcula el objetivo diario de consumo de agua en mililitros.
    Base: 35 ml por kg de peso.
    Ajustes por actividad:
    - bajo: -10%
    - medio: sin ajuste
    - alto: +10%
    """
    base = 35 * peso_kg
    if nivel_actividad == "bajo":
        objetivo = base * 0.9
    elif nivel_actividad == "medio":
        objetivo = base * 1.0
    elif nivel_actividad == "alto":
        objetivo = base * 1.1
    else:
        raise ValueError("Nivel de actividad inválido")
    return objetivo

def estado_hidratacion(consumo_ml, objetivo_ml):
    """
    Devuelve el estado de hidratación comparando consumo con objetivo.
    """
    if consumo_ml < objetivo_ml:
        porcentaje = ((objetivo_ml - consumo_ml) / objetivo_ml) * 100
        return f"Te falta un {porcentaje:.1f}% para llegar"
    elif consumo_ml == objetivo_ml:
        return "Has alcanzado tu objetivo"
    else:
        porcentaje = ((consumo_ml - objetivo_ml) / objetivo_ml) * 100
        return f"Has excedido tu objetivo en {porcentaje:.1f}%"

# Programa principal
personas = []

while True:
    try:
        peso = float(input("Ingrese su peso en kg: "))
        if peso <= 0:
            raise ValueError("El peso debe ser un número positivo")

        actividad = input("Ingrese su nivel de actividad física (bajo, medio, alto): ").lower()
        if actividad not in ["bajo", "medio", "alto"]:
            raise ValueError("Nivel de actividad debe ser 'bajo', 'medio' o 'alto'")

        consumo = float(input("Ingrese la cantidad de agua que ha consumido hoy en ml: "))
        if consumo < 0:
            raise ValueError("El consumo no puede ser negativo")

        objetivo = calcular_objetivo_ml(peso, actividad)
        estado = estado_hidratacion(consumo, objetivo)

        persona = {
            "peso": peso,
            "actividad": actividad,
            "consumo": consumo,
            "objetivo": objetivo
        }
        personas.append(persona)

        print(f"El objetivo diario de consumo de agua es: {objetivo:.0f} ml")
        print(f"El estado de hidratación es: {estado}")

        continuar = input("¿Desea agregar otra persona? (s/n): ").lower()
        if continuar != 's':
            break

    except ValueError as e:
        print(f"Error: {e}. Intente nuevamente.")

# Resumen de todas las personas
print("\nResumen de todas las personas cargadas:")
for i, p in enumerate(personas, 1):
    print(f"Persona {i}: Peso {p['peso']} kg, Actividad {p['actividad']}, Consumo {p['consumo']} ml, Objetivo {p['objetivo']:.0f} ml")