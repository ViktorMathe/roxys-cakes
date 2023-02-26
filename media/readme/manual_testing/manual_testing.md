If you would like to go back to the README file click here: 
    [README](/README.md)

#### **Register New Account**

* Expected: As a User I want to able to register to the website. 
* Test: Create new account with username, create new account with already existing username, create new account with or without email address.  
* Outcome: If the new account has a username the account is created, if an email address is entered because it has to be verified. When trying to create a new account with an existing username, the user is encouraged to choose a different username since it already exists. When the account is registered the user is logged in and is notified by an alert. 

#### Login

* Expected: As a registered site user you should be able to log in to your accout to be able to interact with the site.
* Test: Check Login functionality as registered user. 
* Outcome: When entering valid login details the user is logged in and redirected to the home page and an alert notifies the user that they are logged in. 

#### Logout

* Expected: As a registered and logged in user you should be able to log out of the site. 
* Test: Check Logout functionality as logged in user. 
* Result: When clicking Logout the user is redirected to Logout page and asked to confirm that they are want to log out. When Log Out button is clicked the user is logged out and redirected to home page and an alert notifies the user that they are logged out.  


### **Testing as a User**

#### Add Cake to the bag

* Expected : The user can add cake to the bag and can view it on the bag page.
* Test: Added cakes to the bag then checked it on the bag view page.
* Outcome: When the cake has been added I get the notification and it appeared in the bag page with.

#### Change quantity in the bag

* Expected : The user can edit the quantities of the cakes in the bag, and get a notification when it is done and the price/delivery fee is changing.
* Test: Changed the quantity click on update.
* Outcome: When the quantity has been changed I get the notification and the prices/fees are changed.

#### Delete from bag

* Expected : The user can remove a cake from the bag and the price is deducted.
* Test: Remove cake as a user.
* Outcome: When the cake has been removed I get the notification and it disappeard from the bag page and price is changed.

#### Payment system

* Expected : The user can make a payment with their card and get a confirmation email about the order.
* Test: Made the payment with the Stripe test card.
* Outcome: When the payment was done I get notification toast message and took me to the checkout success page also got an email.

* I tested all the webhooks and the payments if they are went through with the test card or failed with the insufficient funds test card. All test was successful. I attached images about them below.

![Stripe Payment](/media/readme/images/stripe_payments.png)
![Stripe Webhooks](/media/readme/images/stripe_wh.png)

#### Add a Review

* Expected : The user can write a review and can upload a picture if wish, and can view it on the review page.
* Test: Write a review as a user and upload a picture.
* Outcome: When the review has been wrote I get the notification and it appeared on the review page with or without picture.

#### Edit a Review

* Expected : The user can edit a review and can upload or delete picture if wish, and get a notification when it is done.
* Test: Edit a review as a user and deleted a picture.
* Outcome: When the review has been edited I get the notification and it appeared on the review page without picture.

#### Delete a Review

* Expected : The user can delete a review.
* Test: Delete a review as a user.
* Outcome: When the review has been deleted I get the notification and it disappeard from the review page.

#### Contact Us

* Expected : The user can write a message and provide their email and send it to the store manager/owner.
* Test: Sent a message with subject and provide my own email address.
* Outcome: When the form was sent I get a notification about the manager will reply in 48 hours.

#### Newsletter

* Expected: The user can subscribe on the newsletter and get confirmation email.
* Test: Added the email address to the field and subscribe.
* Outcome: When the subscribe was successful get a confirmation email and a notification with the provided email address.

#### Unsubscribe

* Expected: When the newsletter has been sent out the user can see a unique link labeled as unsubscribe and when it is clicked the user has been taken to the home page with a notification which is said the unsubscribewas successful.
* Test: Clicked the link when the newsletter arrived.
* Outcome: The unsubscribe link took me to the home page and get the notification which showed which email has been unsubscribed.

    
### **Testing as a SuperUser**

#### Add Cake to the store

* Expected: Add cake to the store with description, image, price on the front-end.
* Test: On the manager menu choose the add cake option and fill out the form.
* Outcome: The cake has been added to the site.

#### Edit Cake on the front-end

* Expected: If logged in as a superuser, I can see an option to edit cake and get notified when I done it.
* Test: Choose the edit cake option and fill out the form.
* Outcome: The cake has been edited and got notification about it.

#### Delete Cake on the front-end

* Expected: If logged in as a superuser, I can see an option to delete cake.
* Test: Choose the delete cake option and clicked on it.
* Outcome: The cake has been removed from the shop and get a notification which cake has been deleted.

##### Edit Review

* Expected: The superuser can edit all the reviews do not matter who wrote it.
* Test: Edit a review.
* Outcome: The review has been edited and still on the review page.

##### Delete Review
    
* Expected: The superuser is able to delete any review made by anyone.
* Test: Delete review.
* Outcome: The review has been deleted from the database and the frontend.

#### Contact Us messages

* Expected: When a user submit a contact us form, in the manager menu the superuser choose the messages and can reply to the message with real email.
* Test: Press reply under the message and the email field is already pre-populated with the right email address, sent a reply.
* Outcome: The reply has been sent to the receipent and got notification about it.

#### Newsletter 

* Expected: When a superuser choose the newsletter option can write it and send it all the subscribers which is cannot be changed and the subscribers can not see other email addresses and a unique unsubscribe button included in the email.
* Test: Wrote a newsletter and sent out to multiple subscribers at the same time.
* Outcome: The newsletter has been arrived and it included the unique unsubscribe link and I seen just my own email address.

If you would like to go back to the README file click here: 
    [README](/README.md)
