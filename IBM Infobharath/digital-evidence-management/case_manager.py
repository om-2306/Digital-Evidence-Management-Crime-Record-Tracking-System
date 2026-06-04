# """
# Case Manager for managing criminal cases
# """
import json
import os
from typing import List, Optional, Dict, Any
from models import Case
from utils import get_current_timestamp, print_error


class CaseManager:
    # """Manages all case operations"""
    
    def __init__(self, data_file: str = "data/cases.json"):
        self.data_file = data_file
        self.cases: Dict[str, Case] = {}
        self.load_cases()
    
    def load_cases(self):
        """Load cases from JSON file"""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    for case_id, case_data in data.items():
                        self.cases[case_id] = Case.from_dict(case_data)
            else:
                print(f"No existing cases file found. Creating new file at {self.data_file}")
        except Exception as e:
            print(f"Error loading cases: {str(e)}")
            self.cases = {}
    
    def save_cases(self):
        """Save cases to JSON file"""
        try:
            os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
            with open(self.data_file, 'w') as f:
                data = {case_id: case.to_dict() for case_id, case in self.cases.items()}
                json.dump(data, f, indent=2)
        except Exception as e:
            print_error(f"Failed to save cases: {str(e)}")
    
    def add_case(self, case: Case) -> bool:
        """Add a new case"""
        if case.case_id in self.cases:
            return False
        self.cases[case.case_id] = case
        self.save_cases()
        return True
    
    def get_case(self, case_id: str) -> Optional[Case]:
        """Get a case by ID"""
        return self.cases.get(case_id)
    
    def get_all_cases(self) -> List[Case]:
        """Get all cases"""
        return list(self.cases.values())
    
    def update_case(self, case_id: str, case: Case) -> bool:
        """Update an existing case"""
        if case_id not in self.cases:
            return False
        self.cases[case_id] = case
        self.save_cases()
        return True
    
    def delete_case(self, case_id: str) -> bool:
        """Delete a case"""
        if case_id not in self.cases:
            return False
        del self.cases[case_id]
        self.save_cases()
        return True
    
    def case_exists(self, case_id: str) -> bool:
        """Check if a case exists"""
        return case_id in self.cases
    
    def get_case_count(self) -> int:
        """Get total number of cases"""
        return len(self.cases)
    
    def search_by_crime_type(self, crime_type: str) -> List[Case]:
        """Search cases by crime type"""
        return [case for case in self.cases.values() 
                if crime_type.lower() in case.crime_type.lower()]
    
    def search_by_officer(self, officer_name: str) -> List[Case]:
        """Search cases by assigned officer"""
        return [case for case in self.cases.values() 
                if officer_name.lower() in case.officer_assigned.lower()]
    
    def search_by_status(self, status: str) -> List[Case]:
        """Search cases by investigation status"""
        return [case for case in self.cases.values() 
                if case.investigation_status == status]
    
    def search_by_priority(self, priority: str) -> List[Case]:
        """Search cases by priority level"""
        return [case for case in self.cases.values() 
                if case.priority_level == priority]
    
    def search_by_suspect(self, suspect_name: str) -> List[Case]:
        """Search cases by suspect name"""
        return [case for case in self.cases.values() 
                if suspect_name.lower() in case.suspect_name.lower()]
    
    def search_by_location(self, location: str) -> List[Case]:
        """Search cases by crime location"""
        return [case for case in self.cases.values() 
                if location.lower() in case.crime_location.lower()]
    
    def get_cases_by_date_range(self, start_date: str, end_date: str) -> List[Case]:
        """Get cases within a date range"""
        return [case for case in self.cases.values() 
                if start_date <= case.date_of_incident <= end_date]
    
    def get_active_cases(self) -> List[Case]:
        """Get all active cases (not closed)"""
        active_statuses = ["Open", "In Progress", "Under Review", "Reopened"]
        return [case for case in self.cases.values() 
                if case.investigation_status in active_statuses]
    
    def get_closed_cases(self) -> List[Case]:
        """Get all closed cases"""
        return [case for case in self.cases.values() 
                if case.investigation_status == "Closed"]
    
    def get_high_priority_cases(self) -> List[Case]:
        """Get all high priority cases"""
        high_priority = ["High", "Critical"]
        return [case for case in self.cases.values() 
                if case.priority_level in high_priority]
    
    def get_cases_by_status(self, status: str) -> List[Case]:
        """Get cases by specific status"""
        return [case for case in self.cases.values() 
                if case.investigation_status == status]
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get case statistics"""
        active = self.get_active_cases()
        closed = self.get_closed_cases()
        high_priority = self.get_high_priority_cases()
        
        crime_types = {}
        for case in self.cases.values():
            crime_types[case.crime_type] = crime_types.get(case.crime_type, 0) + 1
        
        priorities = {"Low": 0, "Medium": 0, "High": 0, "Critical": 0}
        for case in self.cases.values():
            if case.priority_level in priorities:
                priorities[case.priority_level] += 1
        
        return {
            'total_cases': self.get_case_count(),
            'active_cases': len(active),
            'closed_cases': len(closed),
            'high_priority_cases': len(high_priority),
            'crime_types': crime_types,
            'priority_distribution': priorities
        }
