# Food Tracker System Documentation

## Overview
The Food Tracker is a Django-based web application designed to manage food items, donation centers, and user registrations. It provides functionalities for users to register, log in, add food items, search donation centers, and generate reports on food surplus and distribution.

## Project Structure
- `food_track/`: Django project configuration files.
- `track/`: Main application containing models, views, forms, templates, and static files.
- `manage.py`: Django management script.
- `requirements.txt`: Python dependencies.
- `Dockerfile`: Containerization setup.
- `DOCUMENTATION.md`: This documentation file.

## Key Components

### Models
- `FoodItem`: Represents food items with attributes like name, quantity, category, surplus status, and associated donation center.
- `DonationCenter`: Represents donation centers with name and location.

### Views
- `home`: Displays all food items and statistics on surplus and non-surplus quantities.
- `landing`: Landing page for unauthenticated users.
- `login_view`: Handles user login.
- `logout_view`: Handles user logout.
- `register_view`: Handles user registration with simplified password validation.
- `add_food`: Allows adding new food items.
- `report`: Generates reports on food items and categories.
- `pickup_confirm` and `pickup_food`: Manage food pickup confirmations.
- `search_donation_centers`: Search functionality for donation centers.

### Forms
- `FoodItemForm`: Form for adding food items.
- `DonationCenterSearchForm`: Form for searching donation centers.
- `CustomUserCreationForm`: Custom user registration form with simplified password validation.

### Templates
Located in `track/templates/track/`, includes HTML files for all views such as `home.html`, `login.html`, `register.html`, `add_food.html`, `report.html`, etc.

### Static Files
Located in `track/static/track/`, includes CSS and other static assets.

## Running the Application
1. Install dependencies from `requirements.txt`.
2. Run database migrations.
3. Start the development server using:
   ```
   python manage.py runserver
   ```
4. Access the application at `http://127.0.0.1:8000/`.

## Notes
- The registration form uses a custom user creation form that simplifies password requirements for ease of use in a school project context.
- The system uses PostgreSQL as the database backend; ensure the database is properly configured.
- There is a known collation version mismatch warning in the database; consider rebuilding objects or refreshing collation version as per PostgreSQL documentation.

## Future Improvements
- Enhance password validation for production use.
- Add user roles and permissions.
- Improve UI/UX design.
- Add API endpoints for integration.

## Contact
For questions or support, please contact the project maintainer.
