"""Створіть клас геометричної фігури "Ромб". Клас повинен мати наступні атрибути:

сторона_а (довжина сторони a).
кут_а (кут між сторонами a і b).
кут_б (суміжний з кутом кут_а).
Необхідно реалізувати наступні вимоги:

Значення сторони сторона_а повинно бути більше 0.
Кути кут_а та кут_б повинні задовольняти умову: кут_а + кут_б = 180
Протилежні кути ромба завжди рівні, тому при заданому значенні кут_а, значення кут_б обчислюється автоматично.
Для встановлення значень атрибутів використовуйте метод __setattr__."""

class Rhombus:
    """
    Клас, що представляє ромб. Має атрибути:
    - side_a: довжина сторони ромба (перетворюється у модуль, щоб бути більше 0).
    - angle_a: кут між сторонами (в градусах, повинен бути між 0 і 180).
    - angle_b: суміжний з кутом angle_a (повинен дорівнювати 180 - angle_a).
    """

    def __init__(self, side_a: float, angle_a: float, angle_b: float):
        """Ініціалізуємо ромб з заданою стороною і кутом."""
        if angle_a + angle_b != 180:
            raise ValueError("The sum of angles must be 180.")
        self.side_a = side_a  # Встановлюємо довжину сторони
        self.angle_a = angle_a  # Встановлюємо кут angle_a
        self.angle_b = angle_b  # Встановлюємо кут angle_b

    def __setattr__(self, key, value):
        """
        Встановлюємо атрибути та виконуємо перевірку значень.
        """
        if key == "side_a":
            value = abs(value)  # Беремо модуль, щоб довжина була додатною

        if key in ["angle_a", "angle_b"]:
            if not (0 < value < 180):
                raise ValueError(f"{key} must be between 0 and 180 degrees.")
            if key == "angle_a":
                new_angle_b = 180 - value
                # Перевіряємо, чи кут angle_b вже встановлений і чи відповідає він умові
                if hasattr(self, "angle_b") and self.angle_b != new_angle_b:
                    raise ValueError("The sum of angles must be exactly 180 degrees.")
                object.__setattr__(self, "angle_b", new_angle_b)
            elif key == "angle_b":
                new_angle_a = 180 - value
                # Перевіряємо, чи кут angle_a вже встановлений і чи відповідає він умові
                if hasattr(self, "angle_a") and self.angle_a != new_angle_a:
                    raise ValueError("The sum of angles must be exactly 180 degrees.")
                object.__setattr__(self, "angle_a", new_angle_a)

        object.__setattr__(self, key, value)  # Встановлюємо значення атрибута
