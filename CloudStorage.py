import dropbox


class TransferData:
    def __init__(self, acess_token):
        self.access_token=acess_token

    def upload_file(self, file_from, file_to):
        dbx=dropbox.Dropbox(self.access_token)
        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token='MWSgSBpSkj4AAAAAAAAAAUmpIYcnD3zswduek7oTgzIi_vyhF3aEDWaV6h2agEsy'
    transferData=TransferData(access_token)

    file_from=input("enter the file path")
    file_to=input("enter destination")

    transferData.upload_file(file_from, file_to)

main()
    
