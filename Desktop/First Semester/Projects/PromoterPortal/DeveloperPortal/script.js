// Flag to check if data is encrypted or not
let isEncrypted = false;  // This flag tracks if data has been encrypted

// Function to encrypt all data in the table when Encrypt button is clicked
const encryptAllData = () => {
    // Check if data is already encrypted
    if (isEncrypted) {
        alert("Data is already encrypted.");
        return;  // Don't encrypt again if already encrypted
    }

    const rows = document.querySelectorAll("tr");
    rows.forEach((row) => {
        const emailCell = row.querySelector(".email");
        const phoneCell = row.querySelector(".phone");

        if (emailCell) {
            emailCell.textContent = encryptData(emailCell.textContent); // Encrypt email
        }

        if (phoneCell) {
            phoneCell.textContent = encryptData(phoneCell.textContent); // Encrypt phone
        }
    });

    // Set the flag to true indicating data has been encrypted
    isEncrypted = true;
    console.log("Data encrypted successfully.");
};

// Function to decrypt all data in the table when Decrypt button is clicked
const decryptAllData = () => {
    // Check if data is already decrypted
    if (!isEncrypted) {
        alert("Data is not encrypted yet.");
        return;  // Don't decrypt if data is not encrypted
    }

    const rows = document.querySelectorAll("tr");
    rows.forEach((row) => {
        const emailCell = row.querySelector(".email");
        const phoneCell = row.querySelector(".phone");

        if (emailCell) {
            emailCell.textContent = decryptData(emailCell.textContent); // Decrypt email
        }

        if (phoneCell) {
            phoneCell.textContent = decryptData(phoneCell.textContent); // Decrypt phone
        }
    });

    // Reset the flag to false as data has been decrypted
    isEncrypted = false;
    console.log("Data decrypted successfully.");
};

// Function to display data in the table
const displayDataInTable = (data) => {
    const tableBody = document.getElementById("table-body");
    tableBody.innerHTML = "";  // Clear any previous rows

    for (const id in data) {
        const contact = data[id];
        const row = document.createElement("tr");

        // Create a cell for the name (first name + last name)
        const nameCell = document.createElement("td");
        nameCell.textContent = `${contact.firstName} ${contact.lastName}`;
        row.appendChild(nameCell);

        // Create a cell for the email
        const emailCell = document.createElement("td");
        emailCell.textContent = contact.email;
        emailCell.classList.add("email");
        row.appendChild(emailCell);

        // Create a cell for the phone number
        const phoneCell = document.createElement("td");
        phoneCell.textContent = contact.phone;
        phoneCell.classList.add("phone");
        row.appendChild(phoneCell);

        // Append the row to the table body
        tableBody.appendChild(row);
    }
};
 
// Add event listener to the "Refresh Data" button
document.getElementById('refreshButton').addEventListener('click', function () {
    fetchDataFromFirebase(); // Fetch data from Firebase when the button is clicked
  });

// Fetch data from Firebase
window.onload = () => {
    fetchDataFromFirebase();
};
