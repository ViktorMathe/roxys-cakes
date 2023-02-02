# **Roxy's Cakes** 

I built this website for my wife's little business what she used to have. Roxy's Cakes is a very easy to use website with bag, payment, reviews and contact features. You can browse from different categories of cakes and add them to the bag where you can process forward to the checkout page.

[You can try it here on the live website!]()

![Home page]()

## _**Contents**_

* [User Stories](#user-stories)

* [Features](#features)
    * [Future ideas](#future-ideas)
    * [Bag](#bag)
    * [Payment system](#payment-system)
    * [Reviews](#reviews)
    * [Contact us](#contact-us)

* [Design](#design)
    * [Colors](#colors)
    * [Font](#font)
    * [Images](#images)
    * [Audio](#audio)

* [Testing](#testing)
    * [W3C Validator](#w3c-validator)
    * [CSS Validator](#css-validator)
    * [Lighthouse](#lighthouse)
    * [SEO](#seo)
    * [Manual testing](#manual-testing)
    * [Solved bugs](#solved-bugs)

* [Technology Used](#technology-used)

* [Deployment](#deployment)

* [Credits](#credits)


## _**User Stories**_

* I uploaded my User Stories on to my workspace you can find the PDF file [here](./media/readme/user_story/Roxy's%20Cakes%20User%20Stories%20-%20Sheet1.pdf)
 
* You can find the agile method to my user stories on my github repo just click [here](https://github.com/users/ViktorMathe/projects/5/views/1)

## _**Features**_

* 

* 

* 
 
 ### _Future ideas:_
 * 

## _**Design**_

  * ### _Colors:_
    * 

  * ### _Font:_
    * 
 
  * ### _Images:_
    * 


## _**Testing**_

* ### _W3C Validator:_
    * 

* ### _CSS Validator:_
    * 

* ### _Lighthouse:_
    * I done the lighthouse check through an incognito because that is when I got back the true result which were the following:

    ![Image about the lighthouse results]()


* ### _Manual testing:_

    #### **Register New Account**

    * Expected: As a User I want to able to register to the website to book my cleaning 
    * Test: Create new account with username, create new account with already existing username, create new account with and without email address.  
    * Outcome: If the new account has a username the account is created, if an email address is entered or not. When trying to create a new account with an existing username, the user is encouraged to choose a different username since it already exists. When the account is registered the user is logged in and is notified by an alert. 

    #### Login

    * Expected: As a registered site user you should be able to log in to your accout to be able to interact with the site.
    * Test: Check Login functionality as registered user. 
    * Outcome: When entering valid login details the user is logged in and redirected to the home page and an alert notifies the user that they are logged in. 

    #### Logout

    * Expected: As a registered and logged in user you should be able to log out of the site. 
    * Test: Check Logout functionality as logged in user. 
    * Result: When clicking Logout the user is redirected to Logout page and asked to confirm that they are want to log out. When Log Out button is clicked the user is logged out and redirected to home page and an alert notifies the user that they are logged out.  

    #### **Testing as a User**


    ##### Add a Review

    * Expected : The user can write a review and can upload a picture if wish, and can view it on the review page.
    * Test: Write a review as a user and upload a picture.
    * Outcome: When the review has been wrote I get the notification and it appeared on the review page with or without picture.

    ##### Edit a Review

    * Expected : The user can edit a review and can upload or delete picture if wish, and get a notification when it is done.
    * Test: Edit a review as a user and deleted a picture.
    * Outcome: When the review has been edited I get the notification and it appeared on the review page without picture.

    ##### Delete a Review

    * Expected : The user can delete a review.
    * Test: Delete a review as a user.
    * Outcome: When the review has been deleted I get the notification and it disappeard from the review page.
    
    #### **Testing as a SuperUser**

    ##### Edit Review

    * Expected: The superuser can edit all the reviews do not matter who wrote it.
    * Test: Edit a review.
    * Outcome: The review has been edited and still on the review page.

    ##### Delete Review
    
    * Expected: The superuser is able to delete any review made by anyone.
    * Test: Delete review.
    * Outcome: The review has been deleted from the database and the frontend.

 * ### _Solved bugs_:

    * Bug:
    Solution: 

    * Bug: 
    Solution: 



## _**Technology Used**_
* [Django](https://www.djangoproject.com/ "Django Project website")
    - Django was used to build the models, forms and views of the app, and was the backbone of this project.
* [Bootstrap](https://getbootstrap.com/docs/5.2/getting-started/introduction/ "Bootstrap")
     - Bootstrap was used to implement the responsiveness of the site, using bootstrap classes, but also other styling such as buttons etc.
* [AWS](https://cloudinary.com/ "AWS")
     - Amazon Web Sevices was used as free cloud storage for images uploaded to the site through the cake,review and contact us forms.
* [Stripe](https://stripe.com/en-gb "Stripe website")
     - Stripe features was used to allow to use card payments online.
* [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/ "Crispy Forms documentation")
    - Crispy Forms was used to style the add and edit recipe forms, allowing more than one field to occupy a line on the form.
* [Google Fonts](https://fonts.google.com/ "Google Fonts")
    - Google fonts were used to import the fonts "Lato" into the style.css file. These fonts were used throughout the project.
* [Font Awesome](https://fontawesome.com/ "FontAwesome")
     - Font Awesome was used on all pages throughout the website to import icons (e.g. social media icons) for UX purposes.
* [GitPod](https://git-scm.com/ "GitPod")
     - Git was used for version control by utilizing the GitPod terminal to commit to Git and push to GitHub.
* [GitHub](https://github.com/ "Link to GitHub")
     - GitHub was used to store the project after pushing
* [ElephantSQL](https://www.elephantsql.com/ "ElephantSQL Database")
    - ElephantSQL was used to the new database instead of the Heroku's Postgres
* [Google Maps API](https://developers.google.com/maps/documentation/javascript/marker-clustering/ "Google Maps API")
 -  Google Maps API was used to make the map visible on the site with the marker on it.

## _**Deployment**_

* Create the Heroku App:
    - Select "Create new app" in Heroku.
    - Choose a name for your app and select the location.

* Connect GitHub repo:
    - On the deploy tab you choose the deployment method GitHub
    - You type your GitHub repo name to connect with Heroku
    - Click Connect

* Attach the ElephantSQL database (instead of Postgre on Heroku):  
    - Login to the ElephantSQL website
    - Create New Instance
    - Have to give a name to the plan and had to choose the Tiny Turtle plan which is free
    - Select the region, and data center near your location
    - Click Review and Create Instance
    - Return to the dashboard and click on the instance name and copy the ElephantSQL database URL
    - On the Heroku website go to the settings, reveal config vars
    - Add a new config var called DATABASE_URL and paste your ElephantSQL database url and click Add
    - The database has been added


* Prepare the environment and settings.py file:
    - In the Settings tab, click on Reveal Config Vars and copy the url next to DATABASE_URL.
    - In your GitPod workspace, create an env.py file in the main directory. 
    - Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file.
    - Add the SECRET_KEY value to the Config Vars in Heroku.
    - Update the settings.py file to import the env file and add the SECRETKEY and DATABASE_URL file paths.
    - Update the Config Vars with the AWS url, adding into the settings.py file also.
    - In settings.py add the following sections:
        - Had to the add the followings to the INSTALLED_APPS list:
            - allauth ( for the register/login)
            - crispy forms
            - storages (for the AWS storage)
        - MESSAGE_TAGS ( to get the pop up messages if some action happened)
        - AWS, DATABASE
            - AWS_S3_OBJECT_PARAMETERS (for AWS cache control)
            - AWS_STORAGE_BUCKET_NAME (for to use the AWS)
            - AWS_S3_REGION_NAME
            - AWS_ACCESS_KEY_ID
            - AWS_SECRET_ACCESS_KEY
            - AWS_S3_CUSTOM_DOMAIN
            - STATICFILE_STORAGE
            - STATICFILES_LOCATION
            - DEFAULT_FILE_STORAGE
            - MEDIAFILES_LOCATION
            - MEDIA_URL
            - STATIC_URL
        - STRIPE
            - STRIPE_PUBLIC_KEY
            - STRIPE_SECRET_KEY
            - STRIPE_WH_SECRET
            - STRIPE_CURRENCY
            - DELIVERY_PERCENTAGE
            - FREE_DELIVERY
        - TEMPLATES_DIR
        - Update DIRS in TEMPLATES with TEMPLATES_DIR
        - Update ALLOWED_HOSTS with ['app_name.heroku.com', 'localhost']

* Deployment:
    - On the Heroku website you navigate to the deploy tab
    - You look for the Manual Deploy and choose the "main" branch
    - Click Deploy Branch

* Live website : [Roxy's Cakes]()


* ## _**Credits**_

    * The background I found it on the []()

    * I would like to give credit to my mentor, the tutors helped me a lot during this project. I am really aprreciate it.

    * The logo was made by my wife, Roxana Mathe done it with Adobe Photoshop.
