from case_manager import CaseManager
from evidence_manager import EvidenceManager
from report_generator import ReportGenerator
from models import Case, Evidence
from utils import create_data_directory


def main():
    create_data_directory()
    cm = CaseManager()
    em = EvidenceManager()
    rg = ReportGenerator()

    # Add a sample case
    if not cm.case_exists("CASE001"):
        case = Case(
            case_id="CASE001",
            crime_type="Theft",
            crime_location="Downtown",
            date_of_incident="2026-05-15",
            officer_assigned="Officer Singh",
            suspect_name="John Doe",
            investigation_status="Open",
            priority_level="High"
        )
        cm.add_case(case)
        print("Added sample case: CASE001")
    else:
        print("Sample case CASE001 already exists")

    # Add sample evidence
    if not em.evidence_exists("EVI001"):
        evi = Evidence(
            evidence_id="EVI001",
            case_id="CASE001",
            evidence_type="Images",
            evidence_description="CCTV footage showing suspect",
            location_stored="Evidence Room",
            collected_by="Officer Singh"
        )
        em.add_evidence(evi)
        # link evidence to case
        case = cm.get_case("CASE001")
        if case:
            case.add_evidence("EVI001")
            cm.update_case("CASE001", case)
        print("Added sample evidence: EVI001")
    else:
        print("Sample evidence EVI001 already exists")

    # Generate reports
    print("Generating reports...")
    c_report = rg.generate_case_report_txt(cm.get_case("CASE001"))
    print("Case report:", c_report)

    active_report = rg.generate_active_cases_report_txt(cm.get_active_cases())
    print("Active cases report:", active_report)

    cases_csv = rg.generate_cases_csv(cm.get_all_cases())
    print("Cases CSV:", cases_csv)

    evidence_csv = rg.generate_evidence_csv(em.get_all_evidence())
    print("Evidence CSV:", evidence_csv)

    summary = rg.generate_summary_report_txt(cm.get_statistics(), em.get_evidence_statistics())
    print("Summary report:", summary)

    print("Demo run complete.")


if __name__ == '__main__':
    main()
