// Secret key for encryption and decryption
const secretKey = "your-secret-key";  // Use a secure key for encryption/decryption

// Function to encrypt the data
const encryptData = (data) => {
    return CryptoJS.AES.encrypt(data, secretKey).toString();  // Encrypt the data
};

// Function to decrypt the data
const decryptData = (encryptedData) => {
    const bytes = CryptoJS.AES.decrypt(encryptedData, secretKey);  // Decrypt the data
    return bytes.toString(CryptoJS.enc.Utf8);  // Convert bytes back to string
};
