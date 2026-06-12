# ASCII Art API

This project is a Django backend that converts images into ASCII art using **jp2a**.

## Requirements

This project requires **jp2a** to be installed on the system.

### Ubuntu / Debian

```bash
sudo apt install jp2a
```

### Arch Linux

```bash
sudo pacman -S jp2a
```

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd asciiart
```

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

Install Python dependencies:

```bash
pip install -r requirements.txt
```

Run the Django development server:

```bash
python manage.py runserver
```

## Features

* Convert images to ASCII art
* REST API built with Django
* Uses jp2a for image processing
* Easy integration with frontend applications
