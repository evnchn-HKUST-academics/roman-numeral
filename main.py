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


ui.dark_mode(True)
ui.query('body').classes('bg-gray-950')
ui.query('.nicegui-content').classes('p-0 gap-0')

# Header
with ui.element('div').classes('w-full bg-gradient-to-br from-gray-900 via-gray-900 to-cyan-950 border-b border-cyan-500/30'):
    with ui.element('div').classes('flex flex-col items-center py-10'):
        ui.label('Roman Numeral Converter').classes('text-4xl font-bold text-cyan-400 tracking-tight')
        ui.label('Built with NiceGUI · This project landed me an internship').classes('text-gray-400 text-lg mt-1')

# Main content
with ui.element('div').classes('w-full max-w-2xl mx-auto px-4 mt-8'):

    # Input card
    with ui.element('div').classes('bg-gray-900 border border-gray-800 rounded-2xl p-8'):
        ui.label('Enter Roman Numeral').classes('text-lg font-semibold text-cyan-400 mb-2')
        roman_input = ui.input(placeholder='e.g. XIV, MCMXCIX').classes('w-full text-lg')

        def convert():
            input_val = roman_input.value.strip()
            result_value.set_text('')
            error_label.set_text('')
            result_card.set_visibility(False)

            if not input_val:
                error_label.set_text('Please enter a Roman numeral.')
                return
            try:
                arabic = roman_to_arabic(input_val)
                result_value.set_text(str(arabic))
                result_input_label.set_text(f'"{input_val.upper()}" equals')
                result_card.set_visibility(True)
            except ValueError as e:
                error_label.set_text(str(e))

        roman_input.on('keydown.enter', convert)

        ui.button('Convert', on_click=convert).classes(
            'mt-4 font-semibold px-6 py-2 rounded-lg'
        ).props('no-caps color=cyan unelevated')
        error_label = ui.label('').classes('text-rose-400 mt-2')

    # Results card
    result_card = ui.element('div').classes('bg-gray-900 border border-gray-800 rounded-2xl p-8 mt-4')
    with result_card:
        result_input_label = ui.label('').classes('text-gray-400 text-sm mb-3')
        with ui.element('div').classes('bg-cyan-950/50 rounded-xl p-5 border border-cyan-500/20 flex items-center justify-center'):
            result_value = ui.label('').classes('text-4xl font-bold text-cyan-300')

    result_card.set_visibility(False)

ui.run(port=8080)
