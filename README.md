# Mateo - Elipsis Tech Series

## Setup
### Backend
1. Prepare Node.js (14), Python (3.7), Docker Engine, Local [AWS Credentials](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html)

2. Install Serverless framework
```
cd Mateo/backend/
npm ci
```

3. Prepare the secret keys in AWS
  - Go to AWS Secrets Manager
  - Fill `dev/plaid/key`: Plaid private API key
  - Fill `dev/mateo/plaid/token`: Access token of Mateo organization Plaid access token
  - Fill `dev/mateo/plaid/acc`: Account ID of Mateo organization Plaid account

4. Setup databases
```
cd Mateo/backend/Database
./deploy_db.sh

```

5. Setup Cognito User Pool
```
cd Mateo/backend/cognito-setup
sls deploy --stage dev
```

6. Setup microservices
```
cd Mateo/backend/user-microservice
sls deploy --stage dev

cd Mateo/backend/loan-pool
sls deploy --stage dev
```
