# EdVenture Documentation

---

## Table of contents

- Design
    - [Target Audience](#target-audience)
    - [Development Methodologies](#development-methodologies)
    - [Success Criteria](#success-criteria)
    - [Decomposition of the Problem](#success-criteria)

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

---

## Decomposition of the Problem

As I approach the design of EdVenture, a crucial aspect in correctly
approaching the design of my solution is to decompose the project into a
variety of sub-problems which I will tackle separately and will allow me
to effectively modularise the Project into individual functions which will
allow me to easily test and isolate each feature of the solution.


---





<STYLE>
* {
font-size: 1.05rem;
color: #453A3A;
font-family: "Helvetica";
}
</STYLE>
