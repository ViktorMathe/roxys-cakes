# **Roxy's Cakes** 

I built this website for my wife's little business what she used to have. Roxy's Cakes is has been made to anybody who likes little treats or would like to surprise a relative or friend on any occasions. The customer can subscribe to the newsletter where they can get information about any new cakes which becomes available or any deals for example now the shop offer free delivery if they spend over £30. Anybody can find the shop on the [Facebook](https://www.facebook.com/people/Roxys-Cakes/100090725342238/) as well (which might not be available due to the inactivity as this is just an educational site and the Facebook is remove it, in that case you can find a screenshot below). The customer can browse from different cakes and add them to the bag where you can process forward to the checkout page.

[You can try it here on the live website!](https://roxys-cakes-vm.herokuapp.com/)

<img src="./media/readme/images/home_page.png" width="800" height="400">

## _**Contents**_

* [User Stories](#user-stories)

* [Features](#features)
    * [Database](#database)
    * [Navbar](#navbar)
    * [Cakes](#cakes)
    * [Bag](#bag)
    * [Payment system](#payment-system)
    * [Reviews](#reviews)
    * [Contact us](#contact-us)
    * [Newsletter](#newsletter)
    * [Facebook Shop](#facebook-shop)
    * [Future ideas](#future-ideas)

* [Design](#design)
    * [Wireframe](#wireframe)
    * [Colours](#colours)
    * [Font](#font)
    * [Images](#images)

* [Testing](#testing)
    * [W3C Validator](#w3c-validator)
    * [CSS Validator](#css-validator)
    * [PEP8 Validator](#pep8-validator)
    * [Lighthouse](#lighthouse)
    * [SEO](#seo)
    * [Manual testing](#manual-testing)
    * [Solved bugs](#solved-bugs)

* [Technology Used](#technology-used)

* [Deployment](#deployment)

* [Credits](#credits)


## _**User Stories**_

* I uploaded my User Stories on to my workspace you can find the PDF file [here](./media/readme/user_story/Roxy's%20Cakes%20User%20Stories%20-%20Sheet1.pdf)
 
* You can find the agile method to my user stories on my github repo just click [here](https://github.com/users/ViktorMathe/projects/6)

## _**Features**_

 ### _Database:_

 * I made a database scheme with LucidChart. 

    <img src="./media/readme/images/db_schema.png" width="600" height="500">

 ### _Navbar:_
 
 * I made the navbar to easy to read and navigate on the whole website. If you are on desktop tablet or mobile.
 ![Navbar](./media/readme/images/navbar.png)

   <img src="./media/readme/images/mobile_navbar.png" width="400" height="250">


 ### _Cakes:_

 * If you click to enter the shop or the cakes menu on the navbar it takes you to all the cakes where you can choose to add the cakes to the bag or you would like to have more details about the product. The details menu shows you what ingredients they have in the cake and you can choose how many cakes would you like to add to the bag.

  <img src="./media/readme/images/cakes.png" width="400" height="250"> <img src="./media/readme/images/cake_details.png" width="320" height="450">


 ### _Bag:_
 
 * You can access to the bag by click on the icon which will contains all the items what you have put it in there. You can change the quantity with the provided form and it will update the price the subtotal and calculate it how much more do you need to spend for get a free delivery. From the bag you can proceed to the checkout page.

    <img src="./media/readme/images/bag.png" width="800" height="400">

 ### _Payment System:_

 * On the checkout page you have to provide all the details what they ask for, if you are logged in and already used the shop once or created a profile the website fill out the form with some information so you do not have to fill out the same things again. You can see how much is the total what you have to pay. **PLEASE DO NOT PROVIDE REAL BANK CARD DETAILS!!**  If you wish to try out the payment system used the Stripe own testing card:
    * Card Number : 4242424242424242	
    * CVV: Any 3 digits	
    * Expiry Date: Any future date

     When the payment is complete the user get an email with the order details to the provided email address.

     <img src="./media/readme/images/checkout.png" width="270" height="450">
     <img src="./media/readme/images/profile.png" width="350" height="450">

 ### _Reviews:_

 * Any user can leave a review about the shop and if they wish, image can be uploaded as well. The reviews can be edited or deleted by the person who wrote them or can be done by a superuser.

    <img src="./media/readme/images/reviews.png" width="850" height="350">

 ### _Contact us:_
 
 *  The user can fill out the form to contact the webshop. They have to provide an email address and if they would like can add the phone number as well. The form can be answered by a superuser and send an email to the receipent.

    <img src="./media/readme/images/contact_us.png" width="850" height="300">

 ### _Newsletter:_

 * Anybody can subscribe for a newsletter on the home page with their email address then they got a confirmation email. The superuser can write a newsletter for all of the subscribers and send out real emails with a unique link which is provide the option to unsubscribe.

    <img src="./media/readme/images/subscribe.png" width="800" height="200">
    <img src="./media/readme/images/newsletter.png" width="800" height="500">


 ### _Facebook shop:_

 * I created a page on the Facebook with some information and action buttons to advertise the website so it can reach more people. If the link above in the description is not working anymore I took a screenshot about the page.

   <img src="./media/readme/images/facebook.png" width="320" height="450">
    
 
 ### _Future ideas:_
 
 * I would like to implement login via social platforms. 
 * Make searching option for different categories.

## _**Design**_

 * ### _Wireframe:_
  * I made wireframes on the [wireframe.cc](https://wireframe.cc/) what you can have a look on this [link](./media/readme/wireframe/wireframe.md)

  * ### _Colours:_
    * The main colour theme is dark. The navigation bar and the footer are pure black with rose gold icons on it and light silver text.
        * Background colour: #212121
        * Text/Icon colour: #ce9988
        * Edit button colour: #65c1fb
        * Delete button colour: #ff8a8a
        * Silver text colour: #a2a2a3
    * All colours has been checked for good contrast ratio on the [Accessible WEB website](https://accessibleweb.com/color-contrast-checker/)!

  * ### _Font:_
    * I used a Lato google font for the whole website as it is nice and decorative for the theme.
 
  * ### _Images:_
    * All the images about the cakes are made by my wife, Roxana Mathe. The background and the logo is created by her as well.


## _**Testing**_

* ### _W3C Validator:_
    * I got back the following message : Document checking completed. No errors or warnings to show. from the official [W3C Website](https://validator.w3.org/nu/?doc=https%3A%2F%2Froxys-cakes-vm.herokuapp.com%2F)

    ![Image about the W3C Validator](./media/readme/images/html_validator.png)

* ### _CSS Validator:_
    * I got back the following message: Sorry! We found the following errors (17) URI : https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css from the Jigsaw Validator which is bootstrap fault. My own CSS has no Error!
    ![Image about the Jigsaw validator](./media/readme/images/css_validator.png)

* ### _Lighthouse:_
    * I done the lighthouse check through an incognito because that is when I got back the true result which were the following:

    ![Image about the lighthouse results](./media/readme/images/lighthouse_check.png)


* ### _Manual testing:_

    * You can read about all the manual testing if you click on the link:

        [Manual testing](./media/readme/manual_testing/manual_testing.md)

 * ### _Solved bugs_:

    * Bug: My media files was not loading.
    Solution: I forget to add the +static to the end of the main urls.py file

    * Bug: On the deployed site I could not render the logo and favico images.
    Solution: I missed a dash from the image source field.

    * Bug: I could not handle the webhooks. Keep getting error 401.
    Solution: The tutors help me find that I forget to change the secret key on the gitpod website and instead of the .env file it was pulling the key from there.

    * Bug: I could not pre populate only one field to the contact us reply function.
    Solution: The tutors helped me to find out my mistake was with the indent level was at the wrong place. After I put that in the right place with a initial statement



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

* Live website : [Roxy's Cakes](https://roxys-cakes-vm.herokuapp.com/)


* ## _**Credits**_

    * The background was made by Roxana Mathe, she did it with Adobe Photoshop.

    * I would like to give credit to my mentor, the tutors helped me a lot during this project. I am really aprreciate it.

    * The logo was made by my wife, Roxana Mathe done it with Adobe Photoshop.
