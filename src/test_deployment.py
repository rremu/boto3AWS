from src.ec2.vpc import VPC
from src.client_locator import EC2Client

def main():
    #Create a VPC
    ec2_client=EC2Client().get_client()
    vpc=VPC(ec2_client)

    vpc_response = vpc.create_vpc()

    print('VPC Created' + str(vpc_response))

if __name__ == '__main__':
        main()
