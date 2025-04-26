import gdown

# Replace this with your file's ID
file_id = "1r7YxC5Wfh3Gaz-acNnX7fCcVPc6R-rFJ"
output = "creditcard.csv"

# Construct the download URL
url = f"https://drive.google.com/uc?id={file_id}"

# Download
gdown.download(url, output, quiet=False)
