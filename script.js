function updateStatus(index, checkboxElement) {
    // Assuming local storage will be used to store the status
    const problemStatus = JSON.parse(localStorage.getItem('problemStatus') || '{}');
    problemStatus[index] = checkboxElement.checked ? 'Completed' : '';
    localStorage.setItem('problemStatus', JSON.stringify(problemStatus));
    // Update UI or send data to server as needed
}
