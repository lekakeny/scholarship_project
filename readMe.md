### Scholarship Application

This is a simple scholarship application website developed on the django framework.

For testing the app, clone the repository into your local machine and a media directory for uploading media files on the directory that contains the django project.

Ensure that you have installed postgresql and is running on your machine. Create a database called djangodb, add a user and grant all privilidges for djangodb to the user. Adjust the settings in your database as per the settings in the settings.py code file.
Open your project folder and start the terminal on the folder. Ensure your virtual environment is activated. The requirements.txt file lists the specific required modules for the successful implementation of the project.

Run "python manage.py makemigrations", then run "python manage.py migrate" to create all the tables necessary to run the application. 

Ensure that your database settings ate correctly configured to avoid possible errors.

Run "python manage.py runserver" command to run the django server

copy the url to your browser

#### Project Description

The application has three user: users applying for sponsorship, sponsors and staff.

The staff are automatically registered by running the command "python manage.py createsuperuser". The staff register the sponsors by creating a user then assigning the role of sponsor in the admin panel through the sponsor model. The staff can also view the various sponsorship application through navigating to staff on the navbar. The staff can approve the applications.

The sponsor can login only after they have been registered by staff. Sponsors after login can view appproved applications and decide which one to sponsor.

The user seeking sponsorship has it very easy because the first view is a step by step wizard application for sponsorship. After submission they will automatically be redirected to a success page otherwise they will get an error and will have to redo the wizard again from the beginning.

### Conclusion
This project is my first django project but I am open to improving it further and working on other related projects. The learning curve could take up to a month.