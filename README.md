# Week 21 homework
 This repository holds my week21  homework assignment.
 
## Week21 Homework Assignment Question 1
#### Create a basic API in Azure (as we did in class) that tells you how to access the different endpoints when you go to the home page. You should have the following endpoints:
 - A /all endpoint that displays all of the nobel.json data
	* !['Screenshot1'](./Week21_Question1_1.PNG?raw=true "all endpoint")
 - A /<year> GET endpoint that allows for you to pass in any year and shows you the Nobel prizes from that year
    * !['Screenshot2'](./Week21_Question1_2.PNG?raw=true "year endpoint")
 - A /<year> POST endpoint that lets you add additional data
     - You can use a form or pass the data in to the API url
     - Make sure you see your updates when you go to /all
        * !['Screenshot3'](./Week21_Question1_3.PNG?raw=true "year POST endpoint")
     - Notice new data at the end
        * !['Screenshot5'](./Week21_Question1_5.PNG?raw=true "year POST endpoint")
 - Home page
    * !['Screenshot4'](./Week21_Question1_4.PNG?raw=true "Home page")

## Week21 Homework Assignment Question 2
#### Q.2 What kind of API did you build? What types of APIs are there? Why are APIs important?
   - The API that we built for this week's assignment is web service REST API
   - There are four main types of APIs: referred from (https://rapidapi.com/blog/types-of-apis/)
      - Open APIs: Also known as Public API, there are no restrictions to access these types of APIs because they are publicly available.
      - Partner APIs: A developer needs specific rights or licenses in order to access this type of API because they are not available to the public.
      - Internal APIs: Also known as Private APIs, only internal systems expose this type of API. These are usually designed for internal use within a company. The company uses this type of API among the different internal teams to be able to improve its products and services.
      - Composite APIs: This type of API combines different data and service APIs. It is a sequence of tasks that run synchronously as a result of the execution, and not at the request of a task. Its main uses are to speed up the process of execution and improve the performance of the listeners in the web interfaces.
   - API's are interface that enables two applications to exchange data among each other.APIs are beneficial because they allow developers to add specific functionality to an application, without having to write all of the code themselves. APIs also allow developers to access data from other applications.