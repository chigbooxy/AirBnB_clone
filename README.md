# 0x00. AirBnB clone - The console
![Airbnb project image](hbnb.png)
## Project Description

Welcome to the Airbnb Console Clone – a simplified command-line interface (CLI). This project is built as part of the ALX's curriculum project and provides an interactive shell for managing instances of different classes, such as User, amenity, city, place, state, review and the BaseModel where all other classes inherits from.

## Command Interpreter Description
The command interpreter is a fundamental component of the Airbnb Console Clone project, providing an interactive shell for users to interact with the application. It serves as a text-based interface where users can input commands to perform various operations, including creating, displaying, updating, and deleting instances of different classes.

### Key Features:

- **User-friendly-interface:** The command interpreter offers a straightforward and intuitive interface, making it easy for users to navigate and execute commands.
- **CRUD Operations:** Users can seamlessly perform Create, Read, Update, and Delete operations on instances of different classes within the application.(User, Amenity, City, State, Review and BaseModel).
- **Dynamic handling:** - The interpreter dynamically handles different classes, allowing users to work with multiple models such as BaseModel and User.
- **Command Interpreter:** Utilize a command-line interface to interact with the application.
- **Data Serialization:** The interpreter interacts with a custom FileStorage class, ensuring proper serialization and deserialization of data to and from JSON files for persistent storage.

### Usage

To use the Airbnb Console Clone, follow these steps:

1. Clone the repository:

    ```bash
    git clone [The Git Repository URL]
    ```

2. Navigate to the project repository:

    ```bash
    cd AirBnB_clone
    ```

3. Run the console:

    ```bash
    ./console.py
    ```

4. Start interacting with the shell and managing instances.

### Commands
- `create`: Create a new instance of a specified class and save it.
- `show`: Display the string representation of an instance based on the class name and ID.
- `destroy`: Delete an instance based on the class name and ID.
- `all`: Print string representations of all instances based on the class name.
- `update`: Update an instance based on the class name and ID by adding or updating attributes.

## Classes
- `BaseModel`: The base model class with common attributes and methods - serves as a super class for other classes
- `User`: A class representing a user with attributes like email, password, first name, and last name.
- `State`: A class representing a state with attributes such as name
- `City`: A class representing a City with attributes such as name, `state_id`
- `Amenity`: A class representing an amenity with attributes such as name
- `Place`: A class representing a place with attributes such as `city_id`, `user_id`, name, description, `number_rooms`, `number_bathrooms`, `max_guest`, `price_by_night`, latitude, longitude, `amenity_ids`
- `Review`: A class representing a review with attributes such as `place_id`, `user_id`, and text.

## Contributors
- Chigboo Goodluck
- Favour Idowu
