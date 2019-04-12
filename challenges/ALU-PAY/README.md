<img src="https://raw.githubusercontent.com/code-for-venezuela/2019-april-codeathon/master/assets/alumnUSB.png" alt="AlumnUSB" width="100" />


# Automating scholarship payments

## Who we are
AlumnUSB is a non-profit organization that raises funds for Universidad Simón Bolivar. It has several programs to help the university fulfill its academic mission, including sourcing goods (equipment for laboratories, classrooms, offices, and supplies) and providing grants in the form of scholarships and teaching awards. AlumnUSB is run by USB alumni volunteers around the world who volunteer their time.

## Problem statement
One of AlumnUSB's programs gives financial aid to students of the University with stellar performance. These transfers are made via [Uphold](https://uphold.com) since they handle identity verification and can guarantee that the money arrives directly to the intended recipient. This allows AlumnUSB to operate with transparency.

An AlumnUSB member must manually send transfers to all the grant recipients, a process that currently takes more than two hours every month. We would like a system that automates this process, as it will save a tremendous amount of human time and allow us to scale our operations.

## Challenge

* Make a script that connects to the [Uphold API](https://uphold.com/en/developer/api) to automate AlumnUSB scholarship payments. You are free to define what format would take in the script as a parameter (csv, excel, json, etc). The important parameters are that you script needs to be able to parse are defined in [here](https://uphold.com/en/developer/api/documentation/#create-amp-commit-a-transaction)
* Bonus 1: Make a frontend for this script and have an UI that AlumnUSB's admins can use to interact with the tool you are creating.
* Bonus 2: Create a scheduler that automates the process of when and to whom send the financial aid.

## Skills needed
1. Backend APIs
2. Scripting

## Project Scope

* We believe this project can be done by 2 people focused on the backend (understanding uphold's API, actual building of script backend and documenting how to run/host the solution).
* If you would also like to tackle the frontend, 3-4 people is recommended.

## Project contact
Gabriel Golczer, gabriel@alumnusb.org
