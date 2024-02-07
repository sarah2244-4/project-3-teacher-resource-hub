# Testing

## Contents

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
- [Validation](#validation)
    - [HTML and CSS Validation](#html-and-css-validation)
    - [JS Validation](#js-validation)
    - [PEP8 Validation](#pep8-validation)
    - [Lighthouse Testing](#lighthouse-testing)

## Manual Testing 

### Responsivity

| All pages | iPhone SE | Pixel 5 | Samsung Galazy S8+ | iPad Air | Surface Pro 7 | Nest Hub | Desktop |
| --- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | 
| Responsive | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| All buttons change when hovered over | Yes | Yes | Yes | Yes | Yes | Yes | Yes |

### Browser Compatibility

| All pages | Chrome | Firefox | Edge | Opera |
| --- | :---: | :---: | :---: | :---: |
| Loads as expected | Yes | Yes | Yes | Yes |
| Responsive | Yes | Yes | Yes | Yes |

### Functionality and Usability

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
| Click Sign Out button in navbar | User is logged out and redirected to home page | Yes |
| Use website without being logged in | Navbar displays home, resources, sign up and login buttons | Yes |
| Use website logged in as a user | Navbar displays home, profile, resources, and logout buttons | Yes |
| Click Login button in navbar dropdown | Login form appears | Yes |

#### Login and Sign Up Form Actions
| User Action | Expected response | Correct Response |
| --- | --- | :---: |
| Submit sign up form with a field missing | Form does not submit and user is promtped to fill in required field | Yes |
| Submit sign up form with existing username or email | Form does not submit and message is flashed to say they already exist | Yes |
| Submit sign up form with passwords that don't match | Form does not submit and message is flashed to say passwords should match | Yes |
| Submit valid sign up form | New user is created and profile page is loaded | Yes |
| Submit login form with incorrect email | Form does not submit and message flashed that email does not exist | Yes |
| Submit login form with incorrect password | Form does not submit and message flashed that password is incorrect | Yes |
| Submit valid login form | Profile page loads and message flashed to say login is successful | Yes |

#### Profile Actions
| User Action | Expected response | Correct Response |
| --- | --- | :---: |
| Click Edit Profile button on profile | Edit profile form appears | Yes |
| Submit edit profile form with existing username or email | Form does not submit and message is flashed to say they already exist | Yes |
| Submit valid edit profile form | Form is submitted and user is redirected to profile | Yes |
| Click delete profile | Modal pops up | Yes |
| Click no on modal or space around delete profile modal | Modal disappears and nothing is deleted | Yes |
| Click yes on delete profile modal | Profile is deleted and user is logged off and redirected to home | Yes |
| Log in using deleted profile credentials | Form does not submit and message is flashed to say email does not exist | Yes |

#### Resource Actions
| User Action | Expected response | Correct Response |
| --- | --- | :---: |
| Click add on profile to add resource | Add resource form appears | Yes |
| Submit add resource form with missing field | Message appears above submit button to direct user which field to complete | Yes |
| Submit valid add resource form | Form is submitted and user redirected to profile with flashed message to say successful | Yes |
| Submit valid add resource form | New resource is displayed in the profile resource table | Yes |
| Submit valid add resource form | New resource is displayed in the table of the relevant subject page | Yes |
| Click download icon on resource in table | File is downloaded to user's computer | Yes |
| Click on resource row in table | Large resource view appears | Yes |
| View resource as logged in user | Download file button appears and downloades file to user's computer if clicked | Yes | 
| View resource as guest user | Download file button is not present and user is directed to the login or signup page to download | Yes |
| View resource as user who created it | Edit and delete buttons are visible | Yes |
| View resource as user who did not create it | Edit and delete buttons are not visible | Yes |
| View resource as logged in user | Add comment button is visible | Yes |
| View resource as guest user | Add comment button is not visible | Yes | 
| Click edit resource button on resource view | Edit resource form appears | Yes |
| Submit edit resource form if not resource creator | Form does not submit and user redirected to home with flashed message | Yes | 
| Submit edit resource form with blank field | Form does not submit and user directed to complete missing field | Yes |
| Submit valid edit resource form | Form submits and user redirected to previous view page | Yes |
| Click delete button to delete resource | Modal pops up | Yes |
| Click no on delete resource modal or space around modal | Modal disappears and nothing is deleted | Yes |
| Click yes on delete resource modal | Resource is deleted and removed from resource table | Yes |

#### Comment Actions
| User Action | Expected response | Correct Response |
| --- | --- | :---: |
| Click add button to add comment with blank field | Form not submitted and user directed to fill in field | Yes |
| Click add button to add commment with valid form | Form submitted and page reloaded with comment visible | Yes |
| Click edit icon on comment | Edit comment form appears | Yes |
| Click edit on edit comment form as user who created comment | Form submitted and user redirected to profile | Yes |
| Click edit on edit comment form as user who did not create comment | Form not submitted and profile loads with message flashed | Yes |
| Click cancel button on comment form | Profile page loads | Yes |
| Click delete icon on comment | Delete comment modal pops up | Yes |
| Click no on modal or space around delete comment modal | Modal disappears and nothing is deleted | Yes |
| Click yes on delete comment modal | Comment is deleted, page refreshes and comment is no longer displayed | Yes |

#### Subject Page Actions
| User Action | Expected response | Correct Response |
| --- | --- | :---: |
| Click all button on biology resources | All biology resources are shown in the table | Yes | 
| Click KS3 button on biology resources | Only KS3 biology resources are shown in the table | Yes | 
| Click GCSE button on biology resources | Only GCSE biology resources are shown in the table | Yes | 
| Click AS-Level button on biology resources | Only AS-Level biology resources are shown in the table | Yes | 
| Click A-Level button on biology resources | Only A-Level biology resources are shown in the table | Yes | 
| Click all button on chemistry resources | All chemistry resources are shown in the table | Yes | 
| Click KS3 button on chemistry resources | Only KS3 chemistry resources are shown in the table | Yes | 
| Click GCSE button on chemistry resources | Only GCSE chemistry resources are shown in the table | Yes | 
| Click AS-Level button on chemistry resources | Only AS-Level chemistry resources are shown in the table | Yes | 
| Click A-Level button on chemistry resources | Only A-Level chemistry resources are shown in the table | Yes | 
| Click all button on physics resources | All physics resources are shown in the table | Yes | 
| Click KS3 button on physics resources | Only KS3 physicsy resources are shown in the table | Yes | 
| Click GCSE button on physics resources | Only GCSE physics resources are shown in the table | Yes | 
| Click AS-Level button on physics resources | Only AS-Level physics resources are shown in the table | Yes | 
| Click A-Level button on physics resources | Only A-Level physics resources are shown in the table | Yes | 
| View subject pages as guest user | Download icon not visible | Yes |
| View subject pages as authorized user | Download icon is visible | Yes |
| Click on row in tables | Loads resource view | Yes |


## Testing User Stories

### New Users

| Goal | Result | Image |
| --- | --- | :---: |
| View information so I know what the quiz is about | The header displays the quiz title and the text on the landing page describes what the quiz is about. | [Instructions](assets/images/instructions.JPG) |
| View instructions so I know how to play | The text on the landing page provides basic how to play instructions. | [Instructions](assets/images/instructions.JPG) |

### Existing Users

| Goal | Result | Image |
| --- | --- | :---: |
| See if I have improved by comparing my score to previous tries | The end of quiz well done message appears with a score. Users can compare this score to previous goes. Users can also try the quiz again if they want another go immediately using the try again button under the well done message. | [Final score](assets/images/end-quiz.JPG) [Try again button](assets/images/end-quiz.JPG) |

## Bugs

### Resolved Bugs

- The rows of the table overlapped on smaller screens. Without adding horizontal scroll bars or making text too small to read, created tables with fewer columns to display on smaller screens. Most vital information was shown as the rest can still be accessed when the row is clicked. 
- Comments were added in same row if more than one comment was added to a resource. To fix, had to move for loop outside the table row. 
- Alerts wouldn't close when the close button was clicked. Fix was to add javascript to add an event listener to close the alert when the button is clicked. 

### Unresolved Bugs

- The upload file button can be accidentally clicked from other parts of the form. Tried to move field lower abd change styling of form but it didn't fix this. 


## Validation

### HTML Validation

I used the [W3 Validator](https://validator.w3.org/) to validate my HTML files. I did this by pasting in the URI for each page of my depolyed site. 

Initial issues were: 

- The choice buttons contained `<p>` tags that I changed to `<span>` tags.
- The CSS file had a `background-color: none;` value that didn't exist.

All pages have since been run through the validator and all files pass. 

![W3C Validator message](assets/images/w3-validator.JPG)

### CSS Validation

I used the [W3 Validator](https://validator.w3.org/) to validate my styles.css file. 

### Javascript Validation

I used [JSHint](https://jshint.com/) to validate my script.js file.

The only problems shown was 1 undefined variable. This came from Materialize so was not a problem and there was nothing I needed to change. 

![JSHint message](assets/images/jshint.JPG)

### Python Validation

I used the [Code Institute Python Linter]() to validate my routes.py file. The initial errors were extra whitespaces and some lines were too long. After fixing these, there were no errors. 

### Lighthouse Testing

<details>
<summary>Index Page</summary>

- 

![Index Page Lighthouse Test](/static/images/readme/testing/editdetailslh.webp)

</details>

<details>
<summary>Register</summary>

- 

![Index Page Lighthouse Test](/static/images/readme/testing/editdetailslh.webp)

</details>

<details>
<summary>Login</summary>

- 

![Index Page Lighthouse Test](/static/images/readme/testing/editdetailslh.webp)

</details>

<details>
<summary>Profile</summary>

- 

![Index Page Lighthouse Test](/static/images/readme/testing/editdetailslh.webp)

</details>

<details>
<summary>Edit Profile</summary>

- 

![Index Page Lighthouse Test](/static/images/readme/testing/editdetailslh.webp)

</details>

<details>
<summary>Add Resource</summary>

- 

![Index Page Lighthouse Test](/static/images/readme/testing/editdetailslh.webp)

</details>

<details>
<summary>Edit Resource</summary>

- 

![Index Page Lighthouse Test](/static/images/readme/testing/editdetailslh.webp)

</details>

<details>
<summary>Subject Page</summary>

- 

![Index Page Lighthouse Test](/static/images/readme/testing/editdetailslh.webp)

</details>

<details>
<summary>View Resource</summary>

- 

![Index Page Lighthouse Test](/static/images/readme/testing/editdetailslh.webp)

</details>

<details>
<summary>Edit Comment</summary>

- 

![Index Page Lighthouse Test](/static/images/readme/testing/editdetailslh.webp)

</details>

<details>
<summary>404 Page</summary>

- 

![Index Page Lighthouse Test](/static/images/readme/testing/editdetailslh.webp)

</details>

Return to [README](README.md).