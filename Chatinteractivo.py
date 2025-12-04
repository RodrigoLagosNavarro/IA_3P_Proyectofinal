def responder_por_intencion(tag):
    if tag == "saludo":
        return "¡Hola! Bienvenido a Donas CETI 🍩, ¿en qué puedo ayudarte?"
    if tag == "despedida":
        return "¡Gracias por visitarnos! Que tengas un día muy dulce 🍩."
    if tag == "precio":
        return "Nuestras donas van desde $15 a $20 MXN. También tenemos cajas con descuento. 😉"
    if tag == "menu":
        return "Tenemos donas glaseadas, chocolate, cajeta, fresa con chispas y rellenas de crema. 🍩"
    if tag == "horario":
        return "Abrimos de 8 AM a 8 PM entre semana, y 9 AM a 6 PM los fines de semana."
    if tag == "ubicacion":
        return "Estamos en CETI, área de cafetería de Mecatrónica (ejemplo)."
    # Por si sale algo raro
    return "Lo siento, no entendí muy bien, pero puedo ayudarte con menú, precios, horario y ubicación."

def iniciar_chat():
    print("Chatbot Donas CETI (Deep Learning) 🍩")
    print("Escribe 'salir' para terminar.\n")

    while True:
        msg = input("Tú: ")
        if msg.lower().strip() == "salir":
            print("Chatbot: ¡Hasta luego! 🍩")
            break

        tag, conf = predecir_intencion(msg)
        print(f"(debug) intención: {tag}, confianza: {conf:.2f}")
        respuesta = responder_por_intencion(tag)
        print("Chatbot:", respuesta, "\n")

# Llamar al chat
iniciar_chat()
