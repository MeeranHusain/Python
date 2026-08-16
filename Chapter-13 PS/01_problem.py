# 1. Create two virtual environments, install few packages in the first one. How do you create a similar environment in the second one?

'''
To create two virtual environments and install packages in the first one, you can follow these steps:

    1. **Create the first virtual environment:**
    ```bash
    python -m venv env1
    ```
    
    -----------------------------------------------------------
    2. **Activate the first virtual environment:**
    - On Windows:
    ```bash
    env1\Scripts\activate
    ```
    - On macOS/Linux:
    ```bash
    source env1/bin/activate
    ```
    
    -----------------------------------------------------------
    3. **Install packages in the first virtual environment:**
    ```bash
    pip install package_name1 package_name2
    ```
    
    -----------------------------------------------------------
    4. **Freeze the installed packages to a requirements file:**
    ```bash
    pip freeze > requirements.txt
    ```
    
    -----------------------------------------------------------    
    5. **Deactivate the first virtual environment:**
    ```bash
    deactivate
    ```
    
    -----------------------------------------------------------
    6. **Create the second virtual environment:**
    ```bash
    python -m venv env2
    ```
    
    -----------------------------------------------------------
    7. **Activate the second virtual environment:**
    - On Windows:
    ```bash
    env2\Scripts\activate
    ```
    - On macOS/Linux:
    ```bash
    source env2/bin/activate
    ```
    
    -----------------------------------------------------------
    8. **Install the packages from the requirements file in the second virtual environment:**
    ```bash
    pip install -r requirements.txt
    ```
    
'''
