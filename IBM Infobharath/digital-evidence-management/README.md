# Digital Evidence Management System

A comprehensive console-based application for managing criminal investigation records, evidence tracking, and case progress. Built with Python using Object-Oriented Programming principles.

## Features

### 1. **Case Management System**
- ✅ Add new criminal cases with complete details
- ✅ View all cases with sorted display (by priority)
- ✅ View detailed case information
- ✅ Update case investigation status
- ✅ Update case priority levels
- ✅ Add notes and comments to cases
- ✅ Delete closed cases
- ✅ Track linked evidence per case

### 2. **Evidence Tracking System**
- ✅ Add evidence records for cases
- ✅ Categorize evidence by type (Images, Videos, Documents, Fingerprints, Digital Devices)
- ✅ Update evidence status
- ✅ Maintain chain of custody for each evidence item
- ✅ Track evidence collection details
- ✅ View evidence linked to specific cases
- ✅ Delete evidence records

### 3. **Search & Filtering System**
- ✅ Search cases by crime type
- ✅ Search cases by assigned officer
- ✅ Search cases by suspect name
- ✅ Filter cases by investigation status
- ✅ Filter cases by priority level
- ✅ Filter cases by date range
- ✅ Search evidence by type
- ✅ Search evidence by case ID
- ✅ Search evidence by status

### 4. **Report Generation**
- ✅ Generate detailed case reports (TXT format)
- ✅ Generate evidence reports (TXT format)
- ✅ Generate active investigations report
- ✅ Generate closed cases report
- ✅ Generate high-priority cases report
- ✅ Export cases to CSV
- ✅ Export evidence to CSV
- ✅ Generate system summary reports

### 5. **Data Persistence**
- ✅ Automatic JSON-based data storage
- ✅ Persistent case records
- ✅ Persistent evidence records
- ✅ Automatic loading on application startup
- ✅ Real-time data synchronization

### 6. **Statistics & Analytics**
- ✅ Total case count and breakdown
- ✅ Active vs. closed cases tracking
- ✅ Priority distribution analysis
- ✅ Crime type statistics
- ✅ Evidence statistics by type, status, and location

### 7. **Error Handling**
- ✅ Input validation for all fields
- ✅ Duplicate case/evidence ID prevention
- ✅ Graceful error messages
- ✅ Exception handling throughout

## Project Structure

```
digital-evidence-management/
│
├── main.py                          # Main application entry point
├── case_manager.py                  # Case management operations
├── evidence_manager.py              # Evidence management operations
├── report_generator.py              # Report generation module
├── models.py                        # Data models (Case, Evidence)
├── utils.py                         # Utility functions
├── requirements.txt                 # Python dependencies
├── README.md                        # This file
│
└── data/                            # Data storage directory
    ├── cases.json                   # Persistent case records
    ├── evidence.json                # Persistent evidence records
    └── reports/                     # Generated reports
        ├── *.txt                    # Text format reports
        └── *.csv                    # CSV format reports
```

## Installation & Setup

### Prerequisites
- Python 3.7 or higher
- No external dependencies (uses only standard library)

### Installation Steps

1. **Clone or download the project**
   ```bash
   cd digital-evidence-management
   ```

2. **Verify Python installation**
   ```bash
   python --version
   ```

3. **Run the application**
   ```bash
   python main.py
   ```

## Usage Guide

### Starting the Application
```bash
python main.py
```

### Main Menu Options

#### 1. Case Management
- **Add New Case**: Create a new criminal case record
  - Enter Case ID (unique alphanumeric identifier)
  - Specify crime type
  - Location of incident
  - Date (YYYY-MM-DD format)
  - Assigned officer
  - Suspect name
  - Investigation status and priority

- **View All Cases**: Display all cases in the system
- **View Case Details**: Get complete information for a specific case
- **Update Case Status**: Change investigation status
- **Update Case Priority**: Modify priority level
- **Add Notes**: Document case progress
- **Delete Case**: Remove closed cases from the system

#### 2. Evidence Management
- **Add New Evidence**: Register evidence linked to a case
  - Evidence ID
  - Case ID (must exist)
  - Evidence type
  - Description
  - Storage location
  - Collection officer

- **View All Evidence**: List all evidence records
- **View Evidence Details**: Complete evidence information including chain of custody
- **View Evidence for Case**: All evidence linked to a specific case
- **Update Evidence Status**: Modify evidence status
- **Add Chain of Custody Entry**: Document evidence handling
- **Delete Evidence**: Remove evidence records

#### 3. Search & Filtering
- Search by crime type, officer, suspect
- Filter by status, priority, date range
- Search evidence by type, case, or status
- View detailed search results

#### 4. Generate Reports
- **Case Reports**: Detailed individual case information
- **Evidence Reports**: Complete evidence documentation
- **Batch Reports**: Active cases, closed cases, high-priority cases
- **CSV Exports**: For further analysis in spreadsheet applications
- **Summary Reports**: System-wide statistics and summaries

#### 5. View Statistics
- Total case count and distribution
- Active vs. closed cases
- Priority distribution
- Crime type breakdown
- Evidence statistics

## Data Models

### Case Object
```
- case_id: Unique case identifier
- crime_type: Type of crime
- crime_location: Location where crime occurred
- date_of_incident: Date in YYYY-MM-DD format
- officer_assigned: Assigned investigation officer
- suspect_name: Primary suspect
- investigation_status: Current status (Open, In Progress, Under Review, Closed, Reopened)
- priority_level: Priority (Low, Medium, High, Critical)
- evidence_ids: List of linked evidence IDs
- notes: Case investigation notes
- created_date: Timestamp of creation
- modified_date: Timestamp of last modification
```

