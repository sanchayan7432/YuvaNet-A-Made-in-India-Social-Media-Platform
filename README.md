# YuvaNet - A Made-In-India Social Media Platform


<p align="center"> <img src="https://github.com/sanchayan7432/YuvaNet-A-Made-in-India-Social-Media-Platform/blob/main/socials/static/images/truffle.png" height=200 /> </p>
<br>



<p align="center">
<a href="https://www.python.org/"><img src="https://forthebadge.com/images/badges/made-with-python.svg" border="0" title="Made with Python" />
</p>

<p align="center">
<a href="http://www.djangoproject.com/"><img src="https://www.djangoproject.com/m/img/badges/djangopowered126x54.gif" border="0" alt="Powered by Django." title="Powered by Django." /></a>
</p>


## Project Overview
```
YuvaNet is a Django based social media website where users can utilize the features exactly as on other straightforward social media websites. The goal of the project was to demonstrate how the most popular web development languages might be utilized to create a straightforward social media website.
As mentioned above, this application system has five vital components/features: 
User registration/authentication, User posts, Search users, Like and Comment on user posts and Follow/Unfollow users. 

• User registration/Authentication: Any  application will include this primary feature to register users in their application. To access all the other features, the user must register into the application. We collect users fundamental data such as email, username, first name, last name, password, and store it in the database. Moreover the users can change their password for security purposes.
 
• Profile modification: This is an extended feature of user registration. Here, users can create and modify their profiles. Users can change their profile picture, email address, and their usernames. The altered data reflects in the database system and the front-end of the application.

• User posts: Once the user has registered and set up a profile, they can post photos and modify them accordingly. Users can like and comment and download the  posts.

• Follow/Unfollow users: The logged in user can follow/unfollow users from the user suggestion section.

• Search users: Users can search other users by entering the username in the search bar provided in the home page. A list of all users matching the username typed will appear as a search result.
``` 


## Code Structure
```
YuvaNet-A-Made-in-India-Social-Media-Platform/
│
├── 📄 README.md
├── 📄 LICENSE
├── 📄 requirements.txt            ← Dependencies (Django, etc.)
│
├── 📂 socials/                   ← Main Django app
│   ├── 📄 __init__.py
│   ├── 📄 admin.py
│   ├── 📄 apps.py
│   ├── 📄 models.py              ← Database models (User Profile, Post, Comment, etc.)
│   ├── 📄 views.py               ← Views that handle request logic
│   ├── 📄 urls.py                ← URL routing for the app
│   ├── 📄 forms.py               ← Django forms (e.g., signup, post creation)
│   │
│   ├── 📂 migrations/            ← Database migrations
│   │   └── ...
│   │
│   ├── 📂 templates/             ← HTML templates
│   │   ├── base.html
│   │   ├── signup.html
│   │   ├── login.html
│   │   ├── profile.html
│   │   ├── post_list.html
│   │   ├── post_detail.html
│   │   └── ...                   ← Templates for all pages like home, edit profile
│   │
│   └── 📂 static/                ← Static resources
│       ├── css/
│       ├── js/
│       └── images/
│
├── 📂 YuvaNet/                  ← Django project config
│   ├── 📄 __init__.py
│   ├── 📄 settings.py           ← Project settings (INSTALLED_APPS, DB, etc.)
│   ├── 📄 urls.py               ← Root URL config
│   └── 📄 wsgi.py
│
├── 📄 db.sqlite3                ← Database storage file generated after migrations
├── 📄 manage.py                 ← Django management script
│
└── 📂 media/                    ← Uploaded images/posts (may be created on run)
```

## GUI Appearance

### Pages
```
- Login Page
- Signup Page
- Create Profile Page
- Edit Profile Page
- Create Post Page
- Delete Post Page
- Update post page
- Password Reset Page
- Home page
- User Profile Page
- Search Results Page
- Post Comment Page
```
### Features
```
- Follow/Unfollow Users
- Like/Unlike the posts
- Download the post images
- Comment on user posts
- User suggestion section
- Search users through the search bar
```
## Tools and Techs

Backend Framework: `Django`
<br/><br/>
Front-end : `Bootstrap, SCSS, HTML,CSS, Javascript`
<br/><br/>
Database: `Sqlite3`
<br/><br/>

## Setup Instructions

1. - Fork the [repo](https://github.com/sanchayan7432/YuvaNet-A-Made-in-India-Social-Media-Platform.git)
   - Clone the repo to your local system
   ```git
   git clone [https://github.com/sanchayan7432/YuvaNet-A-Made-in-India-Social-Media-Platform.git
   cd <path>\YuvaNet
   ```
   Make sure you have latest version of python installed on your system.
2. Create a Virtual Environment for the Project

   If u don't have a virtualenv installed

   ```bash
   pip install virtualenv
   ```
   **For Windows Users**
   ```bash
   virtualenv env_name
   env_name/Scripts/activate
   ```


   **For Linux Users**
   ```bash
   virtualenv env_name
   source env_name/Scripts/activate
   ```

   If you are giving a different name than `env`, mention it in `.gitignore` first

3. Install all the requirements

   ```bash
   pip install -r requirements.txt
   ```

    ```bash
   cd socials
   ```


4. Make migrations/ Create db.sqlite3

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a super user.
   This is to access Admin panel and admin specific pages.

   ```djangotemplate
   python manage.py createsuperuser
   ```
   

   Enter your username, email and password.

6. Run server
   ```bash
   python manage.py runserver
   
  
 ## Visual Documentation

**1. Signup Page**

![Signup page](https://github.com/sanchayan7432/YuvaNet-A-Made-in-India-Social-Media-Platform/blob/main/ScreenShots/1.png)

**2. Login Page**

![Login page](https://github.com/sanchayan7432/YuvaNet-A-Made-in-India-Social-Media-Platform/blob/main/ScreenShots/2.png)

**3. Home/Feed Page**

![Home Page](https://github.com/sanchayan7432/YuvaNet-A-Made-in-India-Social-Media-Platform/blob/main/ScreenShots/3.png)

**4. Comment Display**

![Comment Display](https://github.com/sanchayan7432/YuvaNet-A-Made-in-India-Social-Media-Platform/blob/main/ScreenShots/4.png)

**5. Profile Pages**

**User Profile**

![Show Profile](https://github.com/sanchayan7432/YuvaNet-A-Made-in-India-Social-Media-Platform/blob/main/ScreenShots/5.png)

**Other's Profile**

![127 0 0 1_8000_4_profile_(Nest Hub)](https://github.com/sanchayan7432/YuvaNet-A-Made-in-India-Social-Media-Platform/blob/main/ScreenShots/6.png)


**6. Search Result Users Page**

![Search Result](https://github.com/sanchayan7432/YuvaNet-A-Made-in-India-Social-Media-Platform/blob/main/ScreenShots/7.png)

**7. Create a user profile page**

![Create user profile](https://github.com/sanchayan7432/YuvaNet-A-Made-in-India-Social-Media-Platform/blob/main/ScreenShots/8.png)







## Technical Details






