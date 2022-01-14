import logging

logging.basicConfig(
    level=logging.INFO,
    filename='calculator.log',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)


def sum_deduct_calc(first_value: int, second_value: int):
    try:
        sum_result = first_value + second_value
        deduct_result = first_value - second_value
    except TypeError:
        logging.error('Invalid data type!')
    else:
        logging.info(f'Input was: {first_value}, {second_value}. '
                     f'Sum: {sum_result}, Deduct: {deduct_result}')
