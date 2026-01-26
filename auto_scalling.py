#Elastic Compute Cloud (EC2):
import boto3

# Launch an EC2 instance
ec2 = boto3.client('ec2')
ec2.run_instances(ImageId="ami-abc123", InstanceType="t2.micro")
#Elastic Block Store (EBS): Persistent block storage volumes that can be attached to EC2 instances. Enables attaching data drives.


# Create and attach an EBS volume
ec2.create_volume(Size=50, AvailabilityZone='us-east-1a') 
ec2.attach_volume(VolumeId='vol-123abc', InstanceId='i-abc456')


# Auto Scaling: Service to automatically launch or terminate EC2 instances based on metrics like CPU utilization to maintain application availability.

# Elastic Load Balancing: Service to distribute application traffic across multiple targets like EC2 instances in multiple availability zones to improve fault tolerance.

# Amazon Machine Image (AMI): Preconfigured virtual machine image used to launch EC2 instances. Determines software configuration.
# Launch instance from custom AMI 
ec2.run_instances(ImageId='ami-custom123', InstanceType='t2.micro')

