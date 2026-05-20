# GitHub User Events Tracker

CLI application developed in Python that consumes the GitHub API to monitor and display user activity events.

## Features

- Track GitHub user activity
- Display Push Events
- Display Issues Events
- Display Watch Events
- Display Pull Request Review Events
- Display Create Events
- Event filtering and organization
- API response handling
- Error handling for invalid users and connection issues

## Technologies

- Python
- Requests
- GitHub REST API

## Supported Events

| Event Type | Description |
|---|---|
| PushEvent | Repository pushes |
| IssuesEvent | Opened/closed issues |
| WatchEvent | Starred repositories |
| PullRequestReviewEvent | Pull request reviews |
| CreateEvent | Repository/branch/tag creation |

## Installation

Clone the repository:

```bash id="4sq8cj"
git clone YOUR_REPOSITORY_URL
