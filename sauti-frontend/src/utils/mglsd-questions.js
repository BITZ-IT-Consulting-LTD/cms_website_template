const mglsdQuestions = [
    {
        "id": "opening_message",
        "question": "Welcome to the MGLSD Sauti Support System. We handle matters of Labour, Child Protection, and Social Welfare. Your safety is our priority.",
        "type": "info",
        "next": "reporter_role"
    },
    {
        "id": "reporter_role",
        "question": "Kindly tell us who is reporting this issue?",
        "type": "choice",
        "options": [
            "I am the person affected (Victim/Worker)",
            "I am a Parent/Guardian",
            "I am a Neighbor/Concerned Citizen",
            "I am a relative"
        ],
        "next": "reporter_names"
    },
    {
        "id": "reporter_names",
        "question": "What is your full name?",
        "type": "text",
        "placeholder": "Surname, Given names",
        "validation": { "required": true, "min_length": 1 },
        "next": "reporter_phone"
    },
    {
        "id": "reporter_phone",
        "question": "What is your Ugandan phone number?",
        "type": "text",
        "placeholder": "e.g., 0772123456 or +256752...",
        "validation": {
            "required": true,
            "pattern": "^(?:\\+256|256|0)?(7[0-9]|20|3[1-9])[0-9]{7}$",
            "error_message": "Please enter a valid Ugandan phone number."
        },
        "next": "issue_primary_category"
    },

    // --- ISSUE TRIAGE ---
    {
        "id": "issue_primary_category",
        "question": "What is the main nature of the issue you are reporting?",
        "type": "choice",
        "options": [
            "Migrant Worker/Labour Issue",
            "Child Abuse/Protection",
            "Gender-Based Violence (GBV)",
            "Social Welfare/Other"
        ],
        "next": {
            "Migrant Worker/Labour Issue": "check_self_report",
            "Child Abuse/Protection": "victim_child_details",
            "Gender-Based Violence (GBV)": "check_self_report",
            "Social Welfare/Other": "check_self_report"
        }
    },

    // --- LOGIC CHECK: Reporting for self or someone else? ---
    {
        "id": "check_self_report",
        "type": "logic_check",
        "next": (answers) => {
            if (answers.reporter_role === "I am the person affected (Victim/Worker)") {
                return "victim_location";
            }
            return "victim_general_names";
        }
    },

    // --- VICTIM DETAILS (NON-CHILD) ---
    {
        "id": "victim_general_names",
        "question": "What is the name of the person affected?",
        "type": "text",
        "validation": { "required": true },
        "next": "victim_location"
    },

    // --- VICTIM DETAILS (CHILD) ---
    {
        "id": "victim_child_details",
        "question": "What is the child's name (if known)?",
        "type": "text",
        "allowSkip": true,
        "next": "victim_child_age"
    },
    {
        "id": "victim_child_age",
        "question": "What is the estimated age of the child?",
        "type": "choice",
        "options": ["0-5 years", "6-12 years", "13-17 years", "Unknown"],
        "next": "victim_location"
    },

    // --- LOCATION (Universal) ---
    {
        "id": "victim_location",
        "question": "Where is the person/child currently located?",
        "type": "text",
        "placeholder": "District, Village, Street, or Country (if abroad)",
        "validation": { "required": true },
        "next": "branch_on_category_details"
    },

    // --- CATEGORY-SPECIFIC DETAILS ---
    {
        "id": "branch_on_category_details",
        "type": "logic_check",
        "next": (answers) => {
            if (answers.issue_primary_category === "Migrant Worker/Labour Issue") return "migrant_passport";
            return "perpetrator_details";
        }
    },

    // Migrant Specific
    {
        "id": "migrant_passport",
        "question": "What is the worker's Passport Number? (Helps with embassy tracking)",
        "type": "text",
        "allowSkip": true,
        "next": "recruitment_agency"
    },
    {
        "id": "recruitment_agency",
        "question": "Which recruitment agency in Uganda sent the worker abroad?",
        "type": "text",
        "placeholder": "Agency name or 'Independent'",
        "next": "perpetrator_details"
    },

    // --- PERPETRATOR ---
    {
        "id": "perpetrator_details",
        "question": "Who is the person causing the problem? (Name and relationship to the victim)",
        "type": "textarea",
        "placeholder": "e.g., Employer, Step-parent, Neighbor, Agent...",
        "validation": { "required": true },
        "next": "complaint_narrative"
    },

    // --- NARRATIVE & EVIDENCE ---
    {
        "id": "complaint_narrative",
        "question": "Please describe what has happened in detail.",
        "type": "textarea",
        "validation": { "required": true, "min_length": 10 },
        "next": "evidence_upload"
    },
    {
        "id": "evidence_upload",
        "question": "Please upload any evidence (Photos, Audio, Documents, or Screenshots). Max 16MB.",
        "type": "file_upload",
        "allowSkip": true,
        "next": "contact_preference"
    },

    // --- FOLLOW UP ---
    {
        "id": "contact_preference",
        "question": "How should our officers contact you for follow-up?",
        "type": "choice",
        "options": ["WhatsApp", "Direct Phone Call", "Email"],
        "next": "safe_time"
    },
    {
        "id": "safe_time",
        "question": "Is there a specific time it is safe to contact you? (Especially important for domestic violence or labor abuse cases)",
        "type": "text",
        "placeholder": "e.g., 6 PM - 9 PM",
        "next": "final_message"
    },
    {
        "id": "final_message",
        "question": "Thank you. Your report has been submitted to the MGLSD Sauti system. A caseworker will review this. If this is a life-threatening emergency, please call the Police (999) or the Child Helpline (116).",
        "type": "the end"
    }
];

export default mglsdQuestions;