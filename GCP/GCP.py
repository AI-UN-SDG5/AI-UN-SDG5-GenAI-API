from google.cloud import storage
import os
import dotenv
dotenv.load_dotenv()
from datetime import datetime
import json
from requests import get
import base64

class GCP:

    def __init__(self):
        self.gcp_decoded_sa_key_string = base64.b64decode(f"{os.environ.get(
            'GCP_SA_KEY_STRING')}{'=' * (4 - len(os.environ.get('GCP_SA_KEY_STRING')) % 4)}")
        self.gcp_sa_key_json = json.loads(self.gcp_decoded_sa_key_string)
        print(self.gcp_sa_key_json)

    def upload_contents_from_memory(self, bucket_name, contents, destination_blob_name):

        success = False
        start = datetime.now()
        print("Begin attempt to upload contents from memory to GCP Cloud Storage...")

        try:        
            storage_client = storage.Client.from_service_account_info(self.gcp_sa_key_json)
            bucket = storage_client.bucket(bucket_name)
            blob = bucket.blob(destination_blob_name)
            blob.upload_from_string(contents)
            print(
                f"{destination_blob_name} with contents {contents} uploaded to {bucket_name}."
            )
            success = True
        except Exception as e:
            print(f"Error uploading contents from memory to GCP Cloud Storage.")
            success  = False

        end = datetime.now()
        duration = end - start
        print(f"End of attempt to upload contents from memory to GCP Cloud Storage.")
        print(f"Process completed in {duration} seconds.")
        return success

    def upload_local_file(self, bucket_name, source_file_name, destination_blob_name):

        success = False
        start = datetime.now()
        print("Begin attempt to upload file to GCP Cloud Storage...")

        try:
            storage_client = storage.Client.from_service_account_info(self.gcp_sa_key_json)
            bucket = storage_client.bucket(bucket_name)
            blob = bucket.blob(destination_blob_name)
            print(blob)
            generation_match_precondition = 0
            blob.upload_from_filename(file_name=source_file_name, if_generation_match=generation_match_precondition)
            print(
                f"File {source_file_name} uploaded to {destination_blob_name}."
            )
            success = True
        except Exception as e:
            print(f"Exception uploading file to GCP Cloud Storage: {e}")
            success = False

        end = datetime.now()
        duration = end - start
        print(f"End of attempt to upload file to GCP Cloud Storage.")
        print(f"Process completed in {duration} seconds.")
        return success