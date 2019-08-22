entity_id = data.get('entity_id')
brightness_input_id = data.get('brightness_input_id')

def turn_on_light(hass, entity_id, brightness_input_id):
    brightness_100 = float(hass.states.get(brightness_input_id).state)
    brightness_255 = round(brightness_100 * 2.55)
    light_data = {'entity_id': entity_id, 'brightness': brightness_255}
    hass.services.call('light', 'turn_on', light_data, False)

if hass.states.is_state(entity_id, 'on'):
    turn_on_light(hass, entity_id, brightness_input_id)