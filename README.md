# Notion Weekly Planner Reset

This project automates the maintenance of a weekly planner in Notion. It uses the Notion API and GitHub Actions to clear old tasks and reset daily pages for the upcoming week.

## Features

- **Automated Clearing**: Deletes all "to-do" blocks within specific daily pages to provide a clean slate.
- **Icon Management**: Automatically updates the page icon to a consistent checkbox emoji (☑️).
- **Template Restoration**: 
    - Inserts a new empty to-do item under the "To-do" heading.
    - Inserts recurring trackers (Weight-in, [KCAL_LIMIT] kcal) under the "Egyéb" (Other) heading.
- **Smart Scheduling**: 
    - **Sundays**: Resets Monday through Saturday pages.
    - **Mondays**: Resets the Sunday page.
    - **Other days**: The script exits without making changes to preserve your current data.

## Setup

### Prerequisites

- A **Notion Integration Token** (Internal Integration Secret).
- A **Parent Page ID** (the ID of the database or page containing the daily sub-pages).
- The `notion-client` Python library.

### GitHub Actions Configuration

To run this automatically, add the following as **Repository Secrets** in your GitHub repository settings (**Settings > Secrets and variables > Actions**):

1. `NOTION_TOKEN`: Your integration secret.
2. `NOTION_PAGE_ID`: The ID of the parent page containing your daily pages.

## Project Structure

- `restart_week.py`: The main Python script containing the logic and API calls.
- `requirements.txt`: Lists the necessary Python dependencies.
- `.github/workflows/daily_reset.yml`: The GitHub Actions workflow file that triggers the script daily at 04:00 UTC.

## Local Execution

To run the script manually for testing, use the following commands in your terminal:

```bash
export NOTION_TOKEN='your_token_here'
export NOTION_PAGE_ID='your_page_id_here'
pip install -r requirements.txt
python restart_week.py# Notion Weekly Planner Reset

This project automates the maintenance of a weekly planner in Notion. It uses the Notion API and GitHub Actions to clear old tasks and reset daily pages for the upcoming week.

## Features

- **Automated Clearing**: Deletes all "to-do" blocks within specific daily pages to provide a clean slate.
- **Icon Management**: Automatically updates the page icon to a consistent checkbox emoji (☑️).
- **Template Restoration**: 
    - Inserts a new empty to-do item under the "To-do" heading.
    - Inserts recurring trackers (Weight-in, [KCAL_LIMIT] kcal) under the "Egyéb" (Other) heading.
- **Smart Scheduling**: 
    - **Sundays**: Resets Monday through Saturday pages.
    - **Mondays**: Resets the Sunday page.
    - **Other days**: The script exits without making changes to preserve your current data.

## Setup

### Prerequisites

- A **Notion Integration Token** (Internal Integration Secret).
- A **Parent Page ID** (the ID of the database or page containing the daily sub-pages).
- The `notion-client` Python library.

### GitHub Actions Configuration

To run this automatically, add the following as **Repository Secrets** in your GitHub repository settings (**Settings > Secrets and variables > Actions**):

1. `NOTION_TOKEN`: Your integration secret.
2. `NOTION_PAGE_ID`: The ID of the parent page containing your daily pages.

## Project Structure

- `restart_week.py`: The main Python script containing the logic and API calls.
- `requirements.txt`: Lists the necessary Python dependencies.
- `.github/workflows/daily_reset.yml`: The GitHub Actions workflow file that triggers the script daily at 04:00 UTC.

## Local Execution

To run the script manually for testing, use the following commands in your terminal:

```bash
export NOTION_TOKEN='your_token_here'
export NOTION_PAGE_ID='your_page_id_here'
pip install -r requirements.txt
python restart_week.py# Notion Weekly Planner Reset

This project automates the maintenance of a weekly planner in Notion. It uses the Notion API and GitHub Actions to clear old tasks and reset daily pages for the upcoming week.

## Features

- **Automated Clearing**: Deletes all "to-do" blocks within specific daily pages to provide a clean slate.
- **Icon Management**: Automatically updates the page icon to a consistent checkbox emoji (☑️).
- **Template Restoration**: 
    - Inserts a new empty to-do item under the "To-do" heading.
    - Inserts recurring trackers (Weight-in, [KCAL_LIMIT] kcal) under the "Egyéb" (Other) heading.
- **Smart Scheduling**: 
    - **Sundays**: Resets Monday through Saturday pages.
    - **Mondays**: Resets the Sunday page.
    - **Other days**: The script exits without making changes to preserve your current data.

## Setup

### Prerequisites

- A **Notion Integration Token** (Internal Integration Secret).
- A **Parent Page ID** (the ID of the database or page containing the daily sub-pages).
- The `notion-client` Python library.

### GitHub Actions Configuration

To run this automatically, add the following as **Repository Secrets** in your GitHub repository settings (**Settings > Secrets and variables > Actions**):

1. `NOTION_TOKEN`: Your integration secret.
2. `NOTION_PAGE_ID`: The ID of the parent page containing your daily pages.

## Project Structure

- `restart_week.py`: The main Python script containing the logic and API calls.
- `requirements.txt`: Lists the necessary Python dependencies.
- `.github/workflows/daily_reset.yml`: The GitHub Actions workflow file that triggers the script daily at 04:00 UTC.

## Local Execution

To run the script manually for testing, use the following commands in your terminal:

```bash
export NOTION_TOKEN='your_token_here'
export NOTION_PAGE_ID='your_page_id_here'
pip install -r requirements.txt
python restart_week.py
