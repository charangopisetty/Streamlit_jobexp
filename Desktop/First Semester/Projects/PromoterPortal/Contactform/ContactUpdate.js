// Firebase configuration (replace with your own Firebase details)
const firebaseConfig = {
    apiKey: "AIzaSyDEG1ttrjqqHIIVxnSNLvVUs3u_oWw4kno",
    authDomain: "acventure-4d055.firebaseapp.com",
    databaseURL: "https://acventure-4d055-default-rtdb.firebaseio.com",
    projectId: "acventure-4d055",
    storageBucket: "acventure-4d055.firebasestorage.app",
    messagingSenderId: "795261821594",
    appId: "1:795261821594:web:30b57f1cf701f85b5c3523",
    measurementId: "G-GGZDGJMBXP"
  };
  
  // Initialize Firebase (using the modular SDK style)
  import { initializeApp } from "https://www.gstatic.com/firebasejs/9.20.0/firebase-app.js";
  import { getDatabase, ref, push } from "https://www.gstatic.com/firebasejs/9.20.0/firebase-database.js";
  
  // Initialize Firebase
  const app = initializeApp(firebaseConfig);
  const database = getDatabase(app);
  
  // Function to handle form submission and send data to Firebase
  const contactForm = document.getElementById('contactForm');
  
  contactForm.addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent the default form submission
  
    // Get form data
    const firstName = document.getElementById('firstName').value;
    const lastName = document.getElementById('lastName').value;
    const phone = document.getElementById('phone').value;
    const email = document.getElementById('email').value;
  
    // Create an object to store the data
    const contactData = {
      firstName: firstName,
      lastName: lastName,
      phone: phone,
      email: email,
    };
  
    // Send the data to Firebase Realtime Database
    sendDataToFirebase(contactData);
  });
  
  // Function to send data to Firebase Realtime Database
  function sendDataToFirebase(contactData) {
    const contactRef = ref(database, 'contacts'); // 'contacts' is your database path
    push(contactRef, contactData)
      .then(() => {
        alert("Your message has been sent successfully!");
        // Optionally clear the form after successful submission
        document.getElementById('contactForm').reset();
      })
      .catch((error) => {
        console.error("Error sending data to Firebase:", error);
        alert("There was an error. Please try again.");
      });
  }
  