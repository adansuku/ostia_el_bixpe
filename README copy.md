
# Time Tracking Automation with Selenium

This Python script automates time tracking on the Bixpe platform, allowing you to start, stop, pause for breakfast, and resume your workday using Selenium. The script can be run with different flags to handle different actions.

## Requirements

- Python 3.x
- Google Chrome
- [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) (compatible with your Chrome version)

## Setup

Follow these steps to set up the project with a virtual environment and install dependencies.

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```

### 2. Create and Activate a Virtual Environment

#### On Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

#### On Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

With the virtual environment activated, install the required Python packages:

```bash
pip install selenium python-dotenv
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory of your project with the following content:

```
BIXPE_USERNAME=your_bixpe_username
BIXPE_PASSWORD=your_bixpe_password
```

This file stores your Bixpe login credentials and should not be shared publicly.

### 5. Run the Script

You can run the script with different flags to automate specific tasks:

#### To pause for breakfast:

```bash
python script.py --pause
```

#### To resume the workday:

```bash
python script.py --resume
```

#### To register time normally:

```bash
python script.py
```

### 6. Deactivate the Virtual Environment

When you're done working, you can deactivate the virtual environment with:

```bash
deactivate
```

### 7. Optional: Freeze Dependencies

If you want to export the installed dependencies to a `requirements.txt` file:

```bash
pip freeze > requirements.txt
```

### Troubleshooting

- Make sure you have the correct version of ChromeDriver that matches your Chrome browser version.
- Check that the `.env` file is properly configured with your Bixpe credentials.

### License

This project is licensed under the MIT License.
