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


#### Responsivity

| Tests for all gameplay | iPhone SE | Pixel 5 | Samsung Galazy S8+ | iPad Air | Surface Pro 7 | Nest Hub | Desktop |
| --- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | 
| Responsive | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| All buttons change when hovered over | Yes | Yes | Yes | Yes | Yes | Yes | Yes |

#### Browser Compatibility

| Tests for all gameplay | Chrome | Firefox | Edge | Opera |
| --- | :---: | :---: | :---: | :---: |
| Loads as expected | Yes | Yes | Yes | Yes |
| Responsive | Yes | Yes | Yes | Yes |

#### Functionality and Usability

| User Action | Expected response | Correct Response |
| --- | --- | :---: |
| Click 5 Questions | Gives a quiz of 5 questions | Yes | 
| Click 5 Questions | Changes colour | Yes | 

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