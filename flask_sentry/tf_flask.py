import sentry_sdk
from flask import Flask
import os
from dotenv import load_dotenv

#sentry_sdk.init(
 #   dsn="",
    # Add data like request headers and IP for users,
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
  #  send_default_pii=True,
#)

sentry_sdk.init(
    dsn=os.getenv("SENTRY_DSN"),
    traces_sample_rate=1.0,
    send_default_pii=True,
    environment=os.getenv("APP_ENV", "desarrollo")
)


app = Flask(__name__)

@app.route("/")
def hello_world():
    #1/0  # Descomenta esto para probar un error 500
    return "<p>Hello World TalentoFuturo!</p>"
    
@app.route("/error")
def error():
    # Esto genera un error intencional para probar Sentry
    return 1 / 0
    
if __name__ == "__main__":
    app.run(debug=True)
