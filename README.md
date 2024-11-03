<h1 align="center" style="border-bottom: none">
    Student and Teacher Support Platform
</h1>


<div align="center">
 <a href="https://github.com/kestra-io/kestra/releases"><img src="https://img.shields.io/github/tag-pre/kestra-io/kestra.svg?color=blueviolet" alt="Last Version" /></a>
  <a href="https://github.com/kestra-io/kestra/blob/develop/LICENSE"><img src="https://img.shields.io/github/license/kestra-io/kestra?color=blueviolet" alt="License" /></a>
  <a href="https://github.com/kestra-io/kestra/stargazers"><img src="https://img.shields.io/github/stars/kestra-io/kestra?color=blueviolet&logo=github" alt="Github star" /></a> <br>
<a href="https://kestra.io"><img src="https://img.shields.io/badge/Website-kestra.io-192A4E?color=blueviolet" alt="Kestra infinitely scalable orchestration and scheduling platform"></a>
<a href="https://kestra.io/slack"><img src="https://img.shields.io/badge/Slack-Join%20Community-blueviolet?logo=slack" alt="Slack"></a>
</div>

Videos!

<h1 align="center" style="border-bottom: none">
    About Project
</h1>

**The Student and Teacher Support Platform** is an innovative solution designed to make educational processes more effective, accessible, and holistic in a digital environment. The project provides tools that enable teachers to easily prepare lesson content, while also allowing students to quickly access learning materials, analyze their skills and areas of success or difficulty, and receive mentor support whenever needed. By focusing on the needs of both students and teachers, the platform aims to make educational processes more efficient and interactive.

- The basic structure of the project has been established, and initial configurations are complete.
- Layers were designed by analyzing the View, Controller, and Layout components.
- Necessary Entity classes were defined and configured.
- Entity Core packages were integrated into the project, providing the required dependencies.
- The theme was successfully integrated into the project and adapted to be compatible with the Turkish language.
- The Context class was created, and the database connection was successfully established.
- Relevant references were defined, and DbSet properties were configured in the Context class.
- Migration processes were completed, and the database configuration was implemented smoothly.
- The ViewComponent folder was created, necessary classes were added, and it was made functional.
- Relevant Controller classes were created, and workflows were organized.
- Performance optimizations were achieved by focusing on ComponentPartial View usage and Await Async structures.

This project was developed using the ASP.NET Core 8.0 framework and incorporates various technologies commonly used in modern web applications. The project operates on a PostgreSQL database using the Microsoft.EntityFrameworkCore.PostgreSQL 6.0.3 library.

## Technologies and Approaches Used

### Controller and View Components
The best practices of the MVC architecture have been followed to ensure a clear separation between the control and view layers of the application.

### Code First Approach
The database modeling was implemented using the Code First approach, and the database structure was defined in the code.

### LINQ and Entity Framework Queries
Powerful and readable queries were created using LINQ for database operations; Entity Framework was utilized in the data access layer to optimize data management processes.

### N-Tier Architecture
The project uses an N-Tier architecture, with a layered structure that allows each component of the application to be managed and developed independently:
- **Entity Layer:** Represents the core entities of the application.
- **Data Access Layer:** Interacts with the database.
- **Business Layer:** Contains business rules and logic.
- **Presentation Layer:** Manages the user interface.

### Layout and View Management
The view management of the application is structured according to modern design principles. A responsive design was adopted to enhance the user experience.

### API Sections
The project includes necessary APIs to facilitate application functionality and data access. API configurations can be detailed further if needed.

## Important Features

- **_LessonView Component**: This component, added to the homepage, displays lessons retrieved from the PostgreSQL database. Within _LessonComponentPartial, users can navigate to topics filtered by _SubjectComponentPartial through the "Topics" button.

- **_SubjectComponentPartial**: This component enables filtering among lessons and retrieves data from the PostgreSQL database. It includes two main buttons:
  - **Go to Test**: This button connects to the Quiz API, providing users with a test analysis.
  - **Topic Explanation**: Directs the user to the topic explanation page, where they can create real-time presentations by clicking the "Create Presentation" button, integrated with the Presentation API.

- **_MentorsComponentPartial**: Created to provide mentor support, this component retrieves mentor information from the PostgreSQL database and includes two key features:
  - **Appointment System**: Allows students to schedule sessions with mentors.
  - **Messaging System**: Enables direct communication with mentors.

- **_TeamComponentPartial**: The team members component displays information on team members, retrieved from the database.

- **Pre-made Presentations**: An active button provides access to pre-made presentations stored in the PostgreSQL database, which can be filtered among different lesson materials.

# Getting Started

## Installation Instructions

1. **Install Requirements:**
   - To run the project, you need to have the .NET SDK and Python installed. You can download the necessary software from the following links:
     - [Download .NET SDK](https://dotnet.microsoft.com/download)
     - [Download Python](https://www.python.org/downloads/)

2. **Download Project Files:**
   - Clone the project from GitHub or download it as a ZIP file.
   ```bash
   git clone https://github.com/username/project_name.git

3. **Install Required NuGet Packages:**

   - Open a terminal or command prompt in the project directory and run the following command:
    ```bash
   dotnet restore

4. **Install Python Dependencies::**

   - Open a terminal in the Python directory and run the following command to install the required dependencies:
    ```bash
   pip install -r requirements.txt

   
5. **Start Your Project:**

   - Run the following command in the project directory to start the application::
    ```bash
   dotnet run