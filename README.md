- CloudFormation

Files:
- KGDevOpsInterview.json (main template for instance and alb)
- SQSKGDevOpsInterview.json (template for the sqs queue)
VPCs, Subnets with auto public IP enabled, security group with ports 80 and 22 opened and test.pm key created perviously.
I have been checking why the load balancer check throws a 403 and realised that it is because there were no index.html file in /var/www/httml/. I tested this part after doing the Chef part for time and money consuming
Ids of subnets, security grupos, vpcs, etc were added manually. A best practice - future thing will be to add them as variables or even better create them in the template but I didn´t want to add stuff not required 

- Chef

test.rb file created with all the exercises. I have had to read and search for chef recipes. 

- Scripting

It should be run as 
- python3 beers.py 6

- General

I have done all bonus points, so I am sending the files which match all the requirements, not sending a file for each requirement
