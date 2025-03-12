# Section 32: Day 32: App 7 - Build a Weather Forecast Dashboard | Part 1

## 282. Coding the User Interface

### Keynotes

1. app with Graphical User Interface (GUI)
2. web app based on streamlit library
3. integrate with weather forecast data
4. first code the User Interface (UI), frotend
5. second code the backend
6. rule: create a prototype (figma).
But for this app an image is available 'App+Design.png'
7. How to run command in venv:
`streamlit run main.py`
8. View the streamlit app:
  Local URL: http://localhost:8501
  Network URL: http://192.168.1.4:8501


## 283. Plotting Data Dynamically

### Keynotes

1. Add the graph part widget
2. Use the Plotly data visualization library.
`pip install plotly`
3. X and Y should be array types of objects (list, tuple, dataframe column etc)
4. x-axis: Date
5. y-axis: Temperature
6. Note: when we run the script Python executes the code.
7. Note: when the user changes the slider (Forecast days)
Python executes the code again from top to bottom.
8. For this part the data are dummy. To be fetched from the Weather Forecast API.