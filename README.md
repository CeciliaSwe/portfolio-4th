# ABC WOD

## Purpose
ABC WOD is a website for people who workout and need inspiration for their next workout (or Workout of the day - WOD). Any user can view workouts, but only registered users can add workouts. Owners of workouts are also able to edit and delete their posts.

A full list of technologies used can be found in the technologies section of this document. Note that GitHub as of March 2021 automatically creates a Table of Contents for the README file.

## ABC WOD Responsive Website

![Responsive](assets/wireframes_responsive/responsive.png)


[Link to deployed site](https://wod-abc.herokuapp.com/)

## UX

This website was created to showcase my knowledge in Fullstack Development and to provide users with a place to view, create, update and remove Workouts of their own as well as view those created by others.

### User Stories:

Github issues were used to record the user stories. Stories were categorized into different priorities: “Must have”, “Should Have” and “Could Have”.

#### Site administrator:

- As a site admin I can manage site content so that admin remains in control of the site

#### New users:

- As a site user I can view summary content so that I can find inspiration
- As a site user I can register an account so that I can access the full features of the site
- As a site user I can login to the website so that I can use the site´s full functionalities
- As a logged in site user I can add new workouts so that I and other site users can view them
- As a logged in user I can view workout details so that all information is available to me
- As a logged in site user I can edit my workouts so that they can be updated as needed
- As a logged in site user I can delete my workouts so that they can be permanently removed if no longer needed
- As a logged in site user I can logout so that my account and contributions are protected
- As a logged in user, I can use a “What you see is what you get” for formatting text so that it visually displays as expected


### Could haves (not implemented yet)
- As a logged in site user I can search and filter the content so that I can find a workout that suits my preferences
- As a logged in site user I can add workouts to a favorite´s list so that I can easily revisit them
- As a site user I can use social media to login so that I don't have to create a new account

### Wireframes

Wireframes were created with Balsamiq and are uploaded to a separate folder - [View](https://github.com/CeciliaSwe/portfolio-4th/tree/main/assets/wireframes_responsive/P4_workout_wireframes_responsive.pdf). The project was developed from the initial wireframes and some modifications were made during the development process for improved usability and user experience.

### Design

#### Imagery

No physical images will be used on the site. It does make use of Font Awesome icons for visual enhancement.

#### Typography

The font used for my website is "Murecho". The font is provided by Google Fonts.

#### Colour scheme

I chose a dark theme with backgrounds (overall background and card background) in 2 dark shades and a font in white. A bright orange is used for details for contrast.

#### Model

An initial model was created with and is uploaded to a separate folder - [View](https://github.com/CeciliaSwe/portfolio-4th/tree/main/assets/wireframes_responsive/workout_table.pdf)
The final model has minor changes (such as field type) for usability purposes, but the overall structure has been adhered to.

#### Agile Methodology

Github Issues were used to create User Stories and group them according to MoSCoW prioritization technique. GitHub Projects and Kanban board was used to visualize and execute the agile methodology. The issues are currently in two categories: “Done” and “For next release”.


## Features

### Existing Features

#### Navbar and footer
- Navbar and footer are using Bootstrap components and are adjusted to the needs of the project.
![Navbar](assets/features/navbar.png)
![Footer](assets/features/footer.png)

##### Home page

- Home page consists of a Welcome Hero with a short message with buttons to Sign up/Login or Add Workout (depending on the user login status).
![Home](assets/features/index_loggedout.png)

![Home](assets/features/index_loggedin.png)

- Second part of the home page is the list of workouts. The list is generated dynamically as per most current workouts first. The page paginated at 9 workouts and will at that point display Next / Prev buttons to navigate to next and previous pages.

![Home](assets/features/index_pagination.png)

#### Workout full

- Clicking "View Workout" will take the user to the full Workout where the full contents is displayed.

![Workout](assets/features/workout_full_notauthor.png)

- If user is the author of the workout, edit and delete icons will display at the bottom if the workout card to allow user to edit workout or delete workout.

![Workout](assets/features/workout_full_author.png)

#### Add Workout / Edit

- Add Workout button is displayed for logged in users and takes the user to custom form where all fields are required. The content field is a SummerNote WYSIWYG which allows user to customize the visual appearance of the content.

![Add](assets/features/add_form.png)

- Submitting a valid form will redirect user back to the homepage and the newly added workout is displayed first. A success message is displayed and automatically closed after 3,5 seconds.

![Workout](assets/features/add_success.png)

- - If the user does not fill out the title field, the form will not submit and the title field is highlighted. If the user does to fill out any content, the form will reload blank and an error message is displayed and automatically closed after 3,5 seconds.

![Workout](assets/features/add_error.png)

The Edit form is identical to the Add form, but is pre-populated with the current contents.

#### Delete Workout

- If user us the author of a workout, a delete icon will be displayed when viewing the full workout. Clicking the delete icon prompts a Delete Modal, asking "Are you sure you want to delete this workout?". Chosing "Close" will close the modal without action.

![Workout](assets/features/delete_modal.png)

- Chosing "Delete" will delete the workout permanently and display a message to the user that the Workout has been deleted. The message will be automatically closed after 3,5 seconds.

![Workout](assets/features/delete_success.png)

#### Signup / Login / Logout

- Users can signup to gain access to all features (i.e. ability to add, edit and delete their own Workouts).

![Signup](assets/features/signup.png)

- Once an account is created, users can login and logout and are notified by messages when signing in and out.

![Signin](assets/features/signin.png)
![Signin](assets/features/signin_success.png)
![Signout](assets/features/signout.png)
![Signout](assets/features/signout_success.png)


### Features Left to Implement

- Allow users to filter for category, length and number of participants
- Allow users to add favorite workouts to revisit later
- Allow user to login via social media

##### Return to [top](#abc-wod)

## Technologies Used

### Languages

* HTML5
	* This project uses HTML5 as the main language for content and structure of the Website.
* CSS3
	* This project uses CSS3 for Website styling
* Javascript
	*  This project uses Javascript for the required logic to allow for interactivity
* Python - The language that the Django framework is based on

### Frameworks,Libraries and Programs used

* [Django](https://www.djangoproject.com/)
	* High-level Python web framework used to build this application
* [Bootstrap](https://getbootstrap.com/)
	* For components and styling
* [Font Awesome](https://fontawesome.com/)
	* Font awesome Icons are used
* [Google Fonts](https://fonts.google.com/)
	* Google fonts are used throughout the project to import the relevant fonts
* [GitHub](https://github.com/)
	* GithHub is the hosting site used to store the source code for the Website and [Git Pages](https://pages.github.com/) is used for the deployment of the live site.
* [GitPod](https://gitpod.io/)
	* GitPod is used as version control software to commit and push code to the GitHub repository where the source code is stored.
* [Google Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools)
	* Google chromes built in developer tools are used to inspect page elements and help debug issues with the site layout and test different CSS styles.
* [balsamiq Wireframes](https://balsamiq.com/wireframes/)
	* Balsamiq was used to create wireframes and UX design during the planning and design process.
* [Am I Responsive?](http://ami.responsivedesign.is/)
	* Used to generate the screenshots for responsive design.
* [Heroku](https://dashboard.heroku.com/)
	* Could application platform where the deployed application is served from
* [Cloudinary](https://cloudinary.com/)
	* Could application platform where the deployed application is served from


##### Return to [top](#abc-wod)

## Testing

Owing to time constraints, it was not possible to design and implement automatic Unit-testing for this project, and so extensive manual testing was completed instead.
An MS Excel workbook detailing these tests and outcomes can be found [here](https://github.com/CeciliaSwe/portfolio-4th/tree/main/assets/testing/page_tests_portfolio4th.xlsx)

### Bugs

#### Resolved Bugs

- add_items page would not render (could not find path even though it was added correctly to urls). Solved by rearranging order of url paths.
- SummerNote WYSIWYG only displaying in Admin panel and not in front end form. Solved by adding updated SummerNote settings to settings.py
- SummerNote for in front end form overflowing its div on medium and smaller screens. Solved by updating SummerNote settings to settings.py
- Unable to add Workout due to form validation. Solved by (1) add Slugify to generate the slug when adding Workout through the front end form (in addition to it being autogenerated in the Admin panel) and (2) replace Multiselect widget with Radio Buttons.
- HTML validation errors on specific pages if user is logged out. Solved by moving the applicable if statement before the opening div instead of after.
- Signing up using an email address generated a "500 server error". Resolved by updating settings.py with account email verification to optional.

#### Unresolved bugs

- If a user adds a Workout and select a full line, selects a style and then applies a different style to part of that line, this will generate HTML validation errors (as - for example - this can cause a h5 element can become nested inside a h4 element).


### Validation

#### HTML valiation

HTML pages have been validated through the [HTML validator](https://validator.w3.org/nu/#textarea) without errors.
A copy of the HTML reports can be found [here](assets/validation/html)


#### CSS validation

No errors were found when passing through the official [W3C validator](https://jigsaw.w3.org/css-validator/). A copy of the report can be found [here](assets/validation/css/validation_css.pdf)

#### JavaScript validation
Javascript code validation was complited on [jshint](https://jshint.com/) without errors.

A copy of the report can be found [here](assets/validation/js/validation_js.pdf)


#### Python validaton

The Python pages have been validated though the PEP8 validator. Copies of the reports can be found [here](assets/validation/python)


##### Return to [top](#abc-wod)

## Deployment

### Initial deployment

- Gitpod
    - Create new repository from CI template
    - Install Django and required dependencies into Gitpod workspace
    - Create new Django project called "wodabc" and app called "wod"
    - Create Procfile as required
    - Run "pip3 freeze --local > requirements.txt" to update requirements file

- Heroku
    - Log into Heroku
    - Create new app called "wod-abc" (name has to be unique)
    - Go to Resources Tab, Add-ons, search and add Heroku PostgreSQL "hobby" database as resource.
    - Go to section "Config Vars" and click button "Reveal Config Vars"
    - Add the below variables to the list
        - Database URL will be added automaticaly
        - Secret_key - is the django secret key
        - Cloudinary URL can be obtained from [cloudinary](https://cloudinary.com/) follow the steps on the website to register.
        - Configure "DISABLE_COLLECTSTATIC = 1" in Config Vars

- Gitpod
    - Create env.py file and add database path from Heroku
    - Add secret key to env.py
    - Configure database path and secret key in settings.py to be read from environment variables
    - Add Heroku to ALLOWED_HOSTS in settings in your app
    - Perform commit and push to GitHub

- Heroku
    - Under the app app, browse to Deploy
    - Connect to Github, select appropriate repository
    - Run Deploy
    - Wait for confirmation that app has deployed

### Final deployment

- Gitpod
    - Ensure all required files up-to-date and that application is working
    - Run "pip3 freeze --local > requirements.txt" to update requirements file
    - Ensure "DEBUG = False" set in settings.py
    - Perform commit and push to GitHub
- Heroku
    - Under the app, browse to Config Vars
    - Remove the value "DISABLE_COLLECTSTATIC = 1" from Config Vars
    - Browse to Deploy and run deployment
    - Wait for confirmation that app has deployed

##### Return to [top](#abc-wod)

## Credits

Used to set up SummerNote in ModelForms [cdjangocentral](https://djangocentral.com/integrating-summernote-in-django/)
Used to set signup email to optional [django-allauth](https://django-allauth.readthedocs.io/en/latest/configuration.html)

### Content

### Media

### Acknowledgements


