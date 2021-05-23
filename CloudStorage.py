import dropbox
class TransferData:
   def __init__(self, access_token):
       self.access_token=access_token
   def upload_file(self, file_from, file_to):
       dbx=dropbox.Dropbox(self, access_token)
       f=open(file_from, 'rb')
       dbx.files_upload(f.read(),file_to)
def main():
    access_token='sl.AxVHPOFaG0FawiOyyoWarEkxCAeM7ZSqOlg2BVe18wi5ogaBAf9ysZDE-ENllwbQ7Bf2KxtRr6v9ccAoK0XGrNZ8FfkJDunWZQSRz2bLdXU0d6A2b-IxB1xWMPcETzkBwhZvhlE'
    transferData=TransferData(access_token)
    file_from = input("Enter complete file path that needs to be transferred.")
    file_to = input("Enter complete file path to the place you want your file to go to inside of Dropbox.")
    transferData.upload_file(file_from, file_to)
    print("File has been moved!")
main()
