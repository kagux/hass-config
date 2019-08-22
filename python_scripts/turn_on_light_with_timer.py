entity_id = data.get('entity_id')
illumination_sensor_id = data.get('illumination_sensor_id')
brightness_input_id = data.get('brightness_input_id')
duration_input_id = data.get('duration_input_id')
timer_id = data.get('timer_id')

def turn_on_light(hass, entity_id, brightness_input_id):
    brightness_100 = float(hass.states.get(brightness_input_id).state)
    brightness_255 = round(brightness_100 * 2.55)
    light_data = {'entity_id': entity_id, 'brightness': brightness_255}
    hass.services.call('light', 'turn_on', light_data, False)

def restart_timer(hass, timer_id, duration_input_id):
    # stop timer 
    timer_data = {'entity_id': timer_id}
    hass.services.call('timer', 'cancel', timer_data, False)

    # start timer 
    duration = round(float(hass.states.get(duration_input_id).state))
    timer_data = {'entity_id': timer_id, 'duration': duration}
    hass.services.call('timer', 'start', timer_data, False)

# main execution
lux_str = hass.states.get(illumination_sensor_id).state
if hass.states.is_state(entity_id, 'on') or lux_str != 'unknown' and int(lux_str) <= 30:
    turn_on_light(hass, entity_id, brightness_input_id)
    restart_timer(hass, timer_id, duration_input_id)