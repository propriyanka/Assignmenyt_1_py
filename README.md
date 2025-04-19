# 🐍 Python Assignment

## 📌 Project Description

This project consists of multiple Python scripts designed to handle various tasks such as password validation, CPU monitoring, configuration management, and file backup automation. Each script serves a specific purpose and follows best practices for security, efficiency, and ease of use.

## 📁 Folder Structure

Python Assessment/
│-- Q1_passwords.py         # 🔐 Password validation script
│-- Q2_monitor_cpu_usage.py # 💻 CPU monitoring script
│-- Q3_configuration.py     # ⚙️ Configuration management script
│-- Q4_backup.py            # 📂 Backup automation script
│-- custom_password_list.txt # 🚫 Custom password blacklist
│-- config.ini              # 📝 Configuration file for Q3
│-- requirements.txt        # 📜 Dependencies
│-- source/                 # 📂 Source directory for backups

## ⚙️ Prerequisites

Ensure you have Python 3 installed and the necessary dependencies from `requirements.txt`.

## 🔧 Installation Instructions

```sh
# 🛠️ Create a virtual environment
python3 -m venv env  # Creates an isolated Python environment

# 🚀 Activate the virtual environment
source env/bin/activate  # On macOS/Linux
env\Scripts\activate     # On Windows

# 📦 Install dependencies
pip install -r requirements.txt  # Installs required packages
```

## 🚀 Usage Instructions

### 🔐 Q1: Password Validation

This script validates passwords based on security policies, checks against a custom blacklist, and provides strength analysis.

#### 📌 Requirements & Configurations

- Uses `custom_password_list.txt` for blacklisted passwords.
- Requires `json` and `shutil` libraries.

#### ▶️ Running

```sh
python Q1_passwords.py
```

#### 🗘️ Screenshots

<p align="center">
  <img src="Assignment_ss/Screenshot_1.png" alt="Q1 Password Validation" width="800">
  <img src="Assignment_ss/Screenshot_2.png" alt="Q1 Password Validation" width="800">
</p>

### 💻 Q2: CPU Monitoring

This script monitors CPU usage and logs critical levels.

#### 📌 Requirements & Configurations

- Requires `psutil` for system monitoring.
- Logs alerts when CPU usage exceeds thresholds.

#### ▶️ Running

```sh
python Q2_monitor_cpu_usage.py
```

#### 🗼️ Screenshot

<p align="center">
  <img src="Assignment_ss/Screenshot_3.png" alt="Q2 CPU Monitoring" width="800">
</p>

### ⚙️ Q3: Configuration Management

This script reads and manages configurations from a `.ini` file.

#### 📌 Requirements & Configurations

- Uses `config.ini` for storing configurations.
- Requires `configparser` for parsing the configuration file.

#### ▶️ Running

```sh
python Q3_configuration.py
```

#### 🗼️ Screenshot

<p align="center">
  <img src="Assignment_ss/Screenshot_4.png" alt="Q3 Configuration Management" width="800">
  <img src="Assignment_ss/Screenshot_5.png" alt="Q3 Configuration Management" width="800">
  <img src="Assignment_ss/Screenshot_6.png" alt="Q3 Configuration Management" width="800">
</p>

### 📂 Q4: Backup Automation

This script automates file backups from a source directory to a destination directory while ensuring unique filenames.

#### 📌 Requirements & Configurations

- Requires `shutil` for file operations.
- Uses `source/` as the default source directory.
- Creates a backup directory automatically if it does not exist.

#### ▶️ Running

```sh
python Q4_backup.py
```

#### 🗼️ Screenshot

<p align="center">
  <img src="Assignment_ss/Screenshot_7.png" alt="Q4 Backup Automation" width="800">
</p>

## 📜 License

This project is licensed under the MIT License.