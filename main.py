from laba import Digit  # Импортируем класс Digit

def main():
    operations = Digit()  # Создаем экземпляр класса

    print("Сложение:")
    print("Ввод числа №1")
    num1 = int(input())
    print("Число введено:", num1)
    print("Прямой код: [", operations.convert_to_binary_number(num1), "]", sep='')
    print("Обратный код: [", operations.convert_to_reverse_binary(num1), "]", sep='')
    print("Дополнительный код: [", operations.convert_to_additional_binary(num1), "]", sep='')

    print("Ввод числа №2")
    num2 = int(input())
    print("Число введено:", num2)
    print("Прямой код: [", operations.convert_to_binary_number(num2), "]", sep='')
    print("Обратный код: [", operations.convert_to_reverse_binary(num2), "]", sep='')
    print("Дополнительный код: [", operations.convert_to_additional_binary(num2), "]", sep='')

    result = operations.additional_summa(num1, num2)
    decimal_result = operations.convert_to_dec(result)
    print("Результат:", decimal_result)
    print("Прямой код: [", operations.convert_to_binary_number(decimal_result), "]", sep='')
    print("Обратный код: [", operations.convert_to_reverse_binary(decimal_result), "]", sep='')
    print("Дополнительный код: [", operations.convert_to_additional_binary(decimal_result), "]", sep='')

    print("Вычитание:")
    result = operations.additional_subtract(num1, num2)
    decimal_result = operations.convert_to_dec(result)
    print("Результат:", decimal_result)
    print("Прямой код: [", operations.convert_to_binary_number(decimal_result), "]", sep='')
    print("Обратный код: [", operations.convert_to_reverse_binary(decimal_result), "]", sep='')
    print("Дополнительный код: [", operations.convert_to_additional_binary(decimal_result), "]", sep='')

    print("Умножение:")
    print(operations.direct_code_multiplication(num1, num2))

    print("Деление:")
    result = operations.divide_bin(num1, num2)
    print(result)

    # Цикл для сложения чисел с плавающей точкой
    while True:
        print("Сложение чисел с плавающей точкой (для выхода введите 'e'):")
        print("Ввод числа №1")
        float1_input = input()
        if float1_input.lower() == 'e':
            break
        try:
            float1 = float(float1_input)
        except ValueError:
            print("Ошибка: введите число или 'e' для выхода.")
            continue

        print("Ввод числа №2")
        float2_input = input()
        if float2_input.lower() == 'e':
            break
        try:
            float2 = float(float2_input)
        except ValueError:
            print("Ошибка: введите число или 'e' для выхода.")
            continue

        binary_float1 = operations.convert_float_to_bin(float1)
        binary_float2 = operations.convert_float_to_bin(float2)
        operations.display_ieee(binary_float1)
        operations.display_ieee(binary_float2)
        result = operations.float_summa(float1, float2)
        print("Результат:", round(result, 5))  # Округляем результат до 5 знаков после запятой

if __name__ == '__main__':
    main()