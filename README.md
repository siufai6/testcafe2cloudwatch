# testcafe2cloudwatch
Simple python script to upload testcafe json output to cloudwatch.  If you have a regular job (jenkins, crontab) that runs testcafe scripts, 
the outputs can be fed into cloudwatch and you can  monitor  the performance of application overtime.  It would be useful for development teams to watch out 
for bad peformance after a certain checkin if tests are run regularly. 

Requires: boto3, json

This script:
- opens a testcafe json file and parse
- loop thru fixtures and tests and construct metrics with Application name, environment, Fixture, name of test and value, where value is the time taken to finish the test.
- this script assumes the credential is setup with proper IAM and access rights to write to cloudwatch, refer to AWS documentation.
- after feeding the data into cloudwatch, you can now see the metrics in cloudwatch (custom metrics).