### Evidence Object
```
- evidence_id: Unique evidence identifier
- case_id: Associated case ID
- evidence_type: Type (Images, Videos, Documents, Fingerprints, Digital Devices, Other)
- evidence_description: Detailed description
- location_stored: Storage location
- status: Evidence status (Received, In Use, Stored, Returned, Destroyed)
- collected_date: Collection date
- collected_by: Collecting officer
- chain_of_custody: List of custody transfer records
- created_date: Creation timestamp
- modified_date: Modification timestamp
```

## Sample Workflow

### Creating a New Investigation

1. **Add a Case**
   ```
   Case ID: CASE001
   Crime Type: Theft
   Location: Main Street Store
   Date: 2024-01-15
   Officer: Detective Smith
   Suspect: John Doe
   Status: Open
   Priority: High
   ```

2. **Add Evidence**
   ```
   Evidence ID: EVI001
   Case ID: CASE001
   Type: Images
   Description: Security camera footage
   Location: Evidence Room A
   Collected By: Officer Johnson
   ```

3. **Update Investigation**
   - Add notes on investigation progress
   - Update case status as needed
   - Add more evidence as discovered
   - Update priority if circumstances change

4. **Generate Reports**
   - Create investigation report
   - Export case details to CSV
   - Generate chain of custody documentation

## Features in Detail

### Case Status Management
- **Open**: Newly reported case
- **In Progress**: Active investigation
- **Under Review**: Awaiting review or approval
- **Closed**: Investigation completed
- **Reopened**: Previously closed case reopened

### Priority Levels
- **Low**: Minor cases
- **Medium**: Standard priority
- **High**: Urgent cases
- **Critical**: Emergency or high-profile cases

### Evidence Types
- **Images**: Photos, screenshots
- **Videos**: Security footage, recordings
- **Documents**: Written evidence, reports
- **Fingerprints**: Biometric evidence
- **Digital Devices**: Computers, phones, storage media
- **Other**: Miscellaneous evidence

### Chain of Custody
Automatic tracking of:
- Who received the evidence
- When they received it (timestamp)
- What action they performed
- Complete audit trail

## Data Storage

### JSON Format
All data is stored in human-readable JSON format:
- `data/cases.json` - All case records
- `data/evidence.json` - All evidence records

Example case record:
```json
{
  "CASE001": {
    "case_id": "CASE001",
    "crime_type": "Theft",
    "crime_location": "Main Street Store",
    "date_of_incident": "2024-01-15",
    "officer_assigned": "Detective Smith",
    "suspect_name": "John Doe",
    "investigation_status": "Open",
    "priority_level": "High",
    "evidence_ids": ["EVI001", "EVI002"],
    "notes": "[2024-01-15T10:30:00] Initial report filed...",
    "created_date": "2024-01-15T10:30:00.000000",
    "modified_date": "2024-01-15T10:35:00.000000"
  }
}
```

## Report Formats

### TXT Reports
- Human-readable format
- Suitable for printing
- Complete case/evidence details
- Includes timestamps
- Professional formatting

### CSV Reports
- Spreadsheet-compatible format
- Easy data import to Excel
- Structured tabular format
- Multiple export options

## Error Handling

The system includes comprehensive error handling for:
- Invalid input formats
- Duplicate case/evidence IDs
- Missing required fields
- File operation errors
- Invalid date formats
- Non-existent case/evidence references
- Graceful error messages for user guidance

## Advanced Features (Optional Implementations)

To enhance the system further, consider adding:
- [ ] Password-protected admin login
- [ ] SQLite database integration for scalability
- [ ] Graphical dashboard with Matplotlib
- [ ] PDF report export
- [ ] Evidence image attachment support
- [ ] User authentication and roles
- [ ] Email notifications
- [ ] Case assignment notifications
- [ ] Tkinter GUI interface
- [ ] Multi-user support
- [ ] Data backup and recovery
- [ ] Search history and saved filters

## Troubleshooting

### Data Not Persisting
- Ensure `data/` directory exists and is writable
- Check file permissions in the `data/` directory
- Verify disk space availability

### Case ID Already Exists
- Use a unique case ID
- Check existing cases before adding new ones

### Evidence Not Linking to Case
- Ensure case ID exists before adding evidence
- Verify case ID spelling matches exactly

### Reports Not Generating
- Check write permissions in `data/reports/` directory
- Ensure sufficient disk space
- Verify case/evidence data exists

## Performance Considerations

The system is optimized for:
- Small to medium investigation departments (up to several thousand cases)
- JSON-based storage for simplicity and portability
- Efficient searching and filtering
- Real-time data persistence

## Future Enhancements

1. **Database Migration**: SQLite or PostgreSQL for larger datasets
2. **Multi-user Support**: Concurrent access with role-based permissions
3. **Notifications**: Email/SMS alerts for case updates
4. **Mobile App**: Mobile interface for field officers
5. **Cloud Storage**: Backup and sync capabilities
6. **Analytics Dashboard**: Visual case statistics and trends
7. **Integration**: APIs for external systems

## Contributing

To contribute improvements:
1. Fork the repository
2. Create a feature branch
3. Make your improvements
4. Test thoroughly
5. Submit a pull request

## License

This project is provided as-is for educational and institutional use.

## Support

For issues, questions, or suggestions:
- Review the usage guide above
- Check the troubleshooting section
- Examine log outputs for error details
- Verify data file formats

## Version History

### Version 1.0 (Current)
- Initial release
- Core case management features
- Evidence tracking system
- Report generation
- Search and filtering
- Data persistence with JSON
- Comprehensive error handling

---

**Last Updated**: January 2024
**Python Version**: 3.7+
**Status**: Production Ready
