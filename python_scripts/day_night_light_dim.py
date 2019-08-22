brightness_input_id = data.get('brightness_input_id')
night_brightness = data.get('night')
day_brightness = data.get('day')

is_bedtime = hass.states.is_state('binary_sensor.is_bedtime', 'on')
brightness = night_brightness if is_bedtime else day_brightness

# set value
data = {'entity_id': brightness_input_id, 'value': brightness}
hass.services.call('input_number', 'set_value', data, False)