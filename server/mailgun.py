import requests
def send_simple_message(mydata):
    return requests.post(
        "https://api.mailgun.net/v2/sandbox381bc65cf9a0430cb057afb272d83c3a.mailgun.org/messages",
        auth=("api", "APIKEY"),
        data={"from": mydata.get('from'),
              "to": mydata.get('to'),
              "cc": mydata.get('cc'),
              "bcc": mydata.get('bcc'),
              "subject": mydata.get('subject'),
              "text": mydata.get('text', ''),
              "html": mydata.get('html', '') })

def get_data():
	return {
				"from": "DamnForm<postmaster@sandbox381bc65cf9a0430cb057afb272d83c3a.mailgun.org>",
				"to": "Dheeraj <dheerajjoshi1991@gmail.com>",
				"cc": ["Dj <dheerajjoshi@outlook.com>","Joshi <dheerajjoshi1991@yahoo.co.in>"],
				"bcc": ["Dj <dheerajjoshi@outlook.com>"],
				"subject": "Hello World",
				#"text": "Testing Text :::: 1234567890"
				"html": "<html>Testing HTML <b>Bold</b><i>Italics</i><u>Underline</u></html>"
			}

if __name__ == "__main__":
	mydata = get_data()
	send_simple_message(mydata)
