# Project 1 - Python App (Milestone 1)

In the DSCI 532 labs, you will work in [randomly assigned groups](https://github.ubc.ca/MDS-2019-20/DSCI_532_viz-2_students/blob/master/release/DSCI_532_groups.md) towards creating two interactive visualization apps using Dash, one in Python (using Altair) and one in R (using ggplot2).
There are a total of four milestones, two for each dashboard. 
With these labs, we intend for you to practice and understand the mechanics of creating dashboards, deploying them using Heroku, and implementing principles of effective visualizations (and dashboards) discussed in lecture.
The projects will be developed on GitHub.com in public repos. 
You will be required to set-up a Github repository under the [UBC-MDS](https://github.com/UBC-MDS) organization. 

## Milestone 1: Projet set-up and dashboard proposal

In this milestone, you will set-up your project for development and submit a dashboard proposal. In the second milestone, you will submit the final version of your first dashboard created in python and Altair.

## Submission Instructions (10%):
rubric={mechanics:10}

- Be sure to follow the [general lab instructions](https://ubc-mds.github.io/resources_pages/general_lab_instructions/) that are relevant, while also following the specific instructions described in the [expectations](#expectations) section below.

### Project set-up
- In the [UBC-MDS GitHub organization](https://github.com/UBC-MDS) on github.com, set-up a public repository with a reasonable name for your project. We are using github.com for public repos because we will eventually be using some fancy tooling for your dashboard app deployment (*e.g.,* Heroku) in this project. You will need to put your scripts in a public repo on github.com. Additionally, this will help you build a portfolio of your work you can share with others.
- In your GitHub repository create an appropriate file and directory structure (think about what you learned in [lab 4 from DSCI 521](https://github.ubc.ca/MDS-2019-20/DSCI_521_platforms-dsci_students/blob/master/source/lab4/lab4.md).
- In your GitHub repo, also create the following `.md` files: [LICENSE](#LICENSE), [CONTRIBUTING](#CONTRIBUTING), [CODE_OF_CONDUCT](#CODE OF CONDUCT). More details about these files are given below.

#### CONTRIBUTING

It is a good practice to include information about how others can contribute to your project somewhere in your repository.
This is typically done as a separate file in a repo called `CONTRIBUTING.md` or a section in your README.
Here are some examples of this file:
- [Altair](https://github.com/altair-viz/altair/blob/master/CONTRIBUTING.md)
- [dplyr](https://github.com/tidyverse/dplyr/blob/master/.github/CONTRIBUTING.md)
- [Atom editor](https://github.com/atom/atom/blob/master/CONTRIBUTING.md) (very comprehensive)

If you're interested in this, [here's a quick guide](https://help.github.com/en/github/building-a-strong-community/setting-guidelines-for-repository-contributors) to creating this file from GitHub, but in the meantime, you can use the following snippet as a template:

> We welcome all contributions to this project! If you notice a bug, or have a feature request, please open up an issue [here](). If you'd like to contribute a feature or bug fix, you can fork our repo and submit a pull request. We will review pull requests within 7 days. All contributors must abide by our [code of conduct]().

#### LICENSE

You may have noticed when you create a new repo on GitHub, you're asked to set a license for your project. 
If you do not currently have a preference, we recommend you use the [MIT license](https://choosealicense.com/licenses/mit/) for your project.
You will learn more about licenses in the Workflows and Collaborative Software Development courses later in the program.
If you're curious, [here's a primer](http://swcarpentry.github.io/git-novice/11-licensing/index.html) from Software Carpentry and [a more detailed guide](https://doi.org/10.1371/journal.pcbi.1002598) to licenses.

#### Submission on GitHub.ubc.ca

In the README.md file of your individual `milestone1` homework repo on GitHub.ubc.ca, please include:

- **Important:** the links you provide to your code on GitHub.com should point to a specific commit so we can mark the version you submitted as you continue to work on the project.
- A link to your team's GitHub.com repo (where app development should have started)
- A link to your Code of Conduct (which should be on GitHub.com)
- A link to proposal for your dashboard (`proposal.md`, which should be on GitHub.com, see Proposal section below)
- A link to a description of your app as well as a sketch (which lives in the `README.md` file on GitHub.com)
- A link to your team work contract (which should be on GitHub.ubc.ca)
    - The only file that should be on github.ubc.ca is the team work contract, and this is mostly for privacy reasons

#### Expectations

- You should be committing to git every time you work on this project.
- Every time you work on the project, you should first pull the upstream changes (see section below on how to catch up to a forked repo)
- Your git commit messages should be meaningful. These will be marked. It's OK if one or two are less meaningful, but most should be meaningful and useful.
- After the GitHub.com repository is created, each group member should fork the repository to their personal GitHub.com account and work on the app there, and send pull-requests of their work to the upstream repo that they forked). 
- Another team mate should review, review/critique the contribution (if necessary) and finally accept their teammates' pull request. **Do not accept & merge your own pull request.**
- Use GitHub issues to communicate with their teammates (as opposed to email or Slack)
- You should use proper grammar and full sentences in your README. Point form may occur, but should be less than 10% of your written documents.

> ##### How to catch up to a forked repo if there are changes upstream
>
> The first time you need to catch up, you have to tell your computer where the upstream repo is via (you should do this locally inside your forked version of the repo):
> `git remote add upstream <original_repo_URL>`
>
> Then to catch up this time (and any other time) you type:
>
> `git fetch upstream`
> `git merge upstream/master`
>
> These two commands together are like a git pull from the repo you forked.
> 
> Finally, to update your forked remote, push the upstream changes you now have locally
> `git push`

## Proposal (60%)
rubric={reasoning:40,writing:20}

Your proposal should be no more than 1,000 words. You will also submit a sketch of your app, which is separate from this limit.

When submitting your proposal as a (separate) markdown document (named `proposal.md` which lives on GitHub.com), please include the following sections in this order:

1. Motivation and purpose
2. Description of the data
3. Research questions you are exploring

The proposal will be marked as whole, and you will be assessed on the quality and clarity of your writing, the feasability of what you propose using the writing and reasoning rubrics.

Each of the proposal sections are described below and include an example of what is expected. You don't have to write your own proposal _exactly_ the same as the examples; the examples just serve as a guide. When writing your proposal consider whether what you are proposing is realistic to implement in a two week time frame.

### Section 1: Motivation and Purpose

In a few sentences, provide some motivation for why you are creating a dashboard. What problem is could it solve? What is the "purpose" of the dashboard? Be brief and clear.

Example:

> Missed medical appointments cost the healthcare system a lot of money and affects the quality of care. If we could understand what factors lead to missed appointments it may be possible to reduce their frequency. To address this challenge, I propose building a data visualization app that allows health care administrators to visually explore a dataset of missed appointments. My app will use show the distribution of factors contributing to appointment show/no show and allow users to explore different aspects of this data by filtering and re-ordering on different variables in order to compare factors that contribute to absence.

### Section 2: Description of the data

As mentioned in lecture, in your group of 3 or 4, you are expected to select one of your group members DSCI 531 Lab 4 assignments as a template for your dashboard. 
This is to make sure we do not spend a lot of time looking for a new dataset and understanding it in detail.

If you prefer, you can also choose to visualize your own data **IF ALL MEMBERS OF YOUR GROUP AGREE TO THIS**. Note that the purpose of this first dashboard is to get you familiar with the mechanics of building a dashboard. _If you do choose to use your own data, make sure you clear it with a TA first, and state who approved it in your writeup._ If a TA or instructor has already approved your dataset for DSCI 531 Lab 4, you do not need to get it approved again.

In your proposal, briefly describe the dataset and the variables that you will visualize. Note, all data has to be publicly available since you are required to create a public repo.

Please note, if your dataset has _a lot_ of columns and you plan to visualize them all, provide a high level descriptor of the variable types. For example, indicate that the dataset contains a variety of _demographic variables_ and provide a brief list rather than stating and describing every single variable. You may also want to consider visualizing a smaller set of variables given the short duration of this project.

Example:

> I will be visualizing a dataset of approximately 300,000 missed patient appointments. Each appointment has 15 associated variables that describe the patient who made the appointment (`patient_id`, `gender`, `age`), the health status (`health_status`)of the patient (Hypertension, Diabetes, Alcohol intake, physical disabilities), information about the appointment itself (`appointment_id`, `appointment_date`), whether the patient showed up (`status`), and if a text message was sent to the patient about the appointment (`sms_sent`). Using this data I will also derive a new variable, which is the predicted probability that a patient will show up for their appointment (`prob_show`).

In the above example, column names are specified using backticks. Remember if your dataset has _a lot_ of columns, stick to summaries and avoid listing out every single column. The example also differentiates columns that come with the dataset (i.e. `Age`) from new variables that you might derive for your visualizations (i.e `ProbShow`) - you should make a similar distinction in your write-up.

Another example of a good description of a dataset can be found [here](https://www.kaggle.com/unsdsn/world-happiness) for the World Happiness Report dataset on Kaggle.

> We will be visualizing a data set of the number of deaths by risk factors of 196 countries from 1990 to 2017. The data has 6468 rows and 30 columns including the `country name`, `country code`, `year` and factors (e.g. `Unsafe water source (deaths)`, `Low birth weight (deaths)`, `Smoking (deaths)`, `High blood pressure (deaths)`, `Obesity (deaths)`, `Air pollution (outdoor & indoor) (deaths)` etc). 

(p.s. Data got approved by Firas :) The data was published by "Global Burden of Disease Collaborative Network. Global Burden of Disease Study 2017 (GBD 2017) Results. Seattle, United States: Institute for Health Metrics and Evaluation (IHME), 2018". It could be downloaded [here](https://ourworldindata.org/air-pollution).) 

### Section 3: Research questions and usage scenarios

The purpose of this section is to get you to think about how someone else might use the app you're going to design, and to think about those needs before you start coding. 
In Block 2, you learned about several versions of research questions - we will again focus on descriptive and exploratory research questions. 
Revise your research question(s) based on the feedback of your peers, and state them in this section.
Then, consider how the dashboard can be used to answer your research question(s) by a fictional person - these are usage scenarios.

Usage scenarios are typically written in a narrative style and include the specific context of usage, tasks associated with that usage context, and a hypothetical walkthrough of how the user would accomplish those tasks with your app. 
If you are using a Kaggle dataset, you may use their "Overview (inspiration)" to create your usage scenario, or you may come up with your own inspiration.

An example usage scenario with tasks (tasks are indicated in brackets, i.e. [task])

> What's the top 5 risk factors that caused the largest amount number of death in 2017?
> What's these risk factors look like among coutries in 2017?
> What's the trend of these risk factors over time by continents?


> Mary is a policy maker with the Canadian Ministry of Health and she wants to understand what factors lead to missed appointments in order to devise an intervention that improves attendance numbers. 
She wants to be able to [explore] a dataset in order to [compare] the effect of different variables on absenteeism and [identify] the most relevant variables around which to frame her intervention policy. 
When Mary logs on to the "Missed Appointments app", she will see an overview of all the available variables in her dataset, according to the number of people that did or did not show up to their medical appointment. 
She can filter out variables for head-to-head comparisons, and/or rank order patients according to their predicted probability of missing an appointment. 
When she does so, Mary may notice that "physical disability" appears to be a strong predictor missing appointments, and in fact patients with a physical disability also have the largest number of missed appointments. 
She hypothesizes that patients with a physical disability could be having a hard time finding transportation to their appointments, and decides she needs to conduct a follow-on study since transportation information is not captured in her current dataset.

Note that in the above example, "physical disability" being an important variable is fictional - you don't need to conduct an analysis of your data to figure out what is important or not, you just need to imagine what someone could find, and how they may use this information.

## Description of your app & sketch (20%)
rubric={viz:20}

Building from your research questions and usage scenarios, give a high-level description of the interface for the app you will build. Remember to be realistic about your expectations and plans since you will actually be implementing this app.
This content should be about 200-300 words and live in the `README.md` file of your GitHub.com repository.

In this description you are not required to use terminology specific to Dash apps (i.e. widgets, components, etc...) or make reference to specific Python or R libraries. 
Your sketch can be hand-drawn or mocked up using a graphics editor. 
If you can show the app visual design & interaction design in a single image that is ideal, but if you need more space to show some other planned features of your app you can include up to a total of THREE images for this proposal. 
The sketch should be posted in the `README.md` file of your GitHub.com repository underneath the high level description.

**Though you are welcome to commit code to your repo to build your dashboard, you will not be marked for your dashboard in Milestone 1.**.

Example description

> The app contains a landing page that shows the distribution (depending on data type, bar chart, density chart etc) of dataset factors (hypertension, physical disabilities etc.) coloured coded according to whether patients showed up or didn't show up for an appointment. From a dropdown list, users can filter out variables from the distribution display, by patient demographics (i.e. only show female patients), by appointment data (i.e. if SMS was sent), and finally by the date range of appointments. A different dropdown menu will allow users to re-order variables according to the probability of patients being a no-show or in alphabetical order to comorbidities. Users can compare the distribution of co-morbidities by scrolling down through the app interface.

**Example sketch**

The example sketch shows the visual design of the app and one interactive feature (a tooltip).
```{python}
#![dashBoard](AppSketch.png "App Sketch")
```
*A further note on the app sketches:* 

I've choosen to draw up my sketch using Powerpoint and using icons from the [noun project](https://thenounproject.com/). You can use others graphics tools (i.e. Photoshop, Illustrator, GIMP, or Inkscape, etc.) or you can even draw you app by hand and upload the scanned version of your drawing. Whatever you choose to do, make sure that the final image in your report is legible. Please note, this is a very basic illustrative guide to help you in this milestone, it is by no means the limit of what you should submit. 

## Team Contract and Code of Conduct (10%)
rubric={reasoning:10}

In the first lab session, you will be creating a team work contract and a code of conduct. 
This document will govern your working relationship and if done correctly, should help you manage and resolve any issues that arise.

### Team work contract

A team work contract communicates specifically **how** the core group of people who are working together and gives more detail about the logisitics of working together and the expectations you have for each other.
Some aspects of the team work contract could be:
- How will work be distributed in a fair and equitable way?
- What are the expected work hours for the project? 
- How often will group meetings occur ([here is a nice article](http://third-bit.com/2018/05/11/meetings.html) on meetings)? 
- Will you have meeting agendas and minutes? If so, what will be the system for rotating through these responsibilities?
- What will be the style of working? 
    - Will you start each day with [stand-ups](https://www.atlassian.com/agile/scrum/standups), or submit a summary of your contributions 4 hours before each meeting? or something else?
- What is the quality of work each team member expects from themselves and each other?
- When are team members not available (e.g., evenings and Sundays because of family obligations). 
- And any other similar things that govern your working relationships.

Use this opportunity to use your prior knowledge/experience to improve your teamwork, communication, leadership, and organizational skills. 
You will need all of these for your capastone projects (and beyond)!

#### Activity for building a team work contract

In the first lab, we will do the activity below to generate the team work contract:

- Each team member needs 4 post-it-notes and a marker
- For 5 minutes, each team member will silently write out 4 different suggestions for the team work contract
- Next, as a team arrange the sticky notes on the wall and put similar suggestions together
- Each group member should then draw a dot/circle on the suggestions they support
- Spend 10 -15 minutes discussing the suggestions and decide which ones you will use for your team contract (you can of course add new ones at this point if any were missed in the earlier stages of the activity)

#### Team work contract resources:
- [What is a team ground rule or team working agreement](https://agilefaq.wordpress.com/2007/11/21/what-is-a-team-ground-rule-or-team-working-agreement/)

### Code of Conduct

In an attempt to create a safe, positive, productive, and happy community, many organizations and developers create a code of conduct for their projects.
A code of conduct in a Data Science project informs others of social norms, acceptable behaviour and general etiquette.
It is more outward facing than the team work contract discussed above.
We recommend [Project Include](https://projectinclude.org/writing_cocs) for a comprehensive guide to writing an effective Code of Conduct.

At minimum, we believe that a good/effective code of conduct should include:

- A Statement on diversity and inclusivity
- Details on expected, and unacceptable behaviour
- A list of consequences for unacceptable behaviour
- A procedure for reporting and dealing with unacceptable behaviour

#### Sample Codes of Conduct:

  - [UBC Data Science 100 CoC](https://github.com/UBC-DSCI/dsci-100/blob/master/CODE_OF_CONDUCT.md)
  - [idocde Coc](http://www.idocde.net/pages/35)
  - [Python Community CoC](https://www.python.org/psf/conduct/)
  - [Tidyverse CoC](https://github.com/tidyverse/tidyverse.org/blob/master/CODE_OF_CONDUCT.md)
  - [Pandas CoC](https://github.com/pandas-dev/pandas-governance/blob/master/code-of-conduct.md)
  - [Vox Media CoC](http://code-of-conduct.voxmedia.com/?_ga=1.62865454.308680892.1455143920)
