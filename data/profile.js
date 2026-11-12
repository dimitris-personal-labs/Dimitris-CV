// Profile content shared by the website and the generated CV files.
// Edit text here; run `node tools/build-cv.js` afterwards to regenerate the CVs.
window.CV_PROFILE = {
  contact: {
    name: { en: "Dimitrios Christos Asimopoulos", el: "Δημήτριος Χρήστος Ασημόπουλος" },
    role: { en: "Electrical & Computer Engineer / AI Researcher", el: "Ηλεκτρολόγος Μηχανικός & Μηχανικός Υπολογιστών / Ερευνητής Τεχνητής Νοημοσύνης" },
    location: { en: "Thessaloniki, Greece", el: "Θεσσαλονίκη, Ελλάδα" },
    email: "dasimopoulos@metamind.gr",
    emailPersonal: "asimopou@icloud.com",
    phone: "+30 698 310 1663",
    linkedIn: "https://www.linkedin.com/in/dimitris-christos-asimopoulos-2a627a262/",
    scholar: "https://scholar.google.com/citations?user=HO6cbW8AAAAJ&hl=el",
    orcid: "0009-0009-6439-0857"
  },
  // Diploma thesis shown in its own section on the website.
  thesis: {
    file: "assets/asimopoulos-diploma-thesis.pdf",
    cover: "assets/asimopoulos-diploma-thesis-cover.jpg",
    date: "07/2022",
    pages: 87,
    title: {
      el: "Παραγωγικά Ανταγωνιστικά Δίκτυα και Εφαρμογές",
      en: "Generative Adversarial Networks and Applications"
    },
    supervisor: { en: "George F. Fragulis", el: "Γεώργιος Φραγκούλης" },
    institution: {
      en: "Department of Electrical and Computer Engineering, University of Western Macedonia, Kozani",
      el: "Τμήμα Ηλεκτρολόγων Μηχανικών και Μηχανικών Υπολογιστών, Πανεπιστήμιο Δυτικής Μακεδονίας, Κοζάνη"
    },
    abstract: {
      en: "In this diploma thesis, the various architectures of Generative Adversarial Networks were studied and their indicative applications in various fields are presented. Introductory information about the functioning of simple neural networks is first presented, followed by a presentation of convolutional neural networks. The review concludes with the main architectures applied to Generative Adversarial Networks and the fields in which they are applied. Finally, examples of applications and code for indicative Generative Adversarial Network architectures are presented.",
      el: "Στην παρούσα διπλωματική εργασία μελετήθηκαν οι διάφορες αρχιτεκτονικές των παραγωγικών νευρωνικών δικτύων και παρουσιάζονται ενδεικτικές εφαρμογές τους σε διάφορα πεδία. Παρουσιάζονται αρχικά εισαγωγικές πληροφορίες σχετικά με τη λειτουργία των απλών νευρωνικών δικτύων και στη συνέχεια γίνεται μια παρουσίαση των συνελικτικών νευρωνικών δικτύων. Η επισκόπηση ολοκληρώνεται με την παράθεση των κυριότερων αρχιτεκτονικών που εφαρμόζονται στα παραγωγικά νευρωνικά δίκτυα και των γνωστικών πεδίων στα οποία εφαρμόζονται. Τέλος, παρουσιάζονται παραδείγματα εφαρμογών και σχετικοί κώδικες ενδεικτικών αρχιτεκτονικών των παραγωγικών νευρωνικών δικτύων."
    }
  },
  en: {
    // Short summary at the top of the CV. {publications} is replaced with the current count.
    cvSummary: "AI researcher and Electrical & Computer Engineer with R&D experience since 2022 in EU-funded Horizon 2020, Horizon Europe and Digital Europe projects. PhD candidate at the International Hellenic University, researching the security, privacy and ethics of AI in IoT systems. Specialised in adversarial machine learning, AI-enabled intrusion detection, generative models and text anonymisation, with {publications} peer-reviewed publications in IEEE, ACM, Elsevier and AIP venues.",
    profileText: "Dimitris Asimopoulos received his BSc and Integrated Master's degrees in Electrical and Computer Engineering from the University of Western Macedonia (UOWM) (September 2016 - June 2022). He is currently a PhD candidate at the Department of Information and Electronic Engineering of the International Hellenic University (IHU), conducting research in the field of “AI in IoT systems: Security, Privacy, Ethical Challenges & Solutions,” further expanding his expertise in cutting-edge AI trends. Dimitris's interests encompass Machine Learning techniques, Artificial Intelligence, and Generative Adversarial Networks, applied in various domains. Presently, he serves as an AI Researcher and Electrical Engineer at MetaMind Innovations in Thessaloniki, where he actively contributes to the development and research of European Horizon projects. His work primarily focuses on big data processing and cybersecurity, including the prevention, detection, and response to cyberattacks.",
    experience: {
      date: "08/2022 - Current",
      location: "Greece",
      title: "AI Engineer / Electrical Engineer",
      company: "MetaMind Innovations P.C.",
      bullets: [
        "Research and development across multiple Horizon Europe projects, with a primary focus on Artificial Intelligence, Machine Learning and big-data processing applied to cybersecurity, critical infrastructure protection and the energy sector.",
        "Design, implementation and evaluation of AI-enabled Intrusion Detection and Prevention Systems (IDPS), with emphasis on adversarial robustness, anomaly detection and threat mitigation for industrial control systems and the smart grid.",
        "Development of Generative Adversarial Networks (GANs) and other deep-learning models for synthetic data generation, data augmentation, text anonymisation and adversarial-attack simulation.",
        "Active contribution to technical work-packages of EU-funded research projects, including requirements analysis, software development, integration, validation, demonstration activities and deliverable authoring according to EC specifications.",
        "Co-author of peer-reviewed publications in international journals and conferences, including IEEE, ACM, Elsevier and Springer venues."
      ]
    },
    education: [
      {
        date: "Current",
        location: "Greece",
        title: "PhD Candidate",
        org: "International Hellenic University (IHU), Department of Information and Electronic Engineering",
        body: "Proposed dissertation title: “AI in IoT Systems: Security, Privacy, Ethical Challenges & Solutions”."
      },
      {
        date: "10/2025 - Current",
        location: "Greece",
        title: "MBA in Management Information Systems",
        org: "University of Western Macedonia (UOWM), Kozani & Grevena",
        body: "Master in Business Administration (MBA) in Management Information Systems: inter-departmental postgraduate programme of the Department of Electrical and Computer Engineering (School of Engineering) and the Department of Business Administration, Grevena (School of Economic Sciences)."
      },
      {
        date: "09/2016 - 06/2022",
        location: "Greece",
        title: "Electrical and Computer Engineering",
        org: "University of Western Macedonia (UOWM), Kozani",
        body: "Department of Electrical and Computer Engineering, Faculty of Engineering. Specialisation: Computers and Electronics. Diploma thesis: “Generative Adversarial Networks and Applications”."
      },
      {
        date: "09/2016 - 06/2022",
        location: "Greece",
        title: "Integrated Master Electrical and Computer Engineer",
        org: "University of Western Macedonia (UOWM), Kozani",
        body: "Core courses: Machine Learning, Fuzzy Systems, Artificial Intelligence, Biomedical Engineering, Robotics, Design and Analysis of Algorithms, Computer Architecture, Parallel and Distributed Systems and Advanced Topics in Digital Design."
      }
    ],
    certifications: [
      ["Build a Modern Computer from First Principles: From Nand to Tetris", "Coursera / University of Jerusalem, October 2021"],
      ["NDG Linux Unhatched", "Cisco Networking Academy, February 2022"],
      ["NDG Linux Essentials", "Cisco Networking Academy, February 2022"],
      ["International Business Strategy", "International team project jointly delivered by the University of Western Macedonia and Karlsruhe University of Applied Sciences, funded by DAAD, December 2020"]
    ],
    languages: {
      motherTongue: "Mother tongue: Greek",
      rows: [
        ["English", "B2", "B2", "B2", "B2", "B2"],
        ["German", "A1", "A1", "A1", "A1", "A1"]
      ],
      headers: ["Language", "Listening", "Reading", "Spoken production", "Spoken interaction", "Writing"]
    },
    skillGroups: [
      ["Programming languages", ["Python", "C", "C++", "Java", "JavaScript", "MATLAB", "SQL", "Bash"]],
      ["AI / ML frameworks and libraries", ["PyTorch", "TensorFlow", "Keras", "scikit-learn", "Hugging Face Transformers", "NumPy", "Pandas", "OpenCV"]],
      ["Specialisation areas", ["GANs", "Deep Learning", "Adversarial Machine Learning", "Intrusion Detection / Prevention", "Natural Language Processing", "Big Data Analytics"]],
      ["Tools and platforms", ["Git", "GitHub", "GitLab", "Docker", "Linux / Unix", "Jupyter", "MLflow", "MISP", "OpenCTI"]],
      ["Productivity", ["MS Office", "Google Workspace", "LaTeX", "Overleaf", "Atlassian Jira", "Confluence"]]
    ]
  },
  el: {
    cvSummary: "Ερευνητής Τεχνητής Νοημοσύνης και Ηλεκτρολόγος Μηχανικός & Μηχανικός Υπολογιστών, με εμπειρία στην Έρευνα και Ανάπτυξη από το 2022 σε ευρωπαϊκά έργα Horizon 2020, Horizon Europe και Digital Europe. Υποψήφιος διδάκτορας στο Διεθνές Πανεπιστήμιο της Ελλάδος, με αντικείμενο την ασφάλεια, την ιδιωτικότητα και τις ηθικές προκλήσεις της Τεχνητής Νοημοσύνης σε συστήματα ΔτΠ. Εξειδίκευση στην ανταγωνιστική μηχανική μάθηση, στα συστήματα ανίχνευσης εισβολών με Τεχνητή Νοημοσύνη, στα παραγωγικά μοντέλα και στην ανωνυμοποίηση κειμένου, με {publications} δημοσιεύσεις με κρίση σε IEEE, ACM, Elsevier και AIP.",
    profileText: "Ο Δημήτρης Ασημόπουλος έλαβε το πτυχίο και το ολοκληρωμένο μεταπτυχιακό δίπλωμα από το Τμήμα Ηλεκτρολόγων Μηχανικών και Μηχανικών Υπολογιστών του Πανεπιστημίου Δυτικής Μακεδονίας (ΠΔΜ) (Σεπτέμβριος 2016 - Ιούνιος 2022). Αυτή τη στιγμή είναι υποψήφιος διδάκτορας στο Τμήμα Μηχανικών Πληροφορικής και Ηλεκτρονικών Συστημάτων του Διεθνούς Πανεπιστημίου της Ελλάδος (ΔΙΠΑΕ), πραγματοποιώντας έρευνα στο πεδίο της «Τεχνητής Νοημοσύνης σε συστήματα IoT: Ασφάλεια, Ιδιωτικότητα, Ηθικές Προκλήσεις και Λύσεις», επεκτείνοντας περαιτέρω την εξειδίκευσή του στις τελευταίες τάσεις της Τεχνητής Νοημοσύνης. Τα ενδιαφέροντα του Δημήτρη περιλαμβάνουν τις τεχνικές Μηχανικής Μάθησης, την Τεχνητή Νοημοσύνη και τα Γενετικά Αντιπαραθετικά Δίκτυα, εφαρμοσμένα σε διάφορους τομείς. Αυτή τη στιγμή εργάζεται ως Ηλεκτρολόγος Μηχανικός και ερευνητής Τεχνητής Νοημοσύνης στη MetaMind Innovations στη Θεσσαλονίκη, όπου συμβάλλει ενεργά στην ανάπτυξη και στην έρευνα στο πλαίσιο των ευρωπαϊκών έργων Horizon. Οι αρμοδιότητές του επικεντρώνονται κυρίως στην επεξεργασία μεγάλων δεδομένων και την κυβερνοασφάλεια, συμπεριλαμβανομένης της πρόληψης, ανίχνευσης και απόκρισης σε κυβερνοεπιθέσεις.",
    experience: {
      date: "08/2022 - Σήμερα",
      location: "Ελλάδα",
      title: "Μηχανικός Τεχνητής Νοημοσύνης / Ηλεκτρολόγος Μηχανικός",
      company: "MetaMind Innovations P.C.",
      bullets: [
        "Έρευνα και ανάπτυξη σε πολλαπλά Ευρωπαϊκά Προγράμματα Horizon, με κύρια εστίαση στην Τεχνητή Νοημοσύνη, τη Μηχανική Μάθηση και την επεξεργασία μεγάλων δεδομένων με εφαρμογή στην κυβερνοασφάλεια, την προστασία κρίσιμων υποδομών και τον ενεργειακό τομέα.",
        "Σχεδίαση, υλοποίηση και αξιολόγηση Συστημάτων Ανίχνευσης και Πρόληψης Εισβολών (IDPS) με χρήση Τεχνητής Νοημοσύνης, με έμφαση στην ανθεκτικότητα έναντι ανταγωνιστικών επιθέσεων, στην ανίχνευση ανωμαλιών και στη μετρίαση απειλών για βιομηχανικά συστήματα ελέγχου και το έξυπνο ηλεκτρικό δίκτυο.",
        "Ανάπτυξη Παραγωγικών Ανταγωνιστικών Δικτύων (GANs) και άλλων μοντέλων βαθιάς μάθησης για παραγωγή συνθετικών δεδομένων, αύξηση δεδομένων, ανωνυμοποίηση κειμένου και προσομοίωση ανταγωνιστικών επιθέσεων.",
        "Ενεργή συμβολή στα τεχνικά πακέτα εργασίας ευρωπαϊκών ερευνητικών έργων, συμπεριλαμβανομένων της ανάλυσης απαιτήσεων, της ανάπτυξης λογισμικού, της ολοκλήρωσης, της επικύρωσης, των δραστηριοτήτων επίδειξης και της συγγραφής παραδοτέων σύμφωνα με τις προδιαγραφές της Ευρωπαϊκής Επιτροπής.",
        "Συν-συγγραφέας δημοσιεύσεων με κρίση σε διεθνή επιστημονικά περιοδικά και συνέδρια, συμπεριλαμβανομένων IEEE, ACM, Elsevier και Springer."
      ]
    },
    education: [
      {
        date: "Σήμερα",
        location: "Ελλάδα",
        title: "Υποψήφιος Διδάκτορας",
        org: "Διεθνές Πανεπιστήμιο της Ελλάδος (ΔΙΠΑΕ), Τμήμα Μηχανικών Πληροφορικής και Ηλεκτρονικών Συστημάτων",
        body: "Προτεινόμενος τίτλος διδακτορικής διατριβής: «Τεχνητή Νοημοσύνη στα Συστήματα ΔτΠ: Ασφάλεια, ηθικές προκλήσεις και λύσεις»."
      },
      {
        date: "10/2025 - Σήμερα",
        location: "Ελλάδα",
        title: "MBA στη Διοίκηση Επιχειρήσεων με κατεύθυνση Πληροφοριακά Συστήματα Διοίκησης",
        org: "Πανεπιστήμιο Δυτικής Μακεδονίας (ΠΔΜ), Κοζάνη & Γρεβενά",
        body: "Διατμηματικό Πρόγραμμα Μεταπτυχιακών Σπουδών (ΔΠΜΣ) του Τμήματος Ηλεκτρολόγων Μηχανικών και Μηχανικών Υπολογιστών της Πολυτεχνικής Σχολής, σε συνεργασία με το Τμήμα Οργάνωσης και Διοίκησης Επιχειρήσεων (Γρεβενά) της Σχολής Οικονομικών Επιστημών."
      },
      {
        date: "09/2016 - 06/2022",
        location: "Ελλάδα",
        title: "Ηλεκτρολόγος Μηχανικός και Μηχανικός Υπολογιστών",
        org: "Πανεπιστήμιο Δυτικής Μακεδονίας (ΠΔΜ), Κοζάνη",
        body: "Τμήμα Ηλεκτρολόγων Μηχανικών και Μηχανικών Υπολογιστών, Πολυτεχνική Σχολή. Ειδίκευση: Υπολογιστών και Ηλεκτρονικής. Διπλωματική εργασία: «Παραγωγικά Ανταγωνιστικά Δίκτυα και Εφαρμογές»."
      },
      {
        date: "09/2016 - 06/2022",
        location: "Ελλάδα",
        title: "Ενιαίο και Αδιάσπαστο Μεταπτυχιακό Δίπλωμα Ηλεκτρολόγου Μηχανικού και Μηχανικού Υπολογιστών",
        org: "Πανεπιστήμιο Δυτικής Μακεδονίας (ΠΔΜ), Κοζάνη",
        body: "Βασικά μαθήματα: Μηχανική Μάθηση, Ασαφή Συστήματα, Τεχνητή Νοημοσύνη, Βιοϊατρική, Ρομποτική, Σχεδίαση και Ανάλυση Αλγορίθμων, Αρχιτεκτονική Υπολογιστών, Παράλληλα και Διανεμημένα Συστήματα, Προχωρημένα Θέματα Ψηφιακού Σχεδιασμού."
      }
    ],
    certifications: [
      ["Build a Modern Computer from First Principles: From Nand to Tetris", "Coursera / Πανεπιστήμιο της Ιερουσαλήμ, Οκτώβριος 2021"],
      ["NDG Linux Unhatched", "Cisco Networking Academy, Φεβρουάριος 2022"],
      ["NDG Linux Essentials", "Cisco Networking Academy, Φεβρουάριος 2022"],
      ["International Business Strategy", "Διεθνές ομαδικό έργο από το Πανεπιστήμιο Δυτικής Μακεδονίας και το Πανεπιστήμιο Εφαρμοσμένων Επιστημών της Καρλσρούης, χρηματοδοτούμενο από DAAD, Δεκέμβριος 2020"]
    ],
    languages: {
      motherTongue: "Μητρική γλώσσα: Ελληνικά",
      rows: [
        ["Αγγλικά", "Β2", "Β2", "Β2", "Β2", "Β2"],
        ["Γερμανικά", "A1", "A1", "A1", "A1", "A1"]
      ],
      headers: ["Γλώσσα", "Ακρόαση", "Ανάγνωση", "Προφορική παραγωγή", "Προφορική επικοινωνία", "Γραφή"]
    },
    skillGroups: [
      ["Γλώσσες προγραμματισμού", ["Python", "C", "C++", "Java", "JavaScript", "MATLAB", "SQL", "Bash"]],
      ["Πλαίσια και βιβλιοθήκες AI / ML", ["PyTorch", "TensorFlow", "Keras", "scikit-learn", "Hugging Face Transformers", "NumPy", "Pandas", "OpenCV"]],
      ["Τομείς εξειδίκευσης", ["Παραγωγικά Ανταγωνιστικά Δίκτυα (GANs)", "Βαθιά Μάθηση", "Ανταγωνιστική Μηχανική Μάθηση", "Ανίχνευση / Πρόληψη Εισβολών", "Επεξεργασία Φυσικής Γλώσσας", "Ανάλυση Μεγάλων Δεδομένων"]],
      ["Εργαλεία και πλατφόρμες", ["Git", "GitHub", "GitLab", "Docker", "Linux / Unix", "Jupyter", "MLflow", "MISP", "OpenCTI"]],
      ["Παραγωγικότητα", ["MS Office", "Google Workspace", "LaTeX", "Overleaf", "Atlassian Jira", "Confluence"]]
    ]
  }
};
