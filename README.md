Test Stripe Payment

This runs a sample Python code to test Stripe's Checkout Sessions API
https://docs.stripe.com/payments/checkout-sessions


Perquisites:
Setup venv: python -m venv .venv
Run venv: .\.venv\Scripts\Activate
Command: python -m pip install flask stripe

#Set API Key
set "STRIPE_SECRET_KEY=sk_test_REPLACE_WITH_NEW_KEY"


#Turn on Stripe's test mode
1. Go to https://dashboard.stripe.com/
2. On top left click on name and then select "Switch to Sandbox"
3. Then select "Test mode"

#Last step, run the app from within venv
python stripeapp.py
