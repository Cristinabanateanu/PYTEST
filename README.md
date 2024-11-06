Project: Text Transformation Tool

This project is a simple text transformation application that provides basic text formatting capabilities, with clear functionality
and testing to ensure reliability. Below is an overview of the steps taken to implement and document this project.


1. Repository Setup
I cloned the repository BigDataInitialSetupPython and set up my environment.


2. Application Overview
This application provides a straightforward tool to transform text by offering users two primary options:

Convert text to uppercase.
Convert text to lowercase.
Main Function

The main function serves as the interface, displaying available options and prompting the user to:

Choose a transformation type (uppercase or lowercase).
Enter the text to be transformed.
Based on the user’s selection, the application converts the text and displays the result. If the user selects an invalid option, an error message is displayed.

Helper Functions

The app includes two main helper functions:

to_uppercase: Converts input text to uppercase.
to_lowercase: Converts input text to lowercase.
This interactive application relies on user input, making it intuitive and easy to use for basic text transformations.



3. Testing Approach
To ensure the application's reliability, I implemented three types of tests:
Unit Tests (TestAppUnit)

Test individual functions (to_uppercase and to_lowercase) to verify each works independently and as expected.
-Unit Tests (TestAppUnit): Test individual transformation functions (to_uppercase and to_lowercase) to ensure they work independently.
<img width="669" alt="unit testing" src="https://github.com/user-attachments/assets/30d640c5-1412-4435-854e-48fa00f9fb08">

Integration Tests (TestAppIntegration)
Validate the interaction within the main function, ensuring inputs and outputs integrate seamlessly.
<img width="702" alt="integration testing" src="https://github.com/user-attachments/assets/b3e41f9d-b88a-4c14-b449-26cc21f462da">

Functional Tests (TestAppFunctional)
Simulate complete scenarios to test the application's behavior under various use cases, including invalid inputs.
<img width="715" alt="functional testing" src="https://github.com/user-attachments/assets/4f7394c2-76ca-42f0-8bcf-94bd62a09682">
All tests run successfully without errors.

4. Running the Application
The application can be opened in a browser using the command:: pythhon3 -m http.server
<img width="684" alt="Screenshot 2024-11-06 at 22 04 31" src="https://github.com/user-attachments/assets/0f6327ac-ce4c-4bc2-811d-d7d5e27ed111">


5. Documentation Generation
The project's documentation was generated for ease of use and further reference.
<img width="1031" alt="Generate documentation" src="https://github.com/user-attachments/assets/35159bc2-003a-4234-9d31-12b10ad6af90">
<img width="1017" alt="Screenshot 2024-11-06 at 21 52 17" src="https://github.com/user-attachments/assets/c00c8aab-9d9d-49bd-8c16-654caccf1b71">

6. Testing Coverage
For insight into testing coverage:
<img width="875" alt="Screenshot 2024-11-06 at 21 55 30" src="https://github.com/user-attachments/assets/0ebbad5c-7ab7-4f34-a573-2e1459646e73">
<img width="789" alt="Screenshot 2024-11-06 at 21 58 22" src="https://github.com/user-attachments/assets/dd3bc05c-7654-4fcd-ab6d-a8136ab2f3c3">

7. Running in a Container
The application is containerized for easy deployment and consistency across environments.
<img width="1470" alt="runingContainer" src="https://github.com/user-attachments/assets/df99c8d1-5804-47c7-8cc0-8c942849f160">

<img width="1470" alt="Running container" src="https://github.com/user-attachments/assets/499265d3-6015-43c4-8d64-eb174a91ea1e">




Technologies Used
The following technologies and tools were used in this project:

Python: The main programming language used for the application's logic and functions.
Git & GitHub: Version control and repository hosting for project tracking and collaboration.
VS Code: The primary code editor used for writing, debugging, and managing the project’s code.
Unit Testing (unittest in Python): For testing individual functions like to_uppercase and to_lowercase.
Integration Testing: To validate the main function's interaction with helper functions.
Functional Testing: To simulate real-world scenarios and ensure the application behaves as expected.
HTTP Server (http.server in Python): To serve the application locally in a browser for testing and demo purposes.
Containerization (Docker): For creating a containerized version of the application, simplifying deployment and ensuring consistency across environments.





