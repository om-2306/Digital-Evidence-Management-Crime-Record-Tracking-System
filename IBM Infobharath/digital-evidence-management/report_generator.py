"""
Report Generator for creating investigation reports
"""
import csv
import os
from datetime import datetime
from typing import List, Optional
from models import Case, Evidence
from utils import print_success, print_error


class ReportGenerator:
    """Generates investigation reports"""
    
    def __init__(self, report_dir: str = "data/reports"):
        self.report_dir = report_dir
        os.makedirs(report_dir, exist_ok=True)
    
    def _get_report_filename(self, base_name: str, file_format: str) -> str:
        """Generate unique report filename"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return os.path.join(self.report_dir, f"{base_name}_{timestamp}.{file_format}")
    
    # ========== TXT Report Generation ==========
    
    def generate_case_report_txt(self, case: Case) -> Optional[str]:
        """Generate a detailed case report in TXT format"""
        try:
            filename = self._get_report_filename("case_report", "txt")
            
            with open(filename, 'w') as f:
                f.write("=" * 70 + "\n")
                f.write("CRIMINAL CASE INVESTIGATION REPORT\n")
                f.write("=" * 70 + "\n\n")
                
                f.write(f"Report Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                
                # Case Information
                f.write("-" * 70 + "\n")
                f.write("CASE INFORMATION\n")
                f.write("-" * 70 + "\n")
                f.write(f"Case ID: {case.case_id}\n")
                f.write(f"Crime Type: {case.crime_type}\n")
                f.write(f"Crime Location: {case.crime_location}\n")
                f.write(f"Date of Incident: {case.date_of_incident}\n")
                f.write(f"Officer Assigned: {case.officer_assigned}\n")
                f.write(f"Suspect Name: {case.suspect_name}\n\n")
                
                # Investigation Status
                f.write("-" * 70 + "\n")
                f.write("INVESTIGATION STATUS\n")
                f.write("-" * 70 + "\n")
                f.write(f"Status: {case.investigation_status}\n")
                f.write(f"Priority Level: {case.priority_level}\n")
                f.write(f"Created Date: {case.created_date}\n")
                f.write(f"Modified Date: {case.modified_date}\n\n")
                
                # Evidence Information
                f.write("-" * 70 + "\n")
                f.write("LINKED EVIDENCE\n")
                f.write("-" * 70 + "\n")
                if case.evidence_ids:
                    f.write(f"Total Evidence Items: {len(case.evidence_ids)}\n")
                    for evi_id in case.evidence_ids:
                        f.write(f"  - {evi_id}\n")
                else:
                    f.write("No evidence linked to this case\n")
                f.write("\n")
                
                # Notes
                f.write("-" * 70 + "\n")
                f.write("CASE NOTES\n")
                f.write("-" * 70 + "\n")
                if case.notes:
                    f.write(case.notes + "\n")
                else:
                    f.write("No notes recorded\n")
                f.write("\n")
                
                f.write("=" * 70 + "\n")
                f.write("END OF REPORT\n")
                f.write("=" * 70 + "\n")
            
            return filename
        except Exception as e:
            print_error(f"Failed to generate case report: {str(e)}")
            return None
    
    def generate_evidence_report_txt(self, evidence: Evidence) -> Optional[str]:
        """Generate a detailed evidence report in TXT format"""
        try:
            filename = self._get_report_filename("evidence_report", "txt")
            
            with open(filename, 'w') as f:
                f.write("=" * 70 + "\n")
                f.write("EVIDENCE REPORT\n")
                f.write("=" * 70 + "\n\n")
                
                f.write(f"Report Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                
                # Evidence Information
                f.write("-" * 70 + "\n")
                f.write("EVIDENCE DETAILS\n")
                f.write("-" * 70 + "\n")
                f.write(f"Evidence ID: {evidence.evidence_id}\n")
                f.write(f"Case ID: {evidence.case_id}\n")
                f.write(f"Evidence Type: {evidence.evidence_type}\n")
                f.write(f"Description: {evidence.evidence_description}\n")
                f.write(f"Status: {evidence.status}\n\n")
                
                # Storage Information
                f.write("-" * 70 + "\n")
                f.write("STORAGE INFORMATION\n")
                f.write("-" * 70 + "\n")
                f.write(f"Location: {evidence.location_stored}\n")
                f.write(f"Collected Date: {evidence.collected_date}\n")
                f.write(f"Collected By: {evidence.collected_by}\n")
                f.write(f"Created Date: {evidence.created_date}\n")
                f.write(f"Modified Date: {evidence.modified_date}\n\n")
                
                # Chain of Custody
                f.write("-" * 70 + "\n")
                f.write("CHAIN OF CUSTODY\n")
                f.write("-" * 70 + "\n")
                if evidence.chain_of_custody:
                    for i, entry in enumerate(evidence.chain_of_custody, 1):
                        f.write(f"\nEntry {i}:\n")
                        f.write(f"  Timestamp: {entry['timestamp']}\n")
                        f.write(f"  Officer: {entry['officer']}\n")
                        f.write(f"  Action: {entry['action']}\n")
                else:
                    f.write("No chain of custody entries recorded\n")
                f.write("\n")
                
                f.write("=" * 70 + "\n")
                f.write("END OF REPORT\n")
                f.write("=" * 70 + "\n")
            
            return filename
        except Exception as e:
            print_error(f"Failed to generate evidence report: {str(e)}")
            return None
    
    def generate_active_cases_report_txt(self, cases: List[Case]) -> Optional[str]:
        """Generate report for active investigations"""
        try:
            filename = self._get_report_filename("active_cases_report", "txt")
            
            with open(filename, 'w') as f:
                f.write("=" * 70 + "\n")
                f.write("ACTIVE INVESTIGATIONS REPORT\n")
                f.write("=" * 70 + "\n\n")
                
                f.write(f"Report Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"Total Active Cases: {len(cases)}\n\n")
                
                for case in sorted(cases, key=lambda c: c.priority_level == "Critical", reverse=True):
                    f.write("-" * 70 + "\n")
                    f.write(f"Case ID: {case.case_id}\n")
                    f.write(f"Crime Type: {case.crime_type} | Location: {case.crime_location}\n")
                    f.write(f"Officer: {case.officer_assigned} | Suspect: {case.suspect_name}\n")
                    f.write(f"Status: {case.investigation_status} | Priority: {case.priority_level}\n")
                    f.write(f"Date of Incident: {case.date_of_incident}\n")
                    f.write(f"Evidence Items: {len(case.evidence_ids)}\n")
                    f.write("\n")
                
                f.write("=" * 70 + "\n")
                f.write("END OF REPORT\n")
                f.write("=" * 70 + "\n")
            
            return filename
        except Exception as e:
            print_error(f"Failed to generate active cases report: {str(e)}")
            return None
    
    def generate_closed_cases_report_txt(self, cases: List[Case]) -> Optional[str]:
        """Generate report for closed cases"""
        try:
            filename = self._get_report_filename("closed_cases_report", "txt")
            
            with open(filename, 'w') as f:
                f.write("=" * 70 + "\n")
                f.write("CLOSED CASES REPORT\n")
                f.write("=" * 70 + "\n\n")
                
                f.write(f"Report Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"Total Closed Cases: {len(cases)}\n\n")
                
                for case in sorted(cases, key=lambda c: c.modified_date, reverse=True):
                    f.write("-" * 70 + "\n")
                    f.write(f"Case ID: {case.case_id}\n")
                    f.write(f"Crime Type: {case.crime_type}\n")
                    f.write(f"Officer: {case.officer_assigned}\n")
                    f.write(f"Closed Date: {case.modified_date}\n")
                    f.write(f"Evidence Items: {len(case.evidence_ids)}\n")
                    f.write("\n")
                
                f.write("=" * 70 + "\n")
                f.write("END OF REPORT\n")
                f.write("=" * 70 + "\n")
            
            return filename
        except Exception as e:
            print_error(f"Failed to generate closed cases report: {str(e)}")
            return None
    
    def generate_high_priority_report_txt(self, cases: List[Case]) -> Optional[str]:
        """Generate report for high priority cases"""
        try:
            filename = self._get_report_filename("high_priority_report", "txt")
            
            with open(filename, 'w') as f:
                f.write("=" * 70 + "\n")
                f.write("HIGH PRIORITY CASES REPORT\n")
                f.write("=" * 70 + "\n\n")
                
                f.write(f"Report Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"Total High Priority Cases: {len(cases)}\n\n")
                
                for case in sorted(cases, key=lambda c: c.date_of_incident, reverse=True):
                    f.write("-" * 70 + "\n")
                    f.write(f"Case ID: {case.case_id}\n")
                    f.write(f"Crime Type: {case.crime_type} | Priority: {case.priority_level}\n")
                    f.write(f"Officer: {case.officer_assigned}\n")
                    f.write(f"Status: {case.investigation_status}\n")
                    f.write(f"Date of Incident: {case.date_of_incident}\n")
                    f.write("\n")
                
                f.write("=" * 70 + "\n")
                f.write("END OF REPORT\n")
                f.write("=" * 70 + "\n")
            
            return filename
        except Exception as e:
            print_error(f"Failed to generate high priority report: {str(e)}")
            return None
    
    # ========== CSV Report Generation ==========
    
    def generate_cases_csv(self, cases: List[Case]) -> Optional[str]:
        """Generate cases report in CSV format"""
        try:
            filename = self._get_report_filename("cases", "csv")
            
            if not cases:
                print_error("No cases to export")
                return None
            
            with open(filename, 'w', newline='') as f:
                fieldnames = [
                    'Case ID', 'Crime Type', 'Location', 'Date of Incident',
                    'Officer Assigned', 'Suspect Name', 'Status', 'Priority',
                    'Evidence Count', 'Created Date', 'Modified Date'
                ]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                
                for case in cases:
                    writer.writerow({
                        'Case ID': case.case_id,
                        'Crime Type': case.crime_type,
                        'Location': case.crime_location,
                        'Date of Incident': case.date_of_incident,
                        'Officer Assigned': case.officer_assigned,
                        'Suspect Name': case.suspect_name,
                        'Status': case.investigation_status,
                        'Priority': case.priority_level,
                        'Evidence Count': len(case.evidence_ids),
                        'Created Date': case.created_date,
                        'Modified Date': case.modified_date
                    })
            
            return filename
        except Exception as e:
            print_error(f"Failed to generate cases CSV: {str(e)}")
            return None
    
    def generate_evidence_csv(self, evidence_list: List[Evidence]) -> Optional[str]:
        """Generate evidence report in CSV format"""
        try:
            filename = self._get_report_filename("evidence", "csv")
            
            if not evidence_list:
                print_error("No evidence to export")
                return None
            
            with open(filename, 'w', newline='') as f:
                fieldnames = [
                    'Evidence ID', 'Case ID', 'Type', 'Description',
                    'Status', 'Location', 'Collected Date', 'Collected By',
                    'Created Date', 'Modified Date'
                ]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                
                for evi in evidence_list:
                    writer.writerow({
                        'Evidence ID': evi.evidence_id,
                        'Case ID': evi.case_id,
                        'Type': evi.evidence_type,
                        'Description': evi.evidence_description,
                        'Status': evi.status,
                        'Location': evi.location_stored,
                        'Collected Date': evi.collected_date,
                        'Collected By': evi.collected_by,
                        'Created Date': evi.created_date,
                        'Modified Date': evi.modified_date
                    })
            
            return filename
        except Exception as e:
            print_error(f"Failed to generate evidence CSV: {str(e)}")
            return None
    
    def generate_summary_report_txt(self, case_stats: dict, evidence_stats: dict) -> Optional[str]:
        """Generate a summary report"""
        try:
            filename = self._get_report_filename("summary_report", "txt")
            
            with open(filename, 'w') as f:
                f.write("=" * 70 + "\n")
                f.write("INVESTIGATION MANAGEMENT SYSTEM - SUMMARY REPORT\n")
                f.write("=" * 70 + "\n\n")
                
                f.write(f"Report Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                
                # Case Statistics
                f.write("-" * 70 + "\n")
                f.write("CASE STATISTICS\n")
                f.write("-" * 70 + "\n")
                f.write(f"Total Cases: {case_stats.get('total_cases', 0)}\n")
                f.write(f"Active Cases: {case_stats.get('active_cases', 0)}\n")
                f.write(f"Closed Cases: {case_stats.get('closed_cases', 0)}\n")
                f.write(f"High Priority Cases: {case_stats.get('high_priority_cases', 0)}\n\n")
                
                if case_stats.get('crime_types'):
                    f.write("Crime Types:\n")
                    for crime_type, count in case_stats['crime_types'].items():
                        f.write(f"  - {crime_type}: {count}\n")
                f.write("\n")
                
                if case_stats.get('priority_distribution'):
                    f.write("Priority Distribution:\n")
                    for priority, count in case_stats['priority_distribution'].items():
                        f.write(f"  - {priority}: {count}\n")
                f.write("\n")
                
                # Evidence Statistics
                f.write("-" * 70 + "\n")
                f.write("EVIDENCE STATISTICS\n")
                f.write("-" * 70 + "\n")
                f.write(f"Total Evidence Items: {evidence_stats.get('total_evidence', 0)}\n\n")
                
                if evidence_stats.get('by_type'):
                    f.write("Evidence by Type:\n")
                    for evi_type, count in evidence_stats['by_type'].items():
                        f.write(f"  - {evi_type}: {count}\n")
                f.write("\n")
                
                if evidence_stats.get('by_status'):
                    f.write("Evidence by Status:\n")
                    for status, count in evidence_stats['by_status'].items():
                        f.write(f"  - {status}: {count}\n")
                f.write("\n")
                
                f.write("=" * 70 + "\n")
                f.write("END OF REPORT\n")
                f.write("=" * 70 + "\n")
            
            return filename
        except Exception as e:
            print_error(f"Failed to generate summary report: {str(e)}")
            return None
