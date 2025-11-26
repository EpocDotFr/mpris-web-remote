from quart import Quart, render_template, jsonify, request
import dbus

app = Quart(__name__)


@app.route('/')
async def home():
    try:
        async with dbus.Mpris() as d:
            current_state = await d.get_current_state()

        message = None
    except RuntimeError as e:
        current_state = None
        message = 'Please run an MPRIS-compatible software and refresh the page.'

    return await render_template('home.html', current_state=current_state, message=message)


@app.route('/change-state', methods=['POST'])
async def change_state():
    form = await request.form

    async with dbus.Mpris() as d:
        new_state = await d.change_state(form.get('action'))

    return jsonify({
        'new_state': new_state
    })
