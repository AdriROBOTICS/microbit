# Función para botón A - mostrar total
# Función para botón B - reiniciar
# Función para botones A+B - ajustar umbral
# Registrar eventos de botones

def on_button_pressed_a():
    if pasos < 100:
        basic.show_number(pasos)
    else:
        basic.show_string("" + str(pasos))
    basic.pause(2000)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global umbral
    umbral += 200
    basic.show_string("U:" + ("" + str(umbral)))
    basic.pause(2000)
    basic.clear_screen()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global pasos
    pasos = 0
    basic.show_string("0")
    basic.pause(1000)
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

def obtener_aceleracion_total():
    global x, y, z, total
    # Calcula la aceleración total
    x = input.acceleration(Dimension.X)
    y = input.acceleration(Dimension.Y)
    z = input.acceleration(Dimension.Z)
    # Suma de valores absolutos para aproximar magnitud
    total = abs(x) + abs(y) + abs(z)
    return total
ultimo_tiempo = 0
aceleracion_anterior = 0
tiempo_actual = 0
aceleracion_actual = 0
total = 0
z = 0
y = 0
x = 0
pasos = 0
umbral = 0
umbral = 1200
tiempo_minimo = 100
# Inicialización
basic.show_icon(IconNames.HEART)
basic.pause(1000)
basic.show_string("0")
radio.set_group(24)

def on_every_interval():
    radio.send_number(pasos)
loops.every_interval(1000, on_every_interval)

# Iniciar bucle principal

def on_forever():
    global aceleracion_actual, tiempo_actual, pasos, ultimo_tiempo, aceleracion_anterior
    # Obtener aceleración actual
    aceleracion_actual = obtener_aceleracion_total()
    # Obtener tiempo actual
    tiempo_actual = input.running_time()
    # Detectar paso: pico de aceleración
    if aceleracion_actual > umbral and aceleracion_anterior <= umbral and tiempo_actual - ultimo_tiempo > tiempo_minimo:
        # Paso detectado
        pasos += 2
        ultimo_tiempo = tiempo_actual
        # Mostrar el número completo de pasos
        if pasos < 10:
            basic.show_number(pasos)
        else:
            basic.show_string("" + str((pasos)))
        basic.pause(1000)
        basic.clear_screen()
    # Actualizar aceleración anterior
    aceleracion_anterior = aceleracion_actual
basic.forever(on_forever)
