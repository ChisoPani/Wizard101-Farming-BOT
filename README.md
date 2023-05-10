# Wizard101-Farming-BOT
This bot is designed to automate gameplay in Wizard101. It will move the player character around, engage in battles, and choose spells based on the player's current health.


  <h1>Wizard101 Bot</h1>
  <p>This bot is designed to automate gameplay in Wizard101. It will move the player character around, engage in battles, and choose spells based on the player's current health.</p>

  <h2>Features</h2>
  <ul>
    <li>Automated movement using keyboard emulation.</li>
    <li>Recognizes the start of a battle by searching for a particular image on the screen.</li>
    <li>Continually checks the player's health during battles.</li>
    <li>Casts different spells based on the player's health.
      <ul>
        <li>If health is below a certain threshold, it will cast a healing spell (Pixie).</li>
        <li>If health is above that threshold, it will cast an attack spell (Epic and Sandstorm).</li>
      </ul>
    </li>
  </ul>

  <h2>Dependencies</h2>
  <p>This bot uses several Python libraries:</p>
  <ul>
    <li><code>pyautogui</code>: Used for GUI automation, which includes taking screenshots and simulating keyboard inputs.</li>
    <li><code>pytesseract</code>: An OCR tool for Python, used to read the player's health from the screen.</li>
    <li><code>cv2</code>: OpenCV, used for image processing tasks.</li>
    <li><code>numpy</code>: Used for numerical operations with arrays and matrices.</li>
    <li><code>PIL</code>: Python Imaging Library, used for opening, manipulating, and saving different image file formats.</li>
    <li><code>pygetwindow</code>: Used for getting the Wizard101 window and bringing it to the foreground.</li>
  </ul>

  <h2>Installation</h2>
  <ol>
    <li>Clone this repository to your local machine.</li>
    <li>Install the required Python Dependencies.</li>
    <li>Download and install <a href="https://github.com/UB-Mannheim/tesseract/wiki">Tesseract OCR</a>. Make sure to add the Tesseract path to your system's PATH or specify the path in the script with <code>pytesseract.pytesseract.tesseract_cmd</code>.</li>
  </ol>

  <h2>Usage</h2>
  <ol>
    <li>Run the game and place the character in the area where you want the bot to function.</li>
    <li>Run the bot script using Python. The bot will start moving the character around and engage in battles.</li>
    <li>To stop the bot, simply bring the terminal to the foreground and stop the script (usually with <code>Ctrl+C</code>).</li>
    <li>Currently this is configured for a balance wizard that has 5 spells in their deck, 2 epics, 2 sandstorm and a pixie.<li>
    <li>This script does works intendend but not 100% might have issues with OCR. To get the best result <code><strong>RUN wizard101 on maximum screen resolution possible to you and without going fullscreen, and change the ui size to normal/regular. <strong></li> </code>
  </ol>

  <h2>Customization</h2>
  <p>This bot is designed to work with specific images for recognizing the start of a battle and the spells. To customize the bot for your needs, replace the images in the script with your own. Make sure to also adjust the health threshold according to your needs.</p>

  <p>Please note that this README assumes the reader has a basic understanding of Python and command line usage. Adjust accordingly based on your target audience.</p>

