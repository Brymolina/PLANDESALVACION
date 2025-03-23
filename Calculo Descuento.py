def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento sobre un monto total.

    :param monto_total: El monto total de la compra.
    :param porcentaje_descuento: El porcentaje de descuento (por defecto 10%).
    :return: El monto del descuento.
    """
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento


if __name__ == "__main__":
    # Primera llamada con solo el monto total (usar valor por defecto del 10%)
    monto1 = 100
    descuento1 = calcular_descuento(monto1)
    print(f"Compra de ${monto1}: Descuento de ${descuento1}, Total a pagar: ${monto1 - descuento1}")

    # Segunda llamada con un monto total y un porcentaje de descuento específico
    monto2 = 200
    porcentaje = 15
    descuento2 = calcular_descuento(monto2, porcentaje)
    print(f"Compra de ${monto2} con {porcentaje}% de descuento: Descuento de ${descuento2}, Total a pagar: ${monto2 - descuento2}")
