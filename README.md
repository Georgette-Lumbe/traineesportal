# Trainees Portal

<img src="" width="">

The live website can be viewed [here](#)

# Table of contents
1. [Introduction](#introduction)
2. [UX](#UX)
    * [User Stories](#User-Stories)
    * [Development Planes](#development-planes)
        * [Strategy](#Strategy)
         * [Skeleton](#Skeleton)
            * [Wireframes](#Wireframes)
            * [Database Schema](#Database-Schema)
        * [Structure](#Structure)
            * [Existing Features](#Existing-Features) 
                * [Features on all pages](#Features-on-all-pages)
                * [Home Page Features](#Home-Page-Features)
                * [Login Page Features](#Login-Page-Features)
                * [Register Page Features](#Sign-Up-Page-Features)
                * [Profile Page Features](#Profile-Page-Features)
                * [Log Out Features](#Log-Out-Features)
                * [Features exclusive to Admin](#Features-exclusive-to-Admin)
    * [Design](#Design)
        *  [Colors](#Colors)
        * [Typography](#Imagery)
        * [Imagery](#Imagery)
3. [Features Left To Implement](Feature-Left-To-Implement)
4. [Technolgies Used](#Technologies-Used)        
5. [Testing](#Testing)
6. [Issues and bugs](#issues-and-bugs)
7. [Deployment](#Deployment)
    * [Deployment Steps](#Deployment-Steps) 
    * [Making a clone to run locally](#Making-a-clone-to-run-locally)
    * [How to Fork the respository](#How-to-Fork-the-Respository)
8. [Credits](#Credits)
    * [Media](#Media)
    * [Content](#Content)
    * [Code](#Code)
9. [Acknowledgements](#Acknowledgements)

---

# INTRODUCTION

Trainee Portal is a site that facilitate all trainees to be more organised with all tasks they should have on their internship. Since during an internship, trainees very often have several notes to take about work operations, daily tasks to do as well as assignments to test their knowledge. On this, in Trainee Portal, trainees can write down all their notes, tasks and assignments which are well kept and protected. They will be able to update them whenever they want, as well as delete them once the task or assignment is finished. 

Trainee Portal also has some blog posts, which are beneficial to the trainees before, during and even after their work placement. Since these blog posts teach them to work on their mindset, their relationship during the internship, some tips on how to behave and many more. On these blog posts, trainees can read and leave comments.

Trainees must first sign up or register in order to create their information, to comment, and also to view their profile with all due assignments and tasks.

There are many other site features which will be discussed in depth later on in this document.

This is the fourth of five milestone projects that the developer is required to complete as part of their full web development course at the Code Institute.


# UX

## Development Planes

### Strategy

**The Ideal User of this site:**

* is someone who wants to start a work placement
* is someone who wants to start a traineeship
* is someone who has just started a traineeship or work placement

### Skeleton

#### Wireframes

Wireframes were created using [Balsamiq wireframes](https://balsamiq.com/)

The wireframe mockup links can be found below:

* [Home Page]()

* [Profile Page]()

* [Login Page]()

* [Logout Page]()

* [Notes Page]()

* [Assignments Page]()

* [Tasks list Page]()

* [Post 1 Page]()

* [Post 2 Page]()

* [Post 3 Page]()

#### Database Schema

<img src="" width="">

### Structure

#### Existing Features

# Features Left To Implement

# Technolgies Used

# Testing

Testing information can be found in a separate [testing file]().

# Issues and bugs

The developper met some issues during the development of the website, below are the issues, bugs and solutions that the developer has encountered:

1. Git push Issue

    * The developer met an error while trying to push commit changes to github.
    <img src="" width="">

    * To achieve this, the developer consulted the Code Institute Tutor Support. The problem was that the developer pushed a commit changes directly to github and gitpod breaks.

    * The developer did these steps to fix the problem:

    `git add`
    `git remote -v`
    `git log`
    `git status`
    `git log`
    `git add` `git commit -m " any message`
    and `git push origin main --force`

2. Django admin

    * The django admin was working perfectlt but without any style
    <img src="" width="">

    * The developer consulted the Code Institute Tutor Support, to achieve this. The problem was that DEBUG was equal to True in settings.py file. To resolve it, the developer put DEBUG = FALSE and remove DISABLE_COLLECTSTATIC to Heroku settings.

3. Server Error 500:

    * The developer met a lot of times the Server Error 500, the problem was in the views.py code

4. Page not found

    * Profile : the page profile was not working. After many attempts, the developer noticed that the problem was in the urls.py, it was missing a `slash` after profile.

    * Post_details : the post_details was not showing up after the developer create views, connect to the template and get urls. In order to understand and resolve this problem, the developer consulted the Code Institute Tutor Support. The main problem was that the blogs that was showing on the index page awas placeholders, they was not coming from database.  They should normally need to come from database in order to show them and link to the correct id for the url.

    The developer did these following steps to get that sorted:
    * Get all the blog posts from the database
    * Create a context dictionnaries
    * Inside the context dict, create a key:value pair: key is posts, value is the posts got from database
    * Add context into the render: render(request, template, context)
    Then in the post_details TEMPLATE:
    * loop through the list: for post in posts
    * get all fields for each post with post.fieldname
    * update the url to use post.id

5. Update Information

    * 

6. Unfixed Issue

    * Likes: The developer had issues to permit user to like and unlike. So, the developer decide to remove this option and just leave the comment option.

7. Request 

    * There was a error message about request: Unused argument 'request'.
    * The developer visited this [post](https://github.com/PyCQA/pylint-django/issues/155)
    * To this problem, the developer write an `underscore` before request.

# Deployment

This project was developed using [Gitpod IDE](https://gitpod.io) and pushed to Github using the in-built terminal. However, because Github can only host static websites it was necessary to deploy this project to Heroku because it is a compatible hosting platform for a back-end focused site like Trainees Portal.

This project was deployed using Heroku and stored in GitHub.

## Repository Creation

1. Navigate to [Github](https://github.com/).
2. Create a new repository by first clicking the green button labeled new on the top left of the screen.
3. Select the [Code Institute Full Template](https://github.com/Code-Institute-Org/gitpod-full-template) in the templates section.
4. Give the repository a name, in this case Trainees Portal.
5. Click the green 'Create Repository' button at the bottom of the page.
6. Inside the repository click the green 'gitpod' button to initialize your repository.
8. Future access to this workspace must be gained through gitpod workspaces, clicking the green button in gitpod again 
will initialize a new workspace.
9. Use the `git add .` command to add all modified and new files to the staging area.
10. Use the `git commit -m` command to commit a change to the local repository.
11. Use the `git push` command to push all committed changes to github.   

Before deploying the website to Heroku, the following five must be followed to allow the app to work in Heroku:

1.  Install `django-gunicorn`, `psycopg2` and `dj_database_url`, `cloudinary` in your workspace cli.

2. Create requirements.txt file that contains the names of packages being used in Python. It is important to update this file if other packages or modules are installed during project development by using the following command:

    - pip freeze --local > requirements.txt

3. Create Procfile that contains the name of the application file so that Heroku knows what to run. If the Procfile has a blank line when it is created remove this as this may cause problems.

4. Create env.py that conrtains all secret variables as DATABASE_URL, SECRET_KEY and CLOUDINARY_URL, this file is hidden.

5. Push these files to GitHub.

## Deployment Steps

Once the above steps are done, the website can be deployed in Heroku using the steps listed below:

1. Log into Heroku .
2. Click the New button.
3. Click the option to create a new app.
4. Enter the app name in lowercase letters.
5. Select the correct geographical region.
6. Click to create

## Add Heroku Postgres Database
1. Click the resources tab in heroku.
2. Under Add-ons search for heroku postgres.
3. Click on heroku postgres when it appears. 
4. Select the Hobby Dev-Free option in plans. 
5. Click submit order form.

## Setting up environment variables
1. In the heroku settings click the reveal config vars button and set the following variables:
    - DATABASE_URL
    - SECRET_KEY
    - CLOUDINARY_URL
    - DISABLE_COLLECTSTATIC (This variable was removed, see more in [Issues and bugs](#issues-and-bugs))
   
    The values of these variables are secret and for security purposes will not be shared here. 

## Connect Heroku app to Github repository

1. In heroku select the deploy tab.
2. Click github button.
3. Enter the repository name and click search.
4. Select the relevant repository and click connect
5. Select Main branch
6. Click on deploy branch 

## Enable automatic deployment:

1. Click the Deploy tab
2. In the Automatic deploys section, the main branch is enabled to deploy then click Enable Automation Deploys.

## Making a clone to run locally

It is important to note that this project will not run locally unless an env.py file has been set up by the user which contains the DATABASE_URL, SECRET_KEY and CLOUDINARY_URL which have all been kept secret in keeping with best security practices. 

1. Log into GitHub.
2. Select the [respository](https://github.com/Georgette-Lumbe/traineesportal).
3. Click the Code dropdown button next to the green Gitpod button.
4. Download ZIP file and unpackage locally and open with IDE. Alternatively copy the URL in the HTTPS box.
5. Open the alternative editor and terminal window.
6. Type 'git clone' and paste the copied URL.
7. Press Enter. A local clone will be created.

Once the project been loaded into the IDE it is necessary to install the necessary requirements which can be done by typing the following command.

    -pip install -r requirements.txt

## How to Fork the respository.

1. Log into GitHub.
2. In Github go to the [respository](https://github.com/Georgette-Lumbe/traineesportal).
3. In the top right hand corner click "Fork".

---





# Languages used

# Credits

# Acknowledgements


