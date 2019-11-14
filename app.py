import argparse
from flask import Flask
from flask import Response, request, make_response, send_file, render_template, redirect

from ledpi import Ledpi
from swagger import initialize_swagger


app = Flask(__name__)
initialize_swagger(app)
channels = [17,18,22,23,24,6,12]
ledPi = Ledpi(channels)

@app.route('/')
def index():
    return redirect('/swagger/', code=302)

@app.route('/ledpi/<channel>', methods=['GET'])
def use(channel):
    if not channel.isdigit() or int(channel) not in ledPi.channels:
        return render_template('errors_basic.html'
                            , code=400
                            , error="Invalid channel {}, not supported".format(channel))
    state = request.args.get('state'
                                , default="Off"
                                , type = str)
    state = state.upper()
    channel = int(channel)
    print(channel, state)
    if state not in ["ON", "OFF", "ENQUIRE"]:
        return render_template('errors_basic.html'
                            , code=400
                            , error="state expected {} is not supported".format(state))
    if state == "ON":
        status, retStr = ledPi.on(channel)
    elif state == "ENQUIRE":
        status, retStr = ledPi.state(channel)
    else:
        status, retStr = ledPi.off(channel)
    if status == "SUCCESS":
        status_code = 200
        rendered = render_template('success_basic.html', msg=retStr)
    elif status == "NOCHANGE":
        status_code = 200
        rendered = render_template('nochange_basic.html', msg=retStr)
    else:
        status_code = 500
        rendered = render_template('errors_basic.html', error=retStr)
    response = make_response(rendered, status_code)
    return response


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", help="ip for the app", default="0.0.0.0", type=str)
    ap.add_argument("-p",  help= "port for the app", default=6994, type=int)
    args = vars(ap.parse_args())
    app.run(debug=True, port=int(args['p']), host=args['i'])
