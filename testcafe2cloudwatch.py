import json
import boto3


JSON_FILE = './test_result.json'


cloudwatch = boto3.client('cloudwatch')

with open(JSON_FILE) as f:
  data = json.load(f)


testtime = data['endTime']
print("going to push data in {0} tested on {1}".format(JSON_FILE, testtime))

## this creates metrics in cloudwatch with app, environement, fixture, name of test, value of metrics. 
## timestamp of the data point would be the end time of testcafe.
## the script can handle json output containing multiple fixtures and tests.
## TODO: having app and env parameters feeding into the script via parameter or filename of json. 
for f in data['fixtures']:
    fixture_name = f['name']
    for x in f['tests']:
        test_name = x['name']
        elapsed = x['durationMs']
        print("pushing test result of (fixture-test) :{0}-{1} , elapsed time ={2} ".format(fixture_name, test_name, elapsed))
        cloudwatch.put_metric_data(
            MetricData=[
                {
                    'MetricName': 'ElaspedTime',
                    "Timestamp": testtime,
                    'Dimensions': [
                        {
                            'Name': 'App',
                            'Value': 'ABC'  # should be passed in as parameters/included in fixture or other meta
                        },
                        {
                            'Name': 'Env',
                            'Value': 'SIT' # should be passed in as parameters/included in fixture or other meta
                        },
                        {
                            'Name': 'Fixture',
                            'Value':  fixture_name
                        },
                        {
                            'Name': 'Test_name',
                            'Value':  test_name
                        }
                    ],
                    'Unit': 'Milliseconds',
                    'Value': elapsed,
                },
            ],
            Namespace='UI-Test'
            )
    