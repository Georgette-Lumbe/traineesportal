# Trainee Portal - Testing

[Main README.md file](https://github.com/Georgette-Lumbe/traineesportal/blob/main/README.md)

[View live project](https://traineesportal.herokuapp.com/)

[View website in GitHub pages](https://github.com/Georgette-Lumbe/traineesportal)

---

# Table of Contents

1. [Testing User Stories](#testing-user-stories "#Goto testing user stories")
2. [Manual Testing](#manual-testing "#Goto manual testing")

3. [Automated Testing](#automated-testing "#Goto automated testing")
    * [Code Validation](#code-validation "Goto code validation")
    * [Browser Validation](#browser-validation "Goto browser validation")
    * [Lighthouse Auditing](#lighthouse-auditing "Goto lighthouse auditing")

4. [User Testing](#user-testing "Goto user testing")

---

# Testing User Stories


# Manual Testing

## Common Elements Testing

### First Time User goals

* As a first time user, I want to see the main functions of the site

    - When user click on the site, he will see firstly all the main functions on the landing page

* As a first time user, I want to be able to easily navigate throughout the site to find content

    - At the top left, there is a logo which leads user back to the landing page with one click.

    - At the top right, there is a navbar buttons which leads user to each the main options of the site back to the in one click.

    - On each box, there are text as Read More, Notes, assignmenets an task lists that allow the user to go anywhere he wants.

* As a first time user, I want to read the blog post and see the comment

    - There are three blogposts on the bottom of the landing page, on these blogposts, there a Read More button that leads to the blogpost of his choice, then he can read the post.

    - At the bottom of the blogpost, there is a comment area, user can read existing comments and also comment if he want,

### Returning User Goals

* As a returning user, I want the site to be responsive across all devices.

    - The site is created to be responsive across all devices, the user can see the site with a phone, tablet, machine. The user can use the site the same way as on all devices.

* As a returning user, I want to be able to create an account easily.

    - At the top right, the third button `register`, lead the user to the register page
    - The register is simple to fill : write the username, email (optional), create a password and confirm that password.

* As a returning user, I want to be able to creates notes, assignments and tasks

    - At the top right, when the user hits **options**, then he can click on Notes, Assignments and tasks or can hits directly on the Notes, assignments and tasks in the landing page.

    - Once click, user can create his notes, write down assignments and tasks by filling the present form.

* As a returning user, I want to be able to see my profile

    - At the top right, user can hit on the profile that lead to the user profile with all due assignments and tasks.

### Frequent User Goals

* As a frequent user,  I want to be able to login

    - At the top right, the user can hit on the login button that lead to the login page 

    - The login is simple to fill : write the username, and the password.

* As a frequent user, I want to see my notes, assignments and tasks

    - Once the user login, he can see all his notes, tasks and assignments saved in each options.

* As a frequent user, I want to update my assignments and tasks

    - The user can click on mark as completed to update his tasks and assignments.

* As a frequent user, I want to delete my unwanted data

    - The user can click on the trash icon to delete the unwanted delete

* As a frequent user, I want to check to see if there are new blog posts

    - The user can see if there is a new blog post, login or not.

# Manual Testing

## Navbar

* Manual testing for navbar :

![](documentation/testing/gif/navbar.gif)


* The responsiveness of home page

![](documentation/testing/gif/home_responsiveness.gif)

* Manual testing for the profile :

![](documentation/testing/gif/profile.gif)

* The responsiveness of profile page

![](documentation/testing/gif/profile_responsiveness.gif)


* Manual testing for signup :

![](documentation/testing/gif/signup.gif)

* The responsiveness of Signup page

![](documentation/testing/gif/signup_responsiveness.gif)


* Manual testing for logout and login :

![](documentation/testing/gif/logout_login.gif)

* The responsiveness of Sign in page

![](documentation/testing/gif/login_responsiveness.gif)


* Manual testing for notes (create and delete) :

![](documentation/testing/gif/create_delete_note.gif)

* The responsiveness of notes page

![](documentation/testing/gif/notes_responsiveness.gif)


* Manual testing for assignments (create and delete) :

![](documentation/testing/gif/create_delete_assignment.gif)

* The responsiveness of assignments page

![](documentation/testing/gif/assignments_responsiveness.gif)


* Manual testing for tasks (create and delete) :

![](documentation/testing/gif/create_delete_task.gif)

* The responsiveness of all tasks page

![](documentation/testing/gif/tasks_responsiveness.gif)


* Manual testing for blog post Mindset and comment :

![](documentation/testing/gif/comment_mindset.gif)

* Manual testing for blog post Relationship and comment :

![](documentation/testing/gif/comment_relationship.gif)

* Manual testing for blog post advice and comment :

![](documentation/testing/gif/comment_advice.gif)

* The responsiveness of all posts

![](documentation/testing/gif/post_responsiveness.gif)

# Automated Testing

## Code Validation

1. W3C Markup Validator service was used to validate the HTML code used.

* base.html

<img src="" width="100%">

* index.html

<img src="" width="100%">

* notes.html

<img src="documentation/testing/notes_test.PNG" width="100%">

* notes_details.html

<img src="" width="100%">

* assignments.html

<img src="documentation/testing/assignments_test.PNG" width="100%">

* tasks.html

<img src="documentation/testing/tasks_test.PNG" width="100%">

* post_details.html

<img src="" width="100%">

* profile.html

<img src="documentation/testing/profile_test.PNG" width="100%">

2. W3C validator CSS service was used to validate the CSS code used.

* style.css

<img src="documentation/testing/css_validator.PNG" width="100%">

4. P8P online was used to validate the Python code used

* views.py

<img src="documentation/testing/views_test.PNG" width="100%">

* models.py

<img src="documentation/testing/models_test.PNG" width="100%">

* forms.py

<img src="documentation/testing/forms_test.PNG" width="100%">

* urls.py(blog)

<img src="documentation/testing/urls_app_test.PNG" width="100%">

* urls.py(traineesportal)

<img src="documentation/testing/urls_test.PNG" width="100%">

* admin.py

<img src="documentation/testing/admin_test.PNG" width="100%">

* settings.py

There is more details on the Issues and bugs in the README.md file.
<img src="documentation/testing/settings_test.PNG" width="100%">

## Browser Validation

1. Chrome

<img src="documentation/testing/chrome.PNG" width="100%">

2. Edge

<img src="documentation/testing/edge.PNG" width="100%">

3. Opera

<img src="documentation/testing/opera.PNG" width="100%">

4. Firefox

<img src="documentation/testing/firefox.PNG" width="100%">

## Lighthouse Auditing

*  Find the desktop and mobile full reports

<details>
<summary>Desktop</summary>
<img src="documentation/testing/lighthouse_desktop1.PNG" width="100%">
<img src="documentation/testing/lighthouse_desktop2.PNG" width="100%">
<img src="documentation/testing/lighthouse_desktop3.PNG" width="100%">
<img src="documentation/testing/lighthouse_desktop4.PNG" width="100%">
<img src="documentation/testing/lighthouse_desktop5.PNG" width="100%">
<img src="documentation/testing/lighthouse_desktop6.PNG" width="100%">
<img src="documentation/testing/lighthouse_desktop7.PNG" width="100%">
<img src="documentation/testing/lighthouse_desktop8.PNG" width="100%">
</details>

<details>
<summary>Mobile</summary>
<img src="documentation/testing/lighthouse_mobile1.PNG" width="100%">
<img src="documentation/testing/lighthouse_mobile2.PNG" width="100%">
<img src="documentation/testing/lighthouse_mobile3.PNG" width="100%">
<img src="documentation/testing/lighthouse_mobile4.PNG" width="100%">
<img src="documentation/testing/lighthouse_mobile5.PNG" width="100%">
<img src="documentation/testing/lighthouse_mobile6.PNG" width="100%">
<img src="documentation/testing/lighthouse_mobile7.PNG" width="100%">
<img src="documentation/testing/lighthouse_mobile8.PNG" width="100%">
<img src="documentation/testing/lighthouse_mobile9.PNG" width="100%">
</details>

# User testing

Family members, Jimmy , were asked to review, test the the site to point out any bugs and issues.

The following changes were made after their testing:

* Change the color and fonts of the site
* Correct some spelling mistakes.

 [Go to top](#testing-user-stories "#Goto testing user stories")