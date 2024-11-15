// Firebase Realtime Database URL
const databaseUrl = "https://acventure-4d055-default-rtdb.firebaseio.com/contacts.json";

// Function to fetch data from Firebase
const fetchDataFromFirebase = async () => {
    try {
        const response = await fetch(databaseUrl);
        const data = await response.json();
        console.log("Fetched Data:", data);
        if (data) {
            displayDataInTable(data); // Pass data to script.js for rendering
        }
    } catch (error) {
        console.error("Error fetching Firebase data:", error);
    }
};
