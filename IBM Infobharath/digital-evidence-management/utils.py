"""
Utility functions for the Digital Evidence Management System
"""
import os
from datetime import datetime
from typing import List, Dict, Any


def validate_case_id(case_id: str) -> bool:
    """Validate that case ID is not empty and alphanumeric"""
    return bool(case_id) and case_id.isalnum()


def validate_date(date_str: str) -> bool:
    """Validate date format (YYYY-MM-DD)"""
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def validate_priority(priority: str) -> bool:
    """Validate priority level"""
    valid_priorities = ["Low", "Medium", "High", "Critical"]
    return priority in valid_priorities


def validate_investigation_status(status: str) -> bool:
    """Validate investigation status"""
    valid_statuses = ["Open", "In Progress", "Under Review", "Closed", "Reopened"]
    return status in valid_statuses


def validate_crime_type(crime_type: str) -> bool:
    """Validate crime type is not empty"""
    return bool(crime_type.strip())


def validate_location(location: str) -> bool:
    """Validate location is not empty"""
    return bool(location.strip())


def validate_officer_name(officer_name: str) -> bool:
    """Validate officer name is not empty"""
    return bool(officer_name.strip())


def validate_suspect_name(suspect_name: str) -> bool:
    """Validate suspect name is not empty"""
    return bool(suspect_name.strip())


def validate_evidence_type(evidence_type: str) -> bool:
    """Validate evidence type"""
    valid_types = ["Images", "Videos", "Documents", "Fingerprints", "Digital Devices", "Other"]
    return evidence_type in valid_types


def validate_evidence_description(description: str) -> bool:
    """Validate evidence description is not empty"""
    return bool(description.strip())


def get_current_timestamp() -> str:
    """Get current timestamp in ISO format"""
    return datetime.now().isoformat()


def format_date(date_str: str) -> str:
    """Format date string for display"""
    if validate_date(date_str):
        return date_str
    return date_str


def create_data_directory():
    """Create data directory if it doesn't exist"""
    data_dir = os.path.join(os.path.dirname(__file__), "data")
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    return data_dir


def print_header(title: str):
    """Print a formatted header"""
    print("\n" + "="*60)
    print(title.center(60))
    print("="*60 + "\n")


def print_subheader(title: str):
    """Print a formatted subheader"""
    print("\n" + "-"*60)
    print(title)
    print("-"*60 + "\n")


def print_separator():
    """Print a separator line"""
    print("-" * 60)


def print_success(message: str):
    """Print a success message"""
    print(f"\n✓ {message}")


def print_error(message: str):
    """Print an error message"""
    print(f"\n✗ Error: {message}")


def print_info(message: str):
    """Print an info message"""
    print(f"\nℹ {message}")


def get_valid_input(prompt: str, validator=None, error_msg: str = "Invalid input") -> str:
    """Get validated input from user"""
    while True:
        try:
            user_input = input(prompt).strip()
            if validator is None or validator(user_input):
                return user_input
            else:
                print_error(error_msg)
        except KeyboardInterrupt:
            print_error("Operation cancelled")
            return None
        except Exception as e:
            print_error(f"Unexpected error: {str(e)}")


def get_menu_choice(options: List[str]) -> int:
    """Get a valid menu choice from user"""
    while True:
        try:
            for i, option in enumerate(options, 1):
                print(f"{i}. {option}")
            print()
            choice = input("Enter your choice (number): ").strip()
            
            if not choice.isdigit():
                print_error("Please enter a valid number")
                continue
            
            choice_num = int(choice)
            if 1 <= choice_num <= len(options):
                return choice_num
            else:
                print_error(f"Please enter a number between 1 and {len(options)}")
        except KeyboardInterrupt:
            print_error("Operation cancelled")
            return None
        except Exception as e:
            print_error(f"Unexpected error: {str(e)}")
