document.addEventListener("DOMContentLoaded", function () {

    const button =
        document.getElementById("themeToggle");

    if (!button) return;

    const body = document.body;

    const savedTheme =
        localStorage.getItem("theme");

    if (savedTheme === "dark") {

        body.classList.add("dark-mode");

        button.innerHTML =
            "☀️ Light Mode";
    }

    button.addEventListener("click", function () {

        body.classList.toggle("dark-mode");

        if (
            body.classList.contains(
                "dark-mode"
            )
        ) {

            localStorage.setItem(
                "theme",
                "dark"
            );

            button.innerHTML =
                "☀️ Light Mode";

        } else {

            localStorage.setItem(
                "theme",
                "light"
            );

            button.innerHTML =
                "🌙 Dark Mode";
        }

    });

});