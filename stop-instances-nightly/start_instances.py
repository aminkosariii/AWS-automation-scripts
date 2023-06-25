import boto3

def lambda_handler(event , context):
    
    ec2_client = boto3.client('ec2')
    
    # get all regions
    regions = [region['RegionName']
            for region in ec2_client.describe_regions()['Regions']]

    for region in regions:
            ec2 = boto3.resource('ec2',region_name = region)
            
            print("Region:", region)

# get list of all stopped instances
    stopped_instances = ec2.instances.filter(
            Filters = [{'Name':'instance-state-name',
                        'Values':['stopped']}])
    
    # start stopped instances
    for instance in stopped_instances:
            instance.start()
            print("started instances:",instance.id)
            
            
