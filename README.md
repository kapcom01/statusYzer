![screenshot](/docs/screenshot.png)

ENGLISH:
statusYzer is a python application that uses QT for GUI and pcap for network analysis aiming to log the status changes of your MSN contacts. The purpose of this is to exploit for demonstration a BUG on Microsoft's MSN Protocol that allows to know when a contact has set his/her status to "Appear Offline". This is a privacy issue that has been reported to Microsoft since January 2010 and its still allive.

MANUAL:
1) Close your MSN client (Windows Live Messenger, Emesene, Pidgin...)
2) On statusYzer select from the drop down menu the ethernet card that connects you to the Internet
3) Then press the "Start Analyzing..." button
4) And open your MSN client and login

Now leave statusYzer open and when the counter raises it means that the corresponding contact is either on "Appear Offline" status OR it was already and now is really disconnected!

P.S. I developed this app while learning python+qt+pcap :)

------------------------------------------

ΕΛΛΗΝΙΚΑ:
Το statusYzer είναι ένα πρόγραμμα σε python που χρησιμοποιεί QT για το γραφικό περιβάλλον και pcapy για την ανάλυση του δικτύου στοχεύοντας την καταγραφή των αλλαγών της κατάστασης των επαφών σας στο MSN. Ο σκοπός είναι να εκμεταλευτεί για επίδειξη ένα BUG στο πρωτόκολο του MSN της Microsoft που επιτρέπει να γνωρίζουμε πότε μια επαφή έχει θέσει την κατάστασή της σε "Εμφάνιση Εκτός Σύνδεσης". Αυτό είναι ένα πρόβλημα ιδιωτικού απόρρητου το οποίο έχει αναφερθεί στη Microsoft από τον Ιανουάριο του 2010 και δεν έχει διορθωθεί ακόμα.

ΕΓΧΕΙΡΙΔΙΟ:
1) Κλείστε το πρόγραμμα του MSN (Windows Live Messenger, Emesene, Pidgin...)
2) Στο statusYzer επιλέξτε από το αναδυόμενο μενού την κάρτα δικτύου που συνδέεστε στο ίντερνετ
3) Μετά πατήστε το κουμπί "Έναρξη Ανάλυσης..."
4) Και ανοίξτε το πρόγραμμα MSN και κάντε είσοδο

Τώρα αφήστε ανοιχτό το statusYzer και όταν ο μετρητής αυξάνεται σημαίνει ότι η αντίστοιχη επαφή είτε μπήκε σε κατάσταση "Εμφάνιση Εκτός Σύδεσης" ή ήταν ήδη και αποσυνδέθηκε πραγματικά!

Υ.Γ. Ανέπτυξα αυτή την εφαρμογή μαθαίνοντας python+qt+pcap :)

