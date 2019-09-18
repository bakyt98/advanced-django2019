# Django

## How to test project
First, download all apps from [requirements.txt](requirements.txt)
Then do a migration of the model
```bash
python manage.py makemigrations
python manage.py migrate
```
After that you can test the project writing next code:
```bash 
python manage.py runserver
```

## How to test postman's collection?
You can change authorization token in headers putting tick, and check taking and posting articles. Also there in the url writing number of certain article you can delete and partially update or fully (don't forget write new data in body).



## Task:

Using Django, create a simple API that allows users to post and retrieve their reviews.

Acceptance Criteria

The completed assignment must be hosted in a git repository
The repository must include commit history (e.g., more than one commit)
Users are able to submit reviews to the API
Users are able to retrieve reviews that they submitted
Users cannot see reviews submitted by other users
Use of the API requires a unique auth token for each user
Submitted reviews must include, at least, the following attributes:
Rating - must be between 1 - 5
Title - no more than 64 chars
Summary - no more than 10k chars
IP Address - IP of the review submitter
Submission date - the date the review was submitted
Company - information about the company for which the review was submitted, can be simple text (e.g., name, company id, etc.) or a separate model altogether
Reviewer Metadata - information about the reviewer, can be simple text (e.g., name, email, reviewer id, etc.) or a separate model altogether
Unit tests must be included providing 100% code coverage
Include instructions on local setup details for both "app setup" and "data setup"
Document the API

Optional: 

Provide an authenticated admin view that allows me to view review submissions

Organize the schema and data models in whatever manner you think makes the most sense and feel free to add any additional style and flair to the project that you'd like.

