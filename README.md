
# Flask Forum Application

A fully functional forum application built with Flask, allowing users to create, manage, and interact with posts and comments, with an easy-to-use web interface.

---

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Directory Structure](#directory-structure)
- [Contributing](#contributing)
- [Contact](#contact)

---

## Introduction

This project is a forum application designed to facilitate user interaction through posts and comments. It features a clean and intuitive user interface with support for user authentication, profile management, and dynamic content updates.

---

## Features

### General
- User authentication (Sign up, login, logout)
- Account management (update username, password, and profile picture)
- Posts and comments with category filtering

### Posts
- Create, edit, and delete posts
- Add categories to organize posts
- Track edited timestamps

### Comments
- Comment and rate posts
- Manage comments (create, view, delete)

### Admin
- Admin-only user management tools
- View and delete users

---

## Tech Stack

- **Backend**: Flask, Flask-SQLAlchemy, Flask-Login
- **Frontend**: HTML, Jinja2, Bootstrap
- **Database**: SQLite
- **Others**: WTForms for form validation, Flask-WTF for secure forms

---

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)
- A virtual environment (optional but recommended)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/flask-forum-app.git
   cd flask-forum-app
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv forum_env
   source forum_env/bin/activate  # On Windows: forum_env\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```bash
   python run.py
   ```

5. Run the application:
   ```bash
   python run.py
   ```

The application will be available at `http://localhost:8080`.

---

## Usage

### Pages and Features
1. **Home Page** (`/`): Lists all users and a welcome message.
2. **Sign Up** (`/signup`): Create a new user account.
3. **Login** (`/login`): Log in to your account.
4. **Posts** (`/posts`): View all posts.
5. **Create Post** (`/createpost`): Add a new post.
6. **Edit Post** (`/editpost/<post_id>`): Edit an existing post.
7. **View Post** (`/post/<post_id>`): View a post and its comments.
8. **Account** (`/account`): Manage your account details.
9. **Admin Users** (`/users`): Admin-only page to manage users.

### Example Workflow
1. Sign up or log in to access features.
2. Navigate to the "Posts" page to view all posts.
3. Create a new post or comment on an existing one.
4. Update your profile details on the "Account" page.

---

## Directory Structure

```
forum/
├── __pycache__/         # Compiled Python files
├── static/              # Static files
│   ├── js/              # JavaScript files
│   ├── profile_pics/    # Profile pictures
│   └── stylesheets/     # CSS styles
├── templates/           # HTML templates
│   ├── account.html     # Account management page
│   ├── base.html        # Base layout
│   ├── createpost.html  # Create post page
│   ├── editpost.html    # Edit post page
│   ├── index.html       # Home page
│   ├── login.html       # Login page
│   ├── posts.html       # Posts listing page
│   ├── signup.html      # Sign up page
│   ├── users.html       # Admin user management
│   └── view_post.html   # View individual post
├── instance/
│   └── site.db          # SQLite database
├── forum_env/           # Virtual environment
├── forum/               # Main application package
│   ├── __init__.py      # App initialization
│   ├── forms.py         # Form classes
│   ├── models.py        # Database models
│   ├── routes.py        # Application routes
├── requirements.txt     # Python dependencies
├── run.py               # Application entry point
└── README.md            # Project documentation
```

---

## Contributing

Contributions are welcome! Follow these steps:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your message here"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Submit a pull request.

---

## Contact

For any questions or suggestions, please contact:
- Name: Tony Han
- Email: tonytt2008@qq.com
- GitHub: [Loveroin](https://github.com/Loveroin)
