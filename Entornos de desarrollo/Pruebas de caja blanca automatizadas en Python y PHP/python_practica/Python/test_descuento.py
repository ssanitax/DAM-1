from descuento import calcular_descuento


def test_precio_negativo():
    assert calcular_descuento(0, False) == 0
    assert calcular_descuento(-10, True) == 0


def test_cliente_no_vip():
    assert calcular_descuento(100, False) == 90


def test_cliente_vip():
    assert calcular_descuento(100, True) == 80


def test_descuento_muy_alto():
    # Este caso falla a propósito: el resultado real es 480, no 420.
    assert calcular_descuento(600, True) == 420
