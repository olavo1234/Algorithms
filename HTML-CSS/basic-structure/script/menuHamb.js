document.addEventListener("DOMContentLoaded", function() {
    const buttonOpenMenu = document.getElementById("buttonMenu");

    buttonOpenMenu.addEventListener('click', function() {
        const menu = document.getElementById("menu");
        if (menu.style.display === "block") {
            menu.style.display = "none";
        } else {
            menu.style.display = "block";
        }
    });
});
