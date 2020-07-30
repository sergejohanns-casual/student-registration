# Student registration system
This is an enrollment system that lets users register for an activity, confirm the registration through an email and recieve an enrollment ticket. In principle it's targeted at students, but it could also be used for other kinds of enrollment.

## Motivation
This is a practice project, which I made to practice building a webapp with Flask, containerising that app with Docker, and writing the entire thing with Emacs.

## Operation
The user goes to the home page and fills in their 'User id', which could take the form of a handle, student number, etc. and the (numerical) id of the activity they would like to enroll in. Activity ids are incremental, so the first activity has id 1, etc. After this the user clicks 'submit' and an email with a confirmation link is sent to the email address associated with the given user id. If the confirmation link is clicked the user is taken to another page where the enrollment is confirmed, and sent a second email containing their ticket (a unique 16-digit hex string).

## Deployment
To build and deploy the system as a docker container, simply `docker build` on the root of the project and run that image in a container. To run the system locally, pip install from the `requirements.txt` to get the dependencies and `flask run` in the `flaskr` directory, ensuring that `FLASK_APP` is set to `student_registration.py`.

Note that `flask run`, which the docker container also uses, is only meant for development servers. If you are planning to run this system in a production environment you should instead use a suitable application server.

## Lackings
Because this is a practice project, more meant to practice the surrounding technologies than making a webapp in general, it is not optimised for usability. There are a couple of really egregious flaws that I could fix in theory, but I already spent considerably more time on this project than I intended. Examples include:

* There is no way to add users or activities through the API, they have to be in json files on startup.
* There is no way to see the current activities for users, they have to know.
* Users have to know the numerical id of an activity, not the name, in order to enroll, which is not very user friendly.

Good thing noone has to use this system. I might rework this project at some point in the future, in which case I would probably fix those flaws, but for now I'm just going to leave things as is.
