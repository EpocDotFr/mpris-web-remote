from flask import Flask, render_template, jsonify, request
import dbus

app = Flask(__name__)


@app.route('/')
async def home():
    async with dbus.Dbus() as d:
        current_state = await d.get_current_state()

    return render_template('home.html', current_state=current_state)


@app.route('/action', methods=['POST'])
async def action():
    async with dbus.Dbus() as d:
        new_state = await d.change_state(request.form.get('action'))

    return jsonify({
        'new_state': new_state
    })
