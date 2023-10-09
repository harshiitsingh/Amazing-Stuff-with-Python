# LinkedIn Connection Request Automator

Automate the process of accepting LinkedIn connection requests using Selenium in Python.

## Setup

1. **Download ChromeDriver**: Download the ChromeDriver from [this link](https://www.automationtestinghub.com/download-chrome-driver/).

2. **Setting up ChromeDriver in Selenium**: Follow the guide on [BrowserStack](https://www.browserstack.com/guide/run-selenium-tests-using-selenium-chromedriver) to set up ChromeDriver with Selenium.

3. **Install Required Libraries**: Make sure you have Python and the necessary libraries installed. You can install them using pip:

   ```bash
   pip install selenium



<!-- ### Usage

To use this LinkedIn Connection Request Automator, follow these steps:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/linkedin-connection-automator.git
   ```

2. Navigate to the project directory:

   ```bash
   cd linkedin-connection-automator
   ```

3. Open the `linkedin_connection_bot.py` script in a text editor of your choice.

4. Replace `path_to_chromedriver` in the script with the actual path to your downloaded ChromeDriver executable.

5. Customize the bot according to your preferences, especially the conditions for accepting connection requests.

6. Run the script:

   ```bash
   python linkedin_connection_bot.py
   ```

The bot will automate the process of accepting LinkedIn connection requests based on your configured criteria. -->

### Troubleshooting

If you encounter any issues or errors while using this script, you can refer to the following resources for help:

- **Unable to Use Selenium WebDriver**: If you're having trouble using Selenium WebDriver, you can check out [this Stack Overflow thread](https://stackoverflow.com/questions/76461596/unable-to-use-selenium-webdriver-getting-two-exceptions/76463081#76463081) for solutions and common issues.

- **Browser Opens and Closes Immediately**: If the browser opens and closes immediately, you can watch this [video tutorial](https://youtu.be/ijT2sLVdnPM) for troubleshooting steps.

If you still encounter issues, feel free to open an issue in this repository, providing details about the problem you're facing. We'll do our best to assist you.

### References

This bot was built based on the tutorial by Nick McCullum: [Build a Python Bot with Python Selenium](https://www.nickmccullum.com/build-python-bot-python-selenium/). You can refer to this tutorial for additional insights and guidance.

### Extra Features to be added

Following extra features that can be added in the bot:

- **Starting ChromeDriver with Existing Login**: The bot can start ChromeDriver with an existing LinkedIn login instead of starting in guest mode, allowing you to automate actions as an authenticated user.

- **Customized Connection Request Acceptance**: You can customize the conditions for accepting connection requests. For example, you can set it to accept requests only from users with more than 20 mutual connections. Modify the script to meet your specific requirements.

Feel free to contribute to this project by opening an issue or submitting a pull request if you have suggestions, improvements, or additional features to add. Your contributions are welcome!