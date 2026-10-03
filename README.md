# GitHub User Information Fetcher

A beginner-friendly Python project that uses the **Requests module** and **GitHub REST API** to fetch and display information about a GitHub user.

## 📌 About

This project demonstrates how Python can communicate with a web API using HTTP requests.

The user enters a GitHub username, and the program sends a `GET` request to the GitHub API and displays selected information from the response.

## ✨ Features

- Accepts a GitHub username as input
- Sends an HTTP `GET` request
- Uses the GitHub REST API
- Handles JSON responses
- Checks HTTP status codes
- Displays user information
- Handles invalid usernames and request errors
- Uses a request timeout

## 🛠️ Technologies Used

- **Python 3**
- **Requests**
- **GitHub REST API**

## 📂 Project Structure

```text
GitHub-User-Information-Fetcher/
│
├── github_user.py
└── README.md
```

## ⚙️ Installation

Clone the repository:

```bash
git clone <repository-url>
cd GitHub-User-Information-Fetcher
```

Install the required module:

```bash
pip install requests
```

## ▶️ Usage

Run the program:

```bash
python github_user.py
```

Enter a GitHub username when prompted:

```text
Enter GitHub username: torvalds
```

The program fetches and displays information such as:

```text
Username
Name
Public Repositories
Followers
Following
Profile URL
```

## 🔗 API

This project uses the GitHub REST API user endpoint:

```text
https://api.github.com/users/<username>
```

No API key is required for this basic project.

## 📚 Concepts Practiced

- Python `requests` module
- HTTP `GET` requests
- REST APIs
- JSON data
- HTTP status codes
- Exception handling
- Request timeouts
- Working with dictionaries

## 🎯 Purpose

This project was created to gain practical experience with the **Python Requests module and API communication**.

It is part of my journey of learning Python and building practical automation and cybersecurity-related skills.

## 👤 Author

**Gaurav Digari**
