rule_instance_suspected_person = [
    {
        "rule_instance": "Suspected Person - Address",
        "object_name": "Person",
        "age": "empty",
        "gender": "empty",
        "historyRecord": 3,
        "organization": "empty",
        "address": "123 Maple St",
        "severity": 2,
    },
    {
        "rule_instance": "Suspected Person - History",
        "object_name": "Person",
        "age": 34,
        "gender": "male",
        "historyRecord": 5,
        "organization": "unknown",
        "address": "empty",
        "severity": 3,
    },

    {
        "rule_instance": "Suspected Person - Organization",
        "object_name": "Person",
        "age": 42,
        "gender": "empty",
        "historyRecord": "empty",
        "organization": "Acme Corp",
        "address": "the west bank",
        "severity": 1,
    },
    {
        "rule_instance": "Suspected Person - Unknown Details",
        "object_name": "Person",
        "age": "empty",
        "gender": "female",
        "historyRecord": "empty",
        "organization": "Umbrella Inc.",
        "address": "789 Pine Blvd",
        "severity": 1,
    },

]

free_text_suspected_person = [
    [
        "Can you, uh, set up a rule for 'Suspected Person - Address'? The address should be 123 Maple St,History It's 3 it's. Severity? Set it at 2. history 3",
        "Hi, I need a rule instance called 'Address - Suspected Person'. The object is Person, and the address must be '123 Maple St'. history records 3 Oh, and severity should be 2.",
        "We need to monitor for 'Suspected Person - Address'. Address: 123 Maple St. history3 Leave the rest out. Severity: 2.",
        "Please configure 'Suspected Person - Address' for detection. Object: Person, Address:history um 3123 Maple St ,and severity level: 2. Other fields, eh, ignore them."
        "For 'Suspected Person - Address', use Person object. Address: 123 Maple St, severity two. history three Don't include anything else, okay?",
    ],
    [
        "Hi, set up a rule for 'Suspected Person - History'. History count should be 5, and Person's age is 34. Severity? Level 3. Gender? Male.",
        "I’d like a rule for under 'History - Suspected Person'. History is 5, age is 34, and severity is 3. Oh, gender is male.",
        "Create a rule called 'Suspected Person - History'. Key details: Person age 34, history records: 5, severity: 3. Gender: Male. Other fields? Empty.",
        "For 'History - Suspected Person', monitor these: history is 5, age is 34, severity is 3. Gender? Male.",
        "We need a 'Suspected Person - History' rule. Object: Person, with 5 history records, age 34. Severity: 3. Gender: male. Address and organization? Not needed.",
    ],
    [
        "Set up a rule for 'Suspected Person - Organization'. Address is the west bank The Person works for Acme Corp. Severity: 1. Age? 42. Other details are unimportant.",
        "Please create 'Organization - Suspected Person' to monitor. Person, age 42, working at Acme Corp. Severity: 1. Skip history. address the west bank",
        "I need a rule for 'Suspected Person - Organization'. Object: Person. Organization: Acme Corp. Age: 42. Severity: 1.For an address, write the west bank. Other stuff? Leave it out.",
        "Make a rule called 'Suspected Person - Organization'. Details: Person, organization: Acme Corp, age 42. Severity level: 1. Fill in the addressthe west bank.",
        "Hi, for 'Organization - Suspected Person', set Person's details as working in Acme Corp, age 42. Severity is 1. Address and history aren’t relevant.",
    ],
    [
        "I'd like a rule for 'Suspected Person - Unknown Details'. Use Person object with Address: 789 Pine Blvd. Gender? Female. Severity? 1.",
        "Can you create 'Suspected Person - Unknown Details'? Address is 789 Pine Blvd, Gender: Female. Severity: 1.",
        "Set up 'Unknown Details - Suspected Person'. Object: Person. Address: 789 Pine Blvd. Severity: 1. Gender? Female. Everything else? Leave it blank.",
        "For 'Unknown Details - Suspected Person', monitor a Person at 789 Pine Blvd. Gender: Female, severity level: 1. Skip all other fields.",
        "Please create a rule called 'Suspected Person - Unknown Details'. Address: 789 Pine Blvd. Severity is 1. Gender? Female.",
    ],

]
