# EdVenture Documentation

---

## Table of contents

- Design
    - [Target Audience](#target-audience)
    - [Development Methodologies](#development-methodologies)
    - [Success Criteria](#success-criteria)
    - [Decomposition of the Problem](#decomposition-of-the-problem)
    - [Design of the Logo](#design-of-the-logo)

---

# Design

---

## Target Audience

This project's intended target audience is initially for students of
Sixth Form / College, or any other applicable institution in which students
aged 16+. This is as the project is primarily aimed towards university
students receiving offers from the UCAS service and would not be
relevant to anyone younger as they would not have access to the 
variety of matriculation services that someone using this project would
need access to.

During the creation of this project, I will use a variety of matriculated
students in the University of Edinburgh to test and provide feedback
iteratively (see the 
["Development Methodologies"](#development-methodologies) section).
I will present these in each of the respective sections.



---

## Development Methodologies

Upon analysis of multiple development methodologies, I have decided
to use the Rapid Application Development (RAD) methodology for a variety
of reasons. The first reason being that it relies on constant feedback
from the clientele, which will allow for me to be able to better tailor
the project to the client and ensure ease of use for the client. In 
addition to this, this development methodology allows for more
flexibility between each of the stages of development (design,
implementation, testing and maintenance) as opposed to other development
methodologies which would be too restrictive while developing and would
have little opportunity to contact the client (such as the waterfall
methodology).

I will apply the use of Rapid Application Development by contacting
students of the University of Edinburgh at each point in which a 
prototype of the project has been developed, or a new feature added, in
which I will conduct an interview and gather any improvements that can
be added. Once the project is released, I will provide a means of giving
feedback for universities and students matriculating on the project
itself.

---

## Success Criteria

After consulting with selected members of my clientele (students of the
University of Edinburgh), they have provided me with a specification of what
they would like the project to achieve, which has been compiled below as an
idea of the initial v1.0 of the project.

| Number | Criteria                         | Details                                                                                                                                                            | Justification                                                                                                                                                                                                               |
|:------:|:---------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   1    | Login Page                       | Provides the user with a login using a specified username (combination of first and last name) and a user defined password, with database connections              | This allows for users to maintain access to their pairings to university logins without having to re-pair each of the university contacts.                                                                                  |
|   2    | Sign Up Page                     | A separate page to the login, lets user type in the first and last name, as well as a password                                                                     | This allows for users to create an account to ensure that the users only had to bind their university contacts once.                                                                                                        |
|   3    | Calendar Feature                 | Allows for the students institution/s to assign events, as well as user created deadlines and events                                                               | This would give the purpose of allowing the University to insert each of the dates and deadlines required for each student to fill, also so that the user can add any deadlines to be aware of in the matriculation process |
|   4    | Ability to create logins         | Allows the institution to give out logins to students as a setup                                                                                                   | This would make the sign up process less confusing for the student as they do not have to worry about their own signup                                                                                                      |
|   5    | Article Page                     | Scrapes the Unis page for admission articles, as well as the option to create uni specific or general articles                                                     | This would keep the student informed on any other aspects of admissions and prepare the student for freshers week                                                                                                           |
|   6    | Integration between each version | Ensures each version of the application is updated simultaneously, most likely using a database                                                                    | This would keep each caught up with up to date information on each version                                                                                                                                                  |
|   7    | Settings page                    | Allows the user to change specifics of the application, Accessibility settings, privacy Etc.                                                                       | This would provide more accessibility for students with specific needs, eg. larger font or changing the theme of the project                                                                                                |
|   8    | Email Embedding                  | This will filter emails to ones by the university or UCAS and present the user.                                                                                    | This makes the application process to university easier as any important emails that are sent can be seen by the student.                                                                                                   |
|   9    | Task Menu                        | This will allow the university to set "tasks" for matriculating students to do, as well as a deadline which will add to the calender                               | This would centralize each of the tasks that the student has to do before matriculation eg. Applying for accommodation or confirming with your school                                                                       |
|   10   | Societies Page                   | This gives an opportunity for matriculating students to research more about student life at their university, with a filter button for each uni they've applied to | This will encourage students to get more involved and feel more at home at their university                                                                                                                                 |
|   11   | Real time notifications          | This would send notifications to the user telling them whenever a new email/message has come in                                                                    | This will ensure that students are kept as up to date as possible                                                                                                                                                           |

---

## Decomposition of the Problem

As I approach the design of EdVenture, a crucial aspect in correctly
approaching the design of my solution is to decompose the project into a
variety of sub-problems which I will tackle separately and will allow me
to effectively modularise the Project into individual functions which will
allow me to easily test and isolate each feature of the solution.


---

## Design of the Logo

Firstly, in the graphical design of EdVenture, I have decided to create
the logo for EdVenture, as it is the first impression of the application
to any prospective University or Student user.

I have created a logo which is simple and has an education oriented design.
Of this design, I have created 2 alternative designs and presented these to
a sample of my clientele, of which I will display their feedback to each
corresponding design below:

![logoDesign1.png](https://github.com/Jamiephillips915/EdVenture/blob/main/Images/logoDesign1.png)
<div style="text-align: center;">(Design 1)</div>

Upon presenting the first Design to my clientele
members: Lydia Vogiatis, Mohammed Alawami, Noah West
, Henry Holland and Bin Amir Hamnah Binti Abdul Halek, they have
stated that while they like the concise and
simple design of the Letters, they disprove of
the colour scheme, citing that it gives a younger
aesthetic than what university students would
appreciate.

I attempt to remedy this with my next two designs, as I seek a more modern
sleek design that may appeal greater to university aged students.

![logo.png](https://github.com/Jamiephillips915/EdVenture/blob/main/Images/logo.png)
<div style="text-align: center;">(Design 2)</div>

This second design received highly positive feedback from my sample
clientele, citing that they like the darkened gradient theme over the 
primary bright colours.

![logoDesign2.png](https://github.com/Jamiephillips915/EdVenture/blob/main/Images/logoDesign2.png)
<div style="text-align: center;">(Design 3)</div>

This third design was considered an improvement from the first design
by my sample clientele, but they were worried that the 3rd design would
conflict with accessibility settings such as a dark mode.

Overall, in accordance with my client feedback, I will go with the 
second design as my main logo for EdVenture.

---




<STYLE>
* {
font-size: 1.05rem;
color: #453A3A;
font-family: "Helvetica";
}
</STYLE>
