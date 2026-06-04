"""
Evidence Manager for managing case evidence
"""
import json
import os
from typing import List, Optional, Dict, Any
from models import Evidence
from utils import print_error


class EvidenceManager:
    """Manages all evidence operations"""
    
    def __init__(self, data_file: str = "data/evidence.json"):
        self.data_file = data_file
        self.evidence: Dict[str, Evidence] = {}
        self.load_evidence()
    
    def load_evidence(self):
        """Load evidence from JSON file"""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    for evidence_id, evidence_data in data.items():
                        self.evidence[evidence_id] = Evidence.from_dict(evidence_data)
            else:
                print(f"No existing evidence file found. Creating new file at {self.data_file}")
        except Exception as e:
            print(f"Error loading evidence: {str(e)}")
            self.evidence = {}
    
    def save_evidence(self):
        """Save evidence to JSON file"""
        try:
            os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
            with open(self.data_file, 'w') as f:
                data = {evi_id: evi.to_dict() for evi_id, evi in self.evidence.items()}
                json.dump(data, f, indent=2)
        except Exception as e:
            print_error(f"Failed to save evidence: {str(e)}")
    
    def add_evidence(self, evidence: Evidence) -> bool:
        """Add a new evidence record"""
        if evidence.evidence_id in self.evidence:
            return False
        self.evidence[evidence.evidence_id] = evidence
        self.save_evidence()
        return True
    
    def get_evidence(self, evidence_id: str) -> Optional[Evidence]:
        """Get evidence by ID"""
        return self.evidence.get(evidence_id)
    
    def get_all_evidence(self) -> List[Evidence]:
        """Get all evidence records"""
        return list(self.evidence.values())
    
    def update_evidence(self, evidence_id: str, evidence: Evidence) -> bool:
        """Update an evidence record"""
        if evidence_id not in self.evidence:
            return False
        self.evidence[evidence_id] = evidence
        self.save_evidence()
        return True
    
    def delete_evidence(self, evidence_id: str) -> bool:
        """Delete an evidence record"""
        if evidence_id not in self.evidence:
            return False
        del self.evidence[evidence_id]
        self.save_evidence()
        return True
    
    def evidence_exists(self, evidence_id: str) -> bool:
        """Check if evidence exists"""
        return evidence_id in self.evidence
    
    def get_evidence_count(self) -> int:
        """Get total number of evidence records"""
        return len(self.evidence)
    
    def get_evidence_by_case(self, case_id: str) -> List[Evidence]:
        """Get all evidence for a specific case"""
        return [evi for evi in self.evidence.values() 
                if evi.case_id == case_id]
    
    def get_evidence_by_type(self, evidence_type: str) -> List[Evidence]:
        """Get evidence by type"""
        return [evi for evi in self.evidence.values() 
                if evi.evidence_type == evidence_type]
    
    def get_evidence_by_status(self, status: str) -> List[Evidence]:
        """Get evidence by status"""
        return [evi for evi in self.evidence.values() 
                if evi.status == status]
    
    def get_evidence_by_location(self, location: str) -> List[Evidence]:
        """Get evidence by storage location"""
        return [evi for evi in self.evidence.values() 
                if location.lower() in evi.location_stored.lower()]
    
    def get_evidence_by_collector(self, collector_name: str) -> List[Evidence]:
        """Get evidence by collector/officer"""
        return [evi for evi in self.evidence.values() 
                if collector_name.lower() in evi.collected_by.lower()]
    
    def get_evidence_by_date_range(self, start_date: str, end_date: str) -> List[Evidence]:
        """Get evidence collected within a date range"""
        return [evi for evi in self.evidence.values() 
                if start_date <= evi.collected_date <= end_date]
    
    def get_high_priority_case_evidence(self, case_ids: List[str]) -> List[Evidence]:
        """Get all evidence for high priority cases"""
        return [evi for evi in self.evidence.values() 
                if evi.case_id in case_ids]
    
    def get_evidence_statistics(self) -> Dict[str, Any]:
        """Get evidence statistics"""
        evidence_types = {}
        statuses = {}
        locations = {}
        
        for evi in self.evidence.values():
            # Count by type
            evidence_types[evi.evidence_type] = evidence_types.get(evi.evidence_type, 0) + 1
            
            # Count by status
            statuses[evi.status] = statuses.get(evi.status, 0) + 1
            
            # Count by location
            locations[evi.location_stored] = locations.get(evi.location_stored, 0) + 1
        
        return {
            'total_evidence': self.get_evidence_count(),
            'by_type': evidence_types,
            'by_status': statuses,
            'by_location': locations
        }
    
    def get_evidence_chain_of_custody(self, evidence_id: str) -> Optional[List[Dict[str, str]]]:
        """Get chain of custody for evidence"""
        evidence = self.get_evidence(evidence_id)
        if evidence:
            return evidence.chain_of_custody
        return None
    
    def add_chain_of_custody_entry(self, evidence_id: str, officer_name: str, action: str) -> bool:
        """Add a chain of custody entry"""
        evidence = self.get_evidence(evidence_id)
        if not evidence:
            return False
        evidence.add_custody_entry(officer_name, action)
        self.update_evidence(evidence_id, evidence)
        return True
