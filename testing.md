# Testing

## Contents

- [Testing](#testing)
  - [Automated Testing](#automated-testing)
  - [Manual Testing](#manual-testing)
    - [Responsivity](#responsivity)
    - [Browser Compatibility](#browser-compatibility)
    - [Functionality and Usability](#functionality-and-usability)
  - [Testing User Stories](#testing-user-stories)
    - [New Users](#new-users)
    - [Existing Users](#existing-users)
  - [Bugs](#bugs)
    - [Resolved Bugs](#resolved-bugs)
    - [Unresolved Bugs](#unresolved-bugs)
- [HTML and CSS Validation](#html-and-css-validation)
- [JS Validation](#js-validation)
- [Lighthouse Testing](#lighthouse-testing)

### Manual Testing 

#### Responsivity

| All pages | iPhone SE | Pixel 5 | Samsung Galazy S8+ | iPad Air | Surface Pro 7 | Nest Hub | Desktop |
| --- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | 
| Responsive | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| All buttons change when hovered over | Yes | Yes | Yes | Yes | Yes | Yes | Yes |

#### Browser Compatibility

| All pages | Chrome | Firefox | Edge | Opera |
| --- | :---: | :---: | :---: | :---: |
| Loads as expected | Yes | Yes | Yes | Yes |
| Responsive | Yes | Yes | Yes | Yes |

#### Functionality and Usability

| User Action | Expected response | Correct Response |
| --- | --- | :---: |
| Type in website url | Loads home page | Yes | 
| Click logo | Loads home page | Yes | 
| Click Home button in navbar | Loads home page | Yes |
| Hover over Resources button in nav bar | Dropdown menu appears | Yes |
| Click Biology button in navbar dropdown | Biology resources appear | Yes |
| Click Chemistry button in navbar dropdown | Chemistry resources appear | Yes |
| Click Physics button in navbar dropdown | Physics resources appear | Yes |
| Click Sign Up button in navbar dropdown | Sign up form appears | Yes |
| Click Login button in navbar dropdown | Login form appears | Yes |
| Submit sign up form with a field missing | Form does not submit and user is promtped to fill in required field | Yes |
| Submit sign up form with existing username or email | Form does not submit and message is flashed to say they already exist | Yes |
| Submit sign up form with passwords that don't match | Form does not submit and message is flashed to say passwords should match | Yes |
| Submit valid sign up form | New user is created and profile page is loaded | Yes |
| Click Edit Profile button on profile | Edit profile form appears | Yes |
| Submit edit profile form with existing username or email | Form does not submit and message is flashed to say they already exist | Yes |
| Submit valid edit profile form | Form is submitted and user is redirected to profile | Yes |
| Click Add on profile to add resource | Add resource form appears | Yes |
| Submit add resource form with missing field | Message appears above submit button to direct user which field to complete | Yes |
| Submit valid add resource form | Form is submitted and user redirected to profile with flashed message to say successful | Yes |
| Submit valid add resource form | New resource is displayed in the profile resource table | Yes |
| Submit valid add resource form | New resource is displayed in the table of the relevant subject page | Yes |
| Click download icon on resource in table | File is downloaded to user's computer | Yes |
| Click on resource row in table | Large resource view appears | Yes |
| View resource as logged in user | Download file button appears and downloades file to user's computer if clicked | Yes | 
| View resource as guest user | Download file button is not present and user is directed to the login or signup page to download | Yes |
| User who created resource view's resource | Edit and delete buttons are visible | Yes |
| User who did not create resource view's resource | Edit and delete buttons are not visible | Yes |
| View resource as logged in user | Add comment button is visible | Yes |
| View resouece as guest user | Add comment button is not visible | Yes | 

### Testing User Stories

#### New Users

| Goal | Result | Image |
| --- | --- | :---: |
| View information so I know what the quiz is about | The header displays the quiz title and the text on the landing page describes what the quiz is about. | [Instructions](assets/images/instructions.JPG) |
| View instructions so I know how to play | The text on the landing page provides basic how to play instructions. | [Instructions](assets/images/instructions.JPG) |

#### Existing Users

| Goal | Result | Image |
| --- | --- | :---: |
| See if I have improved by comparing my score to previous tries | The end of quiz well done message appears with a score. Users can compare this score to previous goes. Users can also try the quiz again if they want another go immediately using the try again button under the well done message. | [Final score](assets/images/end-quiz.JPG) [Try again button](assets/images/end-quiz.JPG) |

### Bugs

#### Resolved Bugs

#### Unresolved Bugs


## Validation

## HTML and CSS Validation

I used the [W3 Validator](https://validator.w3.org/) to validate my code. 

Initial issues were: 

- The choice buttons contained `<p>` tags that I changed to `<span>` tags.
- The CSS file had a `background-color: none;` value that didn't exist.

All pages have since been run through the validator and all files pass. 

![W3C Validator message](assets/images/w3-validator.JPG)

## JS Validation

I used [JSHint](https://jshint.com/) to validate my script.

Initial issues were: 
- currentQuestion was undefined, which I defined with the global variables. 

It now passes with no issues. 

![JSHint message](assets/images/jshint.JPG)

## Lighthouse Testing

In initial testing:
- There were chrome extension issues affecting performance so the page did not load in time. I retested it in a private browser.
- Accessibility showed that the github icon needed a description so I added an aria-label description. 

Once everything had been fixed I tested the pages with Lighthouse again and they now have high values, with accessibility and SEO at 100 and performance at 99/98. 

Index page:

## PEP 8 Validation