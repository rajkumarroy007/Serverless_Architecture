# Serverless_Architecture

<h1>Automated Instance Management Using AWS Lambda and Boto3 </h1>
<li>Automate the stopping and starting of EC2 instances based on tags (Rajkumar-Auto-Start & Rajkumar-Auto-Stop)</li>
<li> Create two EC2 instances</li>
<li> Edit the tag with Rajkumar-Auto-Start & Rajkumar-Auto-Stop </li>
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

![2 EC2 instances](https://github.com/user-attachments/assets/55a7f50f-6293-4cd7-8b44-c695c2a4ccd9)
![EC2_instance1 tag name](https://github.com/user-attachments/assets/3be87c66-83ec-465e-822c-3a1ef1ca49af)
![EC2_instance2 tag name](https://github.com/user-attachments/assets/89f1347e-8df5-4222-9909-4023186967e8)
![IAM-Role-rajkumar-Lambda](https://github.com/user-attachments/assets/af10ad77-a1a2-4109-bed8-b9e5b704cdf8)
![Lambda_function_code](https://github.com/user-attachments/assets/3c2d6b62-de2f-4d6c-9606-40fb539c37cb)
![Lambda_function_code_test_result](https://github.com/user-attachments/assets/2f10a0f0-938c-4895-ac74-e2965a2bdde3)
![EC2 dashboard and confirm that the instances' states ](https://github.com/user-attachments/assets/39d7c1df-a97c-40db-b095-b71c66dbf210)


<h1>Restore EC2 Instance from Snapshot </h1>
<li> Create a EC2 instance </li> 
<li> Create a snapshot and AMI </li> 
<li> Create Lambda function with </li> 
<li> Open IAM IAM Dashboard select Roles</li>
<li> To create Role select create role choose AWS service then Lambda  </li>
<li> To update the permission - select Add permissions "AmazonEC2FullAccess" </li>
<li> To create Role "Name, review, and create" give Role name "rajkumar-lambda"  </li>
<li> Now create Lambda function assign with role "rajkumar-lambda"</li>
<li> Select Lambda - create function select Author from scratch</li>
<li> Give myFunctionName choose Runtime pytho 3.11</li>
<li> In Change default execution select "Use a existing role "rajkumar-lambda"</li>
<li> Update the python code as per Github file name "Lambda_function_Restore EC2 Instance from Snapshot.py" </li> 
<li>Update the parameter as per comments </li> 
<li> Kindly refer the below screenshot for more details </li> 

![Lambda_test_result](https://github.com/user-attachments/assets/2639a992-cb4c-4ede-a346-23597ca94deb)

![Instance_creating from snapshot_i-086fa169c0963e4f4](https://github.com/user-attachments/assets/37aa7263-d17d-4251-8837-6c1100a557b7)


![Restore_EC2_from Snapshot](https://github.com/user-attachments/assets/d28471bf-8e12-4d82-a3bd-f74284e738ed)

![Lambda_function_EC2Accessrole](https://github.com/user-attachments/assets/7bfd7b17-50da-4953-8943-38de0a49221b)





<li> </li> 
<li> </li> 
<li> </li> 
<li> </li> 
<li> </li> 
<li> </li> 
<li> </li> 
<li> </li> 
<li> </li> 
<li> </li> 
