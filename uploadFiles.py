import dropbox
import os

class TransferData(object):
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):

            for fn in files:
                local_path = os.path.join(root, fn)
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)

                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = "sl.A0LnjWBwfbK7e-xyk-HG2JAJnG2zurWV_0RqnWEyPFSSgePh-glRFxTGfrpnx_HGvMiignd6reo81gSG-78DEWgv3EBUL6OK7nvx5GYRBpS6LX6PPd0BIzzWU64jQQu39vYChksM0sGG"
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer: ")
    file_to = input("Enter the full path to upload to dropbox: ")

    transferData.upload_file(file_from,file_to)

    print("Your files have been uploaded successfully.")
main()