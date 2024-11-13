const themeToggle = document.getElementById('theme-toggle');
themeToggle.checked = localStorage.getItem("theme") === "dark";
const table = document.querySelector('.table');

window.addEventListener('DOMContentLoaded', () => {
    const savedTheme = localStorage.getItem("theme") || "light";
    document.body.setAttribute("data-theme", savedTheme);

    themeToggle.checked = savedTheme === "dark";
    if (savedTheme === "dark") {
        table.classList.add("table-dark");
    } else {
        table.classList.remove("table-dark");
    }
    document.body.classList.remove('hidden');
});

themeToggle.addEventListener('change', () => {
    const newTheme = themeToggle.checked ? "dark" : "light";
    document.body.setAttribute("data-theme", newTheme);
    localStorage.setItem("theme", newTheme);

    if (newTheme === "dark") {
        table.classList.add("table-dark");
    } else {
        table.classList.remove("table-dark");
    }
    document.body.classList.remove('hidden');
});

function redirectToSearch() {
    const query = document.getElementById('q').value;
    const order = document.querySelector('input[name="order"]:checked').value;
    const currentPage = new URLSearchParams(window.location.search).get('page');

    window.location.href = `?q=${encodeURIComponent(query)}&order=${encodeURIComponent(order)}&page=${encodeURIComponent(currentPage || 1)}`;
}
