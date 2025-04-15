# Tasks Overview

This repository contains tasks to assess your skills in scripting, Kubernetes, Helm, Docker, and Bash. Follow the instructions for each task and submit your solutions.

---

## Task 1: Simple Disk Usage Reporter
- **Goal**: Monitor disk usage in your home directory.
- **Requirements**:
  - Write `disk_report.sh` to:
    - Scan the current directory.
    - List the top 5 largest subdirectories and their sizes.
    - Save the output to `disk_report.txt`.

---

## Task 2: Install and Configure a Helm Chart
- **Goal**: Deploy a web application using Helm.
- **Requirements**:
  - Install the WordPress Helm chart.
  - Configure `values.yaml`:
    - Username: `admin`, Password: `admin_password`, Email: `admin@example.com`.
    - Database password: `db_password`.
    - Enable persistent storage.
  - Deploy and verify the application.

---

## Task 3: Containerize a Python Flask App
- **Goal**: Make the app accessible at `http://localhost:5001`.
- **Requirements**:
  - Write a `Dockerfile` for the Flask app.
  - Build the Docker image.
  - Run the app in a container.

---

## Task 4: Simple Log Analyzer Tool
- **Goal**: Analyze log files.
- **Requirements**:
  - Write `log_analyzer.sh` to:
    - Take a log file as an argument.
    - Count `[ERROR]`, `[WARNING]`, and `[INFO]` lines.
    - Output counts to the console.
    - Save `[ERROR]` lines to `errors_only.log`.

---

## Task 5: Create a ConfigMap and Use It in a Pod
- **Goal**: Inject configuration into a Kubernetes Pod.
- **Requirements**:
  - Create a ConfigMap with:
    - `ENV=dev`, `DEBUG=true`.
  - Create a Pod using `busybox` to:
    - Print the variables (`$ENV`, `$DEBUG`).
    - Sleep for 3600 seconds.

---

## Submission
- Organize each task in its own folder.
- Include scripts, YAML files, and any required deliverables.

Good luck!
