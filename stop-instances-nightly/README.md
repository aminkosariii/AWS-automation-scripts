Lambda Function



Create 2 cloudwatch rule -> for start and stop instances

Lambda function timeout high enough (i.e. 1 minute) so that it can iterate through every instance in every region.

CloudWatch Event Rule
Cron expression: 0 23 ? * MON-FRI *
