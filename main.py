from nicegui import ui


def roman_to_arabic(roman: str) -> int:
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    roman = roman.upper().strip()
    if not roman:
        raise ValueError("Input is empty")
    for i, c in enumerate(roman):
        if c not in values:
            raise ValueError(f"Invalid character: {c}")
        if i + 1 < len(roman) and values[c] < values[roman[i + 1]]:
            result -= values[c]
        else:
            result += values[c]
    return result


def convert():
    input_val = roman_input.value.strip()
    result_label.set_text('')
    error_label.set_text('')
    if not input_val:
        error_label.set_text('Please enter a Roman numeral.')
        return
    try:
        arabic = roman_to_arabic(input_val)
        result_label.set_text(str(arabic))
    except ValueError as e:
        error_label.set_text(str(e))


with ui.column().classes('w-full items-center'):
    ui.label('Roman Numeral Converter').classes('text-3xl font-bold mt-8')
    with ui.card().classes('mt-4 p-6 w-96'):
        roman_input = ui.input(label='Roman Numeral', placeholder='e.g. XIV').classes('w-full')
        ui.button('Convert', on_click=convert).classes('mt-4')
        result_label = ui.label('').classes('text-2xl font-bold mt-4')
        error_label = ui.label('').classes('text-red-500 mt-2')

ui.run(port=8080)
