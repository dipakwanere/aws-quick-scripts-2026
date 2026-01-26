# Detecting data drift
from sklearn.metrics import accuracy_score

# Detect data drift  
prod_accuracy = accuracy_score(y_true, y_pred) 
if prod_accuracy < threshold:
    print('Data drift detected. Retrain model.')



## policy 
import boto3

# Allow S3 access only
policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": "*"
        }
    ]
}

iam.put_role_policy(RoleName='app-role', PolicyName='s3', PolicyDocument=json.dumps(policy))
