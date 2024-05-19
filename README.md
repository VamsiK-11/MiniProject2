#MiniProject2

***OVERVIEW OF THE PROJECT***
-Basically the motive of this project is to test a demo website by logging in and adding a contact later provide a test results.
-To Achieve this i have integrated Git and Selenium with Jenkins to obtain a continuous integration(CI).
-Selenium is automated test tool which requires a web driver as an intermediate to test things up.



***STEPS INVOLVED***
1) Install necessary libraries like selenium and image in python.
2) Download any webdriver which is equivalent to your version of specific web browser, I am choosing chrome webdriver for this project and make sure to copy the path of chromedriver.exe file.
3) Create file name as script.py and push it into your newly created repository , make sure that you push into master branch to avoid unnecessary conflicts.
4) Login to your Jenkins account and there install two plugins one is Git plugin as well as Selenium plugin.
5) Create a freestyle project and give any name to it , In SCM(Source Code Management) you choose Git and provide neccesary details like repo link as well as credentials so that Jenkins can pull your code directly.
6) Scroll down and click on build step, choose Windows batch comman since I am using windows os. To execute the python file just type python script.py (In mine i have given the path of my python.exe file since in my local system the environment variable is not setted up properly).
7) Click on save and apply , proceed to build the project.
8) After the execution of the project, head towards the console output and copy the path and paste in local system to see the test results.
