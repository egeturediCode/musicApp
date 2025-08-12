
musicApp is a simple music application built with Django. The project includes basic CRUD operations, user management, and media file handling features.

---

## Features

- User registration, login, and logout  
- Add, edit, and delete songs  
- Manage media files (album covers, audio files)  
- Easy administration via Django admin panel

---

##  Installation

Follow these steps to run the project locally on your machine.

### Requirements

- Python 3.8 or higher
- Django
- Git  
- Virtualenv (for creating a virtual environment)

### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/egeturediCode/musicApp.git
    
    ```

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv musicApp_env
    source musicApp_env/bin/activate  # Mac/Linux
    musicApp_env\Scripts\activate.bat # Windows
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply database migrations:
    ```bash
    cd musicApp
    python manage.py migrate
    ```

5. Run the development server:
    ```bash
    python manage.py runserver
    ```

6. Open your browser and go to `http://127.0.0.1:8000/`.

---

## Usage

- Access the admin panel at `http://127.0.0.1:8000/admin`.
- Default SuperUser =>
    username:
    ```bash
    user
    ```
    password:
    ```bash
    userpassWorD
    ```
- To create an admin user:
    ```bash
    python manage.py createsuperuser
    ```


---

## Contributing

Feel free to fork the repository and submit pull requests if you'd like to contribute.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contact

If you have any questions or suggestions, feel free to reach out:  
[GitHub Profile](https://github.com/egeturediCode)

---

*Thank you!*
