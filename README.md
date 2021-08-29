# Mateo - Elipsis Tech Series

![image](https://user-images.githubusercontent.com/60478523/131246677-c5fe2469-9731-455b-aa3e-5e0d07d052e5.png)

## About
A staggering 75% of adults in Southeast Asia are found to be either underbanked or unbanked - and that number is 40% even in Singapore, one of the strongest financial centres of the region. This statistic clearly illustrates how current global financial inclusion rates are far from ideal. Therefore, our team has come up with Mateo, a hybrid cross-platform web application that enables the underbanked to receive greater access to financial services, achieving greater global financial literacy and inclusion through technology.

## Architecture
![image](screenshot.md)

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

### Frontend
1. Prepare Node.js (14)

2. Install Quasar
```
npm install -g @quasar/cli
```

3. If using custom backend, replace the endpoints accordingly

4. Run build
```
cd Mateo/frontend/
quasar build
```