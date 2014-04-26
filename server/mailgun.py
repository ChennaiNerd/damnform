import requests
def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v2/sandbox381bc65cf9a0430cb057afb272d83c3a.mailgun.org/messages",
        auth=("api", "key-1e4mr4g9yfnhyfhps50ks2tu3xabjok1"),
        data={"from": "Mailgun Sandbox <postmaster@sandbox381bc65cf9a0430cb057afb272d83c3a.mailgun.org>",
              "to": "Dheeraj <dheerajjoshi1991@gmail.com>",
              "subject": "Hello Dheeraj",
              "text": "Congratulations Dheeraj, you just sent an email with Mailgun!  You are truly awesome!  You can see a record of this email in your logs: https://mailgun.com/cp/log .  You can send up to 300 emails/day from this sandbox server.  Next, you should add your own domain so you can send 10,000 emails/month for free."})

if __name__ == "__main__":
	send_simple_message()