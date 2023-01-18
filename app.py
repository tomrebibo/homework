import boto3, urllib

def feed(response):
    num = len(response["Labels"])
    counter = 0
    for i in range(int(num)):
        name = (response["Labels"][i]["Name"]).lower()
        if ((name == "fish") or (name == "milk") or (name == "bread")):
            counter += 1
    if (counter > 0):
        match = True
    else:
        match = False

    return match
def lambda_handler(event, context):
    client = boto3.client("rekognition")
    s3 = boto3.client("s3")
    # get our bucket and file name
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')

    # get our object
    fileObj = s3.get_object(Bucket=bucket, Key=key)

    # reading file from s3 bucket and passing it as bytes
    file_content = fileObj["Body"].read()

    # passing bytes data
    response = client.detect_labels(
        Image={"Bytes": file_content}, MinConfidence=90
    )

    # passing s3 bucket object file reference
    response = client.detect_labels(
        Image={"S3Object": {"Bucket": bucket, "Name": key}},

        MinConfidence=90,
    )

    # checks if the photo is milk, bread or fish and return true if it does.
    match = feed(response)
    return match
