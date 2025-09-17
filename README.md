# Smart Gym Management System (SGMS)

An **Object-Oriented Programming (OOP) Python project** with a graphical interface for managing a fitness centre.  
The system was developed using OOP principles such as **inheritance, encapsulation, and modularity** to improve maintainability and scalability.

---

## 🚀 Features

### 👤 Member Dashboard
- Register and view member profile (including workout history)  
- Log new workout sessions with date tracking  
- Get personalized **fitness tips** based on BMI  
- Summarize weekly workout activity  

### 🧑‍💼 Staff Dashboard
- Secure login with **access key verification** (`admin`)  
- Register new members and update health information  
- Track equipment usage by members  
- View basic equipment statistics (e.g., most used equipment)  

### 🏋️ Equipment Management
- Add new equipment  
- Start/End usage of equipment (updates availability automatically)  
- Track total usage count of equipment  

### 🎨 GUI (Tkinter)
- **Main Menu**  
- **Member Dashboard**  
- **Staff Dashboard**  
- Console backend logs operations for verification  

---

## 🛠️ System Design

The project consists of **6 main classes**:

- **Person**: Base class for Members and Staff (ID, name encapsulation)  
- **Member**: Inherits Person; manages workouts and health info  
- **Staff**: Inherits Person; manages members and equipment, requires access key  
- **Equipment**: Manages equipment details, availability, and usage count  
- **GUI**: Tkinter-based interface for interaction  
- **SGMS**: Integrates all classes and runs the system  

---

## 🔒 Privacy & Security

- **Encapsulation**: Protects sensitive attributes (ID, name, health info)  
- **Access Key**: Staff must enter a valid key to perform operations  

---

## 📂 Project Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/SmartGymManagementSystem.git
   cd SmartGymManagementSystem

2. Install dependencies:
   ```bash
   pip install tk

3. Run the system:
   ```bash
   python gui.py
