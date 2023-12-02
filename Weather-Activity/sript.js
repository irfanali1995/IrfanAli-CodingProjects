function flipContainer() {
    const container = document.getElementById("flip-container");
    container.style.transform = "rotateY(180deg)";
}

function unflipContainer() {
    const container = document.getElementById("flip-container");
    container.style.transform = "rotateY(0deg)";
}
