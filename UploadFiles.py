import os
from typing import Mapping
import dropbox
from dropbox import files
from dropbox.files import Writemode

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token
    def upload_file(self, file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root,dirs,file in os.walk(file_from):
            for filename in files:
                local_path= os.path.join(root, filename)
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to,relative_path)
                
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path , mode=Writemode('overwrite'))

def main():
        access_token = 'qAvH21ENBUUAAAAAAAAAAU3NK1DF1E43J73RvNA5H1_ZFexWKbPJyRh0Mclke_tp'
        transferData = TransferData(access_token)

        file_from = input("Enter The Folder Path To Tranfer : ")
        file_to = input("Enter The Path To Upload To DropBox : ")

        transferData.upload_file(file_from,file_to)
        print("file had been moved !!!")


main()