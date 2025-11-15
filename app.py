from quart import Quart, render_template, jsonify, request, make_response
import dbus
import sse

app = Quart(__name__)


@app.route('/')
async def home():
    async with dbus.Mpris() as d:
        current_state = await d.get_current_state()

    return await render_template('home.html', current_state=current_state)


@app.route('/updates')
async def updates():
    async def send_events():
        # yield sse.message('playing', 'state-changed')
        #
        # sleep(2)
        #
        # yield sse.message('paused', 'state-changed')

        yield sse.message('paused', 'state-changed')

        def on_playback_status_changed(interface, properties, invalidated):
            print(interface, properties, invalidated)

        async with dbus.Properties() as d:
            d.interface.on_properties_changed(on_playback_status_changed)

            await d.bus.wait_for_disconnect()

    response = await make_response(
        send_events(),
        {
            'Content-Type': 'text/event-stream',
            'Cache-Control': 'no-cache',
            'Transfer-Encoding': 'chunked',
        }
    )

    response.timeout = None

    return response


@app.route('/change-state', methods=['POST'])
async def change_state():
    form = await request.form

    async with dbus.Mpris() as d:
        new_state = await d.change_state(form.get('action'))

    return jsonify({
        'new_state': new_state
    })
