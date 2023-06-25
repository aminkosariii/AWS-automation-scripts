import boto3

def lambda_handler(event , context):
    
    # Initialize the EC2 client
    ec2_client = boto3.client('ec2')
    
    
    # Get a list of all regions
    regions = [region['RegionName']
            for region in ec2_client.describe_regions()['Regions']]

    for region in regions:
            ec2 = boto3.resource('ec2',region_name=region)
            
            print("Region:", region)

    # get running instances     
    running_instances = ec2.instances.filter(
            Filters = [{'Name':'instance-state-name',
                        'Values':['running']}])
    
    # stop running instances
    for instance in running_instances:
            instance.stop()
            print("stopped instances:",instance.id)
            