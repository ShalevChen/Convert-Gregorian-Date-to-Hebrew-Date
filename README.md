
# Hebrew Date Converter

This is a simple web application that converts Gregorian dates to Hebrew dates using Python, Flask, JavaScript, and the Hebcal API.

## Prerequisites

Before you begin, make sure you have the following installed on your machine:

- **Python 3.x**
- **Pip** (Python package manager)
- **A modern web browser**

### 1. Install Python and Pip
You can download and install Python from [here](https://www.python.org/downloads/). Pip is included automatically with Python.

### 2. Install Node.js (Optional for frontend work)
If you plan to modify the frontend or use JavaScript-related features, make sure you have [Node.js](https://nodejs.org/) installed. However, this is optional for running the backend only.

---

## Setup Instructions

Follow these steps to set up and run the application:

### 1. Clone the Repository

Clone the repository to your local machine by running the following command:

```bash
git clone <repository-url>
```

If you don't have Git installed, you can download the repository as a ZIP file and extract it.

### 2. Install Python Dependencies

Navigate to the project folder where the files are located.

Install the necessary Python libraries using pip:

```bash
pip install -r requirements.txt
```

If you don’t have the `requirements.txt` file, you can manually install the required dependencies:

```bash
pip install Flask requests flask-cors
```

### 3. Install JavaScript Dependencies (Optional)

If you want to modify the frontend or run JavaScript tasks, install the required Node.js packages. In the project folder, run:

```bash
npm install
```

### 4. Set Up the Flask Backend

Make sure your Python server (`server.py`) is ready. This file will handle incoming requests from the frontend and convert the date using the **Hebcal API**.

---

## Running the Application

### 1. Run the Flask Server

Start the Python backend server by running:

```bash
python server.py
```

This will start a local web server, usually at `http://127.0.0.1:5000/`.

If you have any issues or want to run it publicly, you can adjust the Flask settings to listen on all IPs:

```python
app.run(debug=True, host='0.0.0.0', port=5000)
```

### 2. Access the Web Interface

Open your web browser and go to:

```
http://127.0.0.1:5000/
```

This will show the page where you can select a Gregorian date and convert it to a Hebrew date.

---

## How to Use

1. **Open the web page** in your browser.
2. **Select a date** using the date picker.
3. **Click "Convert"** to send the request to the server and get the corresponding Hebrew date.

---

## Troubleshooting

If you face any issues, here are some common solutions:

- **CORS error**: If you get a CORS error, make sure that the `flask-cors` library is installed and imported in the `server.py` file.
  
  To install it, run:

  ```bash
  pip install flask-cors
  ```

  And in your `server.py`, make sure you add this:

  ```python
  from flask_cors import CORS
  CORS(app)
  ```

- **API request issues**: If the API does not return the expected result, check that the URL and parameters are correctly formatted in the Python code. You can print the parameters being sent to the Hebcal API to debug.

---

## Files Structure

Here’s an overview of the project’s files:

```
/hebrew_date_converter
├── server.py          # Python server file (Flask)
├── script.js          # JavaScript for handling frontend actions
├── index.html         # Frontend HTML page
├── requirements.txt   # List of required Python libraries
├── README.md          # This file
```

---

## Credits

- **Hebcal API**: The Hebrew date conversion is powered by the Hebcal API. You can learn more at [https://www.hebcal.com](https://www.hebcal.com).

---

## License

This project is licensed under the MIT License.
