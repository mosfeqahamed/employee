// Message/Notification timer

var message_timeout = document.getElementById("message-timer");

setTimeout(function()

{

    message_timeout.style.display = "none";


}, 5000);
function confirmDelete(recordId) {
    // Show confirmation dialog
    const confirmed = confirm('Are you sure you want to delete this record?');
    
    if (confirmed) {
        // Submit the form if user confirms
        document.getElementById(`delete-form-${recordId}`).submit();
    }
}