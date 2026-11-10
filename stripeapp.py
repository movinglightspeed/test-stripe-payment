import os

from flask import Flask, abort, redirect, request
from stripe import StripeClient
#python -m pip install flask stripe
api_key = os.environ.get("STRIPE_SECRET_KEY", "")
if not api_key.startswith("sk_test_"):
    raise SystemExit("Set STRIPE_SECRET_KEY to your Stripe test secret key.")

stripe = StripeClient(api_key)
app = Flask(__name__)
base_url = "http://127.0.0.1:5000"


@app.get("/")
def home():
    return """
    <form action="/checkout" method="post">
        <button type="submit">Pay $10.00 in test mode</button>
    </form>
    """


@app.post("/checkout")
def checkout():
    session = stripe.v1.checkout.sessions.create({
        "mode": "payment",
        "line_items": [{
            "price_data": {
                "currency": "usd",
                "unit_amount": 1000,
                "product_data": {"name": "Test product"},
            },
            "quantity": 1,
        }],
        "success_url": base_url + "/success?session_id={CHECKOUT_SESSION_ID}",
        "cancel_url": base_url + "/",
    })
    return redirect(session.url, code=303)


@app.get("/success")
def success():
    session_id = request.args.get("session_id")
    if not session_id:
        abort(400, description="Missing Checkout Session ID.")

    session = stripe.v1.checkout.sessions.retrieve(session_id)
    return {"payment_status": session.payment_status, "livemode": session.livemode}


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)