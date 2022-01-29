import dropbox

class transferData:
    def __init__(self, passcode):
        self.passcode = passcode

    def upload(self, fileFrom, fileTo):
        db = dropbox.Dropbox(self.passcode)
        with open(fileFrom, "rb") as i:
            db.files_upload(i.read(), fileTo)

def chipoutle():
    passkey = "chiknmacroni"
    drop = transferData(passkey)

    fileFrom = input("Enter Source File Address: ")
    fileTo = input("Enter Recieving File Address: ")

    drop.upload(fileFrom, fileTo)
    print("File Transfer Successful!")

chipoutle()