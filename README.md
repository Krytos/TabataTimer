# Tabata Timer

This is a simple Tabata Timer I created for personal use. Feel free to use it as well. The application uses the `nicegui` library for creating a graphical user interface (GUI) and `asyncio` for handling asynchronous operations.

![Tabata Timer](https://i.imgur.com/KIDzPB5.png)


## Requirements

- Python 3.11
- nicegui library

## Installation

1. Make sure you have Python 3.11 installed on your system.
2. Install the nicegui library by running the following command:

```shell
pip install nicegui
```

3. Copy the code from this repository into your Python file.

## Usage

1. Run the Python file containing the code.
2. The Tabata Timer application will open in a new window.
3. Set the desired values for work time, rest time, and rounds using the input fields.
4. Click the "Start" button to start the timer.
5. The timer will display the minutes, seconds, and milliseconds remaining for each interval.
6. The timer will automatically transition between work and rest intervals according to the specified times and number of rounds.
7. Click the "Stop" button to stop the timer.
8. To restart the timer with new settings, update the input fields and click "Start" again.

## Code Explanation

The code uses the `asyncio` library for handling asynchronous operations, allowing the timer to run without blocking the GUI.

The `reset` function is responsible for resetting the timer labels and round counter.

The `countdown` function is used to update the timer labels during each interval. It also plays audio files at specific times using the `ui.audio` function.

The `main` function is the main logic of the timer. It starts or stops the timer based on the current state of the "Start" button. It iterates through the specified number of rounds and calls the `countdown` function for each work and rest interval.

The code also includes the necessary GUI components for displaying the timer labels, input fields for setting the timer values, and the "Start" button.

## Customization

- You can modify the default values for work time, rest time, and rounds by changing the `value` attribute of the corresponding input fields.
- Customize the GUI layout and styling by modifying the styles applied to the UI components.
- Replace the audio files with your own by specifying the file paths in the `ui.audio` function calls.

Feel free to modify the code according to your requirements and preferences.

**Note:** Make sure to credit the `nicegui` library if you include this code or modified versions of it in your projects.