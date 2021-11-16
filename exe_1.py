import boto3

def get_instances():
  client = boto3.client('ec2')
  reservations = client.describe_instances()["Reservations"]
  for reservation in reservations:
    for each in reservation["Instances"]:
      print " instance-id: {}, instance-name: {}, instatnce-state  {}".format(each["InstanceId"], each["KeyName"], each[""]["Name"])

      
def reboot_machine(id):
  client = boto3.client('ec2')
  response = client.reboot_instances (InstanceIds=[id])
  print (response)

def start_or_stop_machine(id):
  client = boto3.client('ec2')
  instance = client.describe_instances_status(InstanceIds=[id])
  code = instance["InstanceState"]["Code"]
  
  if code == 32:
    response = client.start_instances(InstanceIds=[id])
    print(response)
  elif code == 80 or code == 48:
    response = client.stop_instances(InstanceIds=[id])
    print(response)
  else:
    print("Machine is neither started nor stopped")


    
   
