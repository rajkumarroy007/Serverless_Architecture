# Serverless_Architecture

<h1>Automated Instance Management Using AWS Lambda and Boto3 </h1>h1>
<li>Automate the stopping and starting of EC2 instances based on tags</li>
<li> Create two EC2 instances</li>
<li> Edit the tag with  </li>
<li> Go to instance Tags tabs and manage tags </li>
<li> Update Key with with Name and Value with Rajkumar-Auto-Start on first EC2 instance  </li>
<li> Update Key with with Name and Value with Rajkumar-Auto-Stop on Second EC2 instance </li>
<li> Open IAM IAM Dashboard select Roles</li>
<li> To create Role select create role choose AWS service then Lambda  </li>
<li> To update the permission - select Add permissions "AmazonEC2FullAccess" </li>
<li> To create Role "Name, review, and create" give Role name "rajkumar-lambda"  </li>
<li> Now create Lambda function assign with role "rajkumar-lambda"</li>
<li> Select Lambda - create function select Author from scratch</li>
<li> Give myFunctionName choose Runtime pytho 3.11</li>
<li> In Change default execution select "Use a existing role "rajkumar-lambda"</li>
<li> In code tab in Lambda function upload "EC2-Stop-Start-Tag-Lambda and Boto3.zip" from github  </li>
<li>Click on Deloy for deploying Lambda function to trigger click on test </li>
<li> Refer below screenshot for more details</li>
<li> </li>






Serverless Architecture AWS Lambda Boto3 SNS
