document.getElementById("registerForm")
.addEventListener("submit", function(event) {

    event.preventDefault();

    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;

    if(name.length < 2) {
        document.getElementById("message").innerText =
            "Имя слишком короткое";
        return;
    }

    document.getElementById("message").innerText =
        "Форма успешно отправлена";
});