# ABC WOD

ACB WOD is a website for people who workout and need inspiration for their next workout (or Workout of the day - WOD). Any user can view workout, both exerpt and in detail, but only registered users can add workouts. Owners of workouts are also able to edit and delete their posts.

![Image of application pages on different screen sizes]()

[Link to deployed site](https://wod-abc.herokuapp.com/)

## UX

### Imagery

My application doesn't feature any imagery as such, however it does make use of Font Awesome icons where needed to add a bit of visual enhancement.

### Typography

The font used for my website is "Murecho".

### Colour scheme


### Schema

Please see below an overview of the schema for my application:


The details of each schema is as follows:


### Wireframes

Please see below the desktop view wireframes for my application:


### User Stories:
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

### Could haves
- As a logged in site user I can search and filter the content so that *I can find a workout that suits my preferences
- As a logged in site user I can add workouts to a favorite´s list so that I can easily revisit them
- As a site user I can use social media to login so that I don't have to create a new account


## Features

### Existing Features


### Features Left to Implement

- Allow users to filter for category, length and number of participants
- Allow users to add favorite workouts to revisit later
- Allow user to login via social media

## Technologies Used

### Languages

- HTML - Required for the render templates
- CSS - Used to provide required custom styling for the templates
- JavaScript - Used to provide custom code to automatically dismiss messages
- Python - The language that the Django framework is based on

### Libraries

- Bootstrap - Used for various components in the templates as follows:
    - Navbar - For navigation element in header
    - Modal - Used for the post delete confirmation popup
    - Grid - To configure layout of page elements
    - CSS - Used for element styling
    - JavaScript - Used for automation of components

### Frameworks

- Django - Full stack framework used to build this application

### Platforms

- GitHub - Where code repository resides with Git version control
- Gitpod - IDE used for development with Git version control
- Heroku - Where the deployed application is served from
- Cloudinary - Where static files are stored for the deployed application


## Testing


### Bugs



### Validator testing

- HTML<br>


- CSS<br>


- Python<br>


## Deployment

### Initial deployment

- Gitpod
    - Create new repository from CI template
    - Install Django and required dependencies into Gitpod workspace
    - Create new Django project called "wodabc" and app called "wod"
    - Create procfile as required
    - Run "pip3 freeze --local > requirements.txt" to update requirements file
- Heroku
    - Log into Heroku
    - Create new app called "wod-abc"
    - Add a PostgreSQL "hobby" database as resource
    - Configure "DISABLE_COLLECTSTATIC = 1" in Config Vars
- Gitpod
    - Create env.py file and add database path from Heroku
    - Add secret key to env.py
    - Configure database path and secret key in settings.py to be read from environment variables
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


## Credits

### Content

### Media

### Acknowledgements






