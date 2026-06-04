"""
Data models for the Digital Evidence Management System
"""
from datetime import datetime
from typing import Optional, List, Dict, Any


class Case:
    """Represents a criminal case"""
    
    def __init__(
        self,
        case_id: str,
        crime_type: str,
        crime_location: str,
        date_of_incident: str,
        officer_assigned: str,
        suspect_name: str,
        investigation_status: str = "Open",
        priority_level: str = "Medium",
        evidence_ids: Optional[List[str]] = None,
        notes: str = "",
        created_date: Optional[str] = None,
        modified_date: Optional[str] = None
    ):
        self.case_id = case_id
        self.crime_type = crime_type
        self.crime_location = crime_location
        self.date_of_incident = date_of_incident
        self.officer_assigned = officer_assigned
        self.suspect_name = suspect_name
        self.investigation_status = investigation_status
        self.priority_level = priority_level
        self.evidence_ids = evidence_ids or []
        self.notes = notes
        self.created_date = created_date or datetime.now().isoformat()
        self.modified_date = modified_date or datetime.now().isoformat()
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert case to dictionary"""
        return {
            'case_id': self.case_id,
            'crime_type': self.crime_type,
            'crime_location': self.crime_location,
            'date_of_incident': self.date_of_incident,
            'officer_assigned': self.officer_assigned,
            'suspect_name': self.suspect_name,
            'investigation_status': self.investigation_status,
            'priority_level': self.priority_level,
            'evidence_ids': self.evidence_ids,
            'notes': self.notes,
            'created_date': self.created_date,
            'modified_date': self.modified_date
        }
    
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'Case':
        """Create case from dictionary"""
        return Case(
            case_id=data['case_id'],
            crime_type=data['crime_type'],
            crime_location=data['crime_location'],
            date_of_incident=data['date_of_incident'],
            officer_assigned=data['officer_assigned'],
            suspect_name=data['suspect_name'],
            investigation_status=data.get('investigation_status', 'Open'),
            priority_level=data.get('priority_level', 'Medium'),
            evidence_ids=data.get('evidence_ids', []),
            notes=data.get('notes', ''),
            created_date=data.get('created_date'),
            modified_date=data.get('modified_date')
        )
    
    def update_status(self, new_status: str):
        """Update investigation status"""
        self.investigation_status = new_status
        self.modified_date = datetime.now().isoformat()
    
    def update_priority(self, new_priority: str):
        """Update priority level"""
        self.priority_level = new_priority
        self.modified_date = datetime.now().isoformat()
    
    def add_evidence(self, evidence_id: str):
        """Add evidence ID to case"""
        if evidence_id not in self.evidence_ids:
            self.evidence_ids.append(evidence_id)
            self.modified_date = datetime.now().isoformat()
    
    def remove_evidence(self, evidence_id: str):
        """Remove evidence ID from case"""
        if evidence_id in self.evidence_ids:
            self.evidence_ids.remove(evidence_id)
            self.modified_date = datetime.now().isoformat()
    
    def add_notes(self, note: str):
        """Add notes to case"""
        self.notes += f"\n[{datetime.now().isoformat()}] {note}"
        self.modified_date = datetime.now().isoformat()
    
    def __str__(self) -> str:
        """String representation of case"""
        return f"Case ID: {self.case_id} | Type: {self.crime_type} | Status: {self.investigation_status} | Priority: {self.priority_level}"
    
    def __repr__(self) -> str:
        return f"Case(case_id={self.case_id})"


class Evidence:
    """Represents evidence in a case"""
    
    def __init__(
        self,
        evidence_id: str,
        case_id: str,
        evidence_type: str,
        evidence_description: str,
        location_stored: str = "Evidence Room",
        status: str = "Received",
        collected_date: Optional[str] = None,
        collected_by: str = "Unknown",
        chain_of_custody: Optional[List[Dict[str, str]]] = None,
        created_date: Optional[str] = None,
        modified_date: Optional[str] = None
    ):
        self.evidence_id = evidence_id
        self.case_id = case_id
        self.evidence_type = evidence_type
        self.evidence_description = evidence_description
        self.location_stored = location_stored
        self.status = status
        self.collected_date = collected_date or datetime.now().isoformat().split('T')[0]
        self.collected_by = collected_by
        self.chain_of_custody = chain_of_custody or []
        self.created_date = created_date or datetime.now().isoformat()
        self.modified_date = modified_date or datetime.now().isoformat()
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert evidence to dictionary"""
        return {
            'evidence_id': self.evidence_id,
            'case_id': self.case_id,
            'evidence_type': self.evidence_type,
            'evidence_description': self.evidence_description,
            'location_stored': self.location_stored,
            'status': self.status,
            'collected_date': self.collected_date,
            'collected_by': self.collected_by,
            'chain_of_custody': self.chain_of_custody,
            'created_date': self.created_date,
            'modified_date': self.modified_date
        }
    
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'Evidence':
        """Create evidence from dictionary"""
        return Evidence(
            evidence_id=data['evidence_id'],
            case_id=data['case_id'],
            evidence_type=data['evidence_type'],
            evidence_description=data['evidence_description'],
            location_stored=data.get('location_stored', 'Evidence Room'),
            status=data.get('status', 'Received'),
            collected_date=data.get('collected_date'),
            collected_by=data.get('collected_by', 'Unknown'),
            chain_of_custody=data.get('chain_of_custody', []),
            created_date=data.get('created_date'),
            modified_date=data.get('modified_date')
        )
    
    def update_status(self, new_status: str):
        """Update evidence status"""
        self.status = new_status
        self.modified_date = datetime.now().isoformat()
    
    def add_custody_entry(self, officer_name: str, action: str):
        """Add chain of custody entry"""
        entry = {
            'timestamp': datetime.now().isoformat(),
            'officer': officer_name,
            'action': action
        }
        self.chain_of_custody.append(entry)
        self.modified_date = datetime.now().isoformat()
    
    def __str__(self) -> str:
        """String representation of evidence"""
        return f"Evidence ID: {self.evidence_id} | Type: {self.evidence_type} | Case: {self.case_id} | Status: {self.status}"
    
    def __repr__(self) -> str:
        return f"Evidence(evidence_id={self.evidence_id}, case_id={self.case_id})"
