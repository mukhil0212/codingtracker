// Save the status of the checkbox to LocalStorage when changed
function updateStatus(index, checkboxElement) {
    const problemStatus = JSON.parse(localStorage.getItem('problemStatus') || '{}');
    problemStatus[index] = checkboxElement.checked ? 'Completed' : 'Not Completed';
    localStorage.setItem('problemStatus', JSON.stringify(problemStatus));
}

// When the DOM is fully loaded, restore the checkbox status from LocalStorage
document.addEventListener('DOMContentLoaded', function () {
    const problemStatus = JSON.parse(localStorage.getItem('problemStatus') || '{}');
    document.querySelectorAll('input[type="checkbox"]').forEach(function (checkbox, index) {
        checkbox.checked = problemStatus[index] === 'Completed';
    });
});
