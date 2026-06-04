"""
Main module - Console interface for Digital Evidence Management System
"""
from case_manager import CaseManager
from evidence_manager import EvidenceManager
from report_generator import ReportGenerator
from models import Case, Evidence
from utils import (
    print_header, print_subheader, print_separator, print_success, print_error, print_info,
    get_menu_choice, get_valid_input, validate_case_id, validate_date, validate_priority,
    validate_investigation_status, validate_crime_type, validate_location, validate_officer_name,
    validate_suspect_name, validate_evidence_type, validate_evidence_description,
    create_data_directory
)


class DigitalEvidenceManagementSystem:
    """Main application class"""
    
    def __init__(self):
        create_data_directory()
        self.case_manager = CaseManager()
        self.evidence_manager = EvidenceManager()
        self.report_generator = ReportGenerator()
        self.current_user = "Admin"
    
    def display_main_menu(self):
        """Display main menu"""
        print_header("DIGITAL EVIDENCE MANAGEMENT SYSTEM")
        print(f"Logged in as: {self.current_user}")
        print()
        
        options = [
            "Case Management",
            "Evidence Management",
            "Search & Filtering",
            "Generate Reports",
            "View Statistics",
            "Exit"
        ]
        
        return get_menu_choice(options)
    
    # ========== CASE MANAGEMENT ==========
    
    def handle_case_management(self):
        """Handle case management options"""
        while True:
            print_subheader("CASE MANAGEMENT")
            
            options = [
                "Add New Case",
                "View All Cases",
                "View Case Details",
                "Update Case Status",
                "Update Case Priority",
                "Add Notes to Case",
                "Delete Case",
                "Back to Main Menu"
            ]
            
            choice = get_menu_choice(options)
            
            if choice == 1:
                self.add_new_case()
            elif choice == 2:
                self.view_all_cases()
            elif choice == 3:
                self.view_case_details()
            elif choice == 4:
                self.update_case_status()
            elif choice == 5:
                self.update_case_priority()
            elif choice == 6:
                self.add_notes_to_case()
            elif choice == 7:
                self.delete_case()
            elif choice == 8:
                break
            elif choice is None:
                break
    
    def add_new_case(self):
        """Add a new criminal case"""
        print_subheader("ADD NEW CRIMINAL CASE")
        
        try:
            case_id = get_valid_input(
                "Enter Case ID (alphanumeric): ",
                validate_case_id,
                "Case ID must be alphanumeric and not empty"
            )
            
            if not case_id:
                return
            
            if self.case_manager.case_exists(case_id):
                print_error(f"Case ID {case_id} already exists")
                return
            
            crime_type = get_valid_input(
                "Enter Crime Type (e.g., Theft, Assault, Murder): ",
                validate_crime_type,
                "Crime type cannot be empty"
            )
            
            if not crime_type:
                return
            
            crime_location = get_valid_input(
                "Enter Crime Location: ",
                validate_location,
                "Location cannot be empty"
            )
            
            if not crime_location:
                return
            
            date_of_incident = get_valid_input(
                "Enter Date of Incident (YYYY-MM-DD): ",
                validate_date,
                "Date must be in format YYYY-MM-DD"
            )
            
            if not date_of_incident:
                return
            
            officer_assigned = get_valid_input(
                "Enter Officer Assigned Name: ",
                validate_officer_name,
                "Officer name cannot be empty"
            )
            
            if not officer_assigned:
                return
            
            suspect_name = get_valid_input(
                "Enter Suspect Name: ",
                validate_suspect_name,
                "Suspect name cannot be empty"
            )
            
            if not suspect_name:
                return
            
            print("\nAvailable Investigation Statuses: Open, In Progress, Under Review, Closed, Reopened")
            investigation_status = get_valid_input(
                "Enter Investigation Status (default: Open): ",
                validate_investigation_status,
                "Invalid status"
            )
            
            if not investigation_status:
                investigation_status = "Open"
            
            print("Available Priority Levels: Low, Medium, High, Critical")
            priority_level = get_valid_input(
                "Enter Priority Level (default: Medium): ",
                validate_priority,
                "Invalid priority"
            )
            
            if not priority_level:
                priority_level = "Medium"
            
            # Create case
            case = Case(
                case_id=case_id,
                crime_type=crime_type,
                crime_location=crime_location,
                date_of_incident=date_of_incident,
                officer_assigned=officer_assigned,
                suspect_name=suspect_name,
                investigation_status=investigation_status,
                priority_level=priority_level
            )
            
            if self.case_manager.add_case(case):
                print_success(f"Case {case_id} added successfully")
            else:
                print_error("Failed to add case")
        
        except Exception as e:
            print_error(f"Error adding case: {str(e)}")
    
    def view_all_cases(self):
        """View all cases"""
        print_subheader("ALL CASES")
        
        cases = self.case_manager.get_all_cases()
        
        if not cases:
            print_info("No cases found")
            return
        
        print(f"Total Cases: {len(cases)}\n")
        print_separator()
        
        for case in sorted(cases, key=lambda c: c.priority_level == "Critical", reverse=True):
            print(f"Case ID: {case.case_id}")
            print(f"  Crime Type: {case.crime_type}")
            print(f"  Location: {case.crime_location}")
            print(f"  Officer: {case.officer_assigned}")
            print(f"  Suspect: {case.suspect_name}")
            print(f"  Status: {case.investigation_status} | Priority: {case.priority_level}")
            print(f"  Evidence Items: {len(case.evidence_ids)}")
            print_separator()
    
    def view_case_details(self):
        """View detailed information for a specific case"""
        print_subheader("VIEW CASE DETAILS")
        
        case_id = input("Enter Case ID: ").strip()
        case = self.case_manager.get_case(case_id)
        
        if not case:
            print_error(f"Case {case_id} not found")
            return
        
        print_separator()
        print(f"Case ID: {case.case_id}")
        print(f"Crime Type: {case.crime_type}")
        print(f"Location: {case.crime_location}")
        print(f"Date of Incident: {case.date_of_incident}")
        print(f"Officer Assigned: {case.officer_assigned}")
        print(f"Suspect Name: {case.suspect_name}")
        print(f"Investigation Status: {case.investigation_status}")
        print(f"Priority Level: {case.priority_level}")
        print(f"Created Date: {case.created_date}")
        print(f"Modified Date: {case.modified_date}")
        print(f"\nLinked Evidence: {len(case.evidence_ids)}")
        
        if case.evidence_ids:
            print("Evidence IDs:")
            for evi_id in case.evidence_ids:
                evidence = self.evidence_manager.get_evidence(evi_id)
                if evidence:
                    print(f"  - {evi_id}: {evidence.evidence_type}")
        
        if case.notes:
            print(f"\nNotes:\n{case.notes}")
        
        print_separator()
    
    def update_case_status(self):
        """Update case investigation status"""
        print_subheader("UPDATE CASE STATUS")
        
        case_id = input("Enter Case ID: ").strip()
        case = self.case_manager.get_case(case_id)
        
        if not case:
            print_error(f"Case {case_id} not found")
            return
        
        print(f"Current Status: {case.investigation_status}")
        print("Available Statuses: Open, In Progress, Under Review, Closed, Reopened")
        
        new_status = get_valid_input(
            "Enter new status: ",
            validate_investigation_status,
            "Invalid status"
        )
        
        if new_status:
            case.update_status(new_status)
            self.case_manager.update_case(case_id, case)
            print_success(f"Case {case_id} status updated to {new_status}")
    
    def update_case_priority(self):
        """Update case priority level"""
        print_subheader("UPDATE CASE PRIORITY")
        
        case_id = input("Enter Case ID: ").strip()
        case = self.case_manager.get_case(case_id)
        
        if not case:
            print_error(f"Case {case_id} not found")
            return
        
        print(f"Current Priority: {case.priority_level}")
        print("Available Priorities: Low, Medium, High, Critical")
        
        new_priority = get_valid_input(
            "Enter new priority: ",
            validate_priority,
            "Invalid priority"
        )
        
        if new_priority:
            case.update_priority(new_priority)
            self.case_manager.update_case(case_id, case)
            print_success(f"Case {case_id} priority updated to {new_priority}")
    
    def add_notes_to_case(self):
        """Add notes to a case"""
        print_subheader("ADD NOTES TO CASE")
        
        case_id = input("Enter Case ID: ").strip()
        case = self.case_manager.get_case(case_id)
        
        if not case:
            print_error(f"Case {case_id} not found")
            return
        
        note = input("Enter note: ").strip()
        
        if note:
            case.add_notes(note)
            self.case_manager.update_case(case_id, case)
            print_success(f"Note added to case {case_id}")
    
    def delete_case(self):
        """Delete a case"""
        print_subheader("DELETE CASE")
        
        case_id = input("Enter Case ID: ").strip()
        
        if not self.case_manager.case_exists(case_id):
            print_error(f"Case {case_id} not found")
            return
        
        confirm = input(f"Are you sure you want to delete case {case_id}? (yes/no): ").strip().lower()
        
        if confirm == 'yes':
            if self.case_manager.delete_case(case_id):
                print_success(f"Case {case_id} deleted successfully")
                # Also delete linked evidence
                self.evidence_manager.evidence = {
                    evi_id: evi for evi_id, evi in self.evidence_manager.evidence.items()
                    if evi.case_id != case_id
                }
                self.evidence_manager.save_evidence()
            else:
                print_error("Failed to delete case")
        else:
            print_info("Delete operation cancelled")
    
    # ========== EVIDENCE MANAGEMENT ==========
    
    def handle_evidence_management(self):
        """Handle evidence management options"""
        while True:
            print_subheader("EVIDENCE MANAGEMENT")
            
            options = [
                "Add New Evidence",
                "View All Evidence",
                "View Evidence Details",
                "View Evidence for Case",
                "Update Evidence Status",
                "Add Chain of Custody Entry",
                "Delete Evidence",
                "Back to Main Menu"
            ]
            
            choice = get_menu_choice(options)
            
            if choice == 1:
                self.add_new_evidence()
            elif choice == 2:
                self.view_all_evidence()
            elif choice == 3:
                self.view_evidence_details()
            elif choice == 4:
                self.view_evidence_for_case()
            elif choice == 5:
                self.update_evidence_status()
            elif choice == 6:
                self.add_chain_of_custody()
            elif choice == 7:
                self.delete_evidence()
            elif choice == 8:
                break
            elif choice is None:
                break
    
    def add_new_evidence(self):
        """Add new evidence record"""
        print_subheader("ADD NEW EVIDENCE RECORD")
        
        try:
            case_id = input("Enter Case ID: ").strip()
            
            if not self.case_manager.case_exists(case_id):
                print_error(f"Case {case_id} not found")
                return
            
            evidence_id = get_valid_input(
                "Enter Evidence ID (alphanumeric): ",
                lambda x: bool(x) and x.isalnum(),
                "Evidence ID must be alphanumeric"
            )
            
            if not evidence_id or self.evidence_manager.evidence_exists(evidence_id):
                print_error("Invalid or duplicate evidence ID")
                return
            
            print("Available Evidence Types: Images, Videos, Documents, Fingerprints, Digital Devices, Other")
            evidence_type = get_valid_input(
                "Enter Evidence Type: ",
                validate_evidence_type,
                "Invalid evidence type"
            )
            
            if not evidence_type:
                return
            
            evidence_description = get_valid_input(
                "Enter Evidence Description: ",
                validate_evidence_description,
                "Description cannot be empty"
            )
            
            if not evidence_description:
                return
            
            location = input("Enter Storage Location (default: Evidence Room): ").strip()
            if not location:
                location = "Evidence Room"
            
            collected_by = input("Enter Collected By (Officer Name): ").strip()
            if not collected_by:
                collected_by = "Unknown"
            
            # Create evidence
            evidence = Evidence(
                evidence_id=evidence_id,
                case_id=case_id,
                evidence_type=evidence_type,
                evidence_description=evidence_description,
                location_stored=location,
                collected_by=collected_by,
                status="Received"
            )
            
            if self.evidence_manager.add_evidence(evidence):
                # Add evidence to case
                case = self.case_manager.get_case(case_id)
                case.add_evidence(evidence_id)
                self.case_manager.update_case(case_id, case)
                print_success(f"Evidence {evidence_id} added successfully")
            else:
                print_error("Failed to add evidence")
        
        except Exception as e:
            print_error(f"Error adding evidence: {str(e)}")
    
    def view_all_evidence(self):
        """View all evidence records"""
        print_subheader("ALL EVIDENCE RECORDS")
        
        evidence_list = self.evidence_manager.get_all_evidence()
        
        if not evidence_list:
            print_info("No evidence records found")
            return
        
        print(f"Total Evidence Items: {len(evidence_list)}\n")
        print_separator()
        
        for evidence in sorted(evidence_list, key=lambda e: e.case_id):
            print(f"Evidence ID: {evidence.evidence_id}")
            print(f"  Case ID: {evidence.case_id}")
            print(f"  Type: {evidence.evidence_type}")
            print(f"  Status: {evidence.status}")
            print(f"  Location: {evidence.location_stored}")
            print(f"  Description: {evidence.evidence_description}")
            print_separator()
    
    def view_evidence_details(self):
        """View detailed information for specific evidence"""
        print_subheader("VIEW EVIDENCE DETAILS")
        
        evidence_id = input("Enter Evidence ID: ").strip()
        evidence = self.evidence_manager.get_evidence(evidence_id)
        
        if not evidence:
            print_error(f"Evidence {evidence_id} not found")
            return
        
        print_separator()
        print(f"Evidence ID: {evidence.evidence_id}")
        print(f"Case ID: {evidence.case_id}")
        print(f"Type: {evidence.evidence_type}")
        print(f"Description: {evidence.evidence_description}")
        print(f"Status: {evidence.status}")
        print(f"Location: {evidence.location_stored}")
        print(f"Collected Date: {evidence.collected_date}")
        print(f"Collected By: {evidence.collected_by}")
        print(f"Created Date: {evidence.created_date}")
        print(f"Modified Date: {evidence.modified_date}")
        
        if evidence.chain_of_custody:
            print(f"\nChain of Custody ({len(evidence.chain_of_custody)} entries):")
            for i, entry in enumerate(evidence.chain_of_custody, 1):
                print(f"  {i}. {entry['timestamp']} | {entry['officer']} | {entry['action']}")
        
        print_separator()
    
    def view_evidence_for_case(self):
        """View all evidence for a specific case"""
        print_subheader("VIEW EVIDENCE FOR CASE")
        
        case_id = input("Enter Case ID: ").strip()
        
        if not self.case_manager.case_exists(case_id):
            print_error(f"Case {case_id} not found")
            return
        
        evidence_list = self.evidence_manager.get_evidence_by_case(case_id)
        
        if not evidence_list:
            print_info(f"No evidence found for case {case_id}")
            return
        
        print(f"\nEvidence for Case {case_id}: {len(evidence_list)} items\n")
        print_separator()
        
        for evidence in evidence_list:
            print(f"Evidence ID: {evidence.evidence_id}")
            print(f"  Type: {evidence.evidence_type}")
            print(f"  Status: {evidence.status}")
            print(f"  Description: {evidence.evidence_description}")
            print_separator()
    
    def update_evidence_status(self):
        """Update evidence status"""
        print_subheader("UPDATE EVIDENCE STATUS")
        
        evidence_id = input("Enter Evidence ID: ").strip()
        evidence = self.evidence_manager.get_evidence(evidence_id)
        
        if not evidence:
            print_error(f"Evidence {evidence_id} not found")
            return
        
        print(f"Current Status: {evidence.status}")
        print("Available Statuses: Received, In Use, Stored, Returned, Destroyed")
        
        new_status = input("Enter new status: ").strip()
        
        if new_status:
            evidence.update_status(new_status)
            self.evidence_manager.update_evidence(evidence_id, evidence)
            print_success(f"Evidence {evidence_id} status updated to {new_status}")
    
    def add_chain_of_custody(self):
        """Add chain of custody entry"""
        print_subheader("ADD CHAIN OF CUSTODY ENTRY")
        
        evidence_id = input("Enter Evidence ID: ").strip()
        
        if not self.evidence_manager.evidence_exists(evidence_id):
            print_error(f"Evidence {evidence_id} not found")
            return
        
        officer_name = input("Enter Officer Name: ").strip()
        action = input("Enter Action (e.g., Received, Transferred, Analyzed): ").strip()
        
        if officer_name and action:
            if self.evidence_manager.add_chain_of_custody_entry(evidence_id, officer_name, action):
                print_success("Chain of custody entry added")
            else:
                print_error("Failed to add entry")
    
    def delete_evidence(self):
        """Delete evidence record"""
        print_subheader("DELETE EVIDENCE")
        
        evidence_id = input("Enter Evidence ID: ").strip()
        
        if not self.evidence_manager.evidence_exists(evidence_id):
            print_error(f"Evidence {evidence_id} not found")
            return
        
        confirm = input(f"Are you sure you want to delete evidence {evidence_id}? (yes/no): ").strip().lower()
        
        if confirm == 'yes':
            evidence = self.evidence_manager.get_evidence(evidence_id)
            if self.evidence_manager.delete_evidence(evidence_id):
                # Remove from case
                case = self.case_manager.get_case(evidence.case_id)
                if case:
                    case.remove_evidence(evidence_id)
                    self.case_manager.update_case(evidence.case_id, case)
                print_success(f"Evidence {evidence_id} deleted successfully")
            else:
                print_error("Failed to delete evidence")
        else:
            print_info("Delete operation cancelled")
    
    # ========== SEARCH & FILTERING ==========
    
    def handle_search_filtering(self):
        """Handle search and filtering options"""
        while True:
            print_subheader("SEARCH & FILTERING")
            
            options = [
                "Search Cases by Crime Type",
                "Search Cases by Officer",
                "Search Cases by Suspect",
                "Filter Cases by Status",
                "Filter Cases by Priority",
                "Filter Cases by Date Range",
                "Search Evidence by Type",
                "Search Evidence by Case ID",
                "Search Evidence by Status",
                "Back to Main Menu"
            ]
            
            choice = get_menu_choice(options)
            
            if choice == 1:
                self.search_by_crime_type()
            elif choice == 2:
                self.search_by_officer()
            elif choice == 3:
                self.search_by_suspect()
            elif choice == 4:
                self.filter_by_status()
            elif choice == 5:
                self.filter_by_priority()
            elif choice == 6:
                self.filter_by_date_range()
            elif choice == 7:
                self.search_evidence_by_type()
            elif choice == 8:
                self.search_evidence_by_case()
            elif choice == 9:
                self.search_evidence_by_status()
            elif choice == 10:
                break
            elif choice is None:
                break
    
    def search_by_crime_type(self):
        """Search cases by crime type"""
        print_subheader("SEARCH BY CRIME TYPE")
        
        crime_type = input("Enter Crime Type: ").strip()
        
        if not crime_type:
            print_error("Crime type cannot be empty")
            return
        
        results = self.case_manager.search_by_crime_type(crime_type)
        self._display_search_results(results, f"Crime Type: {crime_type}")
    
    def search_by_officer(self):
        """Search cases by officer"""
        print_subheader("SEARCH BY OFFICER")
        
        officer = input("Enter Officer Name: ").strip()
        
        if not officer:
            print_error("Officer name cannot be empty")
            return
        
        results = self.case_manager.search_by_officer(officer)
        self._display_search_results(results, f"Officer: {officer}")
    
    def search_by_suspect(self):
        """Search cases by suspect"""
        print_subheader("SEARCH BY SUSPECT")
        
        suspect = input("Enter Suspect Name: ").strip()
        
        if not suspect:
            print_error("Suspect name cannot be empty")
            return
        
        results = self.case_manager.search_by_suspect(suspect)
        self._display_search_results(results, f"Suspect: {suspect}")
    
    def filter_by_status(self):
        """Filter cases by status"""
        print_subheader("FILTER BY STATUS")
        
        print("Available Statuses: Open, In Progress, Under Review, Closed, Reopened")
        status = input("Enter Status: ").strip()
        
        if not status:
            print_error("Status cannot be empty")
            return
        
        results = self.case_manager.search_by_status(status)
        self._display_search_results(results, f"Status: {status}")
    
    def filter_by_priority(self):
        """Filter cases by priority"""
        print_subheader("FILTER BY PRIORITY")
        
        print("Available Priorities: Low, Medium, High, Critical")
        priority = input("Enter Priority: ").strip()
        
        if not priority:
            print_error("Priority cannot be empty")
            return
        
        results = self.case_manager.search_by_priority(priority)
        self._display_search_results(results, f"Priority: {priority}")
    
    def filter_by_date_range(self):
        """Filter cases by date range"""
        print_subheader("FILTER BY DATE RANGE")
        
        start_date = get_valid_input(
            "Enter Start Date (YYYY-MM-DD): ",
            validate_date,
            "Date must be in format YYYY-MM-DD"
        )
        
        if not start_date:
            return
        
        end_date = get_valid_input(
            "Enter End Date (YYYY-MM-DD): ",
            validate_date,
            "Date must be in format YYYY-MM-DD"
        )
        
        if not end_date:
            return
        
        results = self.case_manager.get_cases_by_date_range(start_date, end_date)
        self._display_search_results(results, f"Date Range: {start_date} to {end_date}")
    
    def search_evidence_by_type(self):
        """Search evidence by type"""
        print_subheader("SEARCH EVIDENCE BY TYPE")
        
        print("Available Types: Images, Videos, Documents, Fingerprints, Digital Devices, Other")
        evi_type = input("Enter Evidence Type: ").strip()
        
        if not evi_type:
            print_error("Evidence type cannot be empty")
            return
        
        results = self.evidence_manager.get_evidence_by_type(evi_type)
        self._display_evidence_results(results, f"Type: {evi_type}")
    
    def search_evidence_by_case(self):
        """Search evidence by case"""
        print_subheader("SEARCH EVIDENCE BY CASE")
        
        case_id = input("Enter Case ID: ").strip()
        
        if not case_id:
            print_error("Case ID cannot be empty")
            return
        
        results = self.evidence_manager.get_evidence_by_case(case_id)
        self._display_evidence_results(results, f"Case ID: {case_id}")
    
    def search_evidence_by_status(self):
        """Search evidence by status"""
        print_subheader("SEARCH EVIDENCE BY STATUS")
        
        status = input("Enter Status: ").strip()
        
        if not status:
            print_error("Status cannot be empty")
            return
        
        results = self.evidence_manager.get_evidence_by_status(status)
        self._display_evidence_results(results, f"Status: {status}")
    
    def _display_search_results(self, results, search_criteria):
        """Display search results"""
        print(f"\nSearch Results: {search_criteria}")
        
        if not results:
            print_info("No results found")
            return
        
        print(f"Found {len(results)} result(s)\n")
        print_separator()
        
        for case in results:
            print(f"Case ID: {case.case_id}")
            print(f"  Crime Type: {case.crime_type}")
            print(f"  Location: {case.crime_location}")
            print(f"  Officer: {case.officer_assigned}")
            print(f"  Status: {case.investigation_status} | Priority: {case.priority_level}")
            print_separator()
    
    def _display_evidence_results(self, results, search_criteria):
        """Display evidence search results"""
        print(f"\nSearch Results: {search_criteria}")
        
        if not results:
            print_info("No results found")
            return
        
        print(f"Found {len(results)} result(s)\n")
        print_separator()
        
        for evidence in results:
            print(f"Evidence ID: {evidence.evidence_id}")
            print(f"  Case ID: {evidence.case_id}")
            print(f"  Type: {evidence.evidence_type}")
            print(f"  Status: {evidence.status}")
            print(f"  Description: {evidence.evidence_description}")
            print_separator()
    
    # ========== REPORT GENERATION ==========
    
    def handle_report_generation(self):
        """Handle report generation options"""
        while True:
            print_subheader("GENERATE REPORTS")
            
            options = [
                "Generate Case Report (TXT)",
                "Generate Evidence Report (TXT)",
                "Generate Active Cases Report (TXT)",
                "Generate Closed Cases Report (TXT)",
                "Generate High Priority Report (TXT)",
                "Export All Cases (CSV)",
                "Export All Evidence (CSV)",
                "Generate Summary Report (TXT)",
                "Back to Main Menu"
            ]
            
            choice = get_menu_choice(options)
            
            if choice == 1:
                self.generate_case_report()
            elif choice == 2:
                self.generate_evidence_report()
            elif choice == 3:
                self.generate_active_cases_report()
            elif choice == 4:
                self.generate_closed_cases_report()
            elif choice == 5:
                self.generate_high_priority_report()
            elif choice == 6:
                self.export_cases_csv()
            elif choice == 7:
                self.export_evidence_csv()
            elif choice == 8:
                self.generate_summary_report()
            elif choice == 9:
                break
            elif choice is None:
                break
    
    def generate_case_report(self):
        """Generate case report"""
        print_subheader("GENERATE CASE REPORT")
        
        case_id = input("Enter Case ID: ").strip()
        case = self.case_manager.get_case(case_id)
        
        if not case:
            print_error(f"Case {case_id} not found")
            return
        
        filename = self.report_generator.generate_case_report_txt(case)
        
        if filename:
            print_success(f"Report generated: {filename}")
    
    def generate_evidence_report(self):
        """Generate evidence report"""
        print_subheader("GENERATE EVIDENCE REPORT")
        
        evidence_id = input("Enter Evidence ID: ").strip()
        evidence = self.evidence_manager.get_evidence(evidence_id)
        
        if not evidence:
            print_error(f"Evidence {evidence_id} not found")
            return
        
        filename = self.report_generator.generate_evidence_report_txt(evidence)
        
        if filename:
            print_success(f"Report generated: {filename}")
    
    def generate_active_cases_report(self):
        """Generate active cases report"""
        print_subheader("GENERATE ACTIVE CASES REPORT")
        
        cases = self.case_manager.get_active_cases()
        
        if not cases:
            print_info("No active cases found")
            return
        
        filename = self.report_generator.generate_active_cases_report_txt(cases)
        
        if filename:
            print_success(f"Report generated: {filename}")
    
    def generate_closed_cases_report(self):
        """Generate closed cases report"""
        print_subheader("GENERATE CLOSED CASES REPORT")
        
        cases = self.case_manager.get_closed_cases()
        
        if not cases:
            print_info("No closed cases found")
            return
        
        filename = self.report_generator.generate_closed_cases_report_txt(cases)
        
        if filename:
            print_success(f"Report generated: {filename}")
    
    def generate_high_priority_report(self):
        """Generate high priority cases report"""
        print_subheader("GENERATE HIGH PRIORITY CASES REPORT")
        
        cases = self.case_manager.get_high_priority_cases()
        
        if not cases:
            print_info("No high priority cases found")
            return
        
        filename = self.report_generator.generate_high_priority_report_txt(cases)
        
        if filename:
            print_success(f"Report generated: {filename}")
    
    def export_cases_csv(self):
        """Export cases to CSV"""
        print_subheader("EXPORT CASES (CSV)")
        
        cases = self.case_manager.get_all_cases()
        
        if not cases:
            print_info("No cases to export")
            return
        
        filename = self.report_generator.generate_cases_csv(cases)
        
        if filename:
            print_success(f"Report generated: {filename}")
    
    def export_evidence_csv(self):
        """Export evidence to CSV"""
        print_subheader("EXPORT EVIDENCE (CSV)")
        
        evidence_list = self.evidence_manager.get_all_evidence()
        
        if not evidence_list:
            print_info("No evidence to export")
            return
        
        filename = self.report_generator.generate_evidence_csv(evidence_list)
        
        if filename:
            print_success(f"Report generated: {filename}")
    
    def generate_summary_report(self):
        """Generate summary report"""
        print_subheader("GENERATE SUMMARY REPORT")
        
        case_stats = self.case_manager.get_statistics()
        evidence_stats = self.evidence_manager.get_evidence_statistics()
        
        filename = self.report_generator.generate_summary_report_txt(case_stats, evidence_stats)
        
        if filename:
            print_success(f"Report generated: {filename}")
    
    # ========== STATISTICS ==========
    
    def view_statistics(self):
        """View system statistics"""
        print_subheader("SYSTEM STATISTICS")
        
        case_stats = self.case_manager.get_statistics()
        evidence_stats = self.evidence_manager.get_evidence_statistics()
        
        print("CASE STATISTICS")
        print_separator()
        print(f"Total Cases: {case_stats['total_cases']}")
        print(f"Active Cases: {case_stats['active_cases']}")
        print(f"Closed Cases: {case_stats['closed_cases']}")
        print(f"High Priority Cases: {case_stats['high_priority_cases']}\n")
        
        if case_stats['crime_types']:
            print("Crime Types:")
            for crime_type, count in case_stats['crime_types'].items():
                print(f"  - {crime_type}: {count}")
        
        print()
        if case_stats['priority_distribution']:
            print("Priority Distribution:")
            for priority, count in case_stats['priority_distribution'].items():
                print(f"  - {priority}: {count}")
        
        print("\n" + "-"*70)
        print("EVIDENCE STATISTICS")
        print_separator()
        print(f"Total Evidence Items: {evidence_stats['total_evidence']}\n")
        
        if evidence_stats['by_type']:
            print("Evidence by Type:")
            for evi_type, count in evidence_stats['by_type'].items():
                print(f"  - {evi_type}: {count}")
        
        print()
        if evidence_stats['by_status']:
            print("Evidence by Status:")
            for status, count in evidence_stats['by_status'].items():
                print(f"  - {status}: {count}")
        
        print()
        if evidence_stats['by_location']:
            print("Evidence by Location:")
            for location, count in evidence_stats['by_location'].items():
                print(f"  - {location}: {count}")
        
        print_separator()
    
    # ========== MAIN LOOP ==========
    
    def run(self):
        """Run the application main loop"""
        while True:
            try:
                choice = self.display_main_menu()
                
                if choice == 1:
                    self.handle_case_management()
                elif choice == 2:
                    self.handle_evidence_management()
                elif choice == 3:
                    self.handle_search_filtering()
                elif choice == 4:
                    self.handle_report_generation()
                elif choice == 5:
                    self.view_statistics()
                elif choice == 6:
                    print_header("THANK YOU FOR USING DEM SYSTEM")
                    print("System shutting down...")
                    break
                elif choice is None:
                    print_header("THANK YOU FOR USING DEM SYSTEM")
                    print("System shutting down...")
                    break
            except KeyboardInterrupt:
                print_header("THANK YOU FOR USING DEM SYSTEM")
                print("System shutting down...")
                break
            except Exception as e:
                print_error(f"An error occurred: {str(e)}")


def main():
    """Main entry point"""
    system = DigitalEvidenceManagementSystem()
    system.run()


if __name__ == "__main__":
    main()
