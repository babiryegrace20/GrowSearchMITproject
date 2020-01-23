#Import the Africa's Talking SDK
import africastalking

#Set up your credentials
username = "sandbox"
api_key = "6b045fda3228cd0e46ff1bb13aef75b37d2d0805f3657e19ce5f067e501931bb"

#Initialize the SDK
africastalking.initialize(username, api_key)

#Define the Payment service
payments = africastalking.Payment

#Set your product name
product_name = "GROWSEARCH"

#Set the phone number you want and set it to the international format
phone_number = "+256788915486"

#Set the 3 letter ISO currency code and checkout amount
currency_code = "UGX"
amount = 20000.0

#You can add in your own metadata which will be resent back to you
#For the final payment notification
metadata = {
    "agentId": "17U3353PS",
    "productId": "4668"
}

#Time to send and we'll handle the rest
try:
    res = payments.mobile_checkout(product_name, phone_number, currency_code, amount, metadata)
    print(res)
except Exception as e:
    print(f"Houston we have a problem {e}")