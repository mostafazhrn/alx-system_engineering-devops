This is a readme file for the task 0x19-postmortem as part of the alx software engineering program

                    Postmortem
-Server out of service incident report-
-Summary of the issue-
On 10th of April, 2024 at 18:28 GMT after doing some updates on the webserver one of the engineers figured out that the apache server running is giving 500 internal server error and the server is completely out of service. We discovered that the problem is affecting 100 % of the users and it rendered the server out of service. The cause of the problem was a typo in configuration file of wordpress.
Timeline (GMT)
18:25: Push updates to the server
18:28: Discovery of the problem
18:29: Started working on the problem (debugging and running some tests)
19:00: Figured out the problem , then fix it and tested again 
19:10 Everything is back to normal again the server is up and running

The root cause of the problem
A typo in the word press configuration file which caused the server to run 500 error internal server error. The issue rendered the server out of service and was not able to display any content. 
The issue was discovered by a mere chance by one of the engineers working on the project. We were lucky to discover it on a very small period of time. The main cause was due to typo in the wp-setting.php this typo caused the apache server to stop rendering content resulting in the 500 error (internal server error). This rendered the whole server out of service.
Resolution
After noticing the problem, we immediately were locked on it, it seems like the issue was coming unexpectedly as everything was running fine. We did not make any crucial changes. 
But the error seemed like we are missing a crucial aspect of the problem. we started debugging by using the strace debugging tool we ran a CURL command to the local server it gave the 500 error (internal server error) which didn’t give me a lot of insight of what was happening. 
we used the following command <strace curl 127.0.0.1> to put our hands on the issue. Then we started inspecting the output carefully. After reviewing the output we noticed that there is a problem with wp-settings.php (word press) so we looked into the configuration file and found the typo ,phpp instead of .php. therefore the solution was to fix the typo in hand , to do so I used the command sed –i to replace the typo with the right word(.php).

Corrective and Preventative measures
-	After this incident we decided to have a mock server to deploy any changes to it before pushing the changes to a live server.
-	Develop a faster mechanism to deploy a backup version of the server to the nearest stable point so that if any outage happen we can deploy the backup copy until we discover and fix the issue.
-	Develop a better mechanism to discover bugs and errors like a monitoring tool (e.g. datadog) 
