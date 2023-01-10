def message_creator(text):
   # Escribe tu solución 👇
    options = {
        'computadora': 'Con mi computadora puedo programar usando Python',
        'celular'    : 'En mi celular puedo aprender usando la app de Platzi',
        'cable'      : '¡Hay un cable en mi bota!'
    }

    result = 'Artículo no encontrado'

    for op, value in options.items():
        if(op == text):
            result = value

    return result
# 
text = 'computadora'
response = message_creator(text)
print(response)

text_2 = 'celular'
response_2 = message_creator(text_2)
print(response_2)

text_3 = 'cable'
response_3 = message_creator(text_3)
print(response_3)

text_4 = 'ornitorrinco'
response_4 = message_creator(text_4)
print(response_4)