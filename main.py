import requests
import json

# Define the API endpoint and headers
url = "https://stake.com/_api/graphql"
headers = {
    "Accept": "*/*",
    "Accept-Language": "en-IN,en-GB;q=0.9,en;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Sec-Fetch-Mode": "cors",
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/126.0.6478.153 Mobile/15E148 Safari/604.1",
    "X-Access-Token": "f883f3e4be040513e6579bb07d116528549e40ac3706e0c8e03f7c3849728844b88a737e521f3d16683b96e5828f9705",
    "X-Lockdown-Token": "s5MNWtjTM5TvCMkAzxov",
    "Sec-Fetch-Dest": "empty",
    "Cookie": "intercom-session-cx1ywgf2=akdxTHIyT0tZbGlyQnlWRjZGUjFiWmtqTExoL3JRdGpOanRmWk9ta3U4RXMyMWxNZEkyY3h0RTFyVFhFdFh1OC0tMzBkWUxuMy83M1BZV2pDMlZtNStlZz09--38925436938fffded68abe57ef71767de421312b; __cf_bm=jAfvlqEx10up95w5BY13cHrfKdY3v6_Y_qpxBGwlFd8-1721796066-1.0.1.1-XCdA1WQJb3BqfCc490E_NDt5DfAwpnQeGsI3mqgE7IWDTebLO098GECVi3i8GFE1bfhxIkBA.Sw5R_3nTxvwxw; hideBalances=false"
}

# Define the payload
payload = {
    "query": "mutation LimboBet($amount: Float!, $multiplierTarget: Float!, $currency: CurrencyEnum!, $identifier: String!) { limboBet(amount: $amount, currency: $currency, multiplierTarget: $multiplierTarget, identifier: $identifier) { ...CasinoBet state { ...CasinoGameLimbo } } } fragment CasinoBet on CasinoBet { id active payoutMultiplier amountMultiplier amount payout updatedAt currency game user { id name } } fragment CasinoGameLimbo on CasinoGameLimbo { result multiplierTarget }",
    "variables": {
        "multiplierTarget": 2,
        "identifier": "osMeOW27cb0EeGh6ntOMI",
        "amount": 0.01,
        "currency": "inr"
    }
}

# Make the request
response = requests.post(url, headers=headers, json=payload)

# Print the response
print(json.dumps(response.json(), indent=4))
