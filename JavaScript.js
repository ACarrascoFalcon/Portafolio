
document.addEventListener("DOMContentLoaded", () => {
    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, {
        threshold: 0.5
    });

    document.querySelectorAll('.progreso').forEach(bar => {
        observer.observe(bar);
    });
});

function mostrarTexto1(visible) {
    document.getElementById("desc1").style.display = visible ? "block" : "none";
}

function mostrarTexto2(visible) {
    document.getElementById("desc2").style.display = visible ? "block" : "none";
}

function mostrarTexto3(visible) {
    document.getElementById("desc3").style.display = visible ? "block" : "none";
}

function mostrarTexto4(visible) {
    document.getElementById("desc4").style.display = visible ? "block" : "none";
}
