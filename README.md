# PocketDoc
***UC Health Hackathon Data Science Project***

### General Solution Description	
An application that contacts the user via some means and has a “conversation” with them on a regular basis to gather health information and log it. Creating a rudimentary recent health history for the patient. (Doctors can decide what to ask and when) Readmission prevention. (Platform!!!)

### Open Health Conversation
Alexa or some other voice integration platform for surgical dressing walkthroughs

**Name/Logo Thoughts**:
J mixed with caduceus
Journal, confidant, check, check-in, deja vu, logger, logging, LogM, LogX, Bloom

### Big Ideas
Get better longitudinal subjective patient information through a more personal message.
**USER-ORIENTED**
Non intrusive, conversational
We want patients to be able to health journal
	- Makes them health conscious
	- Keeps a record for doctors to refer to
	- Gets them used to talking about their health
Could also work in a mental health angle
	- Checking in on people
	- Regularity of check in
Advanced/Enhanced Journalling
Not mind blowing tech, but it is a valuable application.
Still need tech for security much like any journal.
“Personalized” medicine

### Concerns
Very important to make the UI friendly and welcoming
	- Is this possible when working with VUI?
	- Possible use of texting/calling to increase personality
	- It’s harder to ignore a text/call than an app notification
Direct connection to the EHR?
	- Are we alerting medical professionals based on these reports?
	- Will we give them the option?
	- My feeling is this application could stand alone
	- Send compiled results file to doctor as needed
	- Could be integrated into EHR but that seems like a bit much
How can we increase user compliance/truthfulness?
	- This comes back to UI design and overall experience architecture.
	- We want them to want to use the app for themselves.
	- Positive feedback somehow? Streaks? Everyone loves streaks.
	- Cooperation with medical centers can lend credibility

### Features
“Personalized” to ask different conversation trees depending on needs
Knowing needs by physician input or super basic ml based on user-provided history
VUI can call?
Could have Alexa integration also. Can alexa initiate a conversation?
GUI for entry in the app after reminder push notifications
Conversational UI through text message functionality
Could be hosted online and work through text and not be on the phone at all. (twilio)
Friendly welcoming and easy to use conversational UI
Summarizing tools
NLP pipeline to analyze subjective entries
Basic/Advanced data metrics
Lexicon to process content of subjective notes
Check for truthfulness?
Discrete and private and secure. Treat it like a real diary/journal. Extra security.
Some kind of forwarding/sharing mechanism for medical professionals
Extensible structure to allow for further specificity depending on patients needs.
Could also incorporate medication reminders
Connect with patients as a person/confidant NOT an APP
Varying contact frequency, varying frequency of certain questions
Can ask about subjective and objective information
Eventual integrations with other health tracking methods as well.

### Problem
Patients are not returning to the clinic for check-ups and appointments and that will create a lot of problems in the long term if there are complications.
**What to do**: Understand the causes that prevent them from coming to the appointments
Analyze what patients are “high-risk” for non-compliance
Find a way to encourage or improve these patients

Hospitals/clinics may partner with us to send transportation to patients in order to encourage the patients to travel. 
Our app will reduce no-show rates by X% and that will improve the lost cost ratio of patients that don’t show up to appointments 
Think about incentives for hospitals or companies to hire us. What are we offering?

Think about geriatric population: texting or apps might not be optimal. Maybe stick to calling them because they’re most comfortable with that.

Patients who forget their appointment: show their schedule? Can do a text message or robocall. 

	
### Idea
Find out about how patients comply with their medication and lifestyle. Update their lifestyles for the physician 
Input/output that stores patient information. Pinpoint the discussion that we will pitch to one type of conversation (i.e. hypertension/diabetes)
Create the app for the clinic. 

Focus on the specific disease, treatment options and presets for questions
Diabetes: comprehensive diabetes education
At least 2.5 hrs/week moderate-intensity aerobic physical activity
Foot care (avoid going barefoot, test water temp before a bath, trim toe nails, don’t cut cuticles, shoe fit and change socks daily)
Self-measurement of blood sugar (3+ times daily with multiple insulin injections
HgA1C (glycosylated hemoglobin, A1C and HbA1c)
Eating patterns, nutritional status: maintenance of strict glycemic, dietary protein restriction (0.8-1.0g/kg of total body weight)
Diabetes-related complications: eyes (blurry vision, retinopathy)- Amsler grid, 
kidney (polyuria, urine output- urinalysis/dialysis) 
nerve (tingling, numbness, pain)
Cardiac (chest pain, shortness of breath)
PAD (peripheral arterial disease, Claudication- pain in legs after walking a certain distance) 
Medications: ACE inhibitors, aspirin, metformin, insulin, glitazone
Preset questions: 
Don't forget! Your appointment is in X days! 
Press “N” if you cannot make it
Maybe 5→ 1 days before the appointment
How many hours have you worked out/had intense aerobic physical activity
Once a week
Are you changing your socks everyday and keeping your toenails trimmed?
About one every 3 days
Are you taking Metformin/intensive insulin/glitazone/sulfonylurea at X dosage per day?
Informational about dosage (and descriptive of medication) with Y/N
How are you feeling today? Happiness/pain levels

### Achievement Style Game
People get points or achievements for completing the survey every day, the more comprehensive, the better the rewards for people
Important part of healthcare: making sure the patient believes and can trust in the system so they will respond and react well with treatment
What to do with high-risk profiling: use data to inform the clinic/hospital which patients are most at risk for non-compliance
As consequence: spend extra time informing and instilling trust so that they are more motivated to follow directions

### Formatting/Design
Registration Page
Name/Phone #/healthcare information (provider, policy #, etc)/info for Epic connection
Homepage/Dashboard
“My Alerts” Dropdown Menu
My Logs Button → Some obscure recorded info from patient’s responses
Profile/Settings icon

### Settings
Change password, logout, other general settings, etc.
Manage Family Members Page
Manage Providers Page

To make life easier, all “Manage” pages will look the same with a list ordered alphabetically, with an “edit” and “delete” feature for each one

When adding a new family member, the new family member will receive a text to setup the integration:
Terms of Service
Checkbox to receive: Reminders & Alerts, Questions
