import boto3

# AWS API key configuration
# Add your Key ID ex: BLJBRZMQNO5ICMEVCS4F
AWS_ACCESS_KEY_ID = "KEY_ID"
# Add your Secret Access Key ex: vAKNVRD1SYcpGCwm/9K7O23IIZax9BnyeKrOhDRH
AWS_SECRET_ACCESS_KEY = "SECRET_ACCESS_KEY"
# Add your default region ex: us-east-2
AWS_DEFAULT_REGION = "DEFAULT_REGION"

# Create a new session using the provided credentials
session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_DEFAULT_REGION
)

# Create an STS client using the session
sts_client = session.client('sts')

try:
    # Use the STS client to get caller identity
    response = sts_client.get_caller_identity()

    # Print the caller identity information
    print("AWS credentials are valid!")
    print("Account ID:", response['Account'])
    print("User ID:", response['UserId'])
    print("Arn:", response['Arn'])

except Exception as e:
    # Handle any errors that occur during the verification
    print("Error: AWS credentials are not valid.")
    print("Error Details:", str(e))