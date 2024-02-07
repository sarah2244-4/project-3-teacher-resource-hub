# Teacher Resource Hub

The Teacher Resource Hub is a website designed for teachers to collaborate with each other by sharing lesson resources with each other. Users will be able to share their own designs and download resources from others.

The site is live, the link to this is found [HERE](https://sarah2244-4.github.io/project-3-teacher-resource-hub/).

![Website mockup](assets/images/mockup.JPG)

## Contents

- [User Experience (UX)](#user-experience-ux)
  - [Goals](#goals)
  - [Users](#users)
  - [New User Stories](#new-user-stories)
  - [Existing User Stories](#existing-user-stories)
- [Design](#design)
  - [Wireframes](#wireframes)
  - [Colour Scheme](#colour-scheme)
  - [Typography](#typography)
  - [Effects](#effects)
  - [Design Choices](#design-choices)
- [Features](#features)
  - [Existing Features](#existing-features)
    - [Home Page](#home-page)
    - [Sign Up](#sign-up)
    - [Login](#login)
    - [Profile](#profile)
    - [Edit Profile](#edit-profile)
    - [Add Resource](#add-resource)
    - [Edit Resource](#edit-resource)
    - [Delete Modal](#delete-modal)
    - [Subject Pages](#subject-pages)
    - [Comments](#comments)
    - [Logout](#logout)
    - [404 Page](#404-page)
  - [Future Features](#future-features)
- [Testing](#testing)
- [Technologies Used](#technologies-used)
  - [Main Languages](#main-languages)
  - [Frameworks, Libraries and Programs](#frameworks-libraries-and-programs)
- [Deployment](#deployment)
  - [GitHub Pages](#github-pages)
  - [Local Source Files](#local-source-files)
- [Credits](#credits)
  - [Content](#content)
  - [Images](#images)
  - [Acknowledgements](#acknowledgements)

## User Experience (UX)

### Goals

The aim of the site is to allow users to collaborate with each other by uploading and downloading resource and sharing opinions on them. 

Users want to be able to intuitively navigate the site and receive immediate feedback when they interact.

### Users

Users will be educators looking for help with their lesson planning. They may also be looking to share their lesson resources. 

### New User Stories

As a first time user of the site I want to be able to:
- Find information about the website to see what it is used for.
- View resources before signing up to see if they look worth it.
- Easily and intuitively navigate without using browser buttons.
- Easily sign up using a simple form.
- Easily download a resource I like the look of once I have signed up. 

### Existing User Stories

As an existing user I want to be able to:
- Login to my account easily.
- Share my resources with other users using a simple form and view them.
- Edit or delete my uploaded resources easily.
- View other people's resources, filtering by subject or level, and download the resources I want to use.
- View comments to see what other users thought of resources before downloading.
- Provide feedback for other users on resources and edit or delete my comments easily. 
- Edit my details or delete my account.

## Design

### Wireframes

| Home Page | Sign Up | Profile | Subjects Pages |
| :---: | :---: | :---: | :---: |
| [Mobile](assets/images/wireframes/mobile-start.jpg) | [Mobile](assets/images/wireframes/mobile-game.jpg) | [Mobile](assets/images/wireframes/mobile-result.jpg) |
| [Tablet](assets/images/wireframes/tablet-start.jpg) | [Tablet](assets/images/wireframes/tablet-game.jpg) |[Tablet](assets/images/wireframes/tablet-result.jpg)|
| [Desktop](assets/images/wireframes/desktop-start.jpg) | [Desktop](assets/images/wireframes/desktop-game.jpg) | [Desktop](assets/images/wireframes/desktop-result.jpg) |


### Colour Scheme

The site's colour scheme is based on the palette:

![Colour scheme](resourcehub/static/assets/images/colour-scheme.JPG)

The colour palette was selected using the palette generator on [Coolors](coolors.co).
- Blue is associated with trust and intelligence, which is important so users feel they can trust the website and the resources are of high quality. 
- Yellow was chosen as it is associated with happiness, confidence and creativity. All of these are feelings users need to have when uploading their own work. 
- Red was chosen as a contrasting colour to the blue. 
- The off-white was added as a background to the body as the white was too harsh on the eyes and it's easier for people to read from, including those with Dyslexia for example.

I used a [contrast checker](https://webaim.org/resources/contrastchecker/) to ensure elements had a high enough contrast ratio.

![Initial choice colours](assets/images/choice-contrast-one.JPG)
![Fixed choice colours](assets/images/choice-contrast-fixed.JPG)

### Typography

The font Franklin Gothic was chosen for headers and buttons as it is a bold sans-serif font that helps everything stand out. For the smaller text, a different font was chosen as it complements the header font. 

### Effects 

- When the mouse hovers over a button, the colour changes to a contrasting colour (blue to red) to make it clear to the user it can be clicked on. 
- The cursor changes to a pointer when it hovers over a button or a link to show you can click it.
- The navbar displayed different links when a user is logged to when a user is logged out. 


### Design choices

- The site is as consistent as possible across all screen sizes. 
- A small, fairly neutral, colour palette was used for consistency with blue and red added for pops of colour where needed. 
- All buttons/links are animated to make it clear that they could be selectable.
- Cancel buttons are red so they stand out as warning in case users clicked on something by accident. 
- I wanted my hero image fairly bright to make the site welcoming, so I added a dark background to the text overlay so the text is readable. 
- The subject cards are on the index page as well as the navigation bar to encourage first time users to click on them and look through the different resources. 
- The uploaded resources were displayed in cards to start with. However, these looked messy as they were large and different sizes. I decided to change to a table and make the whole row selectable so users could view more information. 
- The downlaod option is on the resources table as well as on the individual resource view. This is because some users will want to download after seeing the title/description without wanting to view any more information. 
- I kept the table the same when viewing all resources for subjects to keep a consistent feel. 


## Features

### Existing Features

<details>
<summary>Home Page</summary>

- 

</details>

#### Sign Up

#### Login

#### Profile

#### Edit Profile

#### Add Resource

#### Edit Resource

#### Delete Modal

#### Subject Pages

#### Comments

#### Logout

#### 404 Page

### Future Features

- images of documents if more time to implement for all the types of documents that would be uploaded
- love button
- upload more than 1 file for each resource and be able to add or delete individual files from the resource.
- add many to many table to add extra filters
- edit comments on the same page
- Add pagination to tables
- Order results by date



## Testing 

View the testing document [here](testing.md). 


## Technologies Used 

### Main Languages

HTML5, CSS3, Javascript, Python used. 

### Frameworks, Libraries and Programs

- Flask to provide Python framework.
- Jinja to help render templates. 
- PostgreSQL to create relational database and store user data.
- [Materialize](https://materializecss.com/) front-end framework for navbar, modals, tables, cards and alignment.
- Visual Studio Code as code editor. 
- GitHub Desktop to store the local repository and allow me to code using VS code. 
- [GitHub](https://github.com/) to store the repository online.
- [Font Awesome](https://fontawesome.com/) for icons.
- Chrome Dev Tools for debugging during development.
- Werkzeug to gennerate passwords in order to store them and to generate secure filenamesfor uploaded files.
- [Heroku] to deploy the live site.

## Deployment

### GitHub Pages

To deploy the site to GitHub pages the steps followed were:
- Log into GitHub account
- Open the correct repository 
- In the GitHub repository, go to 'Settings'
- In the settings menu, go to 'Pages' under the subheading 'Code and automation'
- Under the heading 'Source', select 'Deploy from a branch' from the dropdown menu
- Under the heading 'Branch', ensure 'main' is selected from the dropdown and the folder selected is '/(root)'
- Click 'Save' and the website will be live in a few minutes
- The live link can be found [here]()

### Local Source Files

To deploy the website using source files follow the steps:
- Open the GitHub repository [here](https://github.com/sarah2244-4/project-3-teacher-resource-hub)
- In the repository click on the green '<> Code' dropdown
- Select 'Download ZIP'
- Navigate to the Zip file in your file explorer and open it
- Right click on the 'index.html' file and open with the chosen browser

To clone the repsoitory: 
- Open the GitHub repository [here](https://github.com/sarah2244-4/project-3-teacher-resource-hub)
- In the repository click on the green '<> Code' dropdow
- Copy the HTTPS URL link
- Open the terminal on the computer's IDE
- Type in `git clone` followed by the copied URL 

## Credits

### Content

- I referred back to code I had previously written throughout the course, including the jest testing project to help with the automated Jest tests.
- [Am I Responsive?](https://ui.dev/amiresponsive) to display a mock-up of my site in different viewports.
- I used [Coolors](https://coolors.co/) to help me come up with a colour scheme.
- I used [WebAIM](https://webaim.org/resources/contrastchecker/) to check the contrast of the colours used on all the elements. 

### Images

- Hero image downloaded from [Pexels](https://www.pexels.com/photo/silver-ipad-545057/), which was free with no credit required.
- Favicon was generated at [favicon.io](https://favicon.io/favicon-generator/). 


### Acknowledgements

- Thank you to Code Institute for providing detailed lessons and walkthroughs.
- Thank you to the Code Institute community on Slack for providing advice and motivation.
- Thank you to my mentor Spencer for his invaluable advice and expertise.
