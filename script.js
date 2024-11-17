document.addEventListener("DOMContentLoaded", () => {
    console.log("DOM fully loaded"); // Debugging line
    
    // Loading Screen Handling
    const loadingScreen = document.getElementById("loading-screen");
    const mainContent = document.getElementById("main-content");

    setTimeout(() => {
        loadingScreen.style.display = "none";
        mainContent.style.display = "block";
    }, 3000);

    
    
});
