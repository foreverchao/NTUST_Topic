with open("tinder_api/utils/token.txt", "r") as f:
    tinder_token = f.read()

# it is best for you to write in the token to save yourself the file I/O
# especially if you have python byte code off
tinder_token = "ece7d4f5-150e-4979-a5ef-a1685ca89974"

headers = {
    'app_version': '6.9.4',
    'platform': 'ios',
    'content-type': 'application/json',
    'User-agent': 'Tinder/12.8.0 (iPohone; iOS 14.4.2; Scale/2.00)',
    'X-Auth-Token': tinder_token,
}

host = 'https://api.gotinder.com'

if __name__ == '__main__':
    pass
