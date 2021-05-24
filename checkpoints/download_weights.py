
# This script serves as downloading any file from google drive. 
# adapted from Deepak Ghimire, ghmdeepak@gmail.com 
# google drive used: 2018410638@student.uitm.edu.my

import requests

def download_file_from_google_drive(id, file_name):
    def get_confirm_token(response):
        for key, value in response.cookies.items():
            if key.startswith('download_warning'):
                return value

        return None

    def save_response_content(response, file_name):
        CHUNK_SIZE = 32768

        with open(file_name, "wb") as f:
            for chunk in response.iter_content(CHUNK_SIZE):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)

    URL = "https://drive.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, file_name)    

# downlad pretrained weight files 
print("Downloading file ComplexYOLO_chkpt_800.pth ...")
download_file_from_google_drive("1kNP0ZWYXcS4WlehobyncBN2qUdhKIQk-", "ComplexYOLO_chkpt_800.pth")

print("Downloading file ComplexYOLO_chkpt_500.pth...")
download_file_from_google_drive("1xfDeP3NFjmXdiAK0Zgxut_FVm-ZGM0I0", "ComplexYOLO_chkpt_500.pth")

print("Downloading file TinyYOLO_chkpt_800.pth ...")
download_file_from_google_drive("1fM6QyafGTwNZwz0XB2SH_xGx2PJRBCli", "TinyYOLO_chkpt_800.pth")

print("Downloading file TinyYOLO_chkpt_500.pth ...")
download_file_from_google_drive("1W8cBw3JwcTexHwSRWqQf7OBjfoxW1UXj", "TinyYOLO_chkpt_500.pth")

print("Completed!")