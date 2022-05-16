<h1 align="center">Setlist Sharer</h1>
<img  src="assets/images/readme/amiresponsive.jpg"  alt="Mockup of the Hull College website on a phone, tablet, laptop and monitor screen">

*Image created and taken from [Am I Responsive?](ami.responsivedesign.is).*

[View the live project here](https://mjjstockman.github.io/hull-college).

---

## Table of contents

1. [Introduction](#Introduction)
2. [UX and Design](#UX-and-design)
   - [User Demographics](#User-Demographics)
   - [User Stories](#User-Stories)
   - [Wireframes](#Wireframes)
   - [Changes to the design throughout development](#Changes-to-the-design-throughout-development)
   - [Colour Scheme](#Colour-Scheme)
   - [Typography](#typography)
3. [Database Design](#Database-Design)
   - [ERD](#Entity Relationship Diagram)
4. [Features](#Features)
   - [Navigation and Header](#Navigation-and-Header)
   - [Hero Image](#Hero-Image)
   - [About Information Box](#About-Information-Box)
   - [Award Winning and Student Satisfaction](#Award-Winning-and-Student-Satisfaction)
   - [About Information Box](#About-Information-Box)
   - [Courses Section](#Courses-Section)
   - [Contact Section](#Contact-Section)
   - [Footer](#Footer)
5. [Future Features](#Features-to-Implement-in-the-future)
6. [Testing](#Testing)
7. [Deployment](#Deployment)
   - [How the site was Deployed](#How-the-site-was-Deployed)
   - [How to Fork the Repository](#How-to-Fork-the-Repository)
   - [How to create a Clone](#How-to-create-a-Clone-using-SSH)
8. [Credits](#Credits)
   - [Images](#Images)
   - [Acknowledgements](#Acknowledgements)

---

# Introduction

This is a fictional website (for educational purposes) for potential students to find basic information about **Hull College** in East Yorkshire, England. It gives basic information on the college's success, the courses offered and a way to contact them, so users can gauge the suitability of the college.

[Back to top ⇧](#Hull-College)

# UX and Design

## User Demographics

The target market are individuals who are wanting to find out more about the college to see if they want to enrol. It is not for current students.

## User Stories

1. As a potential student, I want to quickly see what courses are offered, so I can see if they are of interest.

2. As a potential student, I want to see some general "about" text, so I can confirm that I am on the correct site for my needs.

3. As a potential student, I want to see facts and figures on student satisfaction, so I can gauge whether I want to enrol.

4. As a potential student, I want to be able to contact the college, so that I can ask any questions I have.

[Back to top ⇧](#Hull-College)

## Wireframes

| Small screens | Medium screens | Largescreens |
| --------------| -------------- | ------------ |
| <img  src="assets/images/readme/wireframe-small.jpg"  alt="Wireframe of small screen"> | <img  src="assets/images/readme/wireframe-medium.jpg"  alt="Wireframe of medium screen"> | <img  src="assets/images/readme/wireframe-large.jpg"  alt="Wireframe of large screen"> |

*Images created and taken from [Balsamiq](https://balsamiq.com/wireframes)*

[Back to top ⇧](#Hull-College)

## Changes to the design throughout development

The original design was slightly different to the above wireframes. The following particulars were changed during implementation to better the user experience and aesthetics:

The header was changed so that the logo was centered and the navigation drops underneath when the screen is reduced to a particular size. This meant that the navigation links did not get too close together.

Form labels were moved above their inputs, placeholders removed and all inputs and the submit button were stacked and the same width.

A map showing the colleges location was added to the contact section.

[Back to top ⇧](#Hull-College)

## Colour Scheme

Blue was chosen as the main colour for the site. Research had shown that this is a colour associated with reliability, productivity, trust and order, which are the principles the college wish to promote.

[Coolors](https://coolors.co/) was then used to find a mix of blues for the main colour palette, with the following decided upon:

- Header: #03045e ![#f03c15](https://via.placeholder.com/15/03045e/000000?text=+)
- About: #caf0f8 ![#caf0f8](https://via.placeholder.com/15/caf0f8/000000?text=+)
- Courses: #90e0ef ![#90e0ef](https://via.placeholder.com/15/90e0ef/000000?text=+)
- Contact: #00b4d8 ![##00b4d8](https://via.placeholder.com/15/00b4d8/000000?text=+)
- Footer: #0077b6 ![#0077b6](https://via.placeholder.com/15/0077b6/000000?text=+)

<img  src="assets/images/readme/blue-colours.jpg"  alt="Blue colour scheme from Coolors.co">

- Main text: #12130f ![#12130f](https://via.placeholder.com/15/12130f/000000?text=+)
- Navigation and footer text/icons: #fffafa ![#fffafa](https://via.placeholder.com/15/fffafa/000000?text=+)
- Accent color: #800080 ![#800080](https://via.placeholder.com/15/800080/000000?text=+)
- Submit button: #faf482 ![#faf482](https://via.placeholder.com/15/faf482/000000?text=+)

[Back to top ⇧](#Hull-College)

## Typography

[Typespiration](https://typespiration.com/) was used to find complimenting [Google Font](https://fonts.google.com) pairings, with the following decided upon:

- Headings: Roboto Condensed, with a fallback of sans-serif.
- Body: Poppins, with a fallback of sans-serif.

[Back to top ⇧](#Hull-College)

# Database Design

## Entity Relationship Diagram

<img src="docs/readme_images/MVP-ERD.jpg"  alt="The hero image">

# Features

## Navigation and Header

The navigation bar allows the user to easily select which area of the site they wish to view. It will be located at the top of the site as this is common practice and is the area where most users eyes will be initially drawn to. It will be 'sticky', meaning it will stay at the top of the users screen even when they scroll the site. This is because the site is a one-page design and it is essential for the user to always be able to navigate the site wherever their current position. When a link is hovered over it becomes underlined to help the user confirm they are about to select the relevant link. The underline remains once selected and the relevant navigation link is highlighted when the site is scrolled.

The 'hamburger' icon was not used on small screens (where the navigation bar will collapse and be represented as three horizontal lines. When touched/clicked, this would reveal the navigation in a dropdown menu). This is often done due to the limited real estate space making the text hard to read when the screen is this size. However, this design was not used to make the site more easy to navigate for all users. Furthermore, the navigation only contains three links, so they have the space to remain next to each other still on small screens without causing accessibility and design issues. However, the logo will be centered and the navigation drop below at a particular screen width.

<img src="assets/images/readme/header-large.jpg"  alt="Header at full screen">


[Back to top ⇧](#Hull-College)

## Hero Image

An eye-catching full screen image is placed under the navigation. This helps grab the users attention and convey positive, professional feelings.

<img src="assets/images/index/class.jpg"  alt="The hero image">

[Back to top ⇧](#Hull-College)

## About Information Box

A small box containing introductory information is placed below the hero image. This is eye-catching and quickly confirms to the user that they are on the correct site. It offers general information on the college, so users quickly get a feel for its achievements.

<img src="assets/images/readme/about-box.jpg"  alt="The About information box">

[Back to top ⇧](#Hull-College)

## Award Winning and Student Satisfaction

A brief description of the four awards the college has won is displayed under cartoon images of awards. Beneath these are statistics of student success and recommendations. These help to install confidence in the quality of the college and help conversion rates of those viewing the site to enrol. Larger screens display the awards and statistics four in a row, reducing to two and then stacked on top of each other as screens get smaller. This is to give the user the best experience in terms of accessibility and usability. These sections mirror each other to help give the site a sense of balance.

<img src="assets/images/readme/award-large.jpg"  alt="Award Winning area">

***

<img src="assets/images/readme/satisfaction-large.jpg"  alt="Student Satisfaction area">

[Back to top ⇧](#Hull-College)

## Courses Section

This section contains images for the courses available at the college, so users can quickly see if they offer a course they are interested in. Icons from Font Awesome are used for the courses to add visual interest and to make each course quickly identifiable and more memorable. On large screens the courses are displayed three in a row, changing to two and then one as the screen gets smaller.

<img src="assets/images/readme/courses-large.jpg"  alt="Courses section">

[Back to top ⇧](#Hull-College)

## Contact Section

This section allows the user to easily contact the college by using a form to send a message. The fields are clearly marked, all required and the email field must contain a valid email. The message is limited to 400 characters to keep them succinct and reduce the amount of characters needed to be stored in the database. The Submit button is a bright distinctive colour, acting as a call to action for the user.

A map showing the college's location is also included in this section, allowing users to quickly identify where the college is based.

<img src="assets/images/readme/contact-large.jpg"  alt="Contact area">

*Please note the empty box on the left displays a map on the deployed site.*

[Back to top ⇧](#Hull-College)

## Footer

The footer feature at the bottom of the page contains links to Hull Colleges social media links. This will help users find more information and stay up to date with the college. The links open in a new tab, so users are not taken away from Hull College's website. They are the same colour as those in the navigation for consistency and to help them stand out.

<img src="assets/images/readme/footer.jpg"  alt="Footer section">

[Back to top ⇧](#Hull-College)

# Features to Implement in the future

Add a dropdown to each course in the Courses section containing information on the course.

Add script to dynamically display how many characters are left for the form textarea.

Remove inline JavaScript in index.html into a separate script folder.  This was not done as it was outside the scope of the project.
 
The active navigation highlighting does not always work correctly on scroll.  This feature was not fixed as the use of JavaScript is outside the scope of the project.

# Technologies Used

## Main Languages Used

- HTML
- CSS

[Back to top ⇧](#Hull-College)

## Additional Languages Used

- JavaScript was used to change the highlighted navigation link on scroll.

[Back to top ⇧](#Hull-College)

# Testing

Details on site testing can be found [here](TESTING.md).

[Back to top ⇧](#Hull-College)

# Deployment

## How the site was Deployed

The code was deployed to GitHub Pages in the following way:

1. Log into [GitHub](https://github.com/login) or [create an account](https://github.com/join).
2. Select the [GitHub Repository](https://github.com/mjjstockman/hull-college).
3. Open Settings by clicking on the Settings link (with the cog icon).
4. Scroll down to the GitHub Pages section and click on the link.
   <img src="assets/images/readme/github-pages.jpg"  alt="GitHub Pages section">
5. Click the dropdown box in the Source section (which currently states "none") and select master (this may be named "main" for some users).
   <img src="assets/images/readme/github-source.jpg"  alt="Selecting master branch as source">
6. Click Save.
7. The URL address for the deployed site will be shown.
   <img src="assets/images/readme/deployed-address.jpg"  alt="Example of URL once deployed">

[Back to top ⇧](#Hull-College)

## How to Fork the Repository

1. Log into [GitHub](https://github.com/login) or [create an account](https://github.com/join).
2. Select the [GitHub Repository](https://github.com/mjjstockman/hull-college).
3. Click "Fork" at the top right of the page.
4. The repository will be copied into your GitHub account.

[Back to top ⇧](#Hull-College)

## How to create a Clone using SSH

1. Log into [GitHub](https://github.com/login) or [create an account](https://github.com/join).
2. Select the [GitHub Repository](https://github.com/mjjstockman/hull-college).
3. Click on the Code button.
4. Copy the provided SSH link.
   <img src="assets/images/readme/code-dropdown.jpg"  alt="Example of the provided link">
5. Open Terminal.
6. Navigate into the directory you want to clone the repositroy to.
7. Type git clone and paste the copied URL.

```
$ git clone https://github.com/mjjstockman/hull-college
```

8. Press **Enter**.

[Back to top ⇧](#Hull-College)

# Credits

Many thanks to the following which were used throughout the creation of this site:

- [w3c Markup Validator](https://validator.w3.org)
- [Adobe Stock Image](https://stock.adobe.com)
- [Am I Responsive?](http://ami.responsivedesign.is)
- [Balsamiq](https://balsamiq.com/)
- [Coolors](https://coolors.co/)
- [Design Course tutorial](https://www.youtube.com/watch?v=z9H7p1_iI14)
- [Embed My Map](https://www.embedmymap.com/)
- [Favicon.io](https://favicon.io)
- [Font Awesome](https://fontawesome.com)
- [Free Formatter](https://www.freeformatter.com/)
- [Google Fonts](https://fonts.google.com)
- [Git](https://git-scm.com)
- [GitHub](https://github.com)
- [Json Formatter](https://jsonformatter.org/markdown-formatter)
- [Lighthouse](https://developers.google.com/web/tools/lighthouse)
- [Looka](https://looka.com/)
- [Malsu Codepen](https://codepen.io/malsu/pen/VwKzoPG)
- [Pexels](https://www.pexels.com)
- [Placeholder.com/](https://placeholder.com)
- [Responsinator](http://www.responsinator.com)
- [Squoosh](https://squoosh.app)
- [Super Cool Design](https://supercooldesign.co.uk/blog/how-to-write-good-alt-text)
- [TinyPNG](https://tinypng.com)
- [Typespiration](https://typespiration.com)


[Back to top ⇧](#Hull-College)