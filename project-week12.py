# AWS Service List Inventory


# Create a list of services using Python


# The list should be empty initially
aws_services = []


# Populate the list using append or insert
aws_services.append('S3')
aws_services.append('EC2')
aws_services.append('ECS')
aws_services.append('Lambda')
aws_services.append('DynamoDB')


# Print the list and the length of the list
print(aws_services)
print(len(aws_services))


# Remove two specific services from the list by name or by index
del aws_services[1]
del aws_services[3]
print(aws_services)


# Print the new list and the new length of the list
print(aws_services)
print(len(aws_services))