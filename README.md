# GitHub User Information Fetcher

A simple Python project that uses the **Requests module** and **GitHub REST API** to fetch and display basic information about a GitHub user.

## About

This program asks the user to enter a GitHub username, sends a request to the GitHub API, receives the user's information, and displays selected details in the terminal.

## Features

- Takes a GitHub username as input
- Creates a GitHub API URL dynamically
- Sends an HTTP GET request
- Checks whether the requested username exists
- Processes the API response as JSON
- Displays:
  - Username
  - Name
  - Public repositories
  - Followers
  - Following
  - Profile URL

## Technologies Used

- Python 3
- Requests module
- GitHub REST API

## How It Works

```text
User enters GitHub username
          ↓
Create GitHub API URL
          ↓
Send GET request
          ↓
Receive API response
          ↓
Check response status
          ↓
Convert response to JSON
          ↓
Extract user information
          ↓
Display information
```

## Installation

Install the Requests module:

```bash
pip install requests
```

## Usage

Run the program:

```bash
python fetch.py
```

Enter a GitHub username when prompted:

```text
Enter Your Git-Hub Username : torvalds
```

The program will display the available information for that GitHub user.

## API Used

This project uses the GitHub REST API:

```text
https://api.github.com/users/<username>
```

No API key is required for this basic project.

## Concepts Practiced

- Python `requests` module
- HTTP GET requests
- REST APIs
- JSON responses
- HTTP status codes
- User input
- Working with API response data
- Dictionary data access

## Purpose

This project was created to practice using Python's **Requests module** and understand how a Python program can communicate with a real-world API and process the returned data.

## Author

**Gaurav Digari**