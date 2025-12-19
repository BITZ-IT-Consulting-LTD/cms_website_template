const mglsdQuestions = [
    // Opening Message - Shortened
    {
        "id": "opening_message",
        "question": "Welcome to MGLSD Labor Support. We're here to help with work-related concerns for migrant workers. Your safety and privacy are our priority.",
        "type": "info",
        "next": "reporting_for_who"
    },

    // Direct to reporting type - no consent needed
    {
        "id": "reporting_for_who",
        "question": "Are you reporting this issue for yourself, or for someone else?",
        "type": "choice",
        "options": ["For myself", "For someone else"],
        "next": {
            "For myself": "reporter_names",
            "For someone else": "reporter_names"
        }
    },

    // REPORTER DETAILS - Simplified
    {
        "id": "reporter_names",
        "question": "What are your names?",
        "type": "text",
        "placeholder": "surname, given names",
        "validation": { "required": true, "min_length": 1 },
        "next": "reporter_sex"
    },

    {
        "id": "reporter_sex",
        "question": "What is your sex?",
        "type": "choice",
        "options": ["Male", "Female"],
        "next": {
            "Male": "reporter_dob",
            "Female": "reporter_dob"
        }
    },

    {
        "id": "reporter_dob",
        "question": "What is your date of birth? (DD/MM/YYYY)",
        "type": "text",
        "placeholder": "15/01/1990",
        "validation": { 
            "required": true, 
            "pattern": "^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\\d{4}$",
            "error_message": "Please enter date in DD/MM/YYYY format (e.g., 15/01/1990)"
        },
        "next": "reporter_location"
    },

    {
        "id": "reporter_location",
        "question": "What is your current location?",
        "type": "text",
        "placeholder": "street, village, district, country",
        "validation": { "required": true },
        "next": "check_reporting_type_for_passport"
    },

    // Conditional passport question logic
    {
        "id": "check_reporting_type_for_passport",
        "question": "",
        "type": "logic_check",
        "next": {
            "For myself": "reporter_passport",
            "For someone else": "check_reporting_type"
        }
    },

    {
        "id": "reporter_passport",
        "question": "What's your passport number? (This helps us verify your identity)",
        "type": "text",
        "validation": { "required": false },
        "allowSkip": false,
        "next": "check_reporting_type"
    },

    // BRANCHING LOGIC CHECK
    {
        "id": "check_reporting_type",
        "question": "",
        "type": "logic_check",
        "next": {
            "For myself": "job_title_self",
            "For someone else": "victim_names"
        }
    },

    // VICTIM DETAILS - Simplified (Only if reporting for someone else)
    {
        "id": "victim_names",
        "question": "What are the names of the person you're reporting for?",
        "type": "text",
        "placeholder": "surname, given names",
        "validation": { "required": true, "min_length": 1 },
        "next": "victim_sex"
    },

    {
        "id": "victim_sex",
        "question": "What is their sex?",
        "type": "choice",
        "options": ["Male", "Female"],
        "next": {
            "Male": "victim_dob",
            "Female": "victim_dob"
        }
    },

    {
        "id": "victim_dob",
        "question": "What is their date of birth? (DD/MM/YYYY)",
        "type": "text",
        "placeholder": "15/01/1990",
        "validation": { 
            "required": false,
            "pattern": "^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\\d{4}$",
            "error_message": "Please enter date in DD/MM/YYYY format (e.g., 15/01/1990)"
        },
        "allowSkip": true,
        "next": "victim_location"
    },

    {
        "id": "victim_location",
        "question": "What is their current location?",
        "type": "text",
        "placeholder": "street, village, district, country",
        "validation": { "required": true },
        "next": "victim_passport"
    },

    {
        "id": "victim_passport",
        "question": "What is the victim passport number? (This helps us verify their identity)",
        "type": "text",
        "validation": { "required": false },
        "allowSkip": true,
        "next": "job_title_other"
    },

    // JOB-RELATED QUESTIONS
    
    // For self-reporting - UPDATED: Removed employer_type_self
    {
        "id": "job_title_self",
        "question": "What type of job were you hired for? (e.g., domestic worker, construction, security, etc.)",
        "type": "text",
        "validation": { "required": true },
        "next": "employer_email_self"
    },

    {
        "id": "employer_name_self",
        "question": "What's the name of your employer or company?",
        "type": "text",
        "validation": { "required": true },
        "next": "employer_phone_self"
    },

    {
        "id": "employer_phone_self",
        "question": "What is your employer's phone number or contact?",
        "type": "text",
        "allowSkip": true,
        "validation": { "required": false, "pattern": "^[+]?[0-9\\s-()]+$" },
        "next": "employer_email_self"
    },

    {
        "id": "employer_email_self",
        "question": "What is your employer's email address?",
        "type": "text",
        "allowSkip": true,
        "validation": { "required": false, "pattern": "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$" },
        "next": "work_location_self"
    },

    {
        "id": "work_location_self",
        "question": "What is the location of the individual or company ?",
        "type": "text",
        "placeholder": "street, village, district, country",
        "validation": { "required": false },
        "allowSkip": true,
        "next": "perpetrator_names_self"
    },

    // For reporting someone else - UPDATED: Made all fields skippable and removed employer_type_other
    {
        "id": "job_title_other",
        "question": "What type of job was the person you're reporting for hired for? (e.g., domestic worker, construction, security, etc.)",
        "type": "text",
        "validation": { "required": false },
        "allowSkip": true,
        "next": "employer_name_other"
    },

    {
        "id": "employer_name_other",
        "question": "What's the name of their employer or company?",
        "type": "text",
        "validation": { "required": false },
        "allowSkip": true,
        "next": "employer_phone_other"
    },

    {
        "id": "employer_phone_other",
        "question": "What is their employer's phone number or contact?",
        "type": "text",
        "allowSkip": true,
        "validation": { "required": false, "pattern": "^[+]?[0-9\\s-()]+$" },
        "next": "employer_email_other"
    },

    {
        "id": "employer_email_other",
        "question": "What is their employer's email address?",
        "type": "text",
        "allowSkip": true,
        "validation": { "required": false, "pattern": "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$" },
        "next": "work_location_other"
    },

    {
        "id": "work_location_other",
        "question": "Which country is the individual or company in?",
        "type": "text",
        "placeholder": "street, village, district, country",
        "allowSkip": true,
        "validation": { "required": false },
        "next": "perpetrator_names_other"
    },

    // PERPETRATOR QUESTIONS - Simplified
    
    // For self-reporting - UPDATED: Removed "Other" from relationship options
    {
        "id": "perpetrator_names_self",
        "question": "What are the names of the person who you are raising a complaint against?",
        "type": "text",
        "placeholder": "surname, given names",
        "validation": { "required": true },
        "next": "perpetrator_sex_self"
    },

    {
        "id": "perpetrator_sex_self",
        "question": "What is their sex?",
        "type": "choice",
        "options": ["Male", "Female", "Don't know"],
        "next": {
            "Male": "perpetrator_location_self",
            "Female": "perpetrator_location_self",
            "Don't know": "perpetrator_location_self"
        }
    },

    {
        "id": "perpetrator_location_self",
        "question": "What is their location?",
        "type": "text",
        "placeholder": "street, village, district, country",
        "validation": { "required": false },
        "allowSkip": true,
        "next": "perpetrator_relationship_self"
    },

    {
        "id": "perpetrator_relationship_self",
        "question": "What's their relationship to you?",
        "type": "choice",
        "options": ["Employer", "Supervisor", "Agent", "Family member", "Colleague", "Not related"],
        "next": {
            "Employer": "perpetrator_profession_self",
            "Supervisor": "perpetrator_profession_self",
            "Agent": "perpetrator_profession_self",
            "Family member": "perpetrator_profession_self",
            "Colleague": "perpetrator_profession_self",
            "Not related": "perpetrator_profession_self"
        }
    },

    {
        "id": "perpetrator_profession_self",
        "question": "What's their job or profession?",
        "type": "text",
        "validation": { "required": false },
        "allowSkip": true,
        "next": "complaint_categories"
    },

    // For reporting someone else - UPDATED: Removed "Other" from relationship options
    {
        "id": "perpetrator_names_other",
        "question": "What are the names of the person who caused harm to the person you're reporting for?",
        "type": "text",
        "placeholder": "surname, given names",
        "validation": { "required": false },
        "allowSkip": true,
        "next": "perpetrator_sex_other"
    },

    {
        "id": "perpetrator_sex_other",
        "question": "What is their sex?",
        "type": "choice",
        "options": ["Male", "Female", "Don't know", "Skip this question"],
        "next": {
            "Male": "perpetrator_location_other",
            "Female": "perpetrator_location_other",
            "Don't know": "perpetrator_location_other",
            "Skip this question": "perpetrator_relationship_other"
        }
    },

    {
        "id": "perpetrator_location_other",
        "question": "What is their location?",
        "type": "text",
        "placeholder": "street, village, district, country",
        "validation": { "required": false },
        "allowSkip": true,
        "next": "perpetrator_relationship_other"
    },

    {
        "id": "perpetrator_relationship_other",
        "question": "What's their relationship to the person you're reporting for?",
        "type": "choice",
        "options": ["Employer", "Supervisor", "Agent", "Family member", "Colleague", "Not related", "Don't know"],
        "next": {
            "Employer": "perpetrator_profession_other",
            "Supervisor": "perpetrator_profession_other",
            "Agent": "perpetrator_profession_other",
            "Family member": "perpetrator_profession_other",
            "Colleague": "perpetrator_profession_other",
            "Not related": "perpetrator_profession_other",
            "Don't know": "complaint_categories"
        }
    },

    {
        "id": "perpetrator_profession_other",
        "question": "What's their job or profession?",
        "type": "text",
        "validation": { "required": false },
        "allowSkip": true,
        "next": "complaint_categories"
    },

    // COMPLAINT QUESTIONS
    {
        "id": "complaint_categories",
        "question": "Which of these categories best describes the problem? (You can select multiple categories that apply)",
        "type": "multiple_choice",
        "options": [
            {
                "category": "Sexual Violence",
                "cases": [
                    "Attempted Rape",
                    "Rape",
                    "Forced Prostitution",
                    "Indecent Assault",
                    "Sexual Harassment",
                    "Sodomy/Lesbianism",
                    "Unnatural sexual acts"
                ]
            },
            {
                "category": "Demise/Fatalities",
                "cases": [
                    "Death",
                    "Mysterious death",
                    "Accidental death",
                    "Suicide",
                    "Forced abortion"
                ]
            },
            {
                "category": "Legal Issues/ Rights",
                "cases": [
                    "Detention",
                    "Imprisonment",
                    "Lack of legal representation",
                    "Illegal deduction of salary",
                    "Unpaid salary",
                    "Illegal recruitment",
                    "Claim for refund",
                    "Denied exit visa",
                    "Confiscation of travel document",
                    "Delayed salary payment",
                    "Denial of medical care",
                    "Denial of food",
                    "Overworking",
                    "Breach/Change of contract",
                    "Lack of PPE",
                    "Charging exorbitant fees"
                ]
            },
            {
                "category": "Threatening Violence",
                "cases": [
                    "Intimidation and threats"
                ]
            },
            {
                "category": "Physical Violence",
                "cases": [
                    "Torture",
                    "Gross mistreatment",
                    "illegal organ harvesting",
                ]
            },
            {
                "category": "Prolonged sickness",
                "cases": [
                    "Prolonged sickness"
                ]
            },
            {
                "category": "Lack of communication with family",
                "cases": [
                    "Lack of communication with family"
                ]
            },
            {
                "category": "Lack of Legal Representation",
                "cases": [
                    "Lack of legal representation"
                ]
            },
            {
                "category": "Misuse of monies by the family members",
                "cases": [
                    "Misuse of monies by the family members"
                ]
            },
            {
                "category": "Repatriation of remains",
                "cases": [
                    "Repatriation of remains"
                ]
            },
            {
                "category": "Information on labour externalization",
                "cases": [
                    "Information on labour externalization"
                ]
            }
        ],
        "validation": { "required": true, "min_selections": 1 },
        "next": "complaint_narrative"
    },

    {
        "id": "complaint_narrative",
        "question": "Narrate what happened (please share as much details as possible, your story matters and we are here to help)",
        "type": "textarea",
        "validation": { "required": true, "min_length": 10 },
        "next": "evidence_upload"
    },

    // UPDATED: Enhanced file upload with more file types
    {
        "id": "evidence_upload",
        "question": "Do you have any evidence to support your case? (Photos, documents, PDFs, scans, contracts, messages, videos, etc. - Maximum file size: 16MB each)",
        "type": "file_upload",
        "validation": { 
            "required": false, 
            "max_file_size": "16MB",
            "accepted_types": [
                "image/*", 
                "application/pdf", 
                "application/msword", 
                "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                "application/vnd.ms-excel",
                "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                "text/plain",
                "audio/*", 
                "video/*",
                "application/zip",
                "application/x-rar-compressed",
                "application/vnd.ms-powerpoint",
                "application/vnd.openxmlformats-officedocument.presentationml.presentation"
            ],
            "max_files": 10
        },
        "allowSkip": true,
        "next": "contact_preference"
    },

    {
        "id": "contact_preference",
        "question": "We need to contact you for follow-up. How can we reach back to you? (Your privacy and safety are our priority)",
        "type": "choice",
        "allowSkip": true,
        "options": ["WhatsApp", "Email"],
        "next": {
            "WhatsApp": "contact_whatsapp",
            "Email": "contact_email"
        }
    },

    {
        "id": "contact_whatsapp",
        "question": "What's your WhatsApp number? (Please text this number +256 743 889999 to confirm your WhatsApp)",
        "type": "text",
        "allowSkip": true,
        "validation": { "required": false, "pattern": "^[+]?[0-9\\s-()]+$" },
        "next": "contact_email_also"
    },

    {
        "id": "contact_email",
        "question": "What's your email address?",
        "type": "text",
        "allowSkip": true,
        "validation": { "required": false, "pattern": "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$" },
        "next": "contact_whatsapp_also"
    },

    {
        "id": "contact_email_also",
        "question": "Please also provide your email address (for backup contact)",
        "type": "text",
        "allowSkip": true,
        "validation": { "required": false, "pattern": "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$" },
        "next": "contact_phone_also"
    },

    {
        "id": "contact_whatsapp_also",
        "question": "Please also provide your WhatsApp number (for backup contact). Text +256 743 889999 to confirm",
        "type": "text",
        "allowSkip": true,
        "validation": { "required": false, "pattern": "^[+]?[0-9\\s-()]+$" },
        "next": "contact_phone_also"
    },

    {
        "id": "contact_phone_also",
        "question": "Please provide your phone number (for backup contact)",
        "type": "text",
        "allowSkip": true,
        "validation": { "required": false, "pattern": "^[+]?[0-9\\s-()]+$" },
        "next": "safe_contact_time"
    },

    {
        "id": "safe_contact_time",
        "question": "When is it safe for us to contact you? (Time of day, days of week, any special instructions)",
        "type": "text",
        "validation": { "required": false },
        "allowSkip": true,
        "next": "final_message"
    },
    {
        "id": "final_message",
        "question": "Thank you for trusting us with your story. Your courage in speaking up matters. We've received your report and our team will review it carefully. You're not alone - we're here to support you through this. Please stay safe, and remember that help is available whenever you need it.",
        "type": "end"
    }
];

export default mglsdQuestions;